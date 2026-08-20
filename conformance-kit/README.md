---
title: "Portable Conformance Kit"
permalink: /conformance/portable-kit/
parent: "Conformance and Assurance"
artifact_type: "Informative implementation tooling"
normative_status: "Informative"
---
# Portable Conformance Kit

{% include gaam-meta.html %}

The portable kit helps implementations run GAAM's reference behavioural vectors without adopting repository-internal build logic. It is informative tooling: a passing result contributes test evidence but does not by itself establish conformance, production fitness or assessment independence.

## Adapter protocol

For each vector, the runner starts the configured adapter, writes the vector's `input` object as JSON to standard input, and expects a JSON object with one Boolean member:

```json
{"valid": true}
```

The process must exit successfully. Diagnostic fields are permitted but ignored by the portable runner. An adapter is responsible for mapping GAAM's abstract vector vocabulary to the implementation under test.

## Run the reference adapter

```bash
python scripts/gaam.py run-vectors python conformance-kit/reference_adapter.py
```

Use `--pattern 'delegation-*.json'` to select a subset. Results are emitted as machine-readable JSON and identify both the tooling release and frozen normative baseline.

## Boundary

The manifest, adapter protocol and result schema are informative v0.9.1 implementation contracts. They do not add normative requirements, profiles, vocabularies or canonical schemas to GAAM v0.9.0.
