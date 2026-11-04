#!/usr/bin/env python3
"""Validate GAAM's repository-controlled clean-room adoption path."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation-reports" / "fixtures" / "clean-room-implementation-report.json"
MANIFEST = ROOT / "implementation-reports" / "fixtures" / "clean-room-evidence-manifest.json"
REPORT_SCHEMA = ROOT / "implementation-reports" / "implementation-report.schema.json"
MANIFEST_SCHEMA = ROOT / "implementation-reports" / "evidence-manifest.schema.json"
FOUNDATION = ROOT / "profiles" / "manifests" / "foundation.json"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def schema_errors(instance, schema):
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return sorted(validator.iter_errors(instance), key=lambda e: list(e.path))



def audit_fixture_evidence(report, manifest, root, manifest_reference):
    """Check synthetic evidence links and bytes, not independent conformance."""
    failures = []
    if report.get("evidenceManifest") != manifest_reference:
        failures.append("report does not reference the checked evidence manifest")
    if report.get("gaamVersion") != manifest.get("gaamVersion"):
        failures.append("report and evidence manifest GAAM versions differ")
    artifacts = manifest.get("artifacts", [])
    ids = [a.get("evidenceId") for a in artifacts]
    if len(ids) != len(set(ids)):
        failures.append("duplicate evidence IDs")
    by_id = {a.get("evidenceId"): a for a in artifacts}
    results = report.get("results", [])
    result_ids = [v.get("resultId") for v in results]
    if len(result_ids) != len(set(result_ids)):
        failures.append("duplicate result IDs")
    evaluated = set(report.get("requirementsEvaluated", []))
    observed = {v.get("requirementId") for v in results}
    for requirement in sorted(evaluated - observed):
        failures.append(f"{requirement}: evaluated requirement has no result")
    for result in results:
        rid = result.get("resultId")
        requirement = result.get("requirementId")
        if requirement not in evaluated:
            failures.append(f"{rid}: result requirement not declared evaluated")
        citations = result.get("evidenceIds", [])
        if result.get("status") == "pass" and not citations:
            failures.append(f"{rid}: passing result has no evidence IDs")
        for eid in citations:
            evidence = by_id.get(eid)
            if evidence is None:
                failures.append(f"{rid}: evidence {eid} absent from manifest")
            elif requirement not in evidence.get("supports", []):
                failures.append(f"{rid}: evidence {eid} does not support {requirement}")
    for artifact in artifacts:
        relative = artifact.get("path")
        if not isinstance(relative, str) or not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
            failures.append(f"unsafe evidence path: {relative}")
            continue
        target = (root / relative).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            failures.append(f"evidence path escapes repository: {relative}")
            continue
        if not target.is_file():
            failures.append(f"evidence path missing: {relative}")
        elif hashlib.sha256(target.read_bytes()).hexdigest() != artifact.get("sha256"):
            failures.append(f"evidence checksum mismatch: {relative}")
    return failures


def main():
    errors = []
    report = read_json(REPORT)
    manifest = read_json(MANIFEST)
    foundation = read_json(FOUNDATION)

    for label, instance, schema_path in (
        ("implementation report", report, REPORT_SCHEMA),
        ("evidence manifest", manifest, MANIFEST_SCHEMA),
    ):
        found = schema_errors(instance, read_json(schema_path))
        if found:
            errors.append(f"{label} schema: {found[0].message}")

    if report.get("reportId") != manifest.get("reportId"):
        errors.append("clean-room report and evidence manifest reportId differ")
    if report.get("synthetic") is not True:
        errors.append("clean-room report must remain synthetic")
    if report.get("reportStatus") == "accepted":
        errors.append("clean-room report must never be accepted candidate-readiness evidence")
    independence = report.get("independence", {})
    if independence.get("classification") != "self":
        errors.append("repository clean-room exercise must remain self-assessed")
    if independence.get("relationshipsDisclosed") is not True:
        errors.append("repository clean-room exercise must disclose its relationship")
    if report.get("profiles") != [foundation.get("id")]:
        errors.append("clean-room fixture must explicitly target the Foundation Profile")
    foundation_requirements = set(foundation.get("requirements", []))
    reported_requirements = set(report.get("requirementsEvaluated", []))
    if not reported_requirements or not reported_requirements.issubset(foundation_requirements):
        errors.append("clean-room evaluated requirements must be a non-empty Foundation subset")

    errors.extend(audit_fixture_evidence(
        report, manifest, ROOT, str(MANIFEST.relative_to(ROOT))
    ))

    commands = [
        [sys.executable, "scripts/gaam.py", "validate-package", "conformance-kit/starter"],
        [sys.executable, "scripts/gaam.py", "validate-claim", "conformance-kit/starter/artifacts/conformance-claim.json"],
        [sys.executable, "scripts/gaam.py", "run-vectors", sys.executable, "conformance-kit/reference_adapter.py"],
        [sys.executable, "scripts/gaam.py", "run-vectors", "--pattern", "delegation-*.json", sys.executable, "conformance-kit/reference_adapter.py"],
        [sys.executable, "scripts/gaam.py", "run-vectors", "--suite", "v2", sys.executable, "conformance-kit/reference_adapter.py"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            errors.append(
                "clean-room command failed: " + " ".join(command) +
                f"\nstdout={result.stdout[-500:]}\nstderr={result.stderr[-500:]}"
            )


    # Check both positive and negative expectations through the public CLI.
    # These are separate repository-authored adapter surfaces, not composed runtime enforcement.
    required = (
        (commands[3], {"delegation-attenuated-valid": True,
                       "delegation-amplification-rejected": False,
                       "delegation-parent-revoked-rejected": False}, "delegation"),
        (commands[4], {"authority-raw-active-valid": True,
                       "authority-raw-expired-rejected": False,
                       "authority-raw-not-effective-rejected": False,
                       "authority-raw-revoked-rejected": False,
                       "authority-raw-scope-rejected": False}, "raw-authority"),
    )
    for command, expectations, label in required:
        run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=90)
        try:
            data = json.loads(run.stdout)
            checks = {entry["id"]: entry for entry in data["checks"]}
            for case_id, admitted in expectations.items():
                check = checks.get(case_id, {})
                if (check.get("status") != "pass" or
                        f"expected={admitted}; actual={admitted}" not in check.get("detail", "")):
                    errors.append(f"{label}: expected admitted={admitted} result for {case_id}")
            if run.returncode or data.get("status") != "pass":
                errors.append(f"{label}: public runner did not PASS its declared fixture set")
        except (ValueError, KeyError, TypeError):
            errors.append(f"{label}: no usable machine-readable vector results")

    # A trivial always-denying adapter must not generate a false success.
    false_success = subprocess.run([
        sys.executable, "scripts/gaam.py", "run-vectors", "--suite", "v2",
        "--pattern", "authority-raw-active-valid.json", sys.executable,
        "-c", 'print(\'{"valid": false, "reason": "AUTH_REVOKED"}\')',
    ], cwd=ROOT, text=True, capture_output=True, timeout=20)
    try:
        data = json.loads(false_success.stdout)
        if (false_success.returncode == 0 or data.get("status") != "fail" or
                not any(x.get("status") == "fail" for x in data["checks"])):
            errors.append("always-deny false-success probe unexpectedly passed")
    except (ValueError, KeyError, TypeError):
        errors.append("always-deny probe lacked a machine-readable failed check")

    if errors:
        print("GAAM clean-room validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(
        "GAAM clean-room validation: PASS "
        f"({len(reported_requirements)}/{len(foundation_requirements)} Foundation requirements "
        "bounded by a synthetic self-assessed report; 5 portable commands and positive/negative/false-success probes passed)"
    )


if __name__ == "__main__":
    main()
