"""Negative evidence for release-versus-specification-edition publication identity."""
import json
import sys
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from version_identity import check_repository,check_identity

def fixture():
    release=json.loads((ROOT/"release.json").read_text())
    source=(ROOT/release["normativeSpecification"]).read_text()
    index=(ROOT/"docs/current-specification.md").read_text()
    status=yaml.safe_load((ROOT/"PROJECT-STATUS.yaml").read_text())
    return release,source,index,status,(ROOT/"VERSION").read_text().strip()

def test_current_consumer_identity():
    assert check_repository(ROOT)==[]
    a,b,c,d,e=fixture()
    assert a["version"]=="0.9.5" and a["specificationEdition"]=="0.9.0"
    assert a["semanticBaseline"]==a["canonicalArtifactVersion"]=="0.9.0"
    assert check_identity(a,b,c,d,e)==[]

def test_fake_edition_without_new_normative_source_fails():
    a,b,c,d,e=fixture()
    a["specificationEdition"]="0.9.5"
    issues=check_identity(a,b,c,d,e)
    assert any("document title" in x for x in issues)
    assert any("semantic baseline" in x for x in issues)

def test_legacy_release_identity_drift_fails():
    a,b,c,d,e=fixture()
    a["normativeVersion"]="0.9.0"
    assert any("legacy Candidate" in x for x in check_identity(a,b,c,d,e))

def test_stale_current_edition_page_fails():
    a,b,c,d,e=fixture()
    c=c.replace("**Current specification edition:** v0.9.0","**Current specification edition:** v0.9.5")
    assert any("index edition" in x for x in check_identity(a,b,c,d,e))

def test_historical_permalink_drift_fails():
    a,b,c,d,e=fixture()
    b=b.replace("permalink: /specification/gaam-v0.9.0/","permalink: /specification/gaam-v0.9.5/")
    assert any("historical permalink" in x for x in check_identity(a,b,c,d,e))

def test_status_and_schema_namespace_drift_fail():
    a,b,c,d,e=fixture()
    d["project"]["specification_edition"]="0.9.5"
    a["schemaBase"]=a["schemaBase"].replace("v0.9.0","v0.9.5")
    issues=check_identity(a,b,c,d,e)
    assert any("PROJECT-STATUS specification" in x for x in issues)
    assert any("schemaBase canonical" in x for x in issues)

def test_missing_specification_edition_fails_closed():
    a,b,c,d,e=fixture()
    a.pop("specificationEdition")
    assert check_identity(a,b,c,d,e)==["missing or invalid specificationEdition"]
