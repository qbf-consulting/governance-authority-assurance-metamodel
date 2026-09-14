#!/usr/bin/env python3
"""Validate GAAM as an external adopter of the TSMM/TIS conformance boundary.

This validator is intentionally dependency-free. It validates GAAM-owned evidence
and decision invariants; it does not make TSMM or TIS normative dependencies of
GAAM and does not claim external certification.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECLARATION = ROOT / "conformance-kit/tsms-external-conformance/declaration.json"
CASES = ROOT / "conformance-kit/tsms-external-conformance/pressure-cases.json"
PROFILE_ID = "tsmm-external-conformance-core-2026.1"
PROFILE_VERSION = "1.0.0"
REQUIRED_IDS = {
    "TSMM-CONF-AUTHORITY",
    "TSMM-CONF-DELEGATION",
    "TSMM-CONF-SCOPE",
    "TSMM-CONF-CURRENT-STATE",
    "TSMM-CONF-EVIDENCE",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def disposition(case: dict) -> str:
    if not case["supported_profile"] or not case["known_requirement"]:
        return "FAIL"
    # Authority is prior to assurance: no evidence strength may manufacture authority.
    if not case["authority"]:
        return "FAIL"
    if not case["delegation"] or not case["scope"] or not case["current_state"]:
        return "FAIL"
    if not case["evidence"]:
        return "INDETERMINATE"
    return "PASS"


def validate_declaration(declaration: dict) -> list[str]:
    errors: list[str] = []
    if declaration.get("profile_id") != PROFILE_ID:
        errors.append("unsupported profile_id")
    if declaration.get("profile_version") != PROFILE_VERSION:
        errors.append("unsupported profile_version")
    implementation = declaration.get("implementation", {})
    if implementation.get("name") != "Governance, Authority and Assurance Metamodel":
        errors.append("unexpected implementation identity")
    requirements = declaration.get("requirements", [])
    ids = [item.get("id") for item in requirements]
    if len(ids) != len(set(ids)):
        errors.append("duplicate requirement id")
    if set(ids) != REQUIRED_IDS:
        errors.append(f"required profile ids mismatch: {sorted(set(ids))}")
    for requirement in requirements:
        if requirement.get("support") != "supported":
            errors.append(f"{requirement.get('id')}: GAAM declaration must make support explicit")
        evidence = requirement.get("evidence", [])
        if not evidence:
            errors.append(f"{requirement.get('id')}: supported requirement lacks evidence")
        for evidence_path in evidence:
            if not (ROOT / evidence_path).exists():
                errors.append(f"{requirement.get('id')}: missing evidence path {evidence_path}")
    boundary = declaration.get("authority_boundary", {})
    expected = {
        "gaam_remains_independent": True,
        "tsmm_normative_dependency": False,
        "tis_serialization_authority_only": True,
        "external_certification_claimed": False,
    }
    for key, value in expected.items():
        if boundary.get(key) is not value:
            errors.append(f"authority boundary {key} must be {value}")
    return errors


def validate_cases(corpus: dict) -> list[str]:
    errors: list[str] = []
    if corpus.get("profile_id") != PROFILE_ID or corpus.get("profile_version") != PROFILE_VERSION:
        errors.append("pressure corpus profile pin mismatch")
    cases = corpus.get("cases", [])
    if len(cases) < 9:
        errors.append("pressure corpus must contain at least nine cases")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        errors.append("duplicate pressure-case id")
    required_scenarios = {
        "baseline",
        "missing-authority",
        "delegation-without-authority",
        "out-of-scope-effect",
        "revoked-or-superseded-authority",
        "missing-required-evidence",
        "unknown-semantic-requirement",
        "unsupported-profile-version",
        "high-assurance-without-authority",
    }
    scenarios = {case.get("scenario") for case in cases}
    missing = required_scenarios - scenarios
    if missing:
        errors.append(f"missing pressure scenarios: {sorted(missing)}")
    for case in cases:
        actual = disposition(case)
        if actual != case.get("expected"):
            errors.append(f"{case.get('id')}: expected {case.get('expected')}, computed {actual}")
        if case.get("scenario") != "baseline" and actual == "PASS":
            errors.append(f"{case.get('id')}: unsafe pressure case became PASS")
        if case.get("scenario") == "missing-required-evidence" and actual != "INDETERMINATE":
            errors.append("missing required evidence must remain INDETERMINATE")
        if case.get("assurance_only_override") and actual == "PASS":
            errors.append("assurance strength must not compensate for absent authority")
    return errors


def main() -> int:
    errors = validate_declaration(load(DECLARATION)) + validate_cases(load(CASES))
    if errors:
        print("GAAM TSMS external conformance: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("GAAM TSMS external conformance: PASS")
    print("- 5/5 required TSMM profile requirements explicitly evidenced")
    print("- 9 governance-specific pressure cases deterministic")
    print("- authority remains prior to assurance")
    print("- result is a bounded adopter test, not certification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
