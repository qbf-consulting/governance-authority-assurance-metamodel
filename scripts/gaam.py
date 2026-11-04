#!/usr/bin/env python3
"""Portable GAAM v0.9.x validation and conformance-vector runner."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
VECTORS = ROOT / "tests" / "behavioural"
VECTORS_V2 = ROOT / "tests" / "behavioural-v2"


def read_json(path):
    return json.loads(Path(path).read_text())


def emit(command, checks):
    failed = [check for check in checks if check["status"] == "fail"]
    result = {
        "tool": "gaam-portable-validator",
        "command": command,
        "releaseVersion": read_json(ROOT / "release.json")["version"],
        "normativeVersion": read_json(ROOT / "release.json")["normativeVersion"],
        "semanticBaseline": read_json(ROOT / "release.json").get("semanticBaseline", read_json(ROOT / "release.json")["normativeVersion"]),
        "status": "fail" if failed else "pass",
        "checks": checks,
    }
    print(json.dumps(result, indent=2))
    return 1 if failed else 0


def schema_check(instance, schema_path, check_id):
    errors = sorted(Draft202012Validator(read_json(schema_path)).iter_errors(instance), key=lambda e: list(e.path))
    return {
        "id": check_id,
        "status": "fail" if errors else "pass",
        "detail": errors[0].message if errors else f"conforms to {Path(schema_path).name}",
    }


def validate_claim(args):
    claim = read_json(args.claim)
    return emit("validate-claim", [schema_check(claim, SCHEMAS / "conformance-claim.schema.json", "claim-schema")])


def package_member(root, relative):
    """Resolve only ordinary paths contained in the submitted package.

    No absolute paths, parent traversal or symlinks escaping the package.
    This validates *where* a path points, not who authored the package.
    """
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        return None
    if ".." in Path(relative).parts:
        return None
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def validate_package(args):
    package = Path(args.package).resolve()
    manifest_path = package if package.is_file() else package / "manifest.json"
    package_root = manifest_path.parent
    manifest = read_json(manifest_path)
    checks = [schema_check(manifest, SCHEMAS / "gaam-package.schema.json", "package-manifest")]
    if checks[0]["status"] == "fail":
        return emit("validate-package", checks)

    declared = [item["path"] for item in manifest["artifacts"]]
    unsafe = [relative for relative in declared if package_member(package_root, relative) is None]
    checks.append({
        "id": "package-paths",
        "status": "fail" if unsafe else "pass",
        "detail": f"paths outside package: {unsafe}" if unsafe else "declared paths remain within the package",
    })
    missing = [relative for relative in declared
               if (path := package_member(package_root, relative)) is None or not path.is_file()]
    checks.append({
        "id": "declared-artifacts",
        "status": "fail" if missing else "pass",
        "detail": f"missing or unsafe: {missing}" if missing else f"{len(declared)} declared artifacts present",
    })
    schema_by_type = {
        "authority": "authority.schema.json", "delegation": "delegation.schema.json",
        "decision-receipt": "decision-receipt.schema.json", "governance-event": "governance-event.schema.json",
        "remedy": "remedy.schema.json", "appeal": "appeal.schema.json",
        "gaam-conformance-claim": "conformance-claim.schema.json",
    }
    for relative in declared:
        path = package_member(package_root, relative)
        if path is None or not path.is_file() or path.suffix != ".json":
            continue
        artifact = read_json(path)
        schema_name = schema_by_type.get(artifact.get("type"))
        if schema_name:
            checks.append(schema_check(artifact, SCHEMAS / schema_name, f"artifact-schema:{relative}"))

    integrity_name = manifest["integrity"]["manifest"]
    checksum_path = package_member(package_root, integrity_name)
    if checksum_path is None or not checksum_path.is_file():
        checks.append({
            "id": "package-integrity", "status": "fail",
            "detail": "checksum manifest missing or outside the submitted package",
        })
    else:
        checksum_data = read_json(checksum_path)
        records = checksum_data.get("files", [])
        # A checksum manifest may contain more files than the declared artifacts,
        # but each declared artifact must be covered exactly once.
        record_paths = [item.get("path") for item in records]
        uncovered = sorted(set(declared) - set(record_paths))
        duplicates = sorted({p for p in record_paths if record_paths.count(p) > 1})
        mismatched = []
        for record in records:
            relative = record.get("path")
            path = package_member(package_root, relative)
            if path is None or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != record.get("sha256"):
                mismatched.append(relative)
        bad = bool(uncovered or duplicates or mismatched)
        checks.append({
            "id": "package-integrity",
            "status": "fail" if bad else "pass",
            "detail": (f"uncovered={uncovered}; duplicate={duplicates}; mismatched/unsafe={mismatched}"
                       if bad else f"{len(records)} checksums verified against declared artifacts; checksum-only (no source authenticity established)"),
        })
    return emit("validate-package", checks)


def check_v2(vector):
    """Validate v2 test inputs, not their anticipated verdicts."""
    from datetime import datetime
    data = vector.get("input", {})
    if vector.get("vectorVersion") != 2 or not isinstance(data, dict):
        return "invalid vector version or input"
    if not isinstance(vector.get("expectedValid"), bool) or not isinstance(vector.get("expectedReason"), str):
        return "v2 requires Boolean expectedValid and an expectedReason"
    if not isinstance(data.get("requestedEffect"), str) or not data["requestedEffect"]:
        return "requestedEffect missing"
    try:
        clock = datetime.fromisoformat(vector["evaluationTime"].replace("Z", "+00:00"))
        if clock.tzinfo is None:
            return "evaluationTime must be timezone-aware"
    except (KeyError, TypeError, ValueError, AttributeError):
        return "invalid evaluationTime"
    authority = data.get("authority")
    if not isinstance(authority, dict):
        return "authority artifact required"
    errors = list(Draft202012Validator(read_json(SCHEMAS / "authority.schema.json"), format_checker=FormatChecker()).iter_errors(authority))
    return errors[0].message if errors else None


def run_vectors(args):
    vector_paths = sorted((VECTORS if args.suite == "v1" else VECTORS_V2).glob(args.pattern))
    checks = []
    for path in vector_paths:
        vector = read_json(path)
        issue = check_v2(vector) if args.suite == "v2" else None
        if issue:
            checks.append({"id": vector.get("id", path.name), "status": "fail", "detail": "invalid v2 fixture: " + issue})
            continue
        payload = {"artifacts": vector["input"], "evaluationTime": vector["evaluationTime"]} if args.suite == "v2" else vector["input"]
        process = subprocess.run(args.adapter, input=json.dumps(payload), text=True, capture_output=True)
        try:
            response = json.loads(process.stdout)
            actual = response.get("valid")
            reason = response.get("reason")
            ok = (process.returncode == 0 and isinstance(actual, bool) and actual == vector["expectedValid"]
                  and (args.suite == "v1" or reason == vector["expectedReason"]))
            detail = f"expected={vector['expectedValid']}; actual={actual}" + (f"; reason={reason}; expectedReason={vector['expectedReason']}" if args.suite == "v2" else "")
        except json.JSONDecodeError:
            ok = False
            detail = f"adapter returned non-JSON output: {process.stdout[:160]!r}; stderr={process.stderr[:160]!r}"
        checks.append({"id": vector["id"], "status": "pass" if ok else "fail", "detail": detail})
    if not vector_paths:
        checks.append({"id": "vector-selection", "status": "fail", "detail": f"no vectors matched {args.pattern}"})
    return emit("run-vectors", checks)


parser = argparse.ArgumentParser(description=__doc__)
commands = parser.add_subparsers(dest="command", required=True)
claim_parser = commands.add_parser("validate-claim", help="validate a conformance claim")
claim_parser.add_argument("claim")
claim_parser.set_defaults(func=validate_claim)
package_parser = commands.add_parser("validate-package", help="validate an external package directory")
package_parser.add_argument("package")
package_parser.set_defaults(func=validate_package)
vector_parser = commands.add_parser("run-vectors", help="run portable behavioural vectors through an adapter")
vector_parser.add_argument("--pattern", default="*.json", help="test-vector glob relative to the selected suite")
vector_parser.add_argument("--suite", choices=["v1", "v2"], default="v1", help="v1 decision-table vectors (default), or v2 raw-artifact vectors")
vector_parser.add_argument("adapter", nargs=argparse.REMAINDER, help="adapter command; reads input JSON on stdin and returns {valid:boolean}")
vector_parser.set_defaults(func=run_vectors)
args = parser.parse_args()
if args.command == "run-vectors":
    if not args.adapter:
        parser.error("run-vectors requires an adapter command")
    if any(a == "--pattern" or a.startswith("--pattern=") for a in args.adapter):
        parser.error("--pattern must precede the adapter command; after it, the flag is passed to the adapter and silently ignored")
raise SystemExit(args.func(args))
