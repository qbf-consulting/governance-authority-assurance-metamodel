---
title: "GAAM Threat and Misuse-Case Model"
permalink: /threat-model/
nav_order: 7
has_children: false
artifact_type: "Threat model"
normative_status: "Assurance supporting"
---
# GAAM Threat and Misuse-Case Model

{% include gaam-meta.html %}

The v0.9.0 threat model treats governance failures as testable attack and misuse paths. The machine-readable [threat register](threat-register.json) maps threats to protected assets, requirements and executable checks.

Covered classes include authority laundering, delegation amplification, stale revocation, assurance inflation, accountability fragmentation, remedy obstruction and governance-package substitution. Implementations MUST extend this baseline for their actors, deployment boundaries, affected parties and residual risks.

A threat is not considered dispositioned solely because a schema validates. Evidence should include preventive control behaviour, detection records, decision receipts, lifecycle events and remedy outcomes.
