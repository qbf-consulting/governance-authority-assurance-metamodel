# OPA/Rego contextual policy-evaluation experiment

**Status:** experimental/informative, scoped to [GAAM issue #121](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/121). **Normative baseline:** GAAM Candidate specification edition v0.9.0, distributed in the v0.9.5 maintenance line. This example is not a normative profile, conformance adapter, or authorization service.

## Reproduce the experiment

Run from the repository root with the **OPA v1.22.3** CLI installed:

~~~sh
opa check --strict experimental/opa-policy-evaluation/policy.rego
python experimental/opa-policy-evaluation/experiment.py --all
python experimental/opa-policy-evaluation/experiment.py --case positive
python experimental/opa-policy-evaluation/experiment.py --case fake-verification-flags-revoked
~~~

The dedicated CI workflow downloads the official v1.22.3 Linux binary from the OPA GitHub release and verifies SHA-256 **b6e7796ca71c22bffebeb0d58074170830d436a148d0490387e387d2d36d764b** before use. There are no Python dependencies beyond the standard library and no server, externally hosted policy registry or private credentials.

The test runner reuses the actual Basic Governed Decision authority and delegation fixtures; it constructs an *explicitly synthetic* request, applicable policy, observation time, evidence state and revocation state. The 28 scenarios mutate these inputs. They are not evidence of live authority, independent authentication, governance consent, or a real effect.

## Source-to-evaluator mapping

| Domain input | Existing GAAM meaning | OPA evaluation boundary |
| --- | --- | --- |
| Authority source, issuer, effects, status and scope | GAAM-AUTH-001–005, GAAM-ART-001–003 | Parses the existing authority example; cannot independently authenticate its source or legality. |
| Delegate, parent reference, effects and expiry | GAAM-DEL-001–005, GAAM-ART-004–005 | Compares a bounded single-hop relationship; does not validate institutional parent competence, a multi-hop chain or current remote status. |
| Policy revision and prohibition | GAAM-POL-001–005, GAAM-DEC-003 | Uses a synthetic policy version; **does not** demonstrate approved authoritative policy text, precedence or signed package provenance. |
| Evidence freshness and revocation | GAAM-EVID-001–004, GAAM-RUN-002–003 | Checks declared state and deterministic timestamps; no trusted resolver, signature, clock proof, replay protection, conflict resolution or authoritative evidence of freshness. |
| Policy predicate and local hashes | GAAM-ASSUR-001–002, GAAM-OUT-001–003 | Computes a **candidate** predicate and SHA-256 hashes of local Rego/input bytes; these are byte-integrity references, not proof of origin, real authority, or independent assessment. |
| Enforcement, observed effect, review and remedy | GAAM-RUN-004–009, GAAM-ACC-001–003, GAAM-APR-001–003 | No enforcement attempt, execution evidence, true GAAM decision receipt, challenge or remedy is produced. |

The output deliberately contains **authorityEstablished: false**, **enforcementAttempted: false**, **observedEffect: null** and **gaamDecisionReceipt: null** even when the OPA predicate is true. A true predicate is **satisfied**, not an authorized GAAM permit. A false predicate is **not-satisfied**, not necessarily a legitimate denial. Missing, conflicting, unsupported, malformed or unavailable required state yields **indeterminate**. Error paths (nonzero evaluator exit, unavailable binary, undefined/malformed response or timeout) do not become a success.

**Fabricated verification flags are ignored.** The extra booleans sourceVerified, parentActive, scopeValid and evidenceFresh have no Rego rule significance. Even their true values cannot establish an independent authority source. In the revoked-parent negative case they do not alter the failing predicate; in the positive case the outcome remains a mere candidate. The experiment cannot verify whether the underlying authority and evidence fixtures were truthfully issued in the first place.

**Time-of-check / time-of-use:** A cached positive evaluation is never sufficient to establish a valid later enforcement decision. Authority status, evidence freshness, policy changes and the observed effect require separately governed verification at the actual enforcement boundary. The example uses one normalized UTC test clock and checks lexicographically comparable source timestamps; it neither validates a trusted clock nor solves lifecycle convergence. The test harness does not accept arbitrary unversioned predicates as GAAM governance decisions.

## What is actually tested

The [scenario matrix](cases.json) exercises a positive bounded effect, out-of-scope and amplified authority (including an overbroad dormant child grant), replayed evidence, revoked/suspended/expired parent, revoked delegation, unauthorized redelegation, current/superseded/prohibited policy, stale/missing/conflicting evidence, missing authority-source claim, unknown/unavailable revocation, actor mismatch, unrecognized policy/contract versions, malformed time, and deliberate false verification flags.

A successful CI run proves only that the **pinned OPA release** evaluates the sample Rego policy as expected and the wrapper preserves the distinction between false, unknown and true predicate results. Local policy and input digests make the record reproducible, but do not authenticate who approved a rule or its legal authority. This cannot satisfy [independent implementation issue #20](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/20) or [cross-implementation evidence issue #21](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/21).

## Adoption evaluation and final disposition

| Criterion | Existing GAAM reference adapter | This OPA/Rego experiment |
| --- | --- | --- |
| Scope/time/delegation predicate checks | Available in the portable Boolean and raw-artifact vectors, within their documented limits | Reproduces selected single-hop conditions in a policy engine |
| False-success and unknown-state handling | Established runner rejects adapter crashes and malformed results | Explicit additional separation of OPA engine failure, missing state and false predicate |
| Authority-source verification | Not independently established | Not independently established |
| Policy language interoperability | No external policy-language dependency | Native Rego syntax, but no accepted cross-engine semantic contract |
| Operational surface | Python standard library and portable kit | 61 MB external binary, new policy-version and package lifecycle considerations |
| Evidence gained | Repository-authored reference-vector evidence | Repository-authored second evaluation mechanism, not independent adopter evidence |

**Disposition: STOP (no general adapter adoption).** Rego demonstrates that GAAM-compatible *inputs* can be evaluated by an independent policy engine without making the engine an authority source. However, for this one scenario, the new runtime dependency, version governance and policy-authenticity obligations outweigh demonstrated adoption or interoperability gains beyond the reference adapter. Preserve this small **informative research experiment** and its test evidence, but do not maintain a production policy gateway, introduce new normative policy types, promote the example as independent conformance evidence, or start a release.

**Revisit only** if an external adopter presents authenticated sources and a concrete evaluation interoperability need that the existing reference adapter cannot demonstrate. Such work would require a separate authority/evidence/provenance contract and change-control decision. No GAAM normative identifiers, schemas, profile requirements or conformance classes change here.
