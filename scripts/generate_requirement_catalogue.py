#!/usr/bin/env python3
"""Generate and verify GAAM's derivative normative-requirement catalogues."""
from pathlib import Path
import argparse, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "specification/governance-authority-assurance-metamodel.md"
JSON_OUT = ROOT / "artifacts/gaam-v0.9.0-requirements.json"
MD_OUT = ROOT / "artifacts/gaam-v0.9.0-requirements.md"
PATTERN = re.compile(r"\\*\\*(GAAM-[A-Z0-9-]+):\\*\\*\\s*([\\s\\S]*?)(?=\\n\\n|\\n\\*\\*GAAM-|$)")

def requirements():
    text = SOURCE.read_text()
    rows = [{"id": m.group(1), "text": re.sub(r"\\s+", " ", m.group(2)).strip()} for m in PATTERN.finditer(text)]
    ids = [r["id"] for r in rows]
    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    if duplicates:
        raise SystemExit("duplicate requirement identifiers: " + ", ".join(duplicates))
    if not rows:
        raise SystemExit("no GAAM requirements found")
    return rows

def render_json(rows):
    return json.dumps({
        "title": "GAAM v0.9.0 Normative Requirement Catalogue",
        "version": "0.9.0",
        "status": "Candidate Specification",
        "normativeSource": "specification/governance-authority-assurance-metamodel.md",
        "derivative": True,
        "requirementCount": len(rows),
        "requirements": rows,
    }, indent=2) + "\\n"

def render_md(rows):
    groups = {}
    for row in rows:
        groups.setdefault(row["id"].split("-")[1], []).append(row)
    out = """---
title: "Normative Requirement Catalogue"
permalink: /specification/requirements/
parent: "Documentation"
nav_order: 6
artifact_type: "Generated normative requirement catalogue"
normative_status: "Derivative index"
---
# Normative Requirement Catalogue

{% include gaam-meta.html %}

> This catalogue is generated from the authoritative human-readable Candidate Specification. It is a navigation and traceability aid, not an independent normative source. If this catalogue and the specification differ, the specification controls.

**Source:** [Governance, Authority and Assurance Metamodel v0.9.0](../specification/governance-authority-assurance-metamodel.md)  
**Requirement count:** %d  
**Identifier form:** \`GAAM-<SECTION>-<NUMBER>\`

""" % len(rows)
    for group, items in groups.items():
        out += f"## {group}\\n\\n| Requirement | Normative text |\\n|---|---|\\n"
        for row in items:
            body = row["text"].replace("|", "\\\\|").replace("\\n", " ")
            out += f'| \`{row["id"]}\` | {body} |\\n'
        out += "\\n"
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    rows = requirements()
    expected = {JSON_OUT: render_json(rows), MD_OUT: render_md(rows)}
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, content in expected.items() if not p.exists() or p.read_text() != content]
        if stale:
            print("stale generated requirement catalogues: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"requirement catalogue verified: {len(rows)} unique requirements")
        return 0
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    print(f"generated {len(rows)} unique requirements")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
