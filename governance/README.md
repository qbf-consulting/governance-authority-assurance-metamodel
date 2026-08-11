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
- The [Candidate Readiness Dashboard](../docs/candidate-readiness.md) summarises the current state.

Register changes MUST be reviewed alongside the relevant issue or pull request. Closing a blocker requires evidence references and an accountable disposition, not only a status edit.

The candidate review baseline is content-addressed and reviewers, decision authorities, findings, dispositions and closure evidence are validated as separate governance facts.
