---
title: "Threat Register Coverage Reassessment (October 2026)"
nav_exclude: true
artifact_type: "Informative security review"
normative_status: "Informative"
---

# Threat Register Coverage Reassessment (October 2026)

**Status:** informative, repository-maintainer assessment; not an independent security review.

**Baseline:** GAAM v0.9.2 Candidate (frozen v0.9.0 semantic/canonical identifiers).
**Source register:** [threat-register.json](../threat-model/threat-register.json).
**Change boundary:** No edits to canonical threats, requirements, profiles, schemas, conformance semantics or release assets are authorized by this assessment. The [Candidate Stability and Change-Control Policy](candidate-stability-policy.md) governs any subsequent promotion.

## Method

Threat coverage here means the ability to identify a failure mode and articulate a falsifiable expected behaviour; it **does not** mean a mitigation is implemented or independently assured. The original seven register entries are preserved, and newer implementation patterns, experimental pressure cases and future-evolution concepts are assessed for *distinct* failure mechanisms. File existence establishes a research or test surface, not proof of effective operational controls.

Disposition vocabulary:
- **retain**: keep the existing canonical threat;
- **refine**: a narrower risk fits within an existing canonical threat but warrants a better explanatory or evidence mapping;
- **candidate-new**: a distinguishable misuse mechanism merits experimental threat specification and testing before promotion;
- **defer**: material concern without sufficient evidence for canonical promotion.

## Existing canonical register (all retained)

| ID | Existing threat | Coverage conclusion | Reassessment |
| --- | --- | --- | --- |
| GAAM-THR-001 | authority laundering | retain | Still catches misrepresented authority source; action binding and recognition confusion are potential specialisations. |
| GAAM-THR-002 | delegation amplification | retain | Still captures child grant exceeding parent authority; collective exercise is not necessarily delegation and needs independent consideration. |
| GAAM-THR-003 | stale revocation | retain | Covers directly revoked authority used after withdrawal; cross-boundary freshness and dependency propagation need pressure testing. |
| GAAM-THR-004 | assurance inflation | retain | Covers claims exceeding evidence/independence; composition and contradictory evidence are richer failure paths. |
| GAAM-THR-005 | accountability fragmentation | retain | Decision attribution remains fundamental; post-decision effects and accountability continuity need testing. |
| GAAM-THR-006 | remedy obstruction | retain | Covers remedy absence; ineffective or non-propagating remedy can occur even when a formal process exists. |
| GAAM-THR-007 | package substitution | retain | Canonical artifact integrity remains distinct from dynamic authorization and runtime state. |

## Candidate coverage reconciliation

The IDs below (`REVIEW-01` etc.) are **review identifiers, not GAAM-THR identifiers**.

| Review ID | Candidate failure path | Nearest existing threat | Disposition | Source/evidence boundary | Falsification scenario to establish |
| --- | --- | --- | --- | --- | --- |
| REVIEW-01 | Authenticated actor signs an exact commitment exceeding a current mandate or relies on approval bound to another action | THR-001; THR-002 | refine | [Authority at Commitment](future-evolution/concepts/authority-at-commitment.md), informative concept with specified negative cases | Valid signature with absent mandate or stale action-bound approval must not permit the commitment. |
| REVIEW-02 | A collective principal's action is admitted using duplicate, unqualified, stale or insufficient controller approvals | THR-001; THR-002 | candidate-new | [Collective Authority Exercise](future-evolution/concepts/collective-authority-exercise.md), informative pressure test; companion experimental fixture described there | Two signatures from one participant must fail a 2-of-3 rule; missing composition-rule evidence must not permit. |
| REVIEW-03 | Downstream cache/replica/decision continues to accept an authority whose upstream dependency was revoked | THR-003 | refine | [Continuity, Caching and Revocation](future-evolution/concepts/continuity-caching-and-revocation.md), informative; [revocation boundary pattern](../examples/revocation-propagation-boundaries/) | Partition or stale cache must not silently convert unknown current status to authorized use. |
| REVIEW-04 | Individually assured components are treated as proof of end-to-end composed-system assurance | THR-004 | refine | [Assurance Composition](future-evolution/concepts/assurance-composition-and-dependency.md), informative | Component evidence without valid composition/dependency conditions cannot establish system-level assurance. |
| REVIEW-05 | Registry listing, qualification, discovery or recognition is elevated to transaction authority without an applicable authorization policy | THR-001 | candidate-new | [Standing, Qualification and Recognition](future-evolution/concepts/standing-qualification-and-recognition.md), informative; [cross-registry pattern](../examples/cross-registry-recognition/) | Registered or recognized but unauthorized actor must not be permitted to perform the consequential act. |
| REVIEW-06 | Missing, stale, conflicting or unavailable material evidence becomes an implicit positive authorization | THR-001; THR-004 | candidate-new | [Uncertainty and Confidence](future-evolution/concepts/uncertainty-and-confidence.md), informative; v0.9.2 ecosystem-derived unknown-authority vector noted in [changelog](../CHANGELOG.md) | Unknown or conflicting authority evidence never maps to an unqualified permit. |
| REVIEW-07 | Access permission is stretched into inference, tracking, correlation, or decision-use authority across contexts | No adequate explicit category | candidate-new | [Privacy, Inference and Observability](future-evolution/concepts/privacy-inference-and-observability.md), informative; not an asserted baseline control | Authorized collection without inference/use authority must not allow a consequential inferred-attribute decision. |
| REVIEW-08 | Nominal appeal/remedy completes administratively without changing the affected consequential state | THR-006 | refine | [affected-party/remedy concept](future-evolution/concepts/affected-parties-and-remedy.md); [remedy propagation pattern](../examples/downstream-remedy-propagation/); [security and affected-party review commit](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/commit/777847b9346bee53fbe327058ad497d149283fde) | A closed complaint with unchanged harmful downstream effect does not satisfy effective remedy. |
| REVIEW-09 | Evaluation uses authority, approval, or policy state from the wrong time relative to the material effect | THR-003; THR-001 | refine | [Temporal Governance](future-evolution/concepts/temporal-governance.md); [Authority at Commitment](future-evolution/concepts/authority-at-commitment.md), informative | Authority expired before a material transition must not be accepted because it was valid at request creation. |
| REVIEW-10 | Institutional transition incorrectly preserves, destroys or transfers powers and obligations | THR-001; THR-005 | defer | [Institutional Succession](future-evolution/concepts/institutional-succession.md); [succession pattern](../examples/institutional-authority-succession/) | Verify withdrawn predecessor authority cannot silently act as successor; historical accountability remains interpretable. |

### Prioritisation

**First experimental set:** REVIEW-02, REVIEW-05, REVIEW-06 and REVIEW-07. These have plausible failure mechanisms not explicitly named by the seven-entry register. Their status is *candidate-new*, **not** an accepted canonical addition.

**Targeted refinements:** REVIEW-01, 03, 04, 08 and 09 can be captured as additional misuse paths or evidence mappings under existing canonical threats without immediately minting new IDs.

**Deferred:** REVIEW-10 requires stronger cross-implementation evidence and a precise boundary between authority continuity, liability, and archival truth.

## Evidence and promotion gates

For a candidate-new threat to enter the canonical register:
1. Show why the failure is not adequately captured by an existing canonical threat (avoid mere rewording).
2. Identify a governing GAAM Candidate requirement where possible. If none exists, **do not invent a requirement or claim v0.9.2 conformance**.
3. Supply a negative behavioural fixture with a deterministic expected decision and a positive counterexample where appropriate.
4. Record the threat asset, precondition, misuse path, affected parties, control expectation, observable evidence and residual uncertainties.
5. Validate all requirement/test references and assess compatibility, canonical-surface freeze and version impact under Candidate change control.
6. Distinguish repository-tested fixtures from independent implementation/security evidence; neither follows automatically from the other.

No risk score or control effectiveness rating is asserted here. Exposure and residual risk are deployment-specific until implementation evidence is available.

## Decision

**Coverage refresh warranted; canonical register expansion not yet approved.** The seven original categories are credible foundations, but the candidate review identifies four potentially distinct threat mechanisms needing experimental test/evidence packages. Avoid editing the frozen v0.9.0 threat register or its version field until the admission gate above succeeds. This informative review does not itself justify a GAAM release or alter v0.9.2 conformance.

## Follow-up

Track this review and evidence disposition in [issue #72](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/issues/72). Next useful increment is a small set of negative/positive candidate fixtures for REVIEW-02, 05, 06 and 07, followed by a documented promotion decision, not a mechanical increase in register size.
