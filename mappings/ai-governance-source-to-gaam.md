---
title: "AI Governance Source-to-GAAM Crosswalk"
permalink: /mappings/ai-governance-source-to-gaam/
parent: "Mappings and Source Crosswalks"
grand_parent: Appendices
artifact_type: "Informative source crosswalk"
normative_status: "Informative"
---
# AI Governance Source-to-GAAM Crosswalk

{% include gaam-meta.html %}

## Purpose

This crosswalk evaluates the AI-governance/Trust over IP comparative research supplied for issue #32 against GAAM v0.9.0. It tests whether the source identifies AI-governance requirements that require new GAAM core semantics, or whether those requirements can be represented through existing GAAM concepts, existing profiles, profile-specific constraints, evidence classes, and external mappings.

The supplied source is a comparative synthesis of multiple GenAI responses using the same research prompt. The source itself states that the responses were retained substantially as generated, with formatting changes only. It is therefore treated here as **research input**, not as authoritative evidence of law, standards status, protocol capability, or technical feasibility.

## Interpretation states

| State | Meaning |
|---|---|
| `covered` | GAAM core and/or an existing GAAM profile already contains the required governance semantic. |
| `profile-extension` | GAAM semantics are sufficient, but an AI-specific profile should constrain targets, evidence, thresholds, or required artifacts. |
| `external-mapping` | The requirement is substantive AI-domain or regulatory content that should be mapped to GAAM without becoming GAAM core. |
| `core-gap` | A material requirement cannot be represented without adding or changing GAAM core semantics. |

No `core-gap` is established by this assessment.

## Crosswalk

| Source concern | GAAM treatment | State | Evidence / implementation consequence |
|---|---|---|---|
| Model/agent identity and accountability | Governed entity, actor, principal, agent, accountability; Agentic Systems Profile | `covered` | AI identity establishes subject/scope, not authority. Machine actors remain attributable to accountable persons or organisations. |
| Delegation to agents | Authority and delegation semantics; Delegated Authority and Agentic Systems profiles | `covered` | Delegation is bounded, traceable, revocable/terminable and cannot enlarge parent authority without an independent source. |
| Capability scoping / excessive agency | Capability-versus-authority distinction, constraints, runtime decision and effect admission | `covered` | Profile should bind tool/resource/purpose/value/time/depth constraints to AI effects. |
| Runtime authorization | Runtime Governance Profile plus Agentic Systems Profile | `covered` | Consequential effects are evaluated at runtime; possession of credentials or technical capability is insufficient. |
| Machine-testable rules | Policy/rule/control semantics and Machine-Actionable Governance Profile | `covered` | AI implementations may bind external rule languages while preserving traceability to normative policy and authority. |
| Runtime telemetry and observability | Evidence, provenance, freshness, governance events and Continuous Assurance | `profile-extension` | Define AI-specific evidence classes and freshness/invalidation triggers. Telemetry is not itself assurance or authorization. |
| Runtime attestation | Evidence/verification/assessment/assurance chain | `profile-extension` | Attestation can support bounded technical claims. It must not be represented as proof of authority or universal behavioural fitness. |
| "Cognitive-state" challenge/response | Existing evidence and assurance semantics can represent bounded probes, but not an unqualified cognitive-integrity claim | `profile-extension` | Reframe as scoped runtime evidence with explicit limitations; do not standardize a claim that cryptography proves an uncompromised internal cognitive state. |
| Continuous capability/risk evaluation | Continuous Assurance Profile and lifecycle/invalidation requirements | `profile-extension` | Add AI-specific evaluation artifacts, reassessment triggers and capability/risk thresholds; retain indeterminate/degraded states. |
| Human oversight / override | Runtime decision, safety, escalation, effect admission and accountability semantics | `profile-extension` | Express human confirmation as a policy condition for defined consequential effects, not as universal co-signing for every AI action. |
| Consequential action boundaries | Effect-centred runtime governance | `covered` | Govern the proposed effect rather than globally labeling an AI system trusted/safe. |
| Incident and post-deployment monitoring | Governance events, assurance lifecycle, accountability, decision reconstruction, remedy | `profile-extension` | AI profile should define incident evidence and when monitoring causes suspension, reassessment, restriction, review or remedy. |
| Model provenance | Evidence provenance and governed-artifact semantics | `profile-extension` | Define model identity/version/provenance evidence without prescribing a single model-ID scheme. |
| Training/fine-tuning data provenance and quality | Evidence semantics are available; substantive data-governance duties are external | `external-mapping` | Map dataset provenance, consent, quality, bias and lawful-use obligations from applicable standards/regulation. |
| Retrieval/context provenance | Evidence provenance, freshness and permitted-use semantics | `profile-extension` | Treat retrieved context as evidence/input with purpose, freshness, source and transformation metadata where consequential. |
| Output/content provenance | Evidence/provenance semantics are sufficient | `profile-extension` | Bind C2PA or other provenance mechanisms only in implementation/domain profiles; do not require them in GAAM core. |
| Bias/fairness/disparate impact | GAAM can govern evidence, decisions, effects, affected parties and remedy, but does not define fairness metrics | `external-mapping` | Import applicable metric/assessment obligations through profile mappings, not new authority semantics. |
| Explainability/transparency | Decision receipts, reason codes, evidence traceability and accountability provide governance structure; AI explanation duties are external | `external-mapping` | Map jurisdiction/standard-specific documentation and explanation duties to GAAM artifacts. |
| Model cards / technical documentation | Governed artifacts and evidence can carry them | `external-mapping` | Treat required documentation content as domain-specific evidence/artifact requirements. |
| AI risk-tier classification | High-Impact Systems can express consequences and stronger evidence/assurance expectations, but statutory risk tiers are external classifications | `external-mapping` | Crosswalk external risk classes to GAAM profile selection and controls without making the external taxonomy GAAM-native. |
| Independent AI audit / conformity assessment | Verification, assessment, assurance, assessor scope and evidence semantics | `covered` + `external-mapping` | GAAM can represent the assurance claim; accreditation/conformity criteria come from the external regime. |
| Regulatory mapping / mutual recognition | Governance context, cross-context recognition/mapping and evidence semantics | `external-mapping` | Create explicit crosswalks; never imply that a private GAAM conformance claim equals statutory conformity without authority. |
| Revocation / suspension after changed evidence | Delegation lifecycle, authority lifecycle, continuous assurance and runtime governance | `covered` | Profile should define AI-specific invalidation triggers such as model/config/tool or evaluation changes. |
| Redress for AI-mediated decisions | Accountability, affected-party challenge, appeal and remedy | `covered` | AI profile should require decision/evidence references sufficient for review while respecting privacy and security boundaries. |

## Existing profile composition

The supplied concerns overlap heavily with existing profiles rather than requiring a new core layer:

- **Agentic Systems** already maps delegation, outcome, runtime, agent, decision and safety requirements for `agent` and `agent-platform` targets.
- **Runtime Governance** maps outcome, runtime, lifecycle, decision and safety requirements for enforcement points and policy engines.
- **Continuous Assurance** maps assurance, lifecycle and assurance-result requirements for assurance services and governed systems.
- **Delegated Authority**, **Machine-Actionable Governance**, and **High-Impact Systems** provide additional bounded semantics for authority chains, executable rules, and consequential effects.

A future AI Governance Profile should therefore be a **composition and specialization profile**, not a parallel semantic model.

## Key boundary decisions

### Telemetry is evidence, not governance authority

The source's proposal to replace static risk assessment with continuous observability is directionally useful but semantically too strong. Runtime telemetry may become evidence. Evidence may support verification and assessment. Assessment may support a time-bounded assurance conclusion. Policy and authority then determine whether an effect is admitted.

```text
telemetry -> evidence -> verification/assessment -> assurance
          + authority + policy + context -> runtime decision -> effect
```

No link in this chain should be silently collapsed.

### Agent identity is not a fifth trust layer

The source proposes a distinct model/agent identity and delegation layer. GAAM instead treats an agent as a governed actor operating under bounded authority. This keeps governance protocol-neutral and avoids coupling the metamodel to a technology generation.

### Runtime probes must remain bounded claims

A challenge-response or attestation mechanism can establish specified technical conditions. This assessment does not support the stronger proposition that such a mechanism can prove that an AI system's internal "cognitive state" is uncompromised. Any profile claim must identify exactly what was tested, with what evidence, at what time, and with what limitations.

## Candidate disposition

```yaml
disposition: profile-plus-external-mappings
core_change_required: false
profile_candidate_supported: true
normative_promotion_authorized: false
```

The evidence presently supports an informative AI Governance Profile candidate that composes existing GAAM profiles and adds AI-domain constraints/evidence classes. It does not support modifying the frozen v0.9.0 normative core.

## Falsification / reopen conditions

Reassess this disposition if a material AI-governance obligation is demonstrated that cannot be modeled through current GAAM entities, authority/delegation, policy/rule/control, evidence, assessment/assurance, trust decisions, effects, governance events, accountability or remedy, and cannot be represented safely as a profile constraint or external mapping.

## Machine-readable companion

The same disposition matrix is available as [`ai-governance-source-to-gaam.json`](ai-governance-source-to-gaam.json).
