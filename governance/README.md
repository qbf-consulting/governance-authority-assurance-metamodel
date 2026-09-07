---
title: "Candidate Governance Registers"
permalink: /governance/registers/
parent: Assurance and Governance Tracking
artifact_type: "Governance register guide"
normative_status: "Informative"
grand_parent: Documentation
nav_order: 5
---
# Candidate Governance Registers

{% include gaam-meta.html %}

The governance registers make GAAM's progression to v1.0.0 auditable. They record decision authority, specification-release impact, evidence maturity, required evidence and disposition without changing the normative specification.

- [`maturity-model.json`](maturity-model.json) defines the independent specification-maturity and evidence-maturity axes and their authority boundary.
- [`v1-gate-classification.json`](v1-gate-classification.json) classifies each readiness proposition as repository-controlled, shared or external and states what it proves.
- [`candidate-issues.json`](candidate-issues.json) records candidate questions, their control boundary and whether they can block specification maturation.
- [`reviews/README.md`](reviews/README.md) defines the review method and contains structured privacy, security, affected-party, interoperability and implementation-evidence records.
- [`candidate-readiness.json`](candidate-readiness.json) is the generated machine-readable maturity/evidence state.
- The [Maturity and Evidence Dashboard](../docs/candidate-readiness.md) is generated from that state and its authoritative evidence inputs.

Register changes MUST be reviewed alongside the relevant issue or pull request. Closing a repository-controlled blocker requires evidence references and an accountable disposition, not only a status edit.

## Authority boundary

GAAM maintainers govern GAAM's normative specification and may determine whether repository-controlled Stable claims are supported. Independent implementers and reviewers govern the evidence created by their independent activity; maintainers cannot manufacture that independence.

Accordingly, missing external evidence leaves the corresponding external claim unproven. It does not by itself establish that the GAAM specification is unstable. A bounded `Stable / E1` state is valid and explicitly does not assert independent implementation, independent assurance, interoperability, operational fitness or certification.

This separation is not a waiver. External implementation, review or interoperability evidence that exposes a material ambiguity, security/privacy defect, semantic divergence or invalid normative assumption enters the governed finding/change lifecycle and can invalidate Stable readiness until disposition and reassessment complete.

## Evidence-driven readiness

Maturity state is not edited directly. Run `python scripts/build_candidate_readiness.py` after changing candidate issues, review registers, gate classification or implementation reports. `python scripts/validate.py` and `python scripts/test_maturity_model.py` enforce the generated state and authority boundaries.

Implementation evidence contributes to E2/E3 only after a non-synthetic report in `implementation-reports/reports/` is explicitly accepted. Independent claims additionally require declared independence, disclosed relationships and evidence within the report's stated claim boundary. Synthetic examples, self-assessment and repository fixtures are excluded by construction.

Known repository-recorded blocking findings remain fail-closed for Stable even when an independent attestation has not occurred. This prevents the maturity split from becoming a mechanism for hiding known security, privacy, redress or governance defects.

## Evidence-gated evolution

Future-evolution research is governed separately from maturity readiness. [`promotion/`](promotion/README.md) defines the machine-readable gate policy, promotion-candidate contract and separately attributable decision contract for any later move from research into normative GAAM. A research disposition such as `promote-to-profile` admits an item to future review; it does not create a normative profile.
