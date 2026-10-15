---
title: "Five-Minute Implementer Quickstart"
artifact_type: "Informative implementation guidance"
normative_status: "Informative"
parent: Implement
nav_order: 1
---
# Five-Minute Implementer Quickstart

This exercise gives a first result using published GAAM artefacts. It **does not** constitute an independent implementation, runtime authorization service, or conformance claim.

## Run existing delegation vectors

From a fresh checkout, install dependencies and invoke the portable vector runner against GAAM's *reference adapter*:

```bash
python -m pip install -r requirements-dev.txt
python scripts/gaam.py run-vectors python conformance-kit/reference_adapter.py --pattern 'delegation-*.json'
```

Inspect the JSON output. A successful run returns a top-level `status: "pass"` and individual checks marked `pass`, meaning the adapter's judgments matched the bundled vector expectations. The positive `delegation-attenuated-valid` case expects acceptance; `delegation-amplification-rejected` and `delegation-parent-revoked-rejected` expect rejection. A rejected invalid delegation is a **successful negative test**, not a failed validator.

Read the actual input and expected results in [delegation-attenuated-valid](../tests/behavioural/delegation-attenuated-valid.json), [delegation-amplification-rejected](../tests/behavioural/delegation-amplification-rejected.json) and [delegation-parent-revoked-rejected](../tests/behavioural/delegation-parent-revoked-rejected.json). Map these back to the applicable normative delegation requirements through the [requirement-assurance traceability matrix](../matrices/requirement-assurance-traceability.csv).

## Move beyond the reference adapter

The reference adapter is maintained with GAAM and demonstrates its vector contract, **not independent verification**. To evaluate your own implementation, replace the adapter command with one that reads one JSON vector `input` from standard input and returns JSON of the form `{"valid": true}` or `{"valid": false}` according to your own enforcement logic. The [portable conformance kit](../conformance-kit/README.md) documents the interface.

For a complete repository-owned starter and evidence-report workflow, continue with the [clean-room exercise](clean-room-implementation.md). For external reporting, consult [Implementation Reports](../implementation-reports/README.md).

## What PASS does not establish

PASS means *the selected bundled vectors agree with the adapter under test*. It does not establish complete coverage of GAAM's 190 requirements, a deployed policy enforcement point, independent implementation (E2), cross-implementation interoperability (E3), certification, or production safety. Record uncovered requirements and negative/boundary cases rather than treating lack of failures as assurance.
