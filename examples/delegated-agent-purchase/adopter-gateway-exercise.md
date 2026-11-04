---
title: "Adopter Gateway Evaluation Exercise"
permalink: /examples/delegated-agent-purchase/adopter-gateway-exercise/
parent: "Delegated Agent Purchasing"
nav_exclude: true
artifact_type: "Informative implementation exercise"
normative_status: "Informative"
---

# Bounded delegated-agent gateway exercise

This is a **repository-controlled, self-assessed** evaluation of a delegated purchase decision. It is neither a normative GAAM protocol nor a credential/identity verifier, live policy engine, production enforcement gateway, independent E2/E3 implementation, or claim of complete Foundation/Delegated Authority Profile conformance. The implementation is separate from the portable reference adapter but remains maintainer-authored.

From a checkout with development dependencies installed:

```bash
python examples/delegated-agent-purchase/adopter_gateway.py < examples/delegated-agent-purchase/adopter-gateway-case.json
python -m pytest tests/test_adopter_gateway.py -q
```

The first command emits JSON with `status` (`permit`, `deny`, `indeterminate`), a scenario-local reason, the SHA-256 digest of the canonicalized input, a **canonical-schema-shaped decision receipt** where enough information exists, and `effectExecuted: false`. Repeating the same input reproduces the digest and decision. It does not demonstrate a signed receipt, authenticated producer, tamper-evident audit log or replay-prevention mechanism. The operator must verify externally supplied observations; the exercise **cannot authenticate its own inputs**.

## Ten-part evaluation against issue #102

| Scenario element | Demonstrated or missing |
|---|---|
| Principal and acting agent | Request fields are matched to `authority.subject`, `delegation.delegator`, and `delegation.delegate`. Actor binding is scenario-supplied and **not authenticated**. |
| Authority provenance, acceptance and scope | Parent link, issuer/source identifiers, statuses and local scope are inspected. Source authenticity and governed acceptance are **not verified**. |
| Resource, action and effect | Request carries all three, compared using an **informative, local** `resources`/`actions`/`effects` convention. |
| Policy and context | An explicit local policy object is bound by ID, current status and permitted effect/resource. No GAAM-wide policy schema or precedence is invented. |
| Delegation/attenuation | Typed sets enforce child-subset-parent and prohibit amplification. Other opaque scope types produce `indeterminate`. |
| Time, expiry, revocation | Canonical lifecycle fields and fixed evaluation time are tested. Status observations include explicit age bounds; **live registry authority is not verified**. |
| Decision, evidence and receipt | Schema-valid decision receipt references authority and policy; observations carry evidence identifiers. Referenced evidence bytes/authenticity are not verified. |
| Deny, failure, indeterminate | Denied scope/lifecycle, unavailable/stale/conflicting observations and invalid input are distinguished. Unsupported semantics never produce a permit. |
| Decision vs execution | `effectExecuted: false` is explicit on every response; no effect adapter is invoked. |
| Replayable attributable evidence | Canonical input digest and deterministic local decision/receipt ID are produced; source authentication, durable retention, signature and replay rejection are not demonstrated. |

## Explicit scenario-local contracts

The canonical GAAM v0.9.0 `scope` and `delegatedScope` schemas contain **opaque objects**. This example interprets precisely `authority.scope = {resources: [...], actions: [...]}` and `delegation.delegatedScope = {resources: [...], actions: [...], effects: [...]}`. The set-subset comparator is a *local evaluation convention*, not a new normative requirement or a general comparator for arbitrary GAAM scope objects. Unknown keys, absent sets, unsupported policy fields and missing observation data yield `indeterminate`, not implicit permission.

The `policy` and `observations` JSON fields are also informative example-local inputs. A successful run assumes their trust-boundary observations were already validated by an external provider. It **does not** justify an operational permit from an unauthenticated JSON file.

This exercise intentionally leaves actual transaction execution, external effect outcome, cryptographic provenance, cross-registry interpretation, receipt signing, policy precedence, value ceilings, real-world status freshness and replay prevention as **unverified**. Address any needed normative expression through the governed GAAM change lifecycle; do not silently promote this local convention to a canonical profile.

## Regression and evidence

The accompanying tests exercise in-scope acceptance, actor and parent mismatch, amplification, revocation and expiry, missing/stale/future status evidence, opaque scope, a structurally valid artifact without sufficient runtime evidence, deterministic input digests, and invalid JSON. Passing tests establish only the described **synthetic E1 functional behaviour**, not independent profile conformance or E2/E3 readiness.

**Related:** issue #102 (adopter-path evaluation); #20 (independent implementation reports); #21 (cross-implementation interoperability).
