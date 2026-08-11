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

The candidate issue and review registers make GAAM's progression to v1.0.0 auditable. They record decision authority, release impact, required evidence, blocking status and disposition without changing the normative specification.

- [`candidate-issues.json`](candidate-issues.json) records candidate questions and release blockers.
- [`reviews/README.md`](reviews/README.md) defines the review method and contains structured privacy, security, affected-party, interoperability and implementation-evidence records.
- [`candidate-readiness.json`](candidate-readiness.json) is the generated machine-readable candidate decision state.
- The [Candidate Readiness Dashboard](../docs/candidate-readiness.md) is generated from that state and its authoritative evidence inputs.

Register changes MUST be reviewed alongside the relevant issue or pull request. Closing a blocker requires evidence references and an accountable disposition, not only a status edit.

The candidate review baseline is content-addressed and reviewers, decision authorities, findings, dispositions and closure evidence are validated as separate governance facts.


## Evidence-driven readiness

Candidate readiness is not edited directly. Run `python scripts/build_candidate_readiness.py` after changing candidate issues, review registers, or implementation reports. `python scripts/validate.py` fails when either the generated JSON state or the human-readable dashboard is stale.

Implementation evidence only contributes to candidate gates after a report in `implementation-reports/reports/` is explicitly accepted. Synthetic examples and schema fixtures are excluded by construction, and independent-implementation gates additionally require an independent assessor, disclosed relationships, and no failed or indeterminate result or open exception.

## Evidence-gated evolution

Future-evolution research is governed separately from candidate readiness. [`promotion/`](promotion/README.md) defines the machine-readable gate policy, promotion-candidate contract and separately attributable decision contract for any later move from research into normative GAAM. A research disposition such as `promote-to-profile` admits an item to future review; it does not create a normative profile.
