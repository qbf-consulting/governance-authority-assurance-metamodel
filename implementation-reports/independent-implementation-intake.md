---
title: "Independent Implementation Evidence Intake"
permalink: /implementation-reports/independent-intake/
parent: "Implementation Reports"
nav_order: 6
artifact_type: "Implementation guidance"
normative_status: "Informative"
---
# Independent Implementation Evidence Intake

{% include gaam-meta.html %}

This workflow explains how an external implementation can submit admissible evidence toward GAAM's E2 independent-implementation claims. It does not create new normative requirements, confer certification, or allow repository-owned fixtures to satisfy independence.

## Entry conditions

An implementation should identify:

- the GAAM release being targeted;
- the retained semantic/profile identifiers used by the implementation;
- the exact claimed profile set and requirement boundary;
- the implementation source revision or build identity;
- the assessor or evidence producer and their relationship to the implementation.

At least one accepted independent report must cover `gaam:profile:foundation:0.9.0`. At least one accepted independent report must cover Foundation plus at least one additional GAAM profile before the implementation evidence gate can be satisfied.

## Submission sequence

1. Select the claim boundary using the [profile-selection guide](profile-selection-guide.md).
2. Implement the applicable GAAM requirements independently.
3. Run structural and behavioural validation appropriate to the claim, including the [portable conformance kit](../conformance-kit/README.md) where useful.
4. Preserve machine-readable results, logs, test inputs, source revision and tool versions.
5. Prepare an implementation report using the [template](TEMPLATE.md).
6. Encode the machine-readable report against `implementation-report.schema.json`.
7. Create and validate the referenced evidence manifest against `evidence-manifest.schema.json`.
8. Disclose organisational, funding, control, shared-management, subcontracting and evidence-production relationships relevant to independence.
9. Submit the report under `implementation-reports/reports/` through a pull request or another repository-approved evidence path.
10. Address review findings without deleting contradictory evidence or converting failed/indeterminate states into success.

## Acceptance contract

A report may contribute to E2 only when it is:

- non-synthetic;
- in governed `accepted` state;
- evidence-complete and reproducible;
- explicit about the target release, profiles and requirement coverage;
- supported by valid evidence manifests and retained bytes;
- independently assessed under the repository's declared independence rules;
- free of failed or indeterminate results and open exceptions inconsistent with the claim boundary.

Acceptance records the authority, time and evidence for the acceptance decision.

## Evidence bundle

The submission should preserve, at minimum:

- implementation identity and source revision;
- GAAM release and profile boundary;
- report JSON and narrative report;
- evidence manifest and retained evidence bytes;
- structural validation results;
- behavioural results;
- operational evidence where claimed;
- exceptions and contradictory evidence;
- assessor identity and independence disclosure;
- integrity digests;
- reassessment triggers.

See the [Implementation Evidence Guide](evidence-guide.md) for evidence quality, provenance, freshness, retention and contradiction handling.

## Non-substitution rule

Repository examples, reference adapters, fixtures, clean-room exercises and maintainer-authored implementations may demonstrate usability or test portability. They **cannot** be relabelled as independent implementation evidence.

Missing independent evidence leaves the E2 claim unproven. It does not, by itself, establish that the GAAM specification is unstable.

## Relationship to interoperability

Accepted implementation evidence is an input to, but not proof of, cross-implementation interoperability. Once at least two credible independent implementations exist, use the [Cross-Implementation Validation Protocol](cross-implementation-protocol.md).
