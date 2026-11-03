#!/usr/bin/env python3
"""Audit reference mapping without conflating test links with assurance."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "matrices" / "requirement-assurance-traceability.csv"
VECTORS = ROOT / "tests" / "behavioural"
PLACEHOLDERS = {"claim-level-evidence"}


def audit(rows, vector_ids):
    seen = set()
    results = []
    for row in rows:
        rid = row["requirement_id"]
        if rid in seen:
            raise ValueError("duplicate normative requirement ID: " + rid)
        seen.add(rid)
        references = [x for x in row["test_ids"].split(";") if x]
        placeholders = [x for x in references if x in PLACEHOLDERS]
        unresolved = [x for x in references if x not in vector_ids and x not in PLACEHOLDERS]
        # A vector reference is a mapping, not a requirement-level executable assertion.
        disposition = ("no-executable-reference" if not references else
                       "non-test-placeholder" if not set(references) - PLACEHOLDERS else
                       "reference-only")
        results.append({
            "requirementId": rid,
            "testability": row["testability"],
            "evidenceDisposition": disposition,
            "references": [x for x in references if x in vector_ids],
            "placeholders": placeholders,
            "unresolved": unresolved,
            "requirementSpecificallyVerified": False,
        })
    totals = Counter(x["evidenceDisposition"] for x in results)
    return {
        "status": "reference-audit-only",
        "assuranceLevel": "not-assessed",
        "normativeRequirements": len(results),
        "counts": dict(sorted(totals.items())),
        "requirements": results,
        "limitations": [
            "Fixture links are family-level associations, not requirement-specific assertions.",
            "Repository reference adapter results do not establish independent implementation assurance.",
            "Requirements that require human governance or operational evidence cannot be proven by schema validation."
        ],
    }


def main():
    with MATRIX.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    known = {p.stem for p in VECTORS.glob("*.json")}
    result = audit(rows, known)
    unresolved = [x for x in result["requirements"] if x["unresolved"]]
    print(json.dumps(result, indent=2, sort_keys=True))
    if unresolved:
        raise SystemExit(f"{len(unresolved)} requirement mapping(s) refer to missing behavioural fixtures")


if __name__ == "__main__":
    main()
