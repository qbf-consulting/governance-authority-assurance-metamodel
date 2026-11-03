"""Regression tests for the portable vector-runner argument contract."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAAM = [sys.executable, str(ROOT / "scripts" / "gaam.py"), "run-vectors"]
ADAPTER = [sys.executable, str(ROOT / "conformance-kit" / "reference_adapter.py")]


def run(args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True)


def test_pattern_before_adapter_selects_subset():
    result = run(GAAM + ["--pattern", "delegation-*.json"] + ADAPTER)
    report = json.loads(result.stdout)
    assert result.returncode == 0 and report["status"] == "pass"
    assert 0 < len(report["checks"]) < 46
    assert all(check["id"].startswith("delegation-") for check in report["checks"])


def test_pattern_after_adapter_is_rejected():
    result = run(GAAM + ADAPTER + ["--pattern", "delegation-*.json"])
    assert result.returncode != 0
    assert "--pattern must precede the adapter command" in result.stderr


def test_unmatched_pattern_fails():
    result = run(GAAM + ["--pattern", "zzz-*.json"] + ADAPTER)
    assert result.returncode != 0
    assert json.loads(result.stdout)["status"] == "fail"
