"""Tests for v2 raw-artifact validation and verdict/reason anti-gaming."""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = [sys.executable, str(ROOT / "scripts" / "gaam.py"), "run-vectors", "--suite", "v2"]
ADAPTER = [sys.executable, str(ROOT / "conformance-kit" / "reference_adapter.py")]


def run(command):
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True)


def test_raw_artifact_vectors_pass_reference_semantics():
    result = run(RUNNER + ADAPTER)
    assert result.returncode == 0, result.stderr + result.stdout
    checks = json.loads(result.stdout)["checks"]
    assert len(checks) == 5 and all(x["status"] == "pass" for x in checks)


def test_always_deny_cannot_pass_raw_suite():
    liar = [sys.executable, "-c", "import json;print(json.dumps({'valid': False, 'reason': 'AUTH_REVOKED'}))"]
    result = run(RUNNER + liar)
    assert result.returncode != 0
    report = json.loads(result.stdout)
    assert report["status"] == "fail"
    assert any(x["status"] == "fail" for x in report["checks"])


def test_v1_default_remains_unchanged():
    result = run([sys.executable, str(ROOT / "scripts" / "gaam.py"), "run-vectors", "--pattern", "delegation-*.json"] + ADAPTER)
    assert result.returncode == 0
    assert len(json.loads(result.stdout)["checks"]) == 8
