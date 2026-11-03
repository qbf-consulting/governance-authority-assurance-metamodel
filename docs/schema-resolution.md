---
title: "Schema Identifier Resolution Boundary"
artifact_type: "Informative publication and compatibility guide"
normative_status: "Informative"
nav_exclude: true
---
# Schema Identifier Resolution Boundary

The retained v0.9.0 schema `$id` identifiers use the historical personal GitHub Pages namespace. These strings are frozen under GAAM candidate change control. An adversarial review on 2026-11-03 reported that the historical host returned 404 while the sanctioned QBF mirrors responded successfully. Repository-local validation cannot prove current external availability or future maintenance.

The machine-readable [resolver map](schema-resolver-map.json) records an **informative** prefix mapping from historical IDs to the release-controlled QBF Pages mirror. This map does not redefine the frozen `$id`, assert a normative alias, or imply that consumers must fetch remote schemas. Consumers should use version-pinned, locally verified schema bytes or an explicitly configured resolver and should verify remote content where dereferencing is required.

Run `python scripts/audit_schema_resolution.py` to check that the catalog, schema bytes and release metadata agree locally. The deployed-site canonical-publication verifier remains responsible for network-based mirror verification. Neither test proves control of the historical personal namespace. A permanent redirect or byte-identical hosted publication would require a separately authorized action under that namespace. Future candidate IDs should use an organization-controlled, stable URL without modifying legacy identifiers.

This is a documented **residual publication risk**, not a completed fix for the historical host's reachability.
