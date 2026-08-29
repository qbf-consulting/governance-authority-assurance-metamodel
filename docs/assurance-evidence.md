---
layout: default
title: Assurance Evidence
---

# Assurance evidence contract

The governance metamodel uses repository-native controls as executable assurance evidence.

| Claim | Required control | Freshness expectation |
|---|---|---|
| Model validation | `.github/workflows/validate.yml` | Successful execution covering the governed `main` revision |
| Publication integrity | repository Pages publication control | Successful evidence inside the configured freshness window |

A publication success does not substitute for model validation.

Portfolio finding lineage: `PF-61F501F7DBEF` (issue #7).

## Retest rule

After `validate.yml` succeeds for the governed `main` revision, rerun the Portfolio Assurance Monitor and close only when the lifecycle registry records `PF-61F501F7DBEF` as resolved.
