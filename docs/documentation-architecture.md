---
layout: default
title: Documentation Architecture
permalink: /docs/documentation-architecture/
parent: Orientation
nav_order: 2
has_toc: true
grand_parent: Start Here
---
# Documentation Architecture

GAAM documentation is arranged by authority level and implementation function. This prevents informative explanation, normative requirements and conformance evidence from being treated as interchangeable.

| Layer | Authority | Purpose | Start page |
|---|---|---|---|
| Orientation | Informative | Select audience route and outcome | [Documentation → Orientation](orientation.md) |
| Concepts and rationale | Informative | Explain model semantics and design choices | [Documentation → Concepts and Design](concepts-and-design.md) |
| Normative model | Normative | Define required concepts, relationships and constraints | [Specification](../specification/index.md) |
| Profiles | Normative when claimed | Select a bounded conformance target | [Profiles](../profiles/index.md) |
| Machine-verifiable artifacts | Normative support | Encode schemas and controlled values | [Schemas](../schemas/index.md), [Appendices → Controlled Vocabularies](../vocabularies/index.md) |
| Implementation patterns | Informative | Demonstrate application without creating requirements | [Examples](../examples/index.md) |
| Assurance and risk | Normative/informative as marked | Trace requirements, controls, tests and evidence | [Conformance](../conformance/index.md), [Appendices → Matrices](../matrices/index.md) |
| Decision history | Governance evidence | Explain why architectural choices were made | [ADRs](../decisions/index.md) |
| Future evolution | Informative research | Test candidate concepts before normative promotion | [Documentation → Future Evolution](future-evolution/index.md) |

Reference and lookup material, including the glossary, controlled vocabularies, matrices, source crosswalks, frequently asked questions, and editorial guidance, is collected under [Appendices](../appendices/index.md). This navigation grouping does not change the authority of the underlying artifacts.

The route manifest at `_data/learning_paths.json` is validated by `scripts/validate_learning_paths.py`. A path cannot pass validation when a target disappears or a step lacks a declared outcome.

[Choose a learning path →](guided-learning.md)
