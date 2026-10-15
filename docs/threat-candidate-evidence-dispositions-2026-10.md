---
title: "Threat Candidate Evidence Dispositions (October 2026)"
nav_exclude: true
artifact_type: "Informative security review"
normative_status: "Informative"
---

# Threat Candidate Evidence Dispositions (October 2026)

**Status:** informative repository evidence assessment, not independent security assurance or a change to Candidate conformance.

This document closes the evidence-classification questions raised in [issue #72](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/72) following the [coverage reassessment](threat-register-coverage-review-2026-10.md). Canonical [threat identities](../threat-model/threat-register.json) remain unchanged. The [Candidate Stability and Change-Control Policy](candidate-stability-policy.md) controls any normative extension.

## Four candidate propositions

| Review | Existing evidence inspected | What that evidence establishes | Decision |
| --- | --- | --- | --- |
| REVIEW-02 — collective authority composition | [Experimental seven-case pressure fixture](../experimental/examples/collective-authority-pressure-cases.json); `EXP-COLLECTIVE-AUTHORITY` check in [GAAM validator](../scripts/validate.py) | An executable **informative reference predicate** covers valid 2-of-3 exercise and rejects single approval, missing rule, stale membership/rule, duplicate actor and missing exact-action binding. This is not evidence of a deployed authorization engine or independent implementation. | **Retain as informative specialisation of THR-001/002.** Do not mint a canonical threat now. |
| REVIEW-05 — recognition versus authorization | [Out-of-scope authority negative vector](../tests/behavioural/authority-role-out-of-scope-rejected.json), [active authority positive vector](../tests/behavioural/authority-active-valid.json), [qualification record example](../experimental/examples/qualification-record.valid.json) | Existing executable authority tests reject an out-of-scope effect despite a role/recognition artifact. Qualification remains an informative representation, not runtime permission. There is no demonstrated distinct unmet Candidate control obligation. | **Refine THR-001 narrative/evidence mapping in a future controlled revision; no new canonical threat.** |
| REVIEW-06 — indeterminate-to-permit collapse | [Unknown-authority fail-closed vector](../tests/behavioural/runtime-unknown-authority-fail-closed-valid.json), [missing-evidence negative vector](../tests/behavioural/decision-missing-evidence-rejected.json), [stale-state fail-open negative vector](../tests/behavioural/runtime-stale-state-fail-open-rejected.json) | Existing runtime/decision fixtures establish representative rejection of unsafe permit under missing/unknown/stale evidence. They do **not** prove all conflicting or unavailable evidence variants have been independently exercised. | **Classify as cross-cutting THR-001/003/004 misuse mode; no new canonical class.** Record conflicting-source variation as a coverage limitation. |
| REVIEW-07 — inference and observability overreach | [Informative concept](future-evolution/concepts/privacy-inference-and-observability.md), [bounded inferred evidence positive fixture](../tests/behavioural/inferred-evidence-bounded-valid.json) | The existing vector requires traceability, explicitly candidate semantics, fail-safe operation and review path. It does **not** prove that permission to collect data is distinguished from authority to infer or to use derived attributes in a consequential decision. | **Defer canonical admission.** The missing negative authorization/control evidence is genuine but concerns unpromoted informative semantics. |

## Treatment of the remaining six propositions

REVIEW-01 (action binding), REVIEW-03 (revocation propagation), REVIEW-04 (assurance composition), REVIEW-08 (ineffective remedy) and REVIEW-09 (temporal mismatch) remain reasoned refinements of THR-001/002, THR-003, THR-004, THR-006 and THR-001/003 respectively. Existing concept notes and behavioural patterns provide useful starting evidence but do not establish a need for new canonical identifiers. REVIEW-10 (institutional succession) remains deferred pending sharper boundaries and external evidence.

## Explicit evidence limits

- Positive/negative repository fixtures establish only the reference behaviour checked by the current validator. They do not assert implementation-level enforcement, independent assessment or production risk reduction.
- The inferred-evidence vector does not test inference *authorization*; this must not be described as resolved.
- Conflict between independently sourced authority evidence is not exhaustively addressed by a dedicated conflict-source test in this tranche.
- No `GAAM-THR-008` or additional normative requirement is assigned. No existing `residualRisk` field is reinterpreted as proof of mitigation.

## Closing decision and follow-up trigger

**Retain all seven canonical threats without modifying the frozen Candidate register.** This is an affirmative admission decision based on the present evidence, not a claim that all operational threats are mitigated.

There is no presently justified Candidate release or immediate canonical threat addition. The narrow residual research hypothesis is **whether explicit inference authorization (collection versus derived-attribute use), backed by independent implementation and negative evidence, is required at GAAM's abstract governance layer**. Reopen canonical admission only if that proposition is demonstrated, or if tests show a distinct control gap beyond existing threat boundaries.

This documents the bounded issue #72 decision; any future implementation research should be independently justified rather than keeping this completed reassessment open indefinitely.
