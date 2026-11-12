#!/usr/bin/env python3
"""GAAM informative temporal governance pressure cases, not GAAM v0.9.0 conformance.
No output artifact is written; tests include falsification of tempting false positives.
"""
from __future__ import annotations
import copy
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "experimental/temporal-governance/cases.json"

def timestamp(value):
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("UTC timestamp required")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def assess(case):
    def result(outcome, reason):
        return {"outcome": outcome, "reason": reason}
    context = case["context"]
    try:
        effective, cutoff, evaluated = (timestamp(context[name]) for name in ("effectiveAt", "evidenceAsOf", "evaluationAt"))
    except (KeyError, TypeError, ValueError):
        return result("indeterminate", "invalid_temporal_input")
    if effective > evaluated or cutoff > evaluated:
        return result("indeterminate", "invalid_temporal_order")
    requirements = case["requirements"]
    if not requirements:
        return result("indeterminate", "requirements_missing")
    # Cutoffs and source competence are bound to the complete decision context.
    for required in requirements:
        if required.get("evidenceAsOf", context["evidenceAsOf"]) != context["evidenceAsOf"]:
            return result("indeterminate", "incompatible_temporal_context")
        source = case["sources"].get(required["source"])
        if source is None or source.get("authenticated") is not True:
            return result("indeterminate", "source_competence_or_authenticity_unverified")
        try:
            if timestamp(source["completeThrough"]) < cutoff:
                return result("indeterminate", "insufficient_authoritative_history")
        except (KeyError, ValueError, TypeError):
            return result("indeterminate", "insufficient_authoritative_history")
    records = case["records"]
    if len(set(r.get("id") for r in records)) != len(records):
        return result("indeterminate", "duplicate_record_identity")
    for record in records:
        if record.get("source") not in {r["source"] for r in requirements}:
            return result("indeterminate", "source_provenance_mismatch")
        if not record.get("recordedAt"):
            return result("indeterminate", "recording_provenance_missing")
        try:
            timestamp(record["recordedAt"])
            timestamp(record["effectiveFrom"])
            if record.get("effectiveUntil"):
                timestamp(record["effectiveUntil"])
        except (ValueError, TypeError):
            return result("indeterminate", "invalid_temporal_input")
    visible = [r for r in records if timestamp(r["recordedAt"]) <= cutoff]
    eligible = [r for r in visible if timestamp(r["effectiveFrom"]) <= effective
                and (not r.get("effectiveUntil") or effective < timestamp(r["effectiveUntil"]))]
    known_ids = {r["id"] for r in visible}
    # A correction is valid only when its target is visible and belongs to
    # the same governed assertion and competent source.
    for r in eligible:
        for target in r.get("supersedes", []):
            t = next((v for v in visible if v["id"] == target), None)
            if t is None or t["id"] == r["id"] or t["key"] != r["key"] or t["source"] != r["source"]:
                return result("indeterminate", "unresolved_supersession")
    excluded = {target for r in eligible for target in r.get("supersedes", [])}
    selected = [r for r in eligible if r["id"] not in excluded]
    for requirement in requirements:
        key, source = requirement["key"], requirement["source"]
        matching = [r for r in selected if r["key"] == key and r["source"] == source]
        if not matching:
            return result("indeterminate", "required_claim_not_established")
        if any(r.get("policyVersion") != context.get("policyVersion") for r in matching):
            return result("indeterminate", "policy_version_incompatible")
        if len(matching) != 1:
            return result("indeterminate", "unresolved_competent_conflict")
        if matching[0].get("value") not in ("affirm", "deny"):
            return result("indeterminate", "unsupported_claim_state")
    # Explicit competent negative evidence does not imply a positive decision.
    if any(next(r for r in selected if r["key"] == req["key"] and r["source"] == req["source"])["value"] == "deny"
           for req in requirements):
        return result("deny", "competent_negative_assertion")
    return result("permit", "supported_by_qualified_record")

def check_vectors():
    data = json.loads(CASES.read_text(encoding="utf-8"))
    assert data["normativeStatus"] == "non-normative"
    assert len(data["vectors"]) == len({v["id"] for v in data["vectors"]})
    for v in data["vectors"]:
        actual = assess(v)
        assert actual == v["expected"], f"{v['id']}: {actual} != {v['expected']}"
        if "receipt" in v:
            original = copy.deepcopy(v["receipt"])
            assert v["receipt"] == original and v["receipt"]["originalOutcome"] == v["requiredReceiptOutcome"]
            assert actual["outcome"] != v["receipt"]["originalOutcome"]
    return data

def false_success_probes(data):
    base = copy.deepcopy(next(v for v in data["vectors"] if v["id"] == "TG-08-composite-qualified"))
    assert assess(base)["outcome"] == "permit"
    mutations = [
        ("untrusted-source", lambda c: c["sources"]["framework-authority"].update(authenticated=False)),
        ("incomplete-history", lambda c: c["sources"]["registry-authority"].update(completeThrough="2026-10-01T00:00:00Z")),
        ("unrecorded-assertion", lambda c: c["records"][0].pop("recordedAt")),
        ("incompatible-cutoff", lambda c: c["requirements"][1].update(evidenceAsOf="2026-10-09T00:00:00Z")),
        ("policy-mismatch", lambda c: c["records"][2].update(policyVersion="framework-v9")),
        ("contradictory-evidence", lambda c: c["records"].append({
            **c["records"][0], "id": "conflict", "value": "deny"
        })),
    ]
    for name, mutation in mutations:
        changed = copy.deepcopy(base)
        mutation(changed)
        actual = assess(changed)
        assert actual["outcome"] != "permit", f"false-success probe {name}: {actual}"
    return len(mutations)

if __name__ == "__main__":
    data = check_vectors()
    probes = false_success_probes(data)
    print(f"GAAM experimental temporal governance: {len(data['vectors'])} scenarios and {probes} false-success probes passed; no normative conformance asserted")
