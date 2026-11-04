#!/usr/bin/env python3
"""Repository-controlled INFORMATIVE gateway exercise; no effect execution or independent assurance."""
import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]


def stamp(value):
    if not isinstance(value, str):
        raise ValueError("timestamp missing")
    instant = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if instant.tzinfo is None:
        raise ValueError("timezone missing")
    return instant.astimezone(timezone.utc)


def schema_valid(artifact, kind):
    if not isinstance(artifact, dict):
        return False
    schema = json.loads((ROOT / "schemas" / (kind + ".schema.json")).read_text())
    return Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(artifact)


def typed_set(obj, name):
    values = obj.get(name)
    if not isinstance(values, list) or not values or any(not isinstance(x, str) or not x for x in values):
        return None
    return set(values)


def evaluate(bundle):
    """Only explicit scenario-local comparison semantics, never a new GAAM rule."""
    if not isinstance(bundle, dict):
        return "indeterminate", "INVALID_INPUT"
    req, obs, policy = (bundle.get(k) for k in ("request", "observations", "policy"))
    a, d = bundle.get("authority"), bundle.get("delegation")
    if not isinstance(req, dict) or not isinstance(obs, dict) or not isinstance(policy, dict):
        return "indeterminate", "MISSING_CONTEXT"
    try:
        at = stamp(bundle.get("evaluationTime"))
    except (ValueError, TypeError, AttributeError):
        return "indeterminate", "INVALID_EVALUATION_TIME"
    if not schema_valid(a, "authority") or not schema_valid(d, "delegation"):
        return "indeterminate", "INVALID_CANONICAL_ARTIFACT"
    if any(not isinstance(req.get(k), str) or not req[k] for k in ("id", "principal", "agent", "resource", "action", "effect")):
        return "indeterminate", "INVALID_REQUEST"
    if (a["subject"] != req["principal"] or d["delegator"] != req["principal"] or
            d["delegate"] != req["agent"] or d["parentAuthority"] != a["id"]):
        return "deny", "DELEGATION_BINDING_MISMATCH"
    if a.get("delegationPermitted") is not True:
        return "deny", "DELEGATION_NOT_PERMITTED"
    if a["status"] != "active" or d["status"] != "active":
        return "deny", "INACTIVE_AUTHORITY_OR_DELEGATION"
    try:
        for item in (a, d):
            if at < stamp(item["effectiveFrom"]) or (item.get("effectiveUntil") and at >= stamp(item["effectiveUntil"])):
                return "deny", "OUTSIDE_EFFECTIVE_PERIOD"
        if d.get("effectiveUntil") and a.get("effectiveUntil") and stamp(d["effectiveUntil"]) > stamp(a["effectiveUntil"]):
            return "deny", "CHILD_OUTLIVES_PARENT"
    except (ValueError, TypeError, AttributeError, KeyError):
        return "indeterminate", "INVALID_EFFECTIVE_PERIOD"

    # Scope objects are opaque in the normative GAAM schemas. The following
    # resources/actions/effects convention belongs ONLY to this informative test.
    parent, child = a["scope"], d["delegatedScope"]
    if set(parent) != {"resources", "actions"} or set(child) != {"resources", "actions", "effects"}:
        return "indeterminate", "UNSUPPORTED_SCOPE"
    pr, pa = typed_set(parent, "resources"), typed_set(parent, "actions")
    cr, ca, ce = typed_set(child, "resources"), typed_set(child, "actions"), typed_set(child, "effects")
    if any(x is None for x in (pr, pa, cr, ca, ce)):
        return "indeterminate", "UNSUPPORTED_SCOPE"
    if not cr <= pr or not ca <= pa or not ce <= set(a["permittedEffects"]):
        return "deny", "DELEGATION_AMPLIFICATION"
    if (req["resource"] not in cr or req["action"] not in ca or
            req["effect"] not in ce or req["effect"] in a.get("prohibitedEffects", [])):
        return "deny", "REQUEST_OUT_OF_SCOPE"

    # Policy is a local input contract, NOT a normative GAAM policy schema.
    if policy.get("id") != a["authoritySource"]:
        return "deny", "POLICY_BINDING_MISMATCH"
    if set(policy) != {"id", "status", "effects", "resources", "maxObservationAgeSeconds"}:
        return "indeterminate", "UNSUPPORTED_POLICY"
    if policy["status"] != "active":
        return "deny", "POLICY_INACTIVE"
    ttl = policy["maxObservationAgeSeconds"]
    if type(ttl) is not int or ttl <= 0 or ttl > 86400:
        return "indeterminate", "UNSUPPORTED_POLICY"
    pe, pres = typed_set(policy, "effects"), typed_set(policy, "resources")
    if pe is None or pres is None:
        return "indeterminate", "UNSUPPORTED_POLICY"
    if req["effect"] not in pe or req["resource"] not in pres:
        return "deny", "POLICY_REJECTED"

    for key in ("actorBinding", "authorityStatus", "delegationStatus", "policyStatus"):
        observation = obs.get(key)
        if observation is None:
            return "indeterminate", "MISSING_OBSERVATION"
        if not isinstance(observation, dict) or set(observation) != {"value", "observedAt", "source", "evidenceId"}:
            return "indeterminate", "INSUFFICIENT_OBSERVATION"
        if any(not isinstance(observation.get(k), str) or not observation[k] for k in ("source", "evidenceId")):
            return "indeterminate", "INSUFFICIENT_OBSERVATION"
        try:
            seen = stamp(observation["observedAt"])
        except (ValueError, TypeError, AttributeError):
            return "indeterminate", "INVALID_OBSERVATION_TIME"
        if seen > at or at - seen > timedelta(seconds=ttl):
            return "indeterminate", "STALE_OR_FUTURE_OBSERVATION"
        expected = "verified" if key == "actorBinding" else "active"
        if observation["value"] != expected:
            return "indeterminate", "UNRESOLVED_OBSERVATION"
    # Observations are provided by the scenario, not cryptographically verified.
    return "permit", "SCENARIO_LOCAL_CHECKS_SATISFIED"


def decide(bundle):
    verdict, reason = evaluate(bundle)
    digest = hashlib.sha256(json.dumps(bundle, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()
    record = {"status": verdict, "reason": reason, "inputSha256": digest,
              "effectExecuted": False, "evidenceClass": "synthetic-self-assessed",
              "independentAssurance": False, "composedConformance": False, "receipt": None}
    if isinstance(bundle, dict):
        a, p, req = (bundle.get(k) for k in ("authority", "policy", "request"))
        at = bundle.get("evaluationTime")
        if (isinstance(a, dict) and isinstance(p, dict) and isinstance(req, dict) and
                all(isinstance(x, str) and x for x in (a.get("id"), p.get("id"), req.get("id"), at))):
            receipt = {
                "id": "urn:gaam:example:purchase:receipt:" + digest[:20],
                "type": "decision-receipt",
                "decision": "urn:gaam:example:purchase:decision:" + digest[:20],
                "authority": [a["id"]], "policy": [p["id"]],
                "outcome": ("permit" if verdict == "permit" else
                            "deny" if verdict == "deny" else "require-additional-evidence"),
                "decisionTime": at, "enforcementPoint": "scenario-local-gateway",
                "accountableParty": (a.get("accountableParties") or ["scenario-operator"])[0],
            }
            if schema_valid(receipt, "decision-receipt"):
                record["receipt"] = receipt
    return record


def main():
    try:
        case = json.load(sys.stdin)
    except (ValueError, UnicodeError):
        print(json.dumps({"status": "indeterminate", "reason": "INVALID_JSON", "effectExecuted": False}))
        return 2
    print(json.dumps(decide(case), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
