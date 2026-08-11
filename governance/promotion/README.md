---
title: "Evidence-Gated Promotion Governance"
nav_exclude: true
artifact_type: "Repository governance"
normative_status: "Repository governance"
---
# Evidence-Gated Promotion Governance

{% include gaam-meta.html %}

This directory governs how GAAM research, experimental artefacts, draft profiles and future-enhancement findings may be considered for later normative adoption. It does **not** promote any current research artefact and it does not change GAAM v0.9.0 conformance.

## Authority boundary

The future-enhancement register records research dispositions. A value such as `promote-to-profile` means that an item is sufficiently bounded to enter future profile review; it is **not** approval of a normative profile. Normative adoption requires a separate promotion candidate, complete gate evidence, an attributable promotion decision, and a release-managed change when the target is normative.

## Lifecycle

```text
research
  -> prototype
  -> implementation-tested
  -> promotion-candidate
  -> public-review
  -> accepted | deferred | rejected
  -> normative-change-package
```

Only records stored in `candidates/` and `decisions/` are operational promotion records. Files under `examples/` are synthetic and can never satisfy a promotion gate.

## Artifacts

- `promotion-gates.json` defines the 14 evidence gates and proportional thresholds.
- `promotion-candidate.schema.json` defines the evidence envelope for a promotion candidate.
- `promotion-decision.schema.json` defines separately attributable accepted, deferred or rejected decisions.
- `TEMPLATE.md` is the human-readable preparation template.
- `candidates/` stores real promotion candidates when they exist.
- `decisions/` stores decisions that reference those candidates.

## Closure rule

A normative target cannot be accepted unless every promotion gate is satisfied, a matching accepted decision exists, the release impact is `release-required`, and a target version is identified. Research evidence may therefore justify more research, guidance, patterns or review without acquiring normative authority.
