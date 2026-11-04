"""Adversarial contract tests for the bounded informative gateway scenario."""
import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "examples/delegated-agent-purchase/adopter_gateway.py"
CASE = ROOT / "examples/delegated-agent-purchase/adopter-gateway-case.json"
spec = importlib.util.spec_from_file_location("adopter_gateway", SCRIPT)
gateway = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gateway)


def case():
    return json.loads(CASE.read_text())


def result(**updates):
    data = case()
    for key, value in updates.items():
        segments = key.split("__")
        target = data
        for part in segments[:-1]:
            target = target[part]
        target[segments[-1]] = value
    return gateway.decide(data)


def test_positive_evidence_bounded_and_canonical_receipt():
    record = result()
    assert record["status"] == "permit"
    assert record["receipt"]["outcome"] == "permit"
    assert gateway.schema_valid(record["receipt"], "decision-receipt")
    assert record["effectExecuted"] is False
    assert record["evidenceClass"] == "synthetic-self-assessed"
    assert not record["independentAssurance"] and not record["composedConformance"]


def test_public_cli_replayable_deterministic_input_digest():
    run = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(case()),
                         text=True, capture_output=True, cwd=ROOT)
    assert run.returncode == 0
    assert json.loads(run.stdout) == gateway.decide(case())
    assert gateway.decide(case())["inputSha256"] == gateway.decide(case())["inputSha256"]


def test_binding_and_policy_provenance_mismatch_denied():
    for mutation in ({"request__agent": "other"}, {"delegation__parentAuthority": "unknown"},
                     {"authority__subject": "other"}, {"policy__id": "unknown"}):
        assert result(**mutation)["status"] == "deny"


def test_attenuation_and_consequential_effect_boundaries():
    assert result(delegation__delegatedScope__resources=["other"])["reason"] == "DELEGATION_AMPLIFICATION"
    assert result(delegation__delegatedScope__effects=["refund"])["reason"] == "DELEGATION_AMPLIFICATION"
    assert result(request__resource="other")["status"] == "deny"
    assert result(request__effect="refund")["status"] == "deny"
    assert result(authority__delegationPermitted=False)["status"] == "deny"


def test_revocation_expiry_and_temporal_containment():
    assert result(authority__status="revoked")["status"] == "deny"
    assert result(delegation__status="revoked")["status"] == "deny"
    assert result(authority__effectiveUntil="2026-10-01T00:00:00Z")["status"] == "deny"
    assert result(delegation__effectiveFrom="2026-12-01T00:00:00Z")["status"] == "deny"
    assert result(delegation__effectiveUntil="2027-01-01T00:00:00Z")["reason"] == "CHILD_OUTLIVES_PARENT"


def test_missing_stale_unavailable_or_future_observation_indeterminate():
    assert result(observations__authorityStatus=None)["status"] == "indeterminate"
    assert result(observations__authorityStatus__value="unknown")["status"] == "indeterminate"
    assert result(observations__delegationStatus__observedAt="2026-01-01T00:00:00Z")["status"] == "indeterminate"
    assert result(observations__policyStatus__observedAt="2027-01-01T00:00:00Z")["status"] == "indeterminate"
    assert result(observations__actorBinding__value="unverified")["status"] == "indeterminate"


def test_opaque_or_unknown_scope_cannot_silently_grant():
    assert result(delegation__delegatedScope={"opaquePurpose": "purchase"})["reason"] == "UNSUPPORTED_SCOPE"
    assert result(authority__scope={})["reason"] == "UNSUPPORTED_SCOPE"
    assert result(policy__maxObservationAgeSeconds=0)["reason"] == "UNSUPPORTED_POLICY"


def test_schema_valid_artifact_does_not_prove_live_effective_authority():
    bundle = case()
    assert gateway.schema_valid(bundle["authority"], "authority")
    assert gateway.schema_valid(bundle["delegation"], "delegation")
    bundle["observations"].pop("authorityStatus")
    assert gateway.decide(bundle)["status"] == "indeterminate"


def test_receipt_is_not_enforcement_or_replay_protection():
    record = result()
    assert record["receipt"] and not record["effectExecuted"]
    assert record["inputSha256"] == result()["inputSha256"]


def test_malformed_input_never_executes():
    run = subprocess.run([sys.executable, str(SCRIPT)], input="not json", text=True,
                         capture_output=True, cwd=ROOT)
    record = json.loads(run.stdout)
    assert run.returncode == 2
    assert record["status"] == "indeterminate" and not record["effectExecuted"]


def test_observation_source_label_is_not_authenticated_by_example():
    # This is a documented negative assurance finding, not a desired
    # production authorization behaviour. Source text is not verified.
    bundle = case()
    bundle["observations"]["authorityStatus"]["source"] = "untrusted-claimant"
    record = gateway.decide(bundle)
    assert record["status"] == "permit"
    assert record["effectExecuted"] is False
    assert record["independentAssurance"] is False
    assert record["evidenceClass"] == "synthetic-self-assessed"


def test_conflicting_external_observation_is_not_supported_by_local_contract():
    # A second, contradictory observation is outside the one-record format.
    # Do not mislabel an untested conflict adjudication as PASS.
    bundle = case()
    bundle["observations"]["authorityStatus"]["conflictingObservation"] = {
        "value": "revoked", "source": "another-provider"
    }
    record = gateway.decide(bundle)
    assert record["status"] == "indeterminate"
    assert record["reason"] == "INSUFFICIENT_OBSERVATION"
    assert record["effectExecuted"] is False
