"""Schema extension backward compatibility and negative-contract tests."""
import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
NEW = ROOT / "schemas" / "v0.10.0"
OLD = ROOT / "schemas"


def schema(name, base=NEW):
    s = json.loads((base / (name + ".schema.json")).read_text())
    Draft202012Validator.check_schema(s)
    return Draft202012Validator(s, format_checker=FormatChecker())


def sample(name):
    if name == "decision-receipt":
        return {"id":"receipt-1","type":"decision-receipt","decision":"permit","authority":["a"],
                "policy":["p"],"outcome":"permit","decisionTime":"2026-11-03T14:00:00Z",
                "enforcementPoint":"pep","accountableParty":"operator"}
    if name == "runtime-envelope":
        return {"id":"e","type":"runtime-envelope","actor":"agent","requestedEffect":"read",
                "authority":["a"],"policy":["p"],"evidence":[],"decisionPoint":"pep"}
    if name == "delegation":
        return {"id":"d","type":"delegation","parentAuthority":"a","delegator":"principal",
                "delegate":"agent","delegatedScope":{},"redelegation":"prohibited","status":"active",
                "effectiveFrom":"2026-01-01T00:00:00Z","propagation":"bounded-delay"}
    return {"id":"c","type":"gaam-conformance-claim","gaamVersion":"0.9.0",
            "profiles":["foundation"],"target":"pilot","level":"L0","evidence":["report"],
            "issuedBy":"operator","issuedAt":"2026-11-03T14:00:00Z"}


@pytest.mark.parametrize("name", ["decision-receipt","runtime-envelope","delegation","conformance-claim"])
def test_legacy_artifacts_remain_valid(name):
    obj = sample(name)
    assert schema(name, OLD).is_valid(obj)
    assert schema(name).is_valid(obj)


def test_receipt_extensions_valid_and_legacy_rejects():
    obj = sample("decision-receipt")
    obj["integrity"] = {"alg":"sha-256","canonicalization":"example-c14n-v1","digest":"a"*64}
    obj["contributions"] = [{"actor":"agent-a","accountableParty":"operator"}]
    assert schema("decision-receipt").is_valid(obj)
    assert not schema("decision-receipt", OLD).is_valid(obj)
    del obj["integrity"]["digest"]
    assert not schema("decision-receipt").is_valid(obj)


def test_runtime_missing_freshness_source_fails():
    obj = sample("runtime-envelope")
    obj["freshness"] = {"maxAgeSeconds":300,"statusCheckedAt":"2026-11-03T14:00:00Z"}
    assert not schema("runtime-envelope").is_valid(obj)
    obj["freshness"]["source"] = "registry"
    assert schema("runtime-envelope").is_valid(obj)
    obj["freshness"]["maxAgeSeconds"] = -1
    assert not schema("runtime-envelope").is_valid(obj)


def test_structured_scope_unknown_dimension_rejected():
    obj = sample("delegation")
    obj["structuredScope"] = {"effects":["read"],"unknownDimension":["write"]}
    assert not schema("delegation").is_valid(obj)
    obj["structuredScope"].pop("unknownDimension")
    obj["originatingPrincipal"] = "principal"
    obj["acceptance"] = {"by":"agent","at":"2026-11-03T14:00:00Z"}
    obj["propagation"] = {"mode":"bounded-delay","maxDelaySeconds":30}
    assert schema("delegation").is_valid(obj)


def test_claim_release_version_is_distinct_from_semantic_baseline():
    obj = sample("conformance-claim")
    obj["releaseVersion"] = "0.10.0"
    assert schema("conformance-claim").is_valid(obj)
    assert not schema("conformance-claim", OLD).is_valid(obj)
