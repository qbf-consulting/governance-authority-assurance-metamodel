"""Falsification tests for requirement reference auditing."""
import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit_traceability.py"
spec = importlib.util.spec_from_file_location("audit_traceability", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def row(name, refs):
    return {"requirement_id": name, "testability": "behavioural-testable", "test_ids": refs}


def test_vector_link_is_not_assurance():
    result = module.audit([row("GAAM-X-001", "v1-valid")], {"v1-valid"})
    item = result["requirements"][0]
    assert item["evidenceDisposition"] == "reference-only"
    assert item["requirementSpecificallyVerified"] is False
    assert result["assuranceLevel"] == "not-assessed"


def test_placeholder_is_never_a_test():
    result = module.audit([row("GAAM-X-002", "claim-level-evidence")], set())
    assert result["requirements"][0]["evidenceDisposition"] == "non-test-placeholder"
    assert not result["requirements"][0]["references"]


def test_missing_reference_is_explicit():
    result = module.audit([row("GAAM-X-003", "nonexistent-rejected")], set())
    assert result["requirements"][0]["unresolved"] == ["nonexistent-rejected"]


def test_duplicate_requirement_fails():
    with pytest.raises(ValueError, match="duplicate"):
        module.audit([row("GAAM-X-004", ""), row("GAAM-X-004", "")], set())
