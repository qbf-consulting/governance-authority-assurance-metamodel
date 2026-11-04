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
python scripts/gaam.py run-vectors --pattern 'delegation-*.json' python conformance-kit/reference_adapter.py
```

Inspect the JSON output. A successful run returns a top-level `status: "pass"` and individual checks marked `pass`, meaning the adapter's judgments matched the bundled vector expectations. The positive `delegation-attenuated-valid` case expects acceptance; `delegation-amplification-rejected` and `delegation-parent-revoked-rejected` expect rejection. A rejected invalid delegation is a **successful negative test**, not a failed validator.

Read the actual input and expected results in [delegation-attenuated-valid](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/blob/v0.9.4/tests/behavioural/delegation-attenuated-valid.json), [delegation-amplification-rejected](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/blob/v0.9.4/tests/behavioural/delegation-amplification-rejected.json) and [delegation-parent-revoked-rejected](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/blob/v0.9.4/tests/behavioural/delegation-parent-revoked-rejected.json). Map these back to the applicable normative delegation requirements through the [requirement-assurance traceability matrix](../matrices/requirement-assurance-traceability.csv).

## Move beyond the reference adapter

The reference adapter is maintained with GAAM and demonstrates its vector contract, **not independent verification**. To evaluate your own implementation, replace the adapter command with one that reads one JSON vector `input` from standard input and returns JSON of the form `{"valid": true}` or `{"valid": false}` according to your own enforcement logic. The [portable conformance kit](../conformance-kit/README.md) documents the interface.

For a complete repository-owned starter and evidence-report workflow, continue with the [clean-room exercise](clean-room-implementation.md). For external reporting, consult [Implementation Reports](../implementation-reports/README.md).

## What PASS does not establish

PASS means *the selected bundled vectors agree with the adapter under test*. It does not establish complete coverage of GAAM's 190 requirements, a deployed policy enforcement point, independent implementation (E2), cross-implementation interoperability (E3), certification, or production safety. Record uncovered requirements and negative/boundary cases rather than treating lack of failures as assurance.

## Experimental v2 raw-artifact evaluation

The default v1 vectors use abstract decision inputs. To exercise real v0.9.0 authority artifacts with an explicit evaluation clock and reason-code checks, run:

```bash
python scripts/gaam.py run-vectors --suite v2 python conformance-kit/reference_adapter.py
```

For a run-specific, repository-controlled record of expected and observed positive/negative/indeterminate gateway outcomes, use `python scripts/generate_gateway_evidence.py` and inspect `validation/adopter-gateway-evaluation.json`. In CI this file is captured in the existing validation evidence artifact. It remains synthetic E1 evidence.\n\nFor a bounded example that combines **canonical** authority/delegation artifacts, local policy and observations, and a receipt without executing an effect, see the [Delegated Agent Purchasing gateway exercise](../examples/delegated-agent-purchase/adopter-gateway-exercise.md). This is an informative self-assessed exercise, not a general scope comparator or independently verified gateway.

The v2 suite tests a deliberately narrow authority lifecycle boundary; it does not cover delegated-scope composition, multi-agent aggregation, cryptographic receipts or actual external authorization. The source adapter is maintained with the test suite and must not be cited as independent evidence. The [clean-room exercise](clean-room-implementation.md) runs both the abstract delegation and raw-authority lifecycle paths and explicitly checks an always-deny false-success case; it does not establish composed runtime delegated-agent authorization.
