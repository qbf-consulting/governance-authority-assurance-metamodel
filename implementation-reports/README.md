---
title: "Implementation Reports"
permalink: /implementation-reports/
nav_order: 5
has_children: true
artifact_type: "Implementation guidance"
normative_status: "Informative"
---
# Implementation Reports

{% include gaam-meta.html %}

This section helps implementers prepare bounded, reproducible evidence for a GAAM conformance claim. It does not create new GAAM requirements and does not turn a self-assessment into an independent assessment.

## Start here

1. Use the [profile-selection guide](profile-selection-guide.md) to identify the target of evaluation and applicable profile closure.
2. Complete the [self-assessment checklist](self-assessment-checklist.md) before asserting a conformance level.
3. Follow the [evidence guide](evidence-guide.md) to organise provenance, verification, freshness, retention and independence information.
4. Prepare the report using the [implementation report template](TEMPLATE.md).
5. Review the [illustrative report](examples/illustrative-report.md) to see how limitations and failed controls should be disclosed.

## Evidence resources

- [Evidence catalogue](evidence-catalogue.md): informative evidence classes and expected verification attributes.
- [Evidence quality model](evidence-quality-model.md): criteria for relevance, provenance, integrity, freshness, sufficiency and independence.
- [Evidence retention guidance](evidence-retention-guidance.md): lifecycle-aware retention and disposal considerations.
- [`evidence-catalogue.json`](evidence-catalogue.json): machine-readable companion to the human-readable catalogue.

## Machine-readable report contract

A report intended to contribute to candidate-readiness evidence should also be submitted as JSON under `implementation-reports/reports/` and validate against [`implementation-report.schema.json`](implementation-report.schema.json). Its referenced evidence manifest must validate against [`evidence-manifest.schema.json`](evidence-manifest.schema.json), and requirement-level results use [`conformance-result.schema.json`](conformance-result.schema.json).

The report lifecycle is controlled rather than inferred:

```text
submitted
→ structurally-valid
→ evidence-complete
→ reviewed
→ accepted
→ superseded
```

Only a non-synthetic report in `accepted` state can contribute to candidate readiness. Acceptance must identify the accepting authority, time, and decision evidence. To count toward the independent-implementation exit criterion, the report must additionally declare an independent assessor, disclose relevant relationships, and contain no failed or indeterminate evaluated result or open exception.

The machine-readable contract does not replace the narrative report. The JSON record exists so version, implementation provenance, profile and requirement coverage, result state, evidence integrity, independence, limitations and reassessment triggers can be tested consistently.

## Claim boundary

An implementation report records what was evaluated, against which GAAM version and profiles, using which tests and evidence, with which exceptions and limitations. It is not itself proof of conformance. A conformance claim remains bounded by the evidence level and independence rules in the [Conformance and Assurance Guide](../docs/conformance-guide.md).
