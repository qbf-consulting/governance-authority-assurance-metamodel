"""Negative contract tests for the repository-owned clean-room evidence checker."""
import copy
import hashlib
from scripts.validate_clean_room import (
    ROOT, REPORT, MANIFEST, audit_fixture_evidence, read_json,
)


def fixtures():
    return copy.deepcopy(read_json(REPORT)), copy.deepcopy(read_json(MANIFEST))


def audit(report, manifest, root=ROOT):
    return audit_fixture_evidence(report, manifest, root, str(MANIFEST.relative_to(ROOT)))


def test_baseline_synthetic_fixture():
    assert audit(*fixtures()) == []


def test_pass_without_cited_evidence_is_not_sufficient():
    report, manifest = fixtures()
    report["results"][0]["evidenceIds"] = []
    assert any("passing result has no evidence" in x for x in audit(report, manifest))


def test_citation_requires_matching_requirement_support():
    report, manifest = fixtures()
    manifest["artifacts"][0]["supports"] = ["GAAM-AUTH-002"]
    assert any("does not support GAAM-AUTH-001" in x for x in audit(report, manifest))


def test_result_must_belong_to_reported_evaluation_scope():
    report, manifest = fixtures()
    report["results"][0]["requirementId"] = "GAAM-AUTH-002"
    assert any("not declared evaluated" in x for x in audit(report, manifest))


def test_all_evaluated_requirements_need_a_result():
    report, manifest = fixtures()
    report["requirementsEvaluated"].append("GAAM-AUTH-002")
    assert any("evaluated requirement has no result" in x for x in audit(report, manifest))


def test_unknown_and_duplicate_evidence_ids_fail():
    report, manifest = fixtures()
    manifest["artifacts"].append(copy.deepcopy(manifest["artifacts"][0]))
    report["results"][0]["evidenceIds"] = ["UNKNOWN-EVIDENCE"]
    errors = audit(report, manifest)
    assert any("duplicate evidence IDs" in x for x in errors)
    assert any("absent from manifest" in x for x in errors)


def test_duplicate_result_ids_fail():
    report, manifest = fixtures()
    report["results"].append(copy.deepcopy(report["results"][0]))
    assert any("duplicate result IDs" in x for x in audit(report, manifest))


def test_evidence_manifest_reference_must_match():
    report, manifest = fixtures()
    report["evidenceManifest"] = "implementation-reports/fixtures/unrelated.json"
    assert any("does not reference the checked" in x for x in audit(report, manifest))


def test_rejects_traversal_even_with_correct_digest(tmp_path):
    report, manifest = fixtures()
    root = tmp_path / "repo"
    root.mkdir()
    external = tmp_path / "external.json"
    external.write_text("test", encoding="utf-8")
    manifest["artifacts"][0]["path"] = "../external.json"
    manifest["artifacts"][0]["sha256"] = hashlib.sha256(external.read_bytes()).hexdigest()
    assert any("unsafe evidence path" in x for x in audit(report, manifest, root))


def test_rejects_symlink_escape_even_with_correct_digest(tmp_path):
    report, manifest = fixtures()
    root = tmp_path / "repo"
    root.mkdir()
    external = tmp_path / "external.json"
    external.write_text("test", encoding="utf-8")
    (root / "linked.json").symlink_to(external)
    manifest["artifacts"][0]["path"] = "linked.json"
    manifest["artifacts"][0]["sha256"] = hashlib.sha256(external.read_bytes()).hexdigest()
    assert any("escapes repository" in x for x in audit(report, manifest, root))


def test_report_manifest_version_mismatch_fails():
    report, manifest = fixtures()
    manifest["gaamVersion"] = "0.10.0"
    assert any("GAAM versions differ" in x for x in audit(report, manifest))
