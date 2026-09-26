---
title: "Cross-Implementation Validation Protocol"
permalink: /implementation-reports/cross-implementation-protocol/
parent: "Implementation Reports"
nav_order: 7
artifact_type: "Interoperability evidence protocol"
normative_status: "Informative"
---
# Cross-Implementation Validation Protocol

{% include gaam-meta.html %}

This protocol defines the evidence GAAM expects from a cross-implementation exercise intended to support an E3 interoperability claim. It is informative and does not create new GAAM normative requirements.

## Entry condition

At least two credible independent implementations must exist with sufficiently overlapping GAAM profile and requirement boundaries for a meaningful cross-validation exercise.

The exercise must identify:

- implementation A and implementation B;
- source/build revisions;
- GAAM release and retained semantic/profile identifiers;
- claimed profiles and overlapping requirement scope;
- validator/adapter versions;
- participant relationships and independence disclosures.

## Bidirectional exercise

For implementations A and B:

```text
Implementation A artifacts
        ↓
Validator / adapter B
        ↓
Result B(A)

Implementation B artifacts
        ↓
Validator / adapter A
        ↓
Result A(B)
```

Each direction should preserve raw results, configuration, exchanged artifacts and integrity references.

Where the portable adapter contract does not permit direct evaluation of a native implementation artifact, the participants must document the bounded translation or test adapter used and the semantic assumptions introduced by that translation.

## Required probes

The exercise should include, within the overlapping claim boundary:

1. at least one valid decision/receipt path;
2. lifecycle transition semantics;
3. at least one negative or mismatch case;
4. unsupported/unknown extension handling where applicable;
5. at least one deliberate semantic disagreement or incompatibility probe;
6. evidence freshness or revocation/state-change behavior where relevant to the claimed profiles.

A successful happy-path exchange alone is insufficient interoperability evidence.

## Semantic-difference register

Differences must be retained rather than normalised away.

Each observed difference should be classified as one of:

- implementation defect;
- unsupported scope;
- permitted implementation variation;
- adapter/translation defect;
- specification ambiguity;
- indeterminate result;
- candidate semantic divergence.

For each difference record:

- affected artifact/test;
- requirement/profile scope;
- A result;
- B result;
- evidence references;
- classification;
- responsible authority for disposition;
- whether the finding triggers GAAM reassessment.

A material ambiguity or semantic divergence that could invalidate GAAM's normative assumptions enters the governed finding/change lifecycle.

## Evidence bundle

Preserve:

- implementation identities and source revisions;
- participant relationship and independence disclosure;
- GAAM/profile claim boundaries;
- validator, adapter and tool versions;
- artifacts exchanged;
- artifact and evidence digests;
- A→B machine-readable results;
- B→A machine-readable results;
- negative/mismatch-case results;
- lifecycle/receipt evidence;
- semantic-difference register;
- unresolved exceptions;
- reviewer/maintainer dispositions where applicable.

## Result semantics

Do not collapse states:

```text
pass          → proposition supported within the tested boundary
fail          → proposition contradicted
indeterminate → insufficient basis for pass/fail
unsupported   → outside implementation/tool claim boundary
```

A failure, indeterminate state or unresolved exception must remain visible.

## Non-substitution rule

Running GAAM's reference adapter against repository-owned vectors demonstrates portability of the test surface. It does **not** constitute cross-implementation interoperability.

Likewise, two implementations independently passing the same repository vector set is not equivalent to A validating B and B validating A.

Missing E3 evidence leaves the interoperability claim unproven. It does not, by itself, make the specification unstable.

## Closure path

Evidence produced under this protocol can support closure of GAAM-CR-002 only after:

- independence/relationship disclosures are accepted;
- both validation directions are preserved;
- differences and exceptions are dispositioned;
- no unresolved evidence state is misrepresented as success; and
- candidate readiness is regenerated from the accepted evidence.
