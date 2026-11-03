#!/usr/bin/env python3
"""Ensure adversarial review findings cannot disappear or become silently closed."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "docs/adversarial-review-disposition-2026-11.json").read_text())["findings"]
assert len(rows) == 29, "expected 29 findings"
assert {x["id"] for x in rows} == {f"F-{i:02d}" for i in range(1, 30)}, "missing or duplicated findings"
assert all(x["state"] in {"implemented", "partial", "deferred"} for x in rows)
assert all(x.get("pr") and x.get("rationale") for x in rows)
assert {x["id"] for x in rows if x["state"] == "implemented"} == {"F-01", "F-02", "F-03", "F-04"}
print("GAAM review register: 29/29 findings dispositioned; not a conformance or finding-closure certificate")
