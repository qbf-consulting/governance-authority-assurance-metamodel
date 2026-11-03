#!/usr/bin/env python3
"""Exercise npm security policy against safe routine and unsafe major changes."""
from __future__ import annotations
import copy
import json
from pathlib import Path
from check_npm_security import check

ROOT=Path(__file__).resolve().parents[1]
p=json.loads((ROOT/"package.json").read_text())
l=json.loads((ROOT/"package-lock.json").read_text())
assert not check(p,l), "current npm security policy must pass"

def scenario(name, mutator, should_pass):
    pp=copy.deepcopy(p)
    ll=copy.deepcopy(l)
    mutator(pp,ll)
    errors=check(pp,ll)
    if (not errors) != should_pass:
        raise AssertionError(f"{name}: expected {'PASS' if should_pass else 'FAIL'}; got {errors}")
    print(f"PASS: {name} ({'allowed' if should_pass else 'rejected'})")

scenario("mermaid supported minor",lambda x,y:(x["devDependencies"].__setitem__("mermaid","11.17.2"),y["packages"]["node_modules/mermaid"].__setitem__("version","11.17.2")),True)
scenario("mermaid unreviewed major",lambda x,y:(x["devDependencies"].__setitem__("mermaid","12.2.0"),y["packages"]["node_modules/mermaid"].__setitem__("version","12.2.0")),False)
scenario("jsdom supported patch",lambda x,y:(x["devDependencies"].__setitem__("jsdom","^26.1.1"),y["packages"]["node_modules/jsdom"].__setitem__("version","26.1.1")),True)
scenario("jsdom unreviewed major",lambda x,y:(x["devDependencies"].__setitem__("jsdom","^30.1.3"),y["packages"]["node_modules/jsdom"].__setitem__("version","30.1.3")),False)
scenario("dompurify override missing",lambda x,y:x["overrides"].pop("dompurify"),False)
scenario("nested vulnerable katex",lambda x,y:y["packages"].__setitem__("node_modules/mermaid/node_modules/katex",{"version":"0.16.47"}),False)
print("PASS: npm dependency guard permits safe in-line maintenance and fails closed for major/bypass regressions")
