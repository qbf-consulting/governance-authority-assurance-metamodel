---
title: "Authority at Commitment Profile"
permalink: /profiles/authority-at-commitment-profile/
parent: Conformance Profiles
---

# Authority at Commitment Profile

**Status:** experimental additive profile; not part of the v0.9.2 normative baseline.

## Purpose

This profile defines the governance semantics required when an actor or autonomous agent creates a material commitment on behalf of a principal. It addresses the gap between proving who produced a message and proving that the producer had current authority for the exact commitment another party is entitled to rely upon.

The profile is transport-, negotiation-, settlement- and identity-technology neutral.

## Core distinction

A conforming implementation MUST preserve these as different propositions:

1. **Identity** — the actor can be authenticated or otherwise identified.
2. **General authorization** — some principal-derived authority exists.
3. **Commitment authority** — the exact proposed material transition falls within the active mandate and its constraints at evaluation time.

A valid signature MUST NOT, by itself, be treated as evidence of commitment authority.

## Semantic objects

### Mandate

A bounded grant derived from a competent principal or authority source. A mandate identifies the actor, permitted scope, constraints, validity interval, revocation/status semantics, required approvals and the policy context governing exercise.

### AuthorityExercise

The actor's attempted use of a mandate for an exact action. The exercise binds an action identifier or digest, target/counterparty where relevant, material parameters and evaluation time.

### Commitment

An authority exercise that, if admitted, creates a material state or reliance position for another party. A commitment is not valid merely because the actor could communicate or sign it.

### Approval

Additional human or organizational authority required by the mandate or policy. Approval MUST bind to the exact action or commitment it authorizes and MUST NOT be reusable for a materially different or stale action.

### AuthorityDecision

A policy-governed result over the exact AuthorityExercise. At minimum, implementations MUST preserve `permit`, `deny`, and `indeterminate` or equivalently safe states.

### AuthorityEvidence

Replayable evidence sufficient for an authorized verifier to reconstruct what authority, policy, status/revocation state, approvals and action binding were evaluated.

## Required invariants

**AAC-01 — identity is not authority.** Authentication, possession of a signing key, capability advertisement, reputation or successful discovery MUST NOT independently establish commitment authority.

**AAC-02 — action specificity.** A commitment decision MUST bind to the exact action or canonical digest evaluated.

**AAC-03 — authority-at-time-T.** Validity, expiry, suspension and revocation MUST be evaluated at the material transition time or at an explicitly governed evaluation time.

**AAC-04 — bounded scope.** Counterparty, value, field, jurisdictional, temporal and other mandate constraints MUST be enforced when material to the action.

**AAC-05 — approval binding.** Required approval MUST reference the exact action/commitment and MUST be current under the applicable policy.

**AAC-06 — fail safely.** Missing, stale, ambiguous, conflicting or unsupported material authority evidence MUST NOT silently become `permit`.

**AAC-07 — replayability.** The resulting record SHOULD permit later reconstruction of the authority decision without requiring an agent to explain its intent.

**AAC-08 — non-collapsing layers.** Authority verification MUST remain distinct from runtime admission, business selection, negotiation state, settlement and reputation.

## Decision evidence

A decision record SHOULD minimally retain:

- principal and actor references;
- mandate reference and immutable digest where available;
- exact action/commitment reference or digest;
- evaluation time;
- policy identifier/version;
- relevant scope/constraint results;
- status/revocation evidence and freshness;
- required approval reference and binding result;
- decision and stable reason codes;
- evidence/provenance references.

The record MAY minimize or selectively disclose underlying authority data. Privacy-preserving proof is compatible with this profile so long as the verifier can establish the required propositions.

## Falsification cases

| Case | Expected result |
|---|---|
| Current mandate; exact action in scope; all required approvals bound to the action | permit |
| Valid signature but no principal-derived mandate | deny or indeterminate |
| Mandate expired before the material transition | deny |
| Mandate revoked before the material transition | deny |
| Action exceeds a material scope/value/counterparty constraint | deny |
| Approval exists but references a different or stale action digest | deny |
| Required authority status cannot be established | indeterminate or deny according to governing policy |

## Authority boundary

GAAM owns the abstract governance semantics in this profile. It does not define A2A negotiation messages, registry lookup protocols, runtime retry/budget admission, payment settlement, reputation scoring, DID methods, credential formats or cryptographic proof suites.

Downstream projects MAY project this model into protocol-specific contracts while preserving these boundaries and MUST NOT imply that the projection transfers normative authority back to GAAM.

## Assurance expectation

Implementations claiming this profile SHOULD provide executable evidence for AAC-01 through AAC-08. Narrative assertion alone is insufficient for consequential positive claims.
