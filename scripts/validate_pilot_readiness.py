#!/usr/bin/env python3
"""Validate GAAM pilot publication contracts and run source-bound dry-run checks.

Checks documental structure and evidence integrity; does NOT attest institutional
authority, independent implementation, or operational pilot gate acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "pilots" / "gates.json"
REQUIRED_PAGES = [
    "pilots/index.md", "pilots/design.md", "pilots/charter.md",
    "pilots/participant-guide.md", "pilots/test-and-evidence.md",
]
EXPECTED_GATES = [f"G{i}" for i in range(7)]


class GateError(ValueError):
    """An evidence claim cannot be accepted as a structurally complete gate."""


def read_catalogue() -> dict:
    obj = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    gates = obj["gates"]
    if obj.get("notNormative") is not True or obj.get("notCertification") is not True:
        raise GateError("pilot catalogue cannot acquire normative or certification authority")
    if [g.get("id") for g in gates] != EXPECTED_GATES:
        raise GateError("gate IDs must be exactly G0..G6, ordered and unique")
    if set(obj.get("gateStatuses", [])) != {"not-assessed", "passed", "blocked", "failed"}:
        raise GateError("gate status vocabulary must preserve indeterminacy and failure")
    for gate in gates:
        if not all(gate.get(k) for k in ("title", "owner", "entry", "outcome", "stop")):
            raise GateError(f"{gate.get('id')}: incomplete gate contract")
        if len(set(gate.get("evidence", []))) != len(gate.get("evidence", [])) or not gate.get("evidence"):
            raise GateError(f"{gate['id']}: duplicate or missing evidence slots")
    return obj


def validate_record(record: dict, catalogue: dict, evidence_root: Path) -> None:
    """Verify only local evidence manifest consistency, never substantive authority."""
    if record.get("pilotType") not in {"repository-dry-run", "participant-pilot"}:
        raise GateError("pilot type must be declared")
    if record.get("independence") not in {"repository-self", "participant-self", "externally-assessed"}:
        raise GateError("independence classification missing or unknown")
    if record["pilotType"] == "repository-dry-run" and record["independence"] != "repository-self":
        raise GateError("repository evidence cannot claim external independence")
    if record["pilotType"] == "participant-pilot" and record["independence"] == "repository-self":
        raise GateError("participant pilot cannot inherit repository evidence classification")
    entries = record.get("gates")
    if not isinstance(entries, list) or [g.get("id") for g in entries] != EXPECTED_GATES:
        raise GateError("all G0..G6 gate records are required in order")
    statuses = catalogue["gateStatuses"]
    root = evidence_root.resolve()
    for i, (entry, policy) in enumerate(zip(entries, catalogue["gates"])):
        gid = entry["id"]
        state = entry.get("status")
        if state not in statuses:
            raise GateError(f"{gid}: invalid status")
        if state != "passed":
            continue
        if i and any(entries[j]["status"] != "passed" for j in range(i)):
            # G6 can record a defensible failed/blocked pilot, but not masquerade as
            # a fully passed technical pilot.
            if gid != "G6" or not entry.get("closeoutOfFailedPilot"):
                raise GateError(f"{gid}: preceding gate has not passed")
        if record["pilotType"] == "repository-dry-run":
            raise GateError(f"{gid}: repository test output is not an approved participant gate")
        if not entry.get("owner") or not entry.get("reviewedAt"):
            raise GateError(f"{gid}: passed gate lacks owner or review date")
        evidences = entry.get("evidence")
        if not isinstance(evidences, list):
            raise GateError(f"{gid}: missing evidence array")
        kinds = [e.get("kind") for e in evidences if isinstance(e, dict)]
        if len(kinds) != len(set(kinds)) or not set(policy["evidence"]).issubset(kinds):
            raise GateError(f"{gid}: required evidence slots missing or duplicated")
        for e in evidences:
            path = e.get("path")
            digest = e.get("sha256")
            if not isinstance(path, str) or not path or not isinstance(digest, str):
                raise GateError(f"{gid}: evidence path or digest missing")
            candidate = Path(path)
            if candidate.is_absolute() or any(part == ".." for part in candidate.parts):
                raise GateError(f"{gid}: unsafe absolute/traversal evidence path")
            file = (root / candidate).resolve()
            if not file.is_relative_to(root) or not file.is_file():
                raise GateError(f"{gid}: evidence file is absent or escapes evidence root")
            actual = hashlib.sha256(file.read_bytes()).hexdigest()
            if len(digest) != 64 or actual != digest:
                raise GateError(f"{gid}: evidence content digest mismatch")


def test_fail_closed(catalogue: dict) -> int:
    """In-memory and temporary-file adversarial proof; never pilot-gate evidence."""
    with tempfile.TemporaryDirectory(prefix="gaam-pilot-") as tmp:
        root = Path(tmp)
        data = b"synthetic example, not proof of authority\n"
        (root / "proof.txt").write_bytes(data)
        digest = hashlib.sha256(data).hexdigest()
        entries = [
            {"id": gid, "status": "not-assessed"} for gid in EXPECTED_GATES
        ]
        base = {"pilotType": "participant-pilot", "independence": "participant-self", "gates": entries}
        validate_record(base, catalogue, root)
        tests = 0

        def must_reject(obj: dict, message: str) -> None:
            nonlocal tests
            try:
                validate_record(obj, catalogue, root)
            except GateError:
                tests += 1
                return
            raise AssertionError(f"unsafe claim passed: {message}")

        def passed_gate(kind: str, path: str = "proof.txt", sha: str = digest) -> dict:
            return {"id": "G0", "status": "passed", "owner": "synthetic-test-owner",
                    "reviewedAt": "2026-11-03", "evidence": [
                        {"kind": kind, "path": path, "sha256": sha}
                    ]}

        import copy
        claim = copy.deepcopy(base)
        claim["gates"][0] = passed_gate("approval")
        must_reject(claim, "missing charter evidence")
        claim["gates"][0]["evidence"].append({"kind": "charter", "path": "proof.txt", "sha256": digest})
        validate_record(claim, catalogue, root)  # checks structure only, not approval truth
        tests += 1
        altered = copy.deepcopy(claim)
        altered["gates"][0]["evidence"][0]["sha256"] = "0" * 64
        must_reject(altered, "tampered evidence")
        altered = copy.deepcopy(claim)
        altered["gates"][0]["evidence"][0]["path"] = "../proof.txt"
        must_reject(altered, "path traversal")
        altered = copy.deepcopy(claim)
        altered["gates"][0]["evidence"][0]["path"] = "missing.txt"
        must_reject(altered, "missing file")
        altered = copy.deepcopy(claim)
        altered["gates"][1]["status"] = "passed"
        must_reject(altered, "missing G1 evidence")
        altered = copy.deepcopy(claim)
        altered["pilotType"] = "repository-dry-run"
        altered["independence"] = "externally-assessed"
        must_reject(altered, "false independence")
        altered = copy.deepcopy(claim)
        altered["pilotType"] = "repository-dry-run"
        altered["independence"] = "repository-self"
        must_reject(altered, "repository claims gate passage")
        altered = copy.deepcopy(base)
        altered["gates"][1]["status"] = "passed"
        must_reject(altered, "skipped G0")
        altered = copy.deepcopy(base)
        altered["gates"][0]["status"] = "unknown"
        must_reject(altered, "unrecognized gate state")
        altered = copy.deepcopy(claim)
        altered["gates"][0]["evidence"].append({"kind": "approval", "path": "proof.txt", "sha256": digest})
        must_reject(altered, "duplicated kind")
        return tests


def run_existing_entry_path() -> int:
    commands = [
        ["python", "scripts/gaam.py", "validate-package", "conformance-kit/starter"],
        ["python", "scripts/gaam.py", "validate-claim",
         "conformance-kit/starter/artifacts/conformance-claim.json"],
        ["python", "scripts/gaam.py", "run-vectors", "python",
         "conformance-kit/reference_adapter.py", "--pattern", "delegation-attenuated-valid.json"],
        ["python", "scripts/gaam.py", "run-vectors", "python",
         "conformance-kit/reference_adapter.py", "--pattern", "delegation-amplification-rejected.json"],
        ["python", "scripts/gaam.py", "run-vectors", "python",
         "conformance-kit/reference_adapter.py", "--pattern", "delegation-parent-revoked-rejected.json"],
        ["python", "scripts/validate_clean_room.py"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=90)
        if result.returncode != 0:
            raise RuntimeError(f"entry-path failed: {' '.join(command)}: {result.stderr[-1000:]} {result.stdout[-1000:]}")
        if "run-vectors" in command:
            try:
                obj = json.loads(result.stdout)
                if obj.get("status") != "pass":
                    raise RuntimeError(f"unexpected vector disposition: {obj.get('status')}")
                if not obj.get("results") and not obj.get("checks"):
                    raise RuntimeError("vector run produced no assertions")
            except json.JSONDecodeError as exc:
                raise RuntimeError("vector runner did not emit parseable JSON") from exc
        print(f"PASS: {' '.join(command)}")
    return len(commands)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="also execute existing repository dry-run commands")
    args = parser.parse_args()
    cat = read_catalogue()
    for page in REQUIRED_PAGES:
        if not (ROOT / page).is_file():
            raise GateError(f"pilot documentation missing: {page}")
    checked = test_fail_closed(cat)
    print(f"PASS: {len(REQUIRED_PAGES)} pilot pages and {len(cat['gates'])} gate contracts")
    print(f"PASS: {checked} positive/adversarial gate-record cases")
    if args.run:
        n = run_existing_entry_path()
        print(f"PASS: {n} repository-authored entry-path commands")
    print("BOUNDARY: no participant gates approved; no E2/E3 or production claim")


if __name__ == "__main__":
    try:
        main()
    except (GateError, AssertionError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
