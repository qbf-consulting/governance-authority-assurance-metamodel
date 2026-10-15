---
title: "Requirement Evidence Coverage Reading Guide"
artifact_type: "Informative evidence interpretation"
normative_status: "Informative"
parent: Test & Assure
nav_order: 6
---
# Requirement Evidence Coverage Reading Guide

This is a **source-bound snapshot** of the existing [requirement-assurance traceability matrix](../matrices/requirement-assurance-traceability.csv), not a new conformance level or an independent assurance assessment.

## Inventory (current matrix)

| Declared testability | Requirements |
| --- | ---: |
| Behavioural-testable | 57 |
| Mixed | 58 |
| Structural-testable | 23 |
| Reviewable | 30 |
| Procedural | 19 |
| Observable | 3 |
| **Total** | **190** |

- **104/190** requirements have at least one `test_ids` mapping. This is a reference count, **not** 104 independently proven requirements.
- **91/190** have at least one linked test ID with a rejection/failure-oriented name (e.g. `rejected`, `invalid`, `fail-open`). This is a *naming-based inventory*, not a guarantee that every negative boundary has been exercised.
- The matrix refers to **48 distinct test IDs**; the distinct-ID count is different from the number of executed behavioural checks reported by a particular validation run.

## How to interpret coverage

A matrix entry is a *traceability link*. It does not establish that the linked test fully proves the associated normative requirement. A `reviewable` or `procedural` requirement may depend on documentary, organizational or externally audited evidence rather than a deterministic Boolean oracle. `Mixed` requirements can require both machine and human evidence. The source of truth for each requirement remains the normative specification; the matrix and validation outputs are derived views.

**Current independent evidence claim:** E1 repository-authored validation only; no accepted independent implementation reports are reported by the [readiness dashboard](candidate-readiness.md). Do not interpret 321/321 (or any subsequent aggregate PASS count) as 190/190 behavioural conformance or E2/E3 evidence.

## Reproduce

With a checkout, use the standard-library audit script:

```bash
python scripts/report_coverage.py
python scripts/report_coverage.py --check
```

The check verifies that the published counts still match the underlying CSV. Before asserting substantive coverage, inspect the actual fixtures in [tests/behavioural](../tests/behavioural/), review the linked requirement, and evaluate positive, negative, boundary and external implementation evidence independently.
