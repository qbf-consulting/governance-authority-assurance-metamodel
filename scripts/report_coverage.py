#!/usr/bin/env python3
"""Summarize GAAM requirement traceability without claiming conformance."""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROWS = ROOT / "matrices/requirement-assurance-traceability.csv"
GUIDE = ROOT / "docs/requirement-evidence-coverage.md"
CLASSES = ["behavioural-testable", "mixed", "structural-testable", "reviewable", "procedural", "observable"]

def summary():
    with ROWS.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    category = Counter(row["testability"] for row in rows)
    ids = [item for row in rows for item in row["test_ids"].split(";") if item]
    linked = sum(bool(row["test_ids"].strip()) for row in rows)
    negative = sum(any(re.search(r"rejected|invalid|fail-open", item) for item in row["test_ids"].split(";")) for row in rows)
    return {"total": len(rows), "categories": dict(category), "linked_requirements": linked, "negative_named_requirements": negative, "distinct_test_ids": len(set(ids))}

def check(summary):
    text = GUIDE.read_text(encoding="utf-8")
    errors = []
    for name in CLASSES:
        pattern = rf"^\\| {re.escape(name.capitalize() if name == 'mixed' else name.capitalize())} \\| \\*\\*?"
        # Match the row with its actual display name and avoid interpreting prose percentages.
        display = name[0].upper() + name[1:]
        row = f"| {display} | {summary['categories'].get(name, 0)} |"
        if row not in text:
            errors.append(f"coverage category drift: {row}")
    for required in [
        f"| **Total** | **{summary['total']}** |",
        f"**{summary['linked_requirements']}/{summary['total']}**",
        f"**{summary['negative_named_requirements']}/{summary['total']}**",
        f"**{summary['distinct_test_ids']} distinct test IDs**",
    ]:
        if required not in text:
            errors.append(f"coverage summary drift: {required}")
    return errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    values = summary()
    errors = check(values) if args.check else []
    print(json.dumps(values, indent=2, sort_keys=True))
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
