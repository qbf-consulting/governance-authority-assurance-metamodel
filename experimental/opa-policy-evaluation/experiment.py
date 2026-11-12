#!/usr/bin/env python3
"""Bounded OPA predicate experiment; never returns an authorization or effect."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
POLICY = HERE / "policy.rego"
CLOCK = "2026-07-30T12:00:00Z"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(data):
    return "sha256:" + hashlib.sha256(data).hexdigest()


def utc(value):
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("expected UTC Z time")
    value = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None or value.utcoffset().total_seconds() != 0:
        raise ValueError("UTC time required")
    return value.astimezone(timezone.utc)


def base_input():
    example = ROOT / "examples/basic-governed-decision"
    authority = read_json(example / "authority.valid.json")
    delegation = read_json(example / "delegation.valid.json")
    return {
        "contractVersion": "1",
        "evaluationTime": CLOCK,
        "request": {"actor": delegation["delegate"], "effect": "execute-within-scope"},
        "authority": authority,
        "delegation": delegation,
        "policy": {"revision": "demo-policy-1", "state": "current", "prohibited": False},
        "evidence": {"state": "current", "observedAt": "2026-07-30T11:59:00Z",
                     "freshUntil": "2026-07-30T12:05:00Z",
                     "references": ["urn:gaam:evidence:basic-governed-decision:current"]},
        "revocation": {"state": "active"},
    }


def apply_changes(original, changes):
    data = copy.deepcopy(original)
    for path, value in changes.items():
        parts = path.split(".")
        node = data
        for key in parts[:-1]:
            if not isinstance(node, dict) or key not in node:
                raise ValueError("unknown mutation path: " + path)
            node = node[key]
        if not isinstance(node, dict):
            raise ValueError("invalid mutation target: " + path)
        node[parts[-1]] = value
    return data


def contract_complete(p):
    """Unknown, absent and conflicting required facts remain indeterminate."""
    try:
        if p["contractVersion"] != "1":
            return False
        a, d, pol, ev, rev, req = (
            p["authority"], p["delegation"], p["policy"],
            p["evidence"], p["revocation"], p["request"]
        )
        if not all(isinstance(x, dict) for x in (a, d, pol, ev, rev, req)):
            return False
        if pol["revision"] != "demo-policy-1":
            return False
        if pol["state"] not in ("current", "superseded") or type(pol["prohibited"]) is not bool:
            return False
        if a["status"] not in ("active", "revoked", "suspended", "expired"):
            return False
        if d["status"] not in ("active", "revoked", "suspended", "expired"):
            return False
        if ev["state"] not in ("current", "stale"):
            return False
        if rev["state"] not in ("active", "revoked", "suspended"):
            return False
        for item in (a["id"], a["authoritySource"], a["subject"],
                     d["parentAuthority"], d["delegate"], d["delegator"],
                     req["actor"], req["effect"]):
            if not isinstance(item, str) or not item:
                return False
        for v in (a["permittedEffects"], a["prohibitedEffects"],
                  d["delegatedScope"]["effects"]):
            if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                return False
        if type(a["delegationPermitted"]) is not bool:
            return False
        for item in (p["evaluationTime"], a["effectiveFrom"], a["effectiveUntil"],
                     d["effectiveFrom"], d["effectiveUntil"],
                     ev["observedAt"], ev["freshUntil"]):
            utc(item)
        return True
    except (ValueError, TypeError, KeyError, AttributeError):
        return False


def evaluate(p, opa="opa"):
    """OPA result can be true/false/unknown, but cannot certify legitimate authority."""
    raw = json.dumps(p, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result = {
        "status": "indeterminate", "predicateResult": None,
        "authorityEstablished": False, "enforcementAttempted": False,
        "observedEffect": None, "gaamDecisionReceipt": None,
        "policyId": "gaam-opa-experiment:demo-policy-1",
        "policyDigest": sha(POLICY.read_bytes()), "inputDigest": sha(raw),
        "evaluationTime": p.get("evaluationTime") if isinstance(p, dict) else None,
        "evidenceReferences": (p.get("evidence") or {}).get("references", [])
        if isinstance(p, dict) and isinstance(p.get("evidence"), dict) else [],
        "limitation": "Predicate only: no independently authenticated source, status, policy issuance, or effect.",
    }
    if not isinstance(p, dict) or not contract_complete(p):
        result["reason"] = "UNKNOWN_OR_INVALID_INPUT"
        return result
    with tempfile.TemporaryDirectory() as td:
        input_path = Path(td) / "input.json"
        input_path.write_bytes(raw)
        try:
            process = subprocess.run(
                [opa, "eval", "--format=json", "--data", str(POLICY),
                 "--input", str(input_path),
                 "data.gaam_opa_experiment.candidate_eligible"],
                capture_output=True, text=True, timeout=8, check=False
            )
            if process.returncode:
                result["reason"] = "OPA_ERROR"
                return result
            answer = json.loads(process.stdout)["result"][0]["expressions"][0]["value"]
            if type(answer) is not bool:
                result["reason"] = "OPA_UNDEFINED_OR_INVALID_RESULT"
                return result
        except (OSError, subprocess.TimeoutExpired):
            result["reason"] = "OPA_UNAVAILABLE"
            return result
        except (ValueError, KeyError, IndexError, TypeError):
            result["reason"] = "OPA_UNDEFINED_OR_INVALID_RESULT"
            return result

    result["status"] = "satisfied" if answer else "not-satisfied"
    result["predicateResult"] = answer
    result["reason"] = "PREDICATE_TRUE_UNVERIFIED" if answer else "PREDICATE_FALSE"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", help="Named case from cases.json; default positive")
    parser.add_argument("--all", action="store_true", help="Check all cases and false-success boundary")
    parser.add_argument("--opa", default="opa", help="OPA executable; CI pins and checks checksum")
    args = parser.parse_args()
    cases = read_json(HERE / "cases.json")["cases"]
    if args.all:
        failures = []
        for case in cases:
            record = evaluate(apply_changes(base_input(), case["mutations"]), args.opa)
            if record["status"] != case["expected"]:
                failures.append({"id": case["id"], "expected": case["expected"],
                                 "actual": record["status"], "reason": record["reason"]})
            if record["authorityEstablished"] or record["enforcementAttempted"] or record["gaamDecisionReceipt"] is not None:
                failures.append({"id": case["id"], "failure": "false governance success"})
        unavailable = evaluate(base_input(), "/nonexistent/opa")
        if unavailable["status"] != "indeterminate" or unavailable["predicateResult"] is not None:
            failures.append({"id": "engine-unavailable", "failure": "unexpected success"})
        print(json.dumps({"caseCount": len(cases), "failures": failures, "engineUnavailable": unavailable["status"],
                          "authorizationClaims": 0}, sort_keys=True))
        return int(bool(failures))
    case = next((x for x in cases if x["id"] == (args.case or "positive")), None)
    if case is None:
        parser.error("unknown case")
    print(json.dumps(evaluate(apply_changes(base_input(), case["mutations"]), args.opa), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
