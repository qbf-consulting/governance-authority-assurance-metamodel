#!/usr/bin/env python3
"""Check the non-normative legacy schema-id mirror map without dereferencing IDs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "schemas/catalog.json").read_text())
release = json.loads((ROOT / "release.json").read_text())
mapping = json.loads((ROOT / "docs/schema-resolver-map.json").read_text())
old = mapping["canonicalIdPrefix"]
mirror = mapping["publishedMirrorPrefix"]
assert old == catalog["base"] == release["schemaBase"], "canonical ID base drift"
assert mirror == release["publicationBase"], "publication mirror base drift"
seen = set()
for s in catalog["schemas"]:
    name = s["name"]
    assert name not in seen, "duplicate schema name: " + name
    seen.add(name)
    assert s["id"] == old + name, "catalog ID does not match frozen base: " + name
    assert (ROOT / "schemas" / name).is_file(), "missing canonical schema: " + name
    actual = json.loads((ROOT / "schemas" / name).read_text())
    assert actual["$id"] == s["id"], "schema $id differs from catalog: " + name
print(f"Schema identifier mirror mapping: {len(seen)} consistent local IDs; remote liveness and authenticity NOT established.")
