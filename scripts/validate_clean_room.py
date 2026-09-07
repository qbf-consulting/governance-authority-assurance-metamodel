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

manifest_ids = {item.get("evidenceId") for item in manifest.get("artifacts", [])}
for result in report.get("results", []):
    if not set(result.get("evidenceIds", [])).issubset(manifest_ids):
        errors.append(f"{result.get('resultId')}: references evidence absent from manifest")

for artifact in manifest.get("artifacts", []):
    path = ROOT / artifact.get("path", "")
    if not path.is_file():
        errors.append(f"evidence path missing: {artifact.get('path')}")
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != artifact.get("sha256"):
        errors.append(f"evidence checksum mismatch: {artifact.get('path')}")

commands = [
    [sys.executable, "scripts/gaam.py", "validate-package", "conformance-kit/starter"],
    [sys.executable, "scripts/gaam.py", "validate-claim", "conformance-kit/starter/artifacts/conformance-claim.json"],
    [sys.executable, "scripts/gaam.py", "run-vectors", sys.executable, "conformance-kit/reference_adapter.py"],
]
for command in commands:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        errors.append(
            "clean-room command failed: " + " ".join(command) +
            f"\nstdout={result.stdout[-500:]}\nstderr={result.stderr[-500:]}"
        )

if errors:
    print("GAAM clean-room validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(
    "GAAM clean-room validation: PASS "
    f"({len(reported_requirements)}/{len(foundation_requirements)} Foundation requirements "
    "bounded by a synthetic self-assessed report; 3 portable commands passed)"
)
