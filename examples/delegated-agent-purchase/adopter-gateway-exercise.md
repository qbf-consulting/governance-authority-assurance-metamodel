---
title: "Adopter Gateway Evaluation Exercise"
permalink: /examples/delegated-agent-purchase/adopter-gateway-exercise/
parent: "Delegated Agent Purchasing"
nav_exclude: true
artifact_type: "Informative implementation exercise"
normative_status: "Informative"
---

# Adopter Gateway Evaluation Exercise

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
| Deny, failure, indeterminate | Denied scope/lifecycle, unavailable/stale/**unresolved** observations and invalid input are distinguished; independently conflicting observations cannot be represented or adjudicated by the current input contract. Unsupported semantics never produce a permit. |
| Decision vs execution | `effectExecuted: false` is explicit on every response; no effect adapter is invoked. |
| Replayable attributable evidence | Canonical input digest and deterministic local decision/receipt ID are produced; source authentication, durable retention, signature and replay rejection are not demonstrated. |

## Normative-source and evidence disposition (issue #102)

This table reconciles the **ten requested evaluation elements** against the normative [requirements index](../../matrices/normative-requirements-index.csv), canonical v0.9.0 artifacts, and the executable test path. A requirement reference identifies a governing obligation; it is **not** a claim that the example proves conformance with that requirement. `Demonstrated` below means *repository-authored synthetic behaviour only*.

| # | Evaluation question and source | Demonstrated behaviour / actual evidence | Disposition and outstanding boundary |
| --- | --- | --- | --- |
| 1 | Originating principal and acting agent: `authority.subject`, `delegation.delegator`/`delegate`; GAAM-CORE-002, GAAM-AUTH-003, GAAM-DEL-004 | `test_binding_and_policy_provenance_mismatch_denied` compares identifiers, and `actorBinding` is required. | **Partial; external evidence dependency.** Caller authentication and the origin of the binding observation are not established by the CLI. |
| 2 | Authority provenance, acceptance and scope: `authority.authoritySource`, `issuer`, `status`, `scope`; GAAM-AUTH-001/002/003, GAAM-DEL-007 | Authority source is named, parent link and active states are checked; `test_schema_valid_artifact_does_not_prove_live_effective_authority` rejects missing live observation as indeterminate. | **Partial; external verification.** No issuer/source authenticity, governed activation/acceptance, or independent observation verification is established. Normative obligations exist; implementation evidence does not yet satisfy them. |
| 3 | Resource/action/effect: request and canonical `permittedEffects`/`scope`; GAAM-AUTH-002, GAAM-AUTH-005 | Explicit values and rejection of out-of-scope purchase are tested. | **Demonstrated only under local vocabulary.** No portable, normative typed comparator for arbitrary `scope` objects is demonstrated. |
| 4 | Policy/context: `authority.authoritySource`, receipt `policy`; GAAM-DEC-003, GAAM-AUTH-006/007 | The example binds a local policy ID and checks allowed effect/resource, status and freshness threshold. | **Partial; local policy contract.** Risk tolerance, purpose, overlapping-authority precedence and independent policy provenance are not established by this exercise. |
| 5 | Delegation validity and attenuation: canonical `delegation.schema.json`; GAAM-DEL-001/002/003/004/005/007 | Parent/delegate linkage, `delegationPermitted`, typed-set subset, lifecycle and non-amplification tests pass. | **Partial.** Typed scope comparison is scenario-local; actual activation evidence, delegated termination conditions, external provenance and propagation rules are not independently verified. |
| 6 | Evaluation time, expiry, revocation: `effectiveFrom`/`effectiveUntil`, `status`, `propagation`; GAAM-DEL-005, GAAM-LIFE-001/002/004 | Fixed evaluation clock, temporal containment, inactive/revoked cases and age-bounded observations are tested. | **Partial; external evidence dependency.** A timestamp on a supplied observation is not trusted registry freshness, a verified transition, or propagation confirmation. |
| 7 | Decision/evidence/receipt: `decision-receipt.schema.json`; GAAM-DEC-001/003/004, GAAM-ACC-001 | `test_positive_evidence_bounded_and_canonical_receipt` establishes a structurally valid local receipt linked to IDs. | **Partial.** An evidence ID or receipt structure does not authenticate the producer, validate referenced evidence bytes, or prove that the determination is operationally authoritative. |
| 8 | Deny/failure/indeterminate outcomes: receipt `outcome` enum and the example-local `status`; GAAM-AUTH-005, GAAM-LIFE-003 | CLI and tests distinguish `permit`, `deny` and `indeterminate`; unsupported scope, missing/stale observations and malformed JSON do not grant permission. | **Partial; local interpretation.** `indeterminate` is an example response, mapped to receipt `require-additional-evidence`; this is not a new normative receipt outcome. **Contradictory independent observations are not representable or adjudicated** in the single-record input structure. |
| 9 | Authorization-to-execution boundary: enforcement point in receipt; GAAM-AUTH-005, GAAM-ACC-001 | Every result carries `effectExecuted: false`, with no transaction integration; tested by `test_receipt_is_not_enforcement_or_replay_protection`. | **Demonstrated non-execution; enforcement unverified.** No actual effect admission, execution gate, outcome confirmation or redress integration is tested. |
| 10 | Replayable/attributable evidence: `decision`/`decisionTime`/`accountableParty`; GAAM-DEC-001/004, GAAM-EVT-002 | Same input deterministically reproduces digest and receipt ID; accountability identifier appears in schema-valid receipt. | **Partial; external evidence dependency.** Neither digest nor actor string establishes source authenticity, secure storage, audit-log retention, cryptographic attribution or replay prevention. |

### Material findings and disposition

- **F-102-A — Source/observation authenticity:** The executable receives `issuer`, `source`, `observedAt`, `evidenceId` and `value` as untrusted input without verifying their producer or integrity. This is **not** a claim that GAAM lacks authority requirements; GAAM-AUTH-001/003 and GAAM-DEL-004 already constrain authority interpretation. **Disposition:** external implementation/evidence dependency; record as unverified and make the evaluation contract explicit. A synthetic local `permit` is never sufficient to authorize an actual consequential effect.
- **F-102-B — Typed-scope and policy semantics:** Canonical `scope` and `delegatedScope` schemas use open objects. The gateway's subset and policy logic is only a local convention; arbitrary scope/policy objects have no demonstrated interoperable comparator or precedence. **Disposition:** explicitly informative; any proposal for a portable binding must go through Candidate change control, not an informal promotion of these rules.
- **F-102-C — Multiple-source conflict handling:** A single `observations` record per category cannot express conflicting claims from independent providers. Rejection of an `unknown` value is not conflict resolution. **Disposition:** coverage gap, leave unproven rather than claim tested; defer multi-source agreement/precedence to a separately governed proposition if an adopter demonstrates need.
- **F-102-D — Receipt and effect evidence:** The schema-valid receipt and digest are neither signed nor proof of execution. **Disposition:** informative evidence only; any operational E2 implementation must supply attribution, audit integrity, effect/outcome records, retention and replay controls appropriate to its governing framework.
- **F-102-E — Independence:** This repository-authored evaluator is distinct from the portable reference adapter but was not implemented by an external participant. **Disposition:** self-assessed; independent implementation evidence remains governed by issue #20 and cross-implementation evidence by #21.

**Assurance verdict:** the scenario demonstrates an executable **local** decision sequence, negative tests and structural receipt production; the full ten-element proposition is **not proven as independently implementable or operationally authoritative**. All five findings are explicit limitations, not successful independent E2/E3, complete profile conformance or a hidden new normative obligation.

## External independently authored evaluator hand-off

**Reference source:** GAAM **v0.9.3** is the current Candidate maintenance release and retains the normative v0.9.0 semantics, requirements, profiles and canonical schema identifiers. **The runnable gateway exercise was added after the v0.9.3 tag.** Pin the repository revision that contains it, not just the v0.9.3 release. The source revision for this hand-off is `1f85d8835b5db3c383127bd43af1e30c4551b034` (PR #111); later maintenance changes can be assessed separately.

```bash
git clone https://github.com/qbf-consulting/governance-authority-assurance-metamodel.git
cd governance-authority-assurance-metamodel
git checkout 1f85d8835b5db3c383127bd43af1e30c4551b034
python -m pip install -r requirements-dev.txt
python scripts/gaam.py validate-package conformance-kit/starter
python scripts/gaam.py validate-claim conformance-kit/starter/artifacts/conformance-claim.json
python examples/delegated-agent-purchase/adopter_gateway.py < examples/delegated-agent-purchase/adopter-gateway-case.json
python -m pytest tests/test_adopter_gateway.py -q
```

The above commands reproduce **repository-authored reference behaviour** only. A participant seeking to test independent implementability must derive their own minimal evaluator from the published normative specification, selected profile manifests and canonical schemas. Do **not** copy `adopter_gateway.py` or translate its local comparison algorithm and call that independent implementation. The example and its test fixtures can serve as *comparison and adversarial challenge inputs* after implementation, but their local `resources`/`actions`/`effects` comparator, observations format, reason codes and `indeterminate` response are **informative**; where the normative baseline does not specify a comparator or mechanism, record a separate finding instead of inferring an interoperability contract.

### Ten-element implementation and evidence worksheet

For each of the ten elements in the [normative-source and evidence disposition](#normative-source-and-evidence-disposition-issue-102), a participant should retain **their own** source references, request/inputs, expected/observed outputs, policy/context and evaluation clock, test command, environment and tool versions, evidence identifiers and integrity checks, and disposition (`demonstrated`, `partial`, `unsupported normative expression`, or `external evidence dependency`). Report failures and indeterminate outcomes rather than converting them into PASS.

| Element | Minimum independently inspectable result |
| --- | --- |
| 1. Principal and agent | Show actor binding and source of identity/role evidence; a string identifier is insufficient. |
| 2. Source, acceptance and scope | Link operative authority to attributable source, acceptance/activation and scoped grant, or record absent proof. |
| 3. Resource, action and consequential effect | Show which effect was evaluated at what resource and which local semantics interpret it. |
| 4. Policy and context | Record applicable policy version, purpose, context, precedence and external decision authority. |
| 5. Delegation and attenuation | Trace the chain, acceptance and permitted re-delegation, including amplification and inactive-parent negatives. |
| 6. Effective time and revocation | Record evaluation time, status observation provenance, bounded freshness and unavailable/revoked results. |
| 7. Decision, evidence and receipt | Preserve decision, linked evidence and receipt; distinguish schema validity from authenticated provenance. |
| 8. Denied, failed and indeterminate | Test denial, malformed/failing operation, missing and conflicting evidence, and unsupported scope without default permit. |
| 9. Authorization versus execution | Demonstrate that a decision does not itself cause an effect; record actual enforcement/effect evidence **only if** implemented. |
| 10. Replay and attribution | Reproduce inputs, explain accountable party and receipt provenance; identify missing signatures, storage and replay controls. |

**Required counterexamples:** unauthenticated or contradictory authority observations; revoked/expired/not-yet-effective parent; delegation amplification; out-of-scope resource/effect; unsupported scope comparator; stale or unavailable policy/status evidence; and an apparently successful receipt with no performed effect. A repository fixture may demonstrate how to *challenge* a claim but cannot supply the independent participant's real authority, status or execution evidence.

### Evidence acceptance and routing

Use the existing [profile-selection guide](../../implementation-reports/profile-selection-guide.md) to select a declared target and dependency-closed profile boundary. The Foundation and Delegated Authority profiles are **candidates to evaluate**, not automatically satisfied claims. Use the existing [implementation-report template](../../implementation-reports/TEMPLATE.md), [machine-readable report and evidence-manifest contracts](../../implementation-reports/README.md) and [independent implementation intake](../../implementation-reports/independent-implementation-intake.md); disclose the source revision, assessor relationship, limitations and open exceptions.

- **Repository exercise / E1:** running the commands above, adapting maintainer code or producing synthetic outputs does not establish independence.
- **Independent implementation / E2:** independently authored code and admissible non-synthetic evidence require governed assessment and acceptance under [issue #20](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/20). Merely supplying a CLI is not an E2 acceptance.
- **Cross-implementation / E3:** two independent implementations must exchange and evaluate each other's artifacts, preserve mismatch cases and undergo the separate process in [issue #21](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/21).

**Stop rather than assert success** if the participant requires an invented authority source, unchecked status/identity evidence, arbitrary scope comparison, implied enforcement from a receipt, or a claim beyond the actual tested requirement set. Report the issue against the governing GAAM requirement or schema and existing issue #102; any normative proposal must follow the Candidate change-control process.

## Recorded E1 run evidence and impact review

Run `python scripts/generate_gateway_evidence.py` from the same checkout as the published gateway CLI. It invokes that **public CLI** independently for sixteen cases and writes `validation/adopter-gateway-evaluation.json`. The ordinary validation workflow runs the generator and uploads that JSON through the **existing** `gaam-validation-evidence` artifact; this is a run-specific record, not an additional implementation-report registry or an accepted conformance claim. Capture the workflow run URL alongside the generated `sourceCommit`. Individual records include the full synthetic input, expected/observed status, reason, exit code, no-effect flag, command, source/tool versions, start/finish times, digest, fixed evaluation clock, local policy context and unresolved exceptions. **No external human onboarding measurements are inferred.**

A positive **local** result deliberately persists when the `authorityStatus.source` string is changed to an unverified claimant. The dossier highlights that as a **known limitation** rather than an operational success. The conflicting-provider case results in `indeterminate`, without pretending that two trusted sources were reconciled. Missing/expired/stale/unsupported authority conditions cannot be promoted to permission merely because a JSON schema passes. The input digest is reproducible but not cryptographic attribution of the actor or evidence producer.

### Bounded security, privacy, effect and compatibility impacts

| Dimension | Evaluated condition and disposition |
| --- | --- |
| Security and authority | Schema validity, denied amplification, stale/absent status and false-success cases are tested. The source-label counterexample demonstrates absent authentication; **external source trust remains unverified**, and this CLI must never gate a real effect. |
| Privacy | The fixed sample contains synthetic actor, principal, merchant, evidence and accountable-party identifiers. The dossier retains whole inputs for reproducibility; production equivalents would require minimisation, access control, purpose limits and retention decisions **not provided** by the CLI. Do not ingest personal data into these CI artifacts. |
| Scope, lifecycle and time | Local typed-set comparison, expiry, revocation, future/stale evidence and evaluation clock are tested. Arbitrary scopes, trusted freshness and propagated revocation are **not** independently evaluated. |
| Execution, affected parties and remedy | `effectExecuted: false` is mandatory for every case. No payment, enforcement call, notification, interruption, challenge or remedy is executed. A receipt represents a decision only; real operators need separate controlled effect/outcome and remedy records. |
| Compatibility and governance | v0.9.0 schemas/identifiers and v0.9.3 release remain unchanged. The generated record uses **informative** local statuses/reasons, not portable GAAM conformance vocabulary; no OAuth/MCP or v0.10.0 experimental field is made normative. |

## Explicit scenario-local contracts

The canonical GAAM v0.9.0 `scope` and `delegatedScope` schemas contain **opaque objects**. This example interprets precisely `authority.scope = {resources: [...], actions: [...]}` and `delegation.delegatedScope = {resources: [...], actions: [...], effects: [...]}`. The set-subset comparator is a *local evaluation convention*, not a new normative requirement or a general comparator for arbitrary GAAM scope objects. Unknown keys, absent sets, unsupported policy fields and missing observation data yield `indeterminate`, not implicit permission.

The `policy` and `observations` JSON fields are also informative example-local inputs. A successful run assumes their trust-boundary observations were already validated by an external provider. It **does not** justify an operational permit from an unauthenticated JSON file.

This exercise intentionally leaves actual transaction execution, external effect outcome, cryptographic provenance, cross-registry interpretation, receipt signing, policy precedence, value ceilings, real-world status freshness and replay prevention as **unverified**. Address any needed normative expression through the governed GAAM change lifecycle; do not silently promote this local convention to a canonical profile.

## Regression and evidence

The accompanying tests exercise in-scope acceptance, actor and parent mismatch, amplification, revocation and expiry, missing/stale/future status evidence, opaque scope, a structurally valid artifact without sufficient runtime evidence, deterministic input digests, and invalid JSON. Passing tests establish only the described **synthetic E1 functional behaviour**, not independent profile conformance or E2/E3 readiness.

**Related:** issue #102 (adopter-path evaluation); #20 (independent implementation reports); #21 (cross-implementation interoperability).
