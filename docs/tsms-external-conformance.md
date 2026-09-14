---
title: "TSMM/TIS External Conformance Experiment"
permalink: /docs/tsms-external-conformance/
parent: Assurance and Governance Tracking
grand_parent: Documentation
nav_order: 7
---
# TSMM/TIS External Conformance Experiment

GAAM is the second external adopter used to pressure-test the bounded TSMM/TIS conformance interface. The experiment asks whether a governance-authority metamodel can declare a TSMM semantic profile and produce portable evidence without making TSMM or TIS normative dependencies of GAAM.

## Authority boundary

GAAM remains an independent specification. TSMM owns the meaning of the external semantic profile; TIS owns the portable declaration/result contract shape; GAAM owns its implementation claim and evidence. A passing result is a bounded conformance experiment, not certification, legal compliance, ecosystem recognition, or an L4 independent-assessment claim.

GAAM's existing TSMM adoption crosswalk remains informative. This experiment does not rewrite that relationship.

## Profile mapping

| TSMM requirement | GAAM evidence surface |
|---|---|
| `TSMM-CONF-AUTHORITY` | `schemas/authority.schema.json`, normative specification, repository governance |
| `TSMM-CONF-DELEGATION` | `schemas/delegation.schema.json`, normative specification |
| `TSMM-CONF-SCOPE` | authority, delegation and decision-receipt schemas |
| `TSMM-CONF-CURRENT-STATE` | governance-event and authority schemas plus lifecycle semantics |
| `TSMM-CONF-EVIDENCE` | evidence and assurance schemas plus conformance guidance |

## Governance-specific pressure cases

The corpus proves that these conditions remain non-success:

- authority source absent or unresolvable;
- delegation asserted without valid authority;
- requested effect outside governed scope;
- revoked or superseded authority treated as current;
- unknown semantic requirement;
- unsupported profile version;
- high assurance presented as a substitute for absent authority.

Missing required evidence is specifically `INDETERMINATE`, not `PASS`.

The final invariant is important: **assurance strength does not create authority**. GAAM may have strong evidence about a system and still reject an effect if the actor lacks current authority for the scope.

## Reproduce

```bash
python scripts/validate_tsms_external_conformance.py
python scripts/test_tsms_external_conformance.py
```

The repository's normal `Validate` workflow executes the external-conformance validator so the declaration and pressure corpus cannot silently drift.

## Escalation rule

A genuine semantic mismatch is a TSMM issue. An inability to express a portable declaration/result is a TIS issue. GAAM MUST NOT redefine either layer locally merely to obtain a passing disposition.
