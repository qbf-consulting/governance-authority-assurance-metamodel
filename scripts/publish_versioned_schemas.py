#!/usr/bin/env python3
"""Mirror retained schemas into their versioned GitHub Pages publication path.

Schema $id values are retained normative identifiers. They remain unchanged
when stewardship or hosting moves. release.json therefore distinguishes the
retained schemaBase from the current publicationBase.

Run after `jekyll build` and before validating or uploading _site/.
"""
from pathlib import Path
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


def main() -> int:
    release = json.loads((ROOT / "release.json").read_text())
    version = release["version"]
    canonical_version = release.get("canonicalArtifactVersion", release.get("semanticBaseline", release["normativeVersion"]))
    schema_base = release["schemaBase"]
    publication_base = release.get("publicationBase", schema_base)
    version_path = f"v{canonical_version}"

    if not publication_base.rstrip("/").endswith(f"/{version_path}/schemas"):
        print(f"error: publicationBase does not match canonical artifact version path {version_path}: {publication_base}", file=sys.stderr)
        return 1

    if not SITE.is_dir():
        print(f"error: {SITE} does not exist; run jekyll build first", file=sys.stderr)
        return 1

    dest = SITE / version_path / "schemas"
    dest.mkdir(parents=True, exist_ok=True)

    schemas = sorted((ROOT / "schemas").glob("*.schema.json"))
    if not schemas:
        print("error: no schema files found under schemas/", file=sys.stderr)
        return 1

    for src in schemas:
        shutil.copy2(src, dest / src.name)

    # Retained normative identities must continue to match schemaBase. Hosting
    # migration changes publicationBase only; rewriting $id would mutate the
    # retained v0.9.0 bytes and is therefore prohibited by this check.
    mismatched = []
    for src in schemas:
        data = json.loads(src.read_text())
        sid = data.get("$id", "")
        if not sid.startswith(schema_base):
            mismatched.append((src.name, sid))
    if mismatched:
        for name, sid in mismatched:
            print(f"error: {name} retained $id does not start with schemaBase: {sid}", file=sys.stderr)
        return 1

    print(
        f"Mirrored {len(schemas)} retained schema(s) to {dest.relative_to(ROOT)} "
        f"(release {version}; publication base {publication_base})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
