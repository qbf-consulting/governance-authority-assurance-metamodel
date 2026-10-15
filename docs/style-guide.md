---
title: "Editorial and Normative Style Guide"
permalink: /docs/style-guide/
parent: Project & Evolution
nav_order: 6
---
# Editorial and Normative Style Guide

GAAM uses **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** only for normative statements. Every normative requirement has a stable `GAAM-<DOMAIN>-NNN` identifier. Defined terms use sentence case in prose and canonical lower-case values in machine-readable vocabularies. Informative examples must not introduce undeclared requirements. Human-readable normative text governs substantive meaning; designated schemas govern artifact structure.

## Page headings

Every published Markdown document derives its sole level-one heading from the front-matter `title`, rendered automatically by the site theme. The body MUST NOT repeat the title with Markdown `#` syntax and SHOULD begin with introductory prose or a level-two heading. This contract preserves accessible document structure and prevents duplicate or overlapping titles in the rendered publication.

## Navigation front matter

Pages that belong to a section (profiles, schemas, docs, matrices, examples, releases, mappings, decisions, conformance, project governance) declare `parent: "<Section Title>"`, matching the exact `title` of that section's index page. A section's own index page declares `has_children: true` and a `nav_order`. Pages excluded from navigation (redundant landing pages, generated reports, templates) declare `nav_exclude: true`.
