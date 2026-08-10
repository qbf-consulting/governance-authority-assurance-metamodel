---
title: "EUDI and vLEI Comparative GAAM Takeaways"
permalink: /mappings/eudi-vlei-comparative-takeaways/
parent: "Mappings and Source Crosswalks"
grand_parent: "Appendices"
nav_order: 6
artifact_type: "Informative comparative assessment"
normative_status: "Informative"
---
# EUDI and vLEI Comparative GAAM Takeaways

{% include gaam-meta.html %}

The EUDI Wallet ARF and vLEI EGF assessments exercise GAAM against two different governance architectures:

- **EUDI ARF:** a large, federated regulatory and technical architecture where authority often emerges from several coordinated legal, registration, certification and protocol sources;
- **vLEI EGF:** an ecosystem with comparatively explicit credential authority, delegation lineage, role semantics and assurance mechanisms.

Together they expose reusable implementation priorities for GAAM.

## 1. Standardise ecosystem readiness crosswalks

GAAM should use one machine-readable structure for external-framework application exercises. The structure introduced in this commit records target version, claim boundary, mapped requirements, bounded status, actionable takeaway, evidence expectations and candidate tests.

**Governance outcome:** external examples cannot silently become normative dependencies or conformance claims.

## 2. Make positive and negative semantics first-class

Both assessments show that trust artifacts need to say not only what they establish but what they **do not establish**.

Examples include:

- registry inclusion does not establish universal trustworthiness;
- qualification does not guarantee every output;
- organizational role does not establish unlimited transaction authority; and
- credential validity does not establish authority outside the governed scope.

**Candidate future work:** evaluate whether negative reliance semantics need a controlled representation in GAAM implementation guidance or a future profile artifact.

## 3. Treat authority resolution as a graph, not a flag

The EUDI case highlights distributed authority sources. The vLEI case highlights explicit delegation lineage. A reusable authority model should therefore resolve:

```text
authority source
  ↓
role / qualification / delegation
  ↓
active scope and constraints
  ↓
runtime decision
  ↓
consequential effect
```

The graph must also expose conflicts, expiry, revocation and dependency propagation.

## 4. Model assurance composition explicitly

Both ecosystems combine different assurance mechanisms. GAAM should continue to require bounded claims and should make composition evidence especially visible:

```text
assurance mechanism
  → criteria
  → evaluator
  → scope
  → limitations
  → validity
  → dependencies
  → blind spots
```

A composed assurance claim should fail or degrade when a required dependency expires or becomes unknown.

## 5. Preserve unknown and unobserved state

The vLEI review shows why a governance authority may impose requirements without being able to observe every governed actor. The EUDI review shows similar distributed-assurance challenges.

GAAM implementations should never map missing evidence to implicit success. `unknown`, blind-spot and evidence-freshness state should remain visible.

## 6. Make revocation propagation dependency-aware

Neither ecosystem benefits from a simplistic "parent revoked, everything revoked" rule. Propagation depends on relationship semantics.

A reusable test suite should cover:

- revocation of an authority source;
- qualification suspension;
- credential revocation;
- registry withdrawal;
- role termination;
- unaffected sibling branches; and
- stale downstream state.

## 7. Separate correction from remedy

Both assessments reinforce a critical lifecycle distinction:

```text
incorrect assertion
  ↓
challenge
  ↓
correction / revocation
  ↓
future reliance fixed
```

is not equivalent to:

```text
past consequential effect
  ↓
review
  ↓
correction of effect
  ↓
remedy
```

GAAM implementation reports should record both when the target governs consequential effects.

## 8. Keep relying-party accountability explicit

A valid trust artifact does not absolve the final decision-maker. The relying system remains responsible for evaluating whether the artifact supports the requested effect under its governing policy.

This is particularly important for cross-ecosystem interoperability, automated agents and high-impact transactions.

## 9. Convert mappings into test generators, not scorecards

The actionable endpoint of a GAAM crosswalk is not a maturity score. It is a set of evidence expectations and candidate tests.

For example:

```yaml
finding: authority-scope
expected_evidence:
  - authority-source
  - permitted-effect
  - validity-state
negative_test:
  - valid-credential-with-out-of-scope-effect-must-fail
```

This supports implementation reports and independent assessment without overstating what a document review proves.

## 10. Use both ecosystems as complementary GAAM benchmarks

The two assessments should remain paired:

- **EUDI** tests GAAM against federated regulatory authority, registry semantics and multi-party governance;
- **vLEI** tests GAAM against explicit delegation, role authority, cryptographic provenance and differentiated assurance.

A GAAM requirement or implementation pattern that works coherently across both is more likely to be protocol-neutral and reusable.

## Validation path

The next maturity step should be evidence-backed implementation work, not more narrative scoring:

1. keep these crosswalks informative;
2. derive executable test vectors from selected findings;
3. run them against concrete implementations or reference services;
4. record results through the GAAM Implementation Report workflow; and
5. only then consider L0-L4 claims within the existing conformance model.
