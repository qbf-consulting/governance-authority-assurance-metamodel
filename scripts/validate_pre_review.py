#!/usr/bin/env python3
"""Validate repository-controlled GAAM candidate pre-review dossiers."""
from pathlib import Path
import csv
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
PRE = ROOT / "governance" / "reviews" / "evidence" / "pre-review"
BASELINE = "governance/reviews/review-baseline.json"
EXPECTED = {
    "privacy-review-preparation.json": "privacy",
    "security-review-preparation.json": "security",
    "affected-party-review-preparation.json": "affected-party",
}

errors = []

reqs = set()
with (ROOT / "matrices" / "normative-requirements-index.csv").open(encoding="utf-8", newline="") as handle:
    for row in csv.DictReader(handle):
        value = row.get("requirement_id") or row.get("requirementId") or row.get("id")
        if value:
            reqs.add(value)

if not reqs:
    # The specification remains the authoritative fallback if the matrix header changes.
    import re
    text = (ROOT / "specification" / "governance-authority-assurance-metamodel.md").read_text(encoding="utf-8")
    reqs = set(re.findall(r"\bGAAM-[A-Z]+-[0-9]{3}\b", text))

for filename, review_type in EXPECTED.items():
    path = PRE / filename
    if not path.exists():
        errors.append(f"missing pre-review dossier: {filename}")
        continue
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("reviewType") != review_type:
        errors.append(f"{filename}: wrong reviewType")
    if obj.get("gaamVersion") != "0.9.0":
        errors.append(f"{filename}: gaamVersion must be 0.9.0")
    if obj.get("baseline") != BASELINE or not (ROOT / BASELINE).exists():
        errors.append(f"{filename}: must bind the frozen review baseline")
    if obj.get("status") != "prepared-not-attested":
        errors.append(f"{filename}: status must remain prepared-not-attested")
    if obj.get("independence") != "repository-controlled":
        errors.append(f"{filename}: independence must remain repository-controlled")
    if obj.get("cannotSatisfyIndependentReview") is not True:
        errors.append(f"{filename}: must explicitly prohibit satisfying independent review")
    tests = obj.get("pressureTests") or []
    if not tests:
        errors.append(f"{filename}: no pressure tests")
    seen = set()
    for test in tests:
        tid = test.get("id")
        if not tid or tid in seen:
            errors.append(f"{filename}: missing or duplicate pressure-test id")
        seen.add(tid)
        unknown = set(test.get("requirements") or []) - reqs
        if unknown:
            errors.append(f"{filename}/{tid}: unknown requirements {sorted(unknown)}")
        for evidence in test.get("evidence") or []:
            if not (ROOT / evidence).exists():
                errors.append(f"{filename}/{tid}: missing evidence path {evidence}")
        if not test.get("question") or not test.get("falsification"):
            errors.append(f"{filename}/{tid}: question and falsification are required")
    if not obj.get("reviewerOutputsRequired") or not obj.get("closureBoundary"):
        errors.append(f"{filename}: missing reviewer outputs or closure boundary")

# Hard guard: repository preparation must not mutate authoritative review state.
for filename in ("privacy-review.json", "security-review.json", "affected-party-review.json"):
    obj = json.loads((ROOT / "governance" / "reviews" / filename).read_text(encoding="utf-8"))
    if obj.get("status") == "complete":
        errors.append(f"{filename}: independent review cannot be marked complete by pre-review preparation")
    reviewer = obj.get("reviewer") or {}
    if reviewer.get("independence") == "independent" and not reviewer.get("identity"):
        errors.append(f"{filename}: cannot assert independent reviewer without identity")

if errors:
    print("GAAM candidate pre-review validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(
    "GAAM candidate pre-review validation: PASS "
    f"({sum(len(json.loads((PRE / f).read_text())['pressureTests']) for f in EXPECTED)} pressure tests; "
    "3 independent-review boundaries preserved)"
)
