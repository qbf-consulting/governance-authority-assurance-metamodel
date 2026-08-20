#!/usr/bin/env python3
"""Portable GAAM v0.9.x validation and conformance-vector runner."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
VECTORS = ROOT / "tests" / "behavioural"


def read_json(path):
    return json.loads(Path(path).read_text())


def emit(command, checks):
    failed = [check for check in checks if check["status"] == "fail"]
    result = {
        "tool": "gaam-portable-validator",
        "command": command,
        "releaseVersion": read_json(ROOT / "release.json")["version"],
        "normativeVersion": read_json(ROOT / "release.json")["normativeVersion"],
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


def validate_package(args):
    package = Path(args.package).resolve()
    manifest_path = package if package.is_file() else package / "manifest.json"
    package_root = manifest_path.parent
    manifest = read_json(manifest_path)
    checks = [schema_check(manifest, SCHEMAS / "gaam-package.schema.json", "package-manifest")]
    declared = [item["path"] for item in manifest.get("artifacts", [])]
    missing = [path for path in declared if not (package_root / path).is_file()]
    checks.append({"id": "declared-artifacts", "status": "fail" if missing else "pass", "detail": f"missing: {missing}" if missing else f"{len(declared)} declared artifacts present"})
    schema_by_type = {
        "authority": "authority.schema.json", "delegation": "delegation.schema.json",
        "decision-receipt": "decision-receipt.schema.json", "governance-event": "governance-event.schema.json",
        "remedy": "remedy.schema.json", "appeal": "appeal.schema.json",
        "gaam-conformance-claim": "conformance-claim.schema.json",
    }
    for relative in declared:
        path = package_root / relative
        if not path.is_file() or path.suffix != ".json":
            continue
        artifact = read_json(path)
        schema_name = schema_by_type.get(artifact.get("type"))
        if schema_name:
            checks.append(schema_check(artifact, SCHEMAS / schema_name, f"artifact-schema:{relative}"))
    checksum_path = package_root / manifest.get("integrity", {}).get("manifest", "checksums.json")
    if checksum_path.is_file():
        checksum_data = read_json(checksum_path)
        mismatched = []
        for record in checksum_data.get("files", []):
            path = package_root / record.get("path", "")
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != record.get("sha256"):
                mismatched.append(record.get("path"))
        checks.append({"id": "package-integrity", "status": "fail" if mismatched else "pass", "detail": f"mismatched: {mismatched}" if mismatched else f"{len(checksum_data.get('files', []))} checksums verified"})
    else:
        checks.append({"id": "package-integrity", "status": "fail", "detail": f"missing {checksum_path.name}"})
    return emit("validate-package", checks)


def run_vectors(args):
    vector_paths = sorted(VECTORS.glob(args.pattern))
    checks = []
    for path in vector_paths:
        vector = read_json(path)
        process = subprocess.run(args.adapter, input=json.dumps(vector["input"]), text=True, capture_output=True)
        try:
            response = json.loads(process.stdout)
            actual = response.get("valid")
            ok = process.returncode == 0 and isinstance(actual, bool) and actual == vector["expectedValid"]
            detail = f"expected={vector['expectedValid']}; actual={actual}"
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
vector_parser.add_argument("--pattern", default="*.json", help="test-vector glob relative to tests/behavioural")
vector_parser.add_argument("adapter", nargs=argparse.REMAINDER, help="adapter command; reads input JSON on stdin and returns {valid:boolean}")
vector_parser.set_defaults(func=run_vectors)
args = parser.parse_args()
if args.command == "run-vectors" and not args.adapter:
    parser.error("run-vectors requires an adapter command")
raise SystemExit(args.func(args))
