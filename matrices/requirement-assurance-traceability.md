---
title: Requirement Assurance Traceability
parent: Matrices
nav_order: 5
artifact_type: Assurance matrix
normative_status: Informative
grand_parent: Appendices
---
# Requirement Assurance Traceability

{% include gaam-meta.html %}

This matrix connects every indexed normative requirement to an explicit testability disposition, applicable profiles, relevant schemas, informative evidence classes, and included reference tests. It does not convert informative tests or evidence guidance into normative requirements.

## Coverage summary

| Disposition | Requirements |
|---|---:|
| behavioural-testable | 57 |
| mixed | 58 |
| observable | 3 |
| procedural | 19 |
| reviewable | 30 |
| structural-testable | 23 |

**Total requirements:** 190  
**Requirements with included reference tests:** 99  

## Interpretation

- **Behavioural-testable:** an existing requirement can be exercised through runtime inputs and expected outcomes.
- **Structural-testable:** artifact structure or declared relationships can be checked automatically.
- **Observable:** conformance depends on retained operational observations.
- **Reviewable:** a competent reviewer can evaluate documented evidence against stated criteria.
- **Procedural:** fulfilment depends primarily on an accountable process.
- **Mixed:** automated evidence can support, but cannot complete, the evaluation.

## Requirement traceability

| Requirement | Testability | Profiles | Schema | Evidence | Included tests |
|---|---|---|---|---|---|
| `GAAM-CORE-001` | reviewable | foundation | — | `EVD-GOV-001` | — |
| `GAAM-CORE-002` | reviewable | foundation | — | `EVD-GOV-001` | — |
| `GAAM-CORE-003` | reviewable | foundation | — | `EVD-GOV-001` | — |
| `GAAM-CORE-004` | reviewable | foundation | — | `EVD-GOV-001` | — |
| `GAAM-CORE-005` | behavioural-testable | foundation | — | `EVD-GOV-001` | — |
| `GAAM-AUTH-001` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-AUTH-002` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-AUTH-003` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-AUTH-004` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-AUTH-005` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-DEL-001` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected, delegation-cycle-rejected |
| `GAAM-DEL-002` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-003` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-004` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-005` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-006` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-POL-001` | reviewable | foundation, machine-actionable-governance | — | `EVD-GOV-001` | — |
| `GAAM-POL-002` | reviewable | foundation, machine-actionable-governance | — | `EVD-GOV-001` | — |
| `GAAM-POL-003` | procedural | foundation, machine-actionable-governance | — | `EVD-GOV-001` | — |
| `GAAM-POL-004` | reviewable | foundation, machine-actionable-governance | — | `EVD-GOV-001` | — |
| `GAAM-POL-005` | reviewable | foundation, machine-actionable-governance | — | `EVD-GOV-001` | — |
| `GAAM-EVID-001` | mixed | foundation-or-contextual | decision-receipt.schema.json | `EVD-BEH-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected |
| `GAAM-EVID-002` | behavioural-testable | foundation-or-contextual | decision-receipt.schema.json | `EVD-BEH-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected |
| `GAAM-EVID-003` | mixed | foundation-or-contextual | decision-receipt.schema.json | `EVD-BEH-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected |
| `GAAM-EVID-004` | mixed | foundation-or-contextual | decision-receipt.schema.json | `EVD-BEH-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected |
| `GAAM-ASSUR-001` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-002` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-003` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-004` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-DEC-001` | behavioural-testable | foundation-or-contextual | decision-receipt.schema.json | `EVD-DEC-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected, decision-policy-superseded-rejected, decision-receipt-digest-mismatch-rejected, decision-replay-rejected |
| `GAAM-DEC-002` | behavioural-testable | foundation-or-contextual | decision-receipt.schema.json | `EVD-DEC-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected, decision-policy-superseded-rejected |
| `GAAM-DEC-003` | behavioural-testable | foundation-or-contextual | decision-receipt.schema.json | `EVD-DEC-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected, decision-policy-superseded-rejected |
| `GAAM-EFF-001` | reviewable | foundation-or-contextual | — | `EVD-DEC-001` | — |
| `GAAM-EFF-002` | behavioural-testable | foundation-or-contextual | — | `EVD-DEC-001` | — |
| `GAAM-CTX-001` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-CTX-002` | procedural | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-EVT-001` | mixed | foundation-or-contextual | governance-event.schema.json | `EVD-LIF-001` | lifecycle-event-order-valid, lifecycle-event-order-invalid-rejected |
| `GAAM-EVT-002` | mixed | foundation-or-contextual | governance-event.schema.json | `EVD-LIF-001` | lifecycle-event-order-valid, lifecycle-event-order-invalid-rejected |
| `GAAM-ACC-001` | mixed | foundation | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-review-not-independent-rejected |
| `GAAM-ACC-002` | mixed | foundation | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-review-not-independent-rejected |
| `GAAM-ACC-003` | mixed | foundation | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-review-not-independent-rejected |
| `GAAM-HARM-001` | mixed | foundation-or-contextual | — | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected |
| `GAAM-HARM-002` | mixed | foundation-or-contextual | — | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected |
| `GAAM-REL-001` | behavioural-testable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-REL-002` | procedural | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-REL-003` | behavioural-testable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-REL-004` | procedural | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-REL-005` | procedural | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-REL-006` | behavioural-testable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GF-001` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-002` | structural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-003` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-004` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-005` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-006` | behavioural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-007` | behavioural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-008` | behavioural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-009` | behavioural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-010` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-011` | reviewable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-GF-012` | behavioural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-AUTH-006` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-AUTH-007` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-DEL-007` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-008` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-009` | mixed | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-010` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-011` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-012` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-DEL-013` | behavioural-testable | agentic-systems, delegated-authority | authority.schema.json | `EVD-DEL-001` | delegation-attenuated-valid, delegation-amplification-rejected, delegation-depth-rejected, delegation-redelegation-prohibited-rejected, delegation-parent-revoked-rejected, delegation-child-outlives-parent-rejected |
| `GAAM-AUTH-008` | mixed | delegated-authority, foundation | authority.schema.json | `EVD-AUT-001` | authority-active-valid, authority-revoked-rejected, authority-not-yet-effective-rejected, authority-expired-rejected, authority-source-invalid-rejected |
| `GAAM-RUN-001` | behavioural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-002` | behavioural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-003` | behavioural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-004` | behavioural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-005` | structural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-006` | structural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-007` | structural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-008` | mixed | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-RUN-009` | behavioural-testable | agentic-systems, runtime-governance | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-AGT-001` | reviewable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-002` | reviewable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-003` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-004` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-005` | reviewable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-006` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-007` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-008` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-009` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-010` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-011` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-012` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-013` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-014` | reviewable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-015` | reviewable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-016` | structural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-017` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-018` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-019` | reviewable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-020` | procedural | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-021` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-AGT-022` | behavioural-testable | agentic-systems | — | `EVD-DEL-001` | — |
| `GAAM-GRAPH-001` | behavioural-testable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-002` | behavioural-testable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-003` | reviewable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-004` | procedural | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-005` | reviewable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-006` | behavioural-testable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-007` | reviewable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-008` | reviewable | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-GRAPH-009` | procedural | foundation-or-contextual | — | `EVD-LIF-001` | — |
| `GAAM-REG-001` | procedural | trust-graph | — | `EVD-LIF-001` | — |
| `GAAM-REG-002` | structural-testable | trust-graph | — | `EVD-LIF-001` | — |
| `GAAM-REG-003` | structural-testable | trust-graph | — | `EVD-LIF-001` | — |
| `GAAM-REG-004` | structural-testable | trust-graph | — | `EVD-LIF-001` | — |
| `GAAM-REG-005` | procedural | trust-graph | — | `EVD-LIF-001` | — |
| `GAAM-REG-006` | structural-testable | trust-graph | — | `EVD-LIF-001` | — |
| `GAAM-ASSUR-005` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-006` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-007` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-008` | observable | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-009` | observable | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-OBS-001` | mixed | foundation-or-contextual | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-OBS-002` | mixed | foundation-or-contextual | — | `EVD-OPS-001` | runtime-revocation-fail-closed-valid, runtime-stale-state-fail-open-rejected |
| `GAAM-ASSUR-010` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASSUR-011` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-RISK-001` | behavioural-testable | foundation-or-contextual | — | `EVD-SEC-001` | — |
| `GAAM-RISK-002` | observable | foundation-or-contextual | — | `EVD-SEC-001` | — |
| `GAAM-HARM-003` | behavioural-testable | high-impact-systems | — | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected |
| `GAAM-HARM-004` | mixed | high-impact-systems | — | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected |
| `GAAM-RISK-003` | behavioural-testable | foundation-or-contextual | — | `EVD-SEC-001` | — |
| `GAAM-RED-001` | mixed | foundation-or-contextual | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-002` | behavioural-testable | foundation-or-contextual | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-003` | behavioural-testable | foundation-or-contextual | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-004` | mixed | high-impact-systems | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-005` | behavioural-testable | high-impact-systems | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-006` | mixed | high-impact-systems | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-007` | mixed | high-impact-systems | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-RED-008` | mixed | high-impact-systems | remedy.schema.json | `EVD-REM-001` | high-impact-remedy-valid, high-impact-no-remedy-rejected, high-impact-review-not-independent-rejected, high-impact-notice-missing-rejected |
| `GAAM-MAG-001` | structural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-MAG-002` | structural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-MAG-003` | structural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-MAG-004` | structural-testable | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-MAG-005` | procedural | foundation-or-contextual | — | `EVD-GOV-001` | — |
| `GAAM-PROF-001` | mixed | foundation-or-contextual | profile-manifest.schema.json | `EVD-STR-002` | profile-composition-foundation-delegated-valid, profile-composition-missing-foundation-rejected |
| `GAAM-PROF-002` | mixed | foundation-or-contextual | profile-manifest.schema.json | `EVD-STR-002` | profile-composition-foundation-delegated-valid, profile-composition-missing-foundation-rejected |
| `GAAM-CONF-001` | mixed | machine-actionable-governance | conformance-claim.schema.json | `EVD-CLA-001` | claim-level-evidence, assurance-independence-insufficient-rejected |
| `GAAM-CONF-002` | behavioural-testable | machine-actionable-governance | conformance-claim.schema.json | `EVD-CLA-001` | claim-level-evidence, assurance-independence-insufficient-rejected |
| `GAAM-CONF-003` | mixed | machine-actionable-governance | conformance-claim.schema.json | `EVD-CLA-001` | claim-level-evidence, assurance-independence-insufficient-rejected |
| `GAAM-CONF-004` | mixed | machine-actionable-governance | conformance-claim.schema.json | `EVD-CLA-001` | claim-level-evidence, assurance-independence-insufficient-rejected |
| `GAAM-CONF-005` | mixed | machine-actionable-governance | conformance-claim.schema.json | `EVD-CLA-001` | claim-level-evidence, assurance-independence-insufficient-rejected |
| `GAAM-CONF-006` | mixed | machine-actionable-governance | conformance-claim.schema.json | `EVD-CLA-001` | claim-level-evidence, assurance-independence-insufficient-rejected |
| `GAAM-SEC-001` | mixed | foundation-or-contextual | — | `EVD-SEC-001` | package-integrity |
| `GAAM-SEC-002` | mixed | foundation-or-contextual | — | `EVD-SEC-001` | package-integrity |
| `GAAM-PRIV-001` | structural-testable | foundation-or-contextual | — | `EVD-PRI-001` | — |
| `GAAM-PRIV-002` | structural-testable | foundation-or-contextual | — | `EVD-PRI-001` | — |
| `GAAM-RES-001` | reviewable | foundation-or-contextual | — | `EVD-OPS-001` | — |
| `GAAM-ART-001` | structural-testable | delegated-authority, foundation, machine-actionable-governance | gaam-package.schema.json | `EVD-INT-001` | package-integrity |
| `GAAM-ART-002` | structural-testable | delegated-authority, foundation, machine-actionable-governance | gaam-package.schema.json | `EVD-INT-001` | package-integrity |
| `GAAM-ART-003` | structural-testable | delegated-authority, foundation, machine-actionable-governance | gaam-package.schema.json | `EVD-INT-001` | package-integrity |
| `GAAM-ART-004` | structural-testable | delegated-authority, foundation, machine-actionable-governance | gaam-package.schema.json | `EVD-INT-001` | package-integrity |
| `GAAM-ART-005` | behavioural-testable | delegated-authority, foundation, machine-actionable-governance | gaam-package.schema.json | `EVD-INT-001` | package-integrity |
| `GAAM-ART-006` | behavioural-testable | delegated-authority, foundation, machine-actionable-governance | gaam-package.schema.json | `EVD-INT-001` | package-integrity |
| `GAAM-LIFE-001` | mixed | continuous-assurance, delegated-authority, foundation, machine-actionable-governance, runtime-governance | governance-event.schema.json | `EVD-LIF-001` | authority-revoked-rejected, authority-expired-rejected, lifecycle-event-order-invalid-rejected, lifecycle-event-order-replay-rejected |
| `GAAM-LIFE-002` | mixed | continuous-assurance, delegated-authority, foundation, machine-actionable-governance, runtime-governance | governance-event.schema.json | `EVD-LIF-001` | authority-revoked-rejected, authority-expired-rejected, lifecycle-event-order-invalid-rejected |
| `GAAM-LIFE-003` | mixed | continuous-assurance, delegated-authority, foundation, machine-actionable-governance, runtime-governance | governance-event.schema.json | `EVD-LIF-001` | authority-revoked-rejected, authority-expired-rejected, lifecycle-event-order-invalid-rejected |
| `GAAM-LIFE-004` | behavioural-testable | continuous-assurance, delegated-authority, foundation, machine-actionable-governance, runtime-governance | governance-event.schema.json | `EVD-LIF-001` | authority-revoked-rejected, authority-expired-rejected, lifecycle-event-order-invalid-rejected |
| `GAAM-LIFE-005` | mixed | continuous-assurance, delegated-authority, foundation, machine-actionable-governance, runtime-governance | governance-event.schema.json | `EVD-LIF-001` | authority-revoked-rejected, authority-expired-rejected, lifecycle-event-order-invalid-rejected |
| `GAAM-ASR-001` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASR-002` | mixed | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-ASR-003` | behavioural-testable | continuous-assurance | assurance.schema.json | `EVD-ASS-001` | claim-level-evidence, assurance-expired-rejected, assurance-independence-insufficient-rejected |
| `GAAM-PCOMP-001` | mixed | foundation-or-contextual | profile-manifest.schema.json | `EVD-STR-002` | profile-composition-foundation-delegated-valid, profile-composition-missing-foundation-rejected |
| `GAAM-PCOMP-002` | mixed | foundation-or-contextual | profile-manifest.schema.json | `EVD-STR-002` | profile-composition-foundation-delegated-valid, profile-composition-missing-foundation-rejected |
| `GAAM-PROF-003` | mixed | foundation-or-contextual | profile-manifest.schema.json | `EVD-STR-002` | profile-composition-foundation-delegated-valid, profile-composition-missing-foundation-rejected |
| `GAAM-PROF-004` | mixed | foundation-or-contextual | profile-manifest.schema.json | `EVD-STR-002` | profile-composition-foundation-delegated-valid, profile-composition-missing-foundation-rejected |
| `GAAM-OUT-001` | behavioural-testable | agentic-systems, foundation, high-impact-systems, machine-actionable-governance, runtime-governance | — | `EVD-DEC-001` | — |
| `GAAM-OUT-002` | behavioural-testable | agentic-systems, foundation, high-impact-systems, machine-actionable-governance, runtime-governance | — | `EVD-DEC-001` | — |
| `GAAM-OUT-003` | structural-testable | agentic-systems, foundation, high-impact-systems, machine-actionable-governance, runtime-governance | — | `EVD-DEC-001` | — |
| `GAAM-DEC-004` | structural-testable | agentic-systems, foundation, high-impact-systems, machine-actionable-governance, runtime-governance | decision-receipt.schema.json | `EVD-DEC-001` | decision-traceable-valid, decision-missing-evidence-rejected, decision-stale-evidence-rejected, decision-policy-superseded-rejected |
| `GAAM-SAFE-001` | structural-testable | agentic-systems, high-impact-systems, runtime-governance | — | `EVD-SEC-001` | — |
| `GAAM-SAFE-002` | reviewable | agentic-systems, high-impact-systems, runtime-governance | — | `EVD-SEC-001` | — |
| `GAAM-SAFE-003` | reviewable | agentic-systems, high-impact-systems, runtime-governance | — | `EVD-SEC-001` | — |
| `GAAM-APR-001` | reviewable | high-impact-systems | — | `EVD-REM-001` | — |
| `GAAM-APR-002` | behavioural-testable | high-impact-systems | — | `EVD-REM-001` | — |
| `GAAM-APR-003` | behavioural-testable | high-impact-systems | — | `EVD-REM-001` | — |
| `GAAM-SYS-001` | structural-testable | high-impact-systems | — | `EVD-OPS-001` | — |
| `GAAM-SYS-002` | procedural | high-impact-systems | — | `EVD-OPS-001` | — |
| `GAAM-MKT-001` | mixed | high-impact-systems, trust-graph | — | `EVD-INTOP-001` | profile-composition-foundation-delegated-valid |
| `GAAM-MKT-002` | behavioural-testable | high-impact-systems, trust-graph | — | `EVD-INTOP-001` | profile-composition-foundation-delegated-valid |
| `GAAM-MKT-003` | mixed | high-impact-systems, trust-graph | — | `EVD-INTOP-001` | profile-composition-foundation-delegated-valid |
