#!/usr/bin/env python3
"""Illustrative adapter for the GAAM portable conformance protocol."""
import json
import sys

from datetime import datetime, timezone


def as_time(value):
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if date.tzinfo is None:
        raise ValueError("timezone required")
    return date.astimezone(timezone.utc)


def evaluate_v2(payload):
    try:
        a = payload["artifacts"]["authority"]
        requested = payload["artifacts"]["requestedEffect"]
        at = as_time(payload["evaluationTime"])
        if a["status"] == "revoked":
            return False, "AUTH_REVOKED"
        if a["status"] != "active":
            return False, "AUTH_NOT_ACTIVE"
        if at < as_time(a["effectiveFrom"]):
            return False, "NOT_YET_EFFECTIVE"
        if a.get("effectiveUntil") and at >= as_time(a["effectiveUntil"]):
            return False, "AUTH_EXPIRED"
        if requested not in a["permittedEffects"] or requested in a.get("prohibitedEffects", []):
            return False, "EFFECT_OUT_OF_SCOPE"
        return True, "AUTHORIZED"
    except (KeyError, TypeError, ValueError, AttributeError):
        return False, "INDETERMINATE"


def evaluate_legacy(x):
    if {"status", "withinScope", "withinTime", "sourceValid"} <= x.keys():
        valid = x["status"] == "active" and x["withinScope"] and x["withinTime"] and x["sourceValid"]
    elif {"parentEffects", "childEffects"} <= x.keys():
        edges = x.get("delegationEdges", [])
        graph = {}
        for edge in edges:
            graph.setdefault(edge["from"], []).append(edge["to"])
        def cyclic(node, visiting, visited):
            if node in visiting: return True
            if node in visited: return False
            visiting.add(node)
            found = any(cyclic(child, visiting, visited) for child in graph.get(node, []))
            visiting.remove(node); visited.add(node)
            return found
        has_cycle = any(cyclic(node, set(), set()) for node in graph)
        valid = (x.get("delegationPermitted") and set(x["childEffects"]) <= set(x["parentEffects"])
                 and x.get("depth", 0) <= x.get("maxDepth", 0) and x.get("parentActive", True)
                 and x.get("childWithinParentTime", True) and not has_cycle)
    elif "events" in x:
        seq = [event.get("sequence") for event in x["events"]]
        ids = [event.get("eventId") for event in x["events"] if event.get("eventId")]
        valid = bool(seq) and seq == sorted(seq) and len(seq) == len(set(seq)) and len(ids) == len(set(ids)) and x["events"][0].get("type") == "issued"
    elif "authorityId" in x or "policyId" in x:
        valid = (all([x.get("authorityId"), x.get("policyId"), x.get("evidenceIds"), x.get("assuranceIds"), x.get("accountableParty")])
                 and x.get("evidenceFresh", True) and x.get("policyCurrent", True)
                 and x.get("receiptDigestMatches", True) and not x.get("replayed", False))
    elif "evidencePresent" in x:
        ranks = {"self": 1, "reviewed": 2, "independent": 3}
        valid = x.get("evidencePresent") and x.get("withinValidity") and ranks.get(x.get("independence"), 0) >= ranks.get(x.get("requiredIndependence"), 0)
    elif "highImpact" in x:
        valid = ((not x.get("highImpact")) or all([x.get("appealPath"), x.get("remedyPath"), x.get("affectedPartyAnalysis")])) and x.get("noticeProvided", True) and x.get("reviewIndependent", True) and x.get("remedyStateChanged", True)
    elif "stateFresh" in x:
        valid = (x.get("stateFresh") and x.get("authorityStatusKnown")) or (x.get("failurePolicy") == "fail-closed" and not x.get("effectAdmitted"))
    elif "selectedProfiles" in x:
        selected = set(x.get("selectedProfiles", [])); dependencies = x.get("dependencies", {})
        valid = all(set(dependencies.get(profile, [])) <= selected for profile in selected)
    elif x.get("researchPattern"):
        valid = all([x.get("currentAuthorityValid"), x.get("evidenceTraceable"), x.get("candidateSemanticsExplicit"), x.get("failSafe"), x.get("reviewPath")])
    else:
        valid = False
    return bool(valid)

x = json.load(sys.stdin)
if "artifacts" in x or "evaluationTime" in x:
    valid, reason = evaluate_v2(x)
    print(json.dumps({"valid": valid, "reason": reason}))
else:
    print(json.dumps({"valid": evaluate_legacy(x)}))
