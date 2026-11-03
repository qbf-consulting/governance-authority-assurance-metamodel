---
title: "Basic Governed Decision Walkthrough"
permalink: /examples/basic-governed-decision/walkthrough/
parent: "Basic Governed Decision"
grand_parent: "Implementation Patterns"
artifact_type: "Informative implementation walkthrough"
normative_status: "Informative"
---
# Basic Governed Decision Walkthrough

This walkthrough explains the **Basic Governed Decision** pattern as one bounded governance scenario. It describes what an implementer must establish and what the accompanying repository-authored fixtures actually demonstrate. It is not a reference authorization service, a claim of executed effects, or independent implementation evidence. The [Candidate Specification](../../specification/governance-authority-assurance-metamodel.md), [profile manifests](../../profiles/manifests/) and [canonical schemas](../../schemas/) retain authority over semantics and structure.

## Scenario and intended effect

A governed service receives a request from an actor to change a record. The service must decide whether the actor may cause the requested effect *in the present context*. Authentication, ability to call the API, or the possession of a delegation record does not settle that question. The governing institution determines the authority source and policy; the runtime implementation evaluates the evidence and enforces its outcome; affected parties need a route to review and correction.

For this example, the records use the namespace `urn:gaam:example:basic-governed-decision`. The identifier is illustrative and does not stand for a live institutional authority. The `authority.valid.json` and `delegation.valid.json` fixtures intentionally describe a bounded ability to `execute-within-scope`; they do not authorize `execute-outside-scope`.

## Artifact-to-decision map

| Step | Published artifact | What is represented | What is *not* established |
| --- | --- | --- | --- |
| Establish authority | [authority.valid.json](authority.valid.json) | Source, issuer, subject, scope, permitted and prohibited effects, time bounds, revocation authority and accountable party | Legal legitimacy of the governing institution or actual issuer consent |
| Check delegation | [delegation.valid.json](delegation.valid.json) | Delegator, delegate, parent authority, narrowed scope, redelegation prohibition and propagation policy | Independent validity or current status of the parent source at runtime |
| Evaluate current context | [decision-input.json](decision-input.json) | Illustrative authority and policy state, evidence freshness and expected evaluation disposition | An executable policy evaluation or assurance assessment |
| Record decision | [decision-receipt.valid.json](decision-receipt.valid.json) | Decision reference, authority, policy, evidence, assurance, outcome, conditions, enforcement point and review route | A completed external effect or evidence that enforcement succeeded |
| Change authority state | [governance-event.valid.json](governance-event.valid.json) | Suspension event, initiating authority and transition evidence | Demonstrated delivery to every downstream cache or active session |
| Correct an outcome | [remedy.valid.json](remedy.valid.json) | Appeal reference, original decision, corrective action, reviewer authority and supporting evidence | Verified completion of correction in an external system |
| Retain evidence lineage | [evidence-manifest.json](evidence-manifest.json) | Identifiers, producers, purposes and stated freshness of relevant evidence | Cryptographic proof of source authenticity, live availability or independent audit |

The `*.valid.json` and `*.invalid.json` files are **structural and semantic example fixtures** subject to the repository's current validators. A filename does not establish a successful deployed governance decision, and a valid JSON schema cannot alone prove authority, evidence sufficiency or a downstream side effect.

## Positive decision path

1. **Resolve applicability.** Locate the governance context and authoritative policy for the requested effect. Confirm which person or organisation is accountable. In this example the authority fixture identifies an `authoritySource` and an `accountableParties` entry; these references still need authoritative resolution in a real system.
2. **Evaluate active grants.** Verify the source, time window, scope, prohibited effects, delegation rights and current status. Walk the `parentAuthority` chain; do not interpret a valid-looking child record as an independently valid grant. Ensure every hop attenuates or preserves the parent's authority and that prohibited redelegation is not bypassed.
3. **Check evidence and applicable policy.** Evaluate purpose, freshness, assurance and policy precedence, including any contradictory or unavailable evidence. The illustrative `evidenceFresh: true` input is an assertion in a fixture, not a live verification result.
4. **Produce the decision.** When the independently established facts satisfy the applicable requirements, the example receipt represents `permit-with-conditions`, including the condition `scope-and-state-remain-valid`. Evaluate those conditions at the enforcement boundary, not only when the request first enters the system.
5. **Enforce and observe.** The enforcement point attempts the effect under the permitted constraints. The decision receipt alone does not prove that the action ran, completed, or committed externally. Retain operational execution evidence, including failure or indeterminate state, through the implementation's own system-specific contract.
6. **Preserve accountability.** Retain proportionate decision evidence and link the review route to the accountable party. Protect sensitive evidence from unnecessary exposure while ensuring meaningful investigation or challenge remains possible.

## Adversarial and unavailable-state path

Consider a seemingly valid delegation whose parent authority is now suspended. An agent may still possess the earlier token, the delegated scope may look well formed, and a downstream service may hold cached state. **None of these facts authorizes continuation.** The governing source and status must be checked against the relevant lifecycle and freshness policy. If revocation is known, the proposed effect is not permitted; if required status is unavailable or contradictory, the decision must not silently become permit.

The [governance event](governance-event.valid.json) illustrates a suspension transition and an accountable initiating authority. In a deployed system, downstream status propagation, already-running operations, partial effects and evidence of interruption each require their own verification. A revocation can prevent future use without automatically reversing a completed effect. The [remedy fixture](remedy.valid.json) illustrates a later corrective process rather than pretending revocation is equivalent to rollback.

A different adversarial condition is **authority amplification**: a child delegation purports to grant an effect outside the parent scope. The portable negative vectors in [the conformance kit](../../conformance-kit/README.md) test rejection of amplification and revoked-parent delegation via the repository-owned reference adapter. That Boolean contract is a narrowly scoped test oracle, not a replacement for the actual governance decision and enforcement lifecycle.

## How to reproduce the available evidence

From a clean checkout:

```bash
python -m pip install -r requirements-dev.txt
python scripts/gaam.py run-vectors python conformance-kit/reference_adapter.py --pattern 'delegation-*.json'
python scripts/validate.py
```

The reference adapter checks its own supplied vector expectations; the repository validator checks the artifacts and included governance controls it is configured to exercise. Consult the [quickstart](../../docs/implementer-quickstart.md) and [coverage reading guide](../../docs/requirement-evidence-coverage.md) before interpreting PASS. These checks do **not** verify legal authority, deployed execution, independent implementation, complete profile conformance or end-to-end remedy execution.

## Design and conformance boundaries

- The [architecture overview](../../docs/architecture-overview.md) explains why decision, enforcement and observed effect must remain separate.
- The [requirements mapping](requirement-mapping.md) and [normative specification](../../specification/governance-authority-assurance-metamodel.md) establish which requirements govern each part of the model; informative examples add no new obligations.
- The [implementation guide](../../docs/implementation-guide.md) explains package assembly and the lifecycle beyond this one pattern.
- No specific identity, policy, messaging, registry or cryptographic stack is prescribed by this example. The deployment must supply its own bindings, failure semantics, authoritative status, evidence retention, incident response and genuine review/remedy operations.
