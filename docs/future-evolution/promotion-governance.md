---
title: Evidence-Gated Promotion
permalink: /docs/future-evolution/promotion-governance/
parent: Future Evolution
grand_parent: Documentation
nav_order: 5
artifact_type: Evolution governance
normative_status: Informative
---
# Evidence-Gated Promotion

{% include gaam-meta.html %}

GAAM separates **research maturity** from **normative authority**. The future-enhancement register can conclude that an item should enter profile review or remain experimental, but that disposition does not itself alter conformance.

## Promotion path

```text
research
   ↓
prototype
   ↓
implementation-tested
   ↓
promotion-candidate
   ↓
public-review
   ↓
accepted / deferred / rejected
   ↓
normative-change-package
```

The operational contracts live under [`governance/promotion/`](../../governance/promotion/README.md).

## Fourteen evidence gates

A normative promotion must establish: a reproduced problem; demonstrated insufficiency in current GAAM; consideration of documentation and pattern remedies; implementation evidence; interoperability impact; authority/delegation and revocation/supersession effects; privacy, security and affected-party impact; threat-model impact; compatibility and migration; conformance testability; affected normative surface; and the approving authority.

The machine-readable source is [`promotion-gates.json`](../../governance/promotion/promotion-gates.json).

## Proportional evidence

Guidance and informative patterns can advance with lighter evidence because they do not change conformance. Normative vocabularies, schemas, profiles and core semantics require progressively stronger implementation, interoperability, review, migration and conformance evidence.

## No implicit promotion

The existing future-evolution assessment contains several `promote-to-profile` dispositions. Those mean **admit to future profile review**, not “create a normative profile.” No current future-evolution asset is promoted by this governance mechanism.
