#!/usr/bin/env python3
"""Reject vulnerable or ambiguous GAAM npm dependency trees (read-only)."""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
RULES={"dompurify":("3.4.17", "3.4.17"), "katex":("0.18.2", "0.18.2")}
def semver(value):
    match=re.fullmatch(r"(\d+)\.(\d+)\.(\d+)",value)
    if not match:
        raise ValueError(f"unparseable version: {value!r}")
    return tuple(map(int,match.groups()))
def check(package: dict, lock: dict):
    failures=[]
    if lock.get("lockfileVersion") != 3:
        failures.append("expected npm lockfile version 3")
    declared=package.get("overrides", {})
    installed=lock.get("packages",{})
    # Version-update PRs may advance the tested major line, but moving to a
    # different major requires explicit compatibility review outside this guard.
    for name, supported_major, baseline in (
        ("mermaid", 11, (11, 16, 1)),
        ("jsdom", 26, (26, 1, 0)),
    ):
        declared_version=package.get("devDependencies", {}).get(name, "")
        match=re.fullmatch(r"\^?(\d+)\.(\d+)\.(\d+)", declared_version)
        if not match:
            failures.append(f"{name}: unsupported version requirement {declared_version!r}")
            continue
        candidate=tuple(map(int,match.groups()))
        if candidate[0]!=supported_major or candidate<baseline:
            failures.append(f"{name}: version {declared_version} outside reviewed major/baseline")
        actual=installed.get("node_modules/"+name, {}).get("version", "")
        try:
            actual_version=semver(actual)
            if actual_version[0]!=supported_major or actual_version<baseline or actual_version<candidate:
                failures.append(f"{name}: installed version {actual} outside reviewed major/baseline")
        except ValueError as exc:
            failures.append(f"{name}: installed version error: {exc}")
    for name,(minimum,target) in RULES.items():
        if declared.get(name)!=target:
            failures.append(f"{name}: expected reviewed override {target}")
        entries=[(p,m) for p,m in installed.items() if p=="node_modules/"+name or p.endswith("/node_modules/"+name)]
        if not entries:
            failures.append(f"{name}: no installed lockfile entry")
            continue
        for path,entry in entries:
            try:
                if semver(entry["version"]) < semver(minimum):
                    failures.append(f"{path}: vulnerable version {entry['version']}")
                if entry["version"]!=target:
                    failures.append(f"{path}: unreviewed version {entry['version']}, expected {target}")
            except (KeyError,ValueError) as error:
                failures.append(f"{path}: {error}")
            if entry.get("resolved")!=f"https://registry.npmjs.org/{name}/-/{name}-{target}.tgz" or not entry.get("integrity","").startswith("sha512-"):
                failures.append(f"{path}: missing canonical registry provenance or SHA-512 SRI")
    for name in RULES:
        if name not in lock["packages"]["node_modules/mermaid"].get("dependencies",{}):
            failures.append(f"Mermaid dependency chain no longer includes {name}; reassess mitigation")
    return failures

if __name__=="__main__":
    package=json.loads((ROOT/"package.json").read_text())
    lock=json.loads((ROOT/"package-lock.json").read_text())
    failures=check(package,lock)
    if failures:
        for issue in failures: print(f"FAIL: {issue}",file=sys.stderr)
        raise SystemExit(1)
    print("PASS: reviewed Mermaid -> DOMPurify/KaTeX lockfile versions, overrides and package provenance")
