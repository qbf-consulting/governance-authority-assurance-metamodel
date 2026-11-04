---
title: "Portable Conformance Kit"
permalink: /conformance/portable-kit/
parent: Implement
artifact_type: "Informative implementation tooling"
normative_status: "Informative"
nav_order: 4
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

Use `--pattern 'delegation-*.json'` before the adapter command to select a subset; a misplaced filter is rejected rather than silently ignored. Results are emitted as machine-readable JSON and identify the tooling release, the current normative Candidate baseline and the retained semantic baseline.

## Boundary

The manifest, adapter protocol and result schema are informative implementation contracts provided with the v0.9.3 maintenance release. They do not add normative requirements, profiles, vocabularies or canonical schemas to the v0.9.3 normative Candidate maintenance baseline; the underlying semantic and canonical identifiers remain the frozen v0.9.0 set.

## Version 2 experimental raw-artifact vectors

Run `python scripts/gaam.py run-vectors --suite v2 python conformance-kit/reference_adapter.py`. V2 supplies a schema-valid authority artifact, explicit evaluation clock, requested effect and expected reason code. The runner validates v2 fixture shape before invoking the adapter and checks both verdict and reason. It deliberately does not pass the expected verdict, reason, or fixture ID to the adapter. Legacy v1 remains the default and uses its original payload contract. This reference adapter is not independent enforcement or conformance evidence. The v2 set initially exercises authority admission; delegation, aggregation, receipt proof and freshness semantics require separate contracts and cannot be considered covered by these fixtures.

## Package path and integrity validation

The portable package validator rejects absolute paths, parent-directory traversal and symlink escapes in artifact and checksum references. Each declared artifact must have exactly one checksum record; a missing digest is a failed integrity check, not a PASS. These checks establish **local package containment and byte consistency**, not source authenticity, trust in the package author, or actual runtime authorization. The canonical v0.9.0 package schema is unchanged.
