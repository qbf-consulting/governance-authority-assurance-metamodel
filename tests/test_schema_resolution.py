"""Mirror map cannot turn unknown identifiers into trusted publications."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_map_is_informative_and_prefix_is_exact():
    m = json.loads((ROOT / "docs/schema-resolver-map.json").read_text())
    catalog = json.loads((ROOT / "schemas/catalog.json").read_text())
    assert m["status"] == "informative-derived"
    assert m["canonicalIdPrefix"] == catalog["base"]
    assert all(x["id"].startswith(m["canonicalIdPrefix"]) for x in catalog["schemas"])
    assert "not established" in m["liveness"]
