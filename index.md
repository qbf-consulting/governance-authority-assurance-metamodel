---
title: "Governance, Authority and Assurance Metamodel"
permalink: /
nav_exclude: true
artifact_type: "Publication landing page"
normative_status: "Candidate Specification"
---
# Governance, Authority and Assurance Metamodel

{% include gaam-meta.html %}

GAAM defines protocol-neutral governance semantics for **authority, delegation, evidence, assurance, trust decisions, effects, accountability and remedy** across distributed and agentic systems. Its specification identifies the obligations that governed implementations must satisfy; a JSON Schema check alone cannot demonstrate that an authority decision was correct. The bundled portable tests provide reference evidence, not independent implementation assurance.

The six routes below are the recommended reader journeys. Legacy and supplementary entries may also appear in the site navigation; their presence does not change normative authority.

| Route | Use it when you need to… |
|---|---|
| [Start Here](docs/start-here.md) | orient yourself, choose a role-based path, or get a first result |
| [Understand GAAM](docs/understand-gaam.md) | learn the model, architecture, terminology and design rationale |
| [Specification & Profiles](docs/specification-and-profiles.md) | read normative semantics and select conformance artifacts |
| [Implement](docs/implement.md) | build governed artifacts, run the quickstart, and use implementation patterns |
| [Test & Assure](docs/test-and-assure.md) | inspect requirements, tests, threats, evidence and validation |
| [Project & Evolution](docs/project-and-evolution.md) | review governance, releases, decisions, mappings and future work |

## Current publication state

| Attribute | Value |
|---|---|
| Current release | v0.9.4 |
| Status | Normative Candidate Specification |
| Semantic/canonical baseline | v0.9.0 identifiers retained |
| Repository validation | Automated structural, behavioural, conformance and publication checks |
| Assurance boundary | Repository validation is not certification or independent assessment |

### Minimal artifact set

The checked-in [authority artifact](conformance-kit/starter/artifacts/authority.json), [decision receipt](conformance-kit/starter/artifacts/decision-receipt.json) and [conformance claim](conformance-kit/starter/artifacts/conformance-claim.json) form a source-bound starter package. They illustrate how authority, effect decisions and evidence claims fit together; none demonstrates a deployed authorization service or independently verified provenance. See the [five-minute quickstart](docs/implementer-quickstart.md) for the reproducible first test and the [conformance kit](conformance-kit/README.md) for the external adapter interface.

### Fastest practical path

If you are implementing GAAM, run the [Five-Minute Implementer Quickstart](docs/implementer-quickstart.md), then continue to [Implementation Guidance](docs/implementation-guidance.md).

If you are assessing GAAM, begin with [Test & Assure](docs/test-and-assure.md) and the [Requirement Evidence Coverage](docs/requirement-evidence-coverage.md) guide.

The authoritative normative semantics remain in the [Specification](specification/). Reader-oriented navigation does not alter normative authority, canonical identifiers, or existing public permalinks.
