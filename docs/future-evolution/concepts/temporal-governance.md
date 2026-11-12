---
title: Temporal Governance
permalink: /docs/future-evolution/concepts/temporal-governance/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# Temporal Governance

{% include gaam-meta.html %}

> Informative research under the GAAM v0.9.0 specification edition and v0.9.5 distribution. No canonical schema, profile, requirement, vocabulary, or conformance claim is amended. The implementation-specific contracts of TRQP, ARPA, TSMM and TIS are independently governed.

## Problem

Governance determinations apply to assertions whose effective intervals, authoritative recording, observation, decision, execution, publication, enforcement and correction occur at distinct times. An evaluator may correctly know today that an assertion applied at an earlier time without proving that the assertion had entered a competent authoritative record at the time of a consequential action. Likewise, proof of a recorded assertion does not show that an operator observed or acted on it.

**Temporal governance** defines how these time roles qualify authority and evidence conclusions. **Bitemporal evaluation** is one important instance: it distinguishes subject/effective time from an authoritative recording-time cutoff. It is neither a universal two-field representation nor the entire temporal governance model.

## Semantic roles

| Role | Meaning | Must not be conflated with |
|---|---|---|
| Effective time | When an assertion or rule purports to govern a subject/action | When its source recorded the assertion |
| Authoritative recording time | When a competent source committed an assertion to its governed record, with verifiable provenance | Client receipt, observation or cache ingestion |
| Publication and observation time | When content became available or was actually obtained by a recipient | Authority or authorization to rely on it |
| Decision time | When a policy-governed determination was made under identified inputs | Action execution or retrospective assessment |
| Execution and enforcement time | When an action occurred or a control became effective | Policy decision, revocation publication or convergence |
| Correction and supersession | When a competent source records a revision, its asserted effective effect, and what prior claim it supersedes | Silent rewriting of an earlier as-known-at record |
| Reconstruction time | When an investigator performs historical evaluation | The authoritative recording cutoff applied to that evaluation |

The model does not require all roles to be material to every case or impose a database, clock source, retention period, wire field or event-sourcing technology. Whenever a time role determines a consequential predicate, its source, precision, confidence and applicable policy must be explicit.

## Candidate invariants (informative)

**TG-01 Context separation.** Historical effective-state reconstruction, as-recorded-at reconstruction, contemporaneous observation and decision-time reliance are separately assessable claims.

**TG-02 Temporal provenance.** Recording time requires evidence from the competent source; an observation timestamp or asserted backdate cannot substitute for it.

**TG-03 Qualified completeness.** Absence of a recorded claim is not authoritative evidence of absence without verifiable historical coverage of relevant competent sources. Unknown coverage is indeterminate.

**TG-04 Explicit correction.** Later-recorded retrospective corrections may alter present reconstruction of past effective state but must not silently change a reproducible earlier as-known-at result. Competent supersession and conflicts must be traceable.

**TG-05 Temporal non-amplification.** Reformatting, projecting, combining, caching or reconstructing temporal evidence cannot create affirmative authority unsupported by competent provenance, governed scope, policy and the declared temporal context.

**TG-06 Composable contexts.** Cross-source authority evaluation must declare whether evidence cutoffs, policy versions and source coverage are compatible; incompatible contexts cannot silently compose into permit.

**TG-07 Immutable decision evidence.** A later reconstruction may challenge or overturn a determination without altering its original decision receipt. A new correction, remedy or retrospective assessment is separately attributable.

**TG-08 Operational separation.** Historical evaluation, revocation propagation, recipient observation, enforcement convergence and legal reliance remain separate propositions.

**TG-09 Qualified failure.** Unknown, contradictory, withheld, unsupported, stale or unauthenticated material evidence must not silently produce an affirmative result.

These are research invariants, **not** new BCP 14 requirements applicable to GAAM v0.9.0 implementations.

## Interpretive model and dependency chain

A historical inquiry may specify an effective time `tₑ`, evidence-recording cutoff `tᵣ`, reconstruction time `tₓ`, governing policy `P` and provenance-qualified evidence `E`. The resulting assessment `G(tₑ,tᵣ,P,E;tₓ)` is conditional on competent source history, policy applicability and declared evidence quality. The notation neither mandates this interface nor implies that every decision is reducible to two timestamps.

For chained authority, competence of the issuer, validity of the mandate and applicable policy must each be established in compatible temporal contexts. A downstream grant cannot repair a missing competent parent assertion. A later negative assertion does not imply the recipient had contemporaneous notice. Legitimate changes of evidence may change the evaluated result while preserving prior as-known-at outcomes and decision evidence.

## Executable pressure cases

The [experimental temporal governance cases](../../../experimental/temporal-governance/README.md) evaluate effective versus recorded state; retroactive and prospective changes; source competence, provenance, coverage, conflicting claims, policy/version compatibility; mixed cutoffs in composite authority; and immutable original decision receipts. The script runs in validation CI but offers **synthetic modeled evidence only**, not authentic timestamp, source, policy or independent interoperability assurance.

See [cross-system alignment](../temporal-governance-alignment.md) for independently governed TRQP, ARPA, TSMM and TIS relationships and [temporal promotion disposition](../temporal-governance-disposition.md) for a bounded decision.

## Limits and evolution

Do not create new normative temporal contracts solely because a field name appears in another system. Further work is warranted only if independent implementations or concrete conformance failures demonstrate insufficient semantics in the frozen GAAM model. Future changes require the established research-to-normative promotion governance, including compatibility and migration evidence.
