#!/usr/bin/env python3
"""Reject links from published Markdown into Jekyll-excluded directories."""
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
excluded = [Path(e) for e in yaml.safe_load((ROOT / "_config.yml").read_text()).get("exclude", [])]
LINK = re.compile(r"\]\(([^)\s]+)\)")


def is_excluded(rel):
    return any(rel == e or e in rel.parents for e in excluded)


problems = []
for page in sorted(ROOT.rglob("*.md")):
    relative = page.relative_to(ROOT)
    if is_excluded(relative) or relative.parts[0] in {".git", "node_modules", "vendor", "_site"}:
        continue
    for target in LINK.findall(page.read_text(errors="ignore")):
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|/|\{\{)", target, re.I):
            continue
        local = target.split("#", 1)[0].split("?", 1)[0]
        if not local:
            continue
        resolved = (page.parent / local).resolve()
        try:
            rel_target = resolved.relative_to(ROOT)
        except ValueError:
            continue
        if is_excluded(rel_target):
            problems.append(f"{relative} -> {rel_target}")
for problem in problems:
    print("EXCLUDED-LINK", problem)
print(f"check_excluded_links.py: {len(problems)} link(s) into Jekyll-excluded paths")
sys.exit(bool(problems))
