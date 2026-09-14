#!/usr/bin/env python3
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "gaam_tsms_external_conformance",
    ROOT / "scripts/validate_tsms_external_conformance.py",
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


def base_case():
    return {
        "authority": True,
        "delegation": True,
        "scope": True,
        "current_state": True,
        "evidence": True,
        "known_requirement": True,
        "supported_profile": True,
        "assurance_only_override": False,
    }


class ExternalConformanceDecisionTests(unittest.TestCase):
    def test_baseline_passes(self):
        self.assertEqual(module.disposition(base_case()), "PASS")

    def test_missing_evidence_is_indeterminate(self):
        case = base_case()
        case["evidence"] = False
        self.assertEqual(module.disposition(case), "INDETERMINATE")

    def test_absent_authority_fails_even_with_assurance_override(self):
        case = base_case()
        case["authority"] = False
        case["assurance_only_override"] = True
        self.assertEqual(module.disposition(case), "FAIL")

    def test_revoked_state_fails(self):
        case = base_case()
        case["current_state"] = False
        self.assertEqual(module.disposition(case), "FAIL")

    def test_unknown_requirement_fails(self):
        case = base_case()
        case["known_requirement"] = False
        self.assertEqual(module.disposition(case), "FAIL")

    def test_unsupported_profile_fails(self):
        case = base_case()
        case["supported_profile"] = False
        self.assertEqual(module.disposition(case), "FAIL")


if __name__ == "__main__":
    unittest.main()
