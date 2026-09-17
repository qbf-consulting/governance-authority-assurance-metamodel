---
title: AI Governance Profile Candidate
permalink: /docs/future-evolution/concepts/ai-governance-profile/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# AI Governance Profile Candidate

## Status and boundary

This is an **informative research artifact** produced from issue #32. It does not modify GAAM v0.9.0, create a conformance claim, or make any external AI regulation, standard, protocol, model-evaluation method, identity scheme, or attestation technology normative for GAAM.

The working disposition is **profile + external standards mapping**: GAAM's current core semantics appear sufficient for the governance structure of AI systems and agents, while AI-specific obligations should be expressed through profile constraints, evidence classes, implementation guidance, and source crosswalks.

## Research proposition

AI governance should not create a second semantic model for machine actors. An AI system or agent remains a governed entity whose consequential effects are evaluated under authority, delegation, policy, evidence, assurance, context, runtime conditions, accountability, and redress.

The profile candidate therefore composes existing GAAM profiles rather than adding a new trust-stack layer or treating model identity, credentials, or runtime attestation as authority.

## Candidate conformance targets

A future AI Governance Profile could apply to:

- `ai-system`;
- `ai-agent`;
- `ai-agent-platform`;
- `ai-runtime-enforcement-point`;
- `ai-assurance-service`.

These target names are research vocabulary only. They are not v0.9.0 conformance targets.

## Existing GAAM profile composition

A future profile SHOULD be constructed by composing, at minimum where applicable:

- `gaam:profile:foundation:0.9.0`;
- `gaam:profile:agentic-systems:0.9.0`;
- `gaam:profile:runtime-governance:0.9.0`;
- `gaam:profile:continuous-assurance:0.9.0`;
- `gaam:profile:delegated-authority:0.9.0`;
- `gaam:profile:machine-actionable-governance:0.9.0`;
- `gaam:profile:high-impact-systems:0.9.0` when consequential-impact thresholds warrant it.

The Agentic Systems profile already maps delegation, runtime, agent-governance, decision, outcome and safety requirements. Runtime Governance separately covers enforcement points and policy engines, and Continuous Assurance covers assurance lifecycle requirements. This existing partitioning is preferable to duplicating the same semantics in an AI-specific core.

## Candidate AI-specific profile constraints

The profile layer, rather than GAAM core, is the appropriate place to require domain-specific declarations such as:

### Governed artifacts

An implementation should identify which governed artifacts are in scope, for example:

- model or model family;
- model version or immutable model artifact;
- AI system configuration;
- agent and agent runtime;
- prompts or instruction sets where governance-relevant;
- tools and external services;
- training, fine-tuning, evaluation, or retrieval datasets where relevant;
- generated outputs or consequential decisions.

Artifact identification establishes scope and provenance. It does **not** establish authority or fitness.

### Capability and authority

AI capability MUST remain distinct from authority. A model's demonstrated ability to perform a task, possession of a credential, registry inclusion, runtime identity, or successful attestation must not by itself admit a consequential effect.

A future profile should require explicit authority scope for consequential actions, including relevant purpose, resources, value/risk thresholds, delegation depth, expiry, supervision, and human-confirmation conditions.

### Runtime evidence

AI-specific runtime evidence may include:

- model and runtime identity;
- model/configuration version;
- tool grants and active capability constraints;
- workload or execution-environment attestations;
- policy version;
- evaluation and red-team results;
- drift or behavioural monitoring results;
- incident or degraded-state indicators;
- relevant provenance records.

These remain evidence inputs. The profile must preserve:

```text
telemetry != evidence sufficiency
attestation != authority
verification != assessment
assessment != assurance
assurance != authorization
```

### Continuous evaluation and assurance

AI capability and risk can change through model updates, configuration changes, tool changes, retrieved context, external dependencies, or new evidence. A future profile should therefore define assurance freshness, invalidation triggers, reassessment conditions, and degraded/indeterminate states using existing GAAM continuous-assurance semantics.

The profile should not claim that a cryptographic challenge can establish that an agent's internal "cognitive state" is uncompromised. Runtime probes may establish bounded technical propositions; broader behavioural fitness remains an assessment and assurance question with explicit limits.

### Consequential effects and human intervention

The unit of runtime governance should be the proposed **effect**, not a global label that an AI system is "trusted" or "safe".

Policy may permit, deny, restrict, suspend, or route an effect for human review. Human confirmation should therefore be represented as an effect-admission condition under policy rather than as a universal architectural requirement for every AI operation.

### Provenance

Training-data provenance, model provenance, retrieved-context provenance, and output/content provenance are important AI-domain evidence classes. GAAM can represent their provenance, freshness, permitted use, assurance, and relationship to decisions without defining a specific provenance protocol.

C2PA, credential formats, workload identity systems, model-card formats, or other mechanisms may be bound by an implementation profile or external mapping, but are not required by GAAM core.

### Incidents, monitoring, and remedy

A future profile should bind AI incidents and post-deployment monitoring to GAAM governance events, assurance invalidation, decision reconstruction, accountability, appeal, correction, and remedy. Monitoring evidence must be capable of changing operational state when policy requires it; reporting without an enforcement or remediation path is insufficient for consequential governance.

## External obligations and crosswalks

Requirements such as risk-tier classification, training-data governance, bias/fairness evaluation, explainability, model documentation, statutory incident reporting, conformity assessment, and jurisdiction-specific transparency obligations are domain or regulatory content. They should be mapped to GAAM semantics without silently importing them into GAAM core.

The companion mapping records whether each concern is:

- already covered by GAAM core/existing profiles;
- an AI-profile constraint or evidence-class extension;
- an external standards/regulatory mapping concern; or
- a genuine candidate core gap.

See [AI Governance Source-to-GAAM Crosswalk](../../../mappings/ai-governance-source-to-gaam.md).

## Falsification conditions

The conclusion that an AI profile is sufficient should be rejected if a material AI-governance requirement is found that:

1. cannot be represented as a governed entity, actor/agent, authority, delegation, policy/rule/control, claim/evidence, verification/assessment, assurance conclusion, trust decision, effect, governance event, accountability or remedy concept;
2. cannot be expressed as a profile constraint, evidence class, external obligation, or implementation binding without semantic loss;
3. requires a new decision state or authority semantic that GAAM cannot represent safely; or
4. causes existing GAAM requirements to produce contradictory governance outcomes.

Any such finding should become a separate promotion candidate. It must not be inferred from the mere existence of AI-specific terminology.

## Current research disposition

No material requirement in the supplied AI-governance/ToIP analysis currently demonstrates a new GAAM core primitive. The source does identify useful AI-domain requirements for profile composition and external mappings, especially model/capability evaluation, runtime evidence, training-data and output provenance, post-deployment monitoring, and regulatory crosswalks.

This conclusion is bounded by the supplied research source and the current GAAM v0.9.0 profile surface. It is not a claim that GAAM alone satisfies any particular AI law or standard.
