"""The gateway evidence dossier runs the public CLI and records limitations honestly."""
import importlib.util
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/generate_gateway_evidence.py"
spec = importlib.util.spec_from_file_location("generate_gateway_evidence", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_dossier_cases_include_positive_negative_indeterminate_and_false_success():
    rows = {row[0]: row for row in mod.cases()}
    assert all(key in rows for key in ("valid-local", "revoked-authority", "amplified-resource",
                   "missing-observation", "stale-observation", "conflicting-observation",
                   "untrusted-source-label", "invalid-json"))
    assert rows["untrusted-source-label"][2] == "permit"  # known E1 limitation, NOT operational authorization
    assert rows["conflicting-observation"][2] == "indeterminate"

def test_dossier_invokes_cli_and_preserves_source_context():
    result = mod.evaluate_all()
    assert result["summary"]["failed"] == 0
    assert result["summary"]["total"] >= 16
    assert result["synthetic"] and not result["independentAssurance"]
    assert len(result["sourceCommit"]) == 40
    assert result["normativeSemanticBaseline"] == "0.9.0"
    assert result["evaluationClock"] == "2026-11-04T10:00:00Z"
    for row in result["cases"]:
        assert row["inputSha256"] and row["expected"] == row["observed"]
        assert row["startedAt"] and row["completedAt"]
        assert row["observed"]["effectExecuted"] is False
    assert any(row["limitations"] for row in result["cases"])
