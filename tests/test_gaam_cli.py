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


def _copy_starter(tmp_path):
    import shutil
    package = tmp_path / "starter"
    shutil.copytree(ROOT / "conformance-kit" / "starter", package)
    return package


def _validate_package(package):
    result = run([sys.executable, str(ROOT / "scripts" / "gaam.py"), "validate-package", str(package)])
    return result.returncode, json.loads(result.stdout)


def test_starter_package_is_valid(tmp_path):
    package = _copy_starter(tmp_path)
    code, report = _validate_package(package)
    assert code == 0 and report["status"] == "pass"


def test_package_rejects_parent_traversal_without_reading_sibling(tmp_path):
    package = _copy_starter(tmp_path)
    sibling = tmp_path / "outside.json"
    sibling.write_text('{"type":"authority"}', encoding="utf-8")
    manifest = json.loads((package / "manifest.json").read_text())
    manifest["artifacts"][0]["path"] = "../outside.json"
    (package / "manifest.json").write_text(json.dumps(manifest))
    code, report = _validate_package(package)
    assert code != 0 and report["status"] == "fail"
    assert next(x for x in report["checks"] if x["id"] == "package-paths")["status"] == "fail"


def test_package_rejects_absolute_artifact_path(tmp_path):
    package = _copy_starter(tmp_path)
    manifest = json.loads((package / "manifest.json").read_text())
    manifest["artifacts"][0]["path"] = str(tmp_path / "outside.json")
    (package / "manifest.json").write_text(json.dumps(manifest))
    code, report = _validate_package(package)
    assert code != 0
    assert next(x for x in report["checks"] if x["id"] == "package-paths")["status"] == "fail"


def test_package_rejects_symlink_escape(tmp_path):
    package = _copy_starter(tmp_path)
    sibling = tmp_path / "outside.json"
    sibling.write_text('{"type":"authority"}', encoding="utf-8")
    (package / "artifacts" / "authority.json").unlink()
    (package / "artifacts" / "authority.json").symlink_to(sibling)
    code, report = _validate_package(package)
    assert code != 0
    assert next(x for x in report["checks"] if x["id"] == "package-paths")["status"] == "fail"


def test_package_rejects_missing_declared_checksum(tmp_path):
    package = _copy_starter(tmp_path)
    checksum_path = package / "checksums.json"
    manifest = json.loads(checksum_path.read_text())
    manifest["files"] = manifest["files"][1:]
    checksum_path.write_text(json.dumps(manifest))
    code, report = _validate_package(package)
    assert code != 0
    check = next(x for x in report["checks"] if x["id"] == "package-integrity")
    assert check["status"] == "fail" and "uncovered=" in check["detail"]


def test_package_rejects_checksum_manifest_escape(tmp_path):
    package = _copy_starter(tmp_path)
    manifest = json.loads((package / "manifest.json").read_text())
    manifest["integrity"]["manifest"] = "../other-checksums.json"
    (package / "manifest.json").write_text(json.dumps(manifest))
    code, report = _validate_package(package)
    assert code != 0
    assert next(x for x in report["checks"] if x["id"] == "package-integrity")["status"] == "fail"
