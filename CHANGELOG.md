---
title: "Changelog"
permalink: /releases/changelog/
parent: "Project Governance"
artifact_type: "Changelog"
normative_status: "Release record"
---
# Changelog

### Documentation

- Add a reusable, machine-readable ecosystem readiness crosswalk method and validated informative mappings for EUDI Wallet ARF v3.0.0 and GLEIF vLEI EGF v4.0.
- Add comparative implementation takeaways covering authority/reliance boundaries, assurance composition, unknown state, dependency-aware revocation, correction versus remedy, and test generation. These artifacts do not change GAAM v0.9.0 normative requirements or conformance semantics.

- Added a validator-controlled Future Evolution programme with expansion principles, concept classification, a normative boundary, a four-commit delivery roadmap, fifteen candidate concept pages, and a 25-entry machine-readable enhancement register. GAAM v0.9.0 normative requirements, schemas, profiles, vocabularies, conformance semantics, and threat-model content remain unchanged.
- Reorganised site navigation with four grouped Documentation routes, a top-level Implementation Reports workflow, and an Appendices section for glossary, vocabularies, matrices, mappings, FAQ, style guidance, and publication documentation. Existing file paths and permalinks remain unchanged.

## Unreleased: assurance-ready composed patterns

- Expanded the delegated agent purchasing, cross-registry recognition and high-impact multi-agent service examples into assurance-ready implementation patterns.
- Added pattern manifests, differentiated architecture and authority documentation, lifecycle, evidence, review, remedy, privacy, security and affected-party analysis.
- Added valid and invalid authority, delegation, decision-receipt, governance-event and remedy fixtures.
- Added a shared pattern catalogue, maturity model, template, validation guide and composed-pattern comparison.
- Preserved normative GAAM requirements, schemas, profiles, vocabularies, threat-model content and conformance semantics.

{% include gaam-meta.html %}

All notable changes will be documented here. The project uses Semantic Versioning adapted for an evolving specification.

## Unreleased

### Governance

- Add `PROJECT-STATUS.yaml` as GAAM's repository-local status and authority declaration for portfolio consumption.
- Freeze a content-addressed candidate review baseline and add machine-verifiable review/finding contracts, controlled review vocabulary, evidence directories and a joint disposition register.
- Strengthen validation so reviewer independence, decision authority, evidence references, blocker state and evidence-backed finding closure are checked without changing the v0.9.0 normative surface.

### Fixed

- Separate repository README files from GitHub Pages landing pages for all implementation patterns.
- Publish each pattern at a clean directory URL through `index.md`.
- Exclude supporting pattern pages from primary sidebar navigation while retaining direct-link and search access.
- Add publication-hygiene validation for front matter, duplicate landing pages and unexpected navigable pattern-support pages.

- Enable Just the Docs' Mermaid support (`mermaid: version: "11.16.0"` in `_config.yml`). Disabled by default when the theme is consumed as a gem, so the ```` ```mermaid ```` fenced diagrams in `diagrams/architecture-diagrams.md` were rendering as plain code blocks instead of diagrams.

- Add empty `_includes/head_custom.html`, `header_custom.html`, `footer_custom.html` and `nav_footer_custom.html` stubs. Just the Docs' own bundled templates include these unconditionally and the gem does not ship default versions of them, so the Jekyll build failed with "could not locate the included file" until the site provided them.

- Remove duplicate body-level H1 headings from page-layout documents and establish front matter as the authoritative title source.
- Refactor the GAAM page header and artifact metadata to prevent overlapping or floating titles across responsive layouts.
- Declare `kramdown-parser-gfm` explicitly so strict Jekyll builds do not depend on transitive gem resolution.
- Bring the homepage (`index.md`) and mappings landing page (`mappings/index.md`) under the shared `layout: page` template; both previously used `layout: default` and rendered without the site stylesheet, status banner, breadcrumbs and artifact metadata.
- Replace the implicit, silent `gaam-page`-marker skip in `scripts/validate_pages.py` with an explicit, empty exemption list, so any future page using `layout: default` fails the structural-contract check instead of being skipped unnoticed.
- Add a local `_layouts/default.html` override so the theme's own site-title banner no longer renders as a second `h1` on every page alongside GAAM's page-specific title; every page now has exactly one `h1`, matching the page-title contract the site already claimed. (Superseded below: the site no longer uses `jekyll-theme-minimal` or this override.)
- Add `scripts/publish_versioned_schemas.py`, run in both CI workflows after the Jekyll build, to mirror `schemas/*.json` into the versioned path (`_site/<version>/schemas/`) declared by every schema's `$id`. Previously no build step published anything at that path, so every canonical schema identifier pointed at a URL that did not exist on the live site.

### Changed

- Migrate the GitHub Pages site from `jekyll-theme-minimal` to [Just the Docs](https://just-the-docs.com). Retires the hand-built `_layouts/page.html`, `_layouts/default.html`, `_includes/status-banner.html`, `_includes/artifact-meta.html` and `assets/css/gaam.css` in favour of the theme's own layout, nested sidebar navigation, breadcrumbs, built-in search and `_sass/custom/custom.scss` extension point. Adds `_includes/gaam-meta.html`, a small include for the artifact-type/normative-status/version disclosure the theme has no equivalent for. All 65+ content pages gain `parent`/`nav_order`/`has_children` front matter driving the new sidebar; five files that previously had no front matter at all (`README.md`, `NOTICE.md`, `CODE_OF_CONDUCT.md`, `docs/open-questions.md`, `implementation-reports/TEMPLATE.md`) now do. `README.md` is excluded from the Jekyll build and remains a GitHub-rendered document only, since `index.md` is the site's actual homepage. `scripts/validate_pages.py` is rewritten to check theme-independent invariants (required pages render, exactly one `h1` per page, a stylesheet loads, a search index is published) rather than the retired theme's specific region markup.

- Upgrade supported first-party GitHub Actions to Node 24-compatible major releases.
- Add source and rendered-publication checks for the one-H1 rule, publication-region ordering and stylesheet availability.

### Documentation

- Add machine-readable candidate issue and review registers, governed GitHub issue and pull-request templates, and a v1.0.0 readiness dashboard without changing the normative specification surface.
- Add requirement-level assurance traceability, testability dispositions, and expanded negative and boundary fixtures for existing GAAM v0.9.0 obligations.
- Add an informative implementation and evidence readiness toolkit covering profile selection, self-assessment, evidence organisation, quality, retention and report preparation. Include a machine-readable evidence catalogue and an explicitly non-conformant illustrative report without changing normative requirements, schemas, profiles or conformance semantics.
- Align the GitHub Pages publication surface with the compact `jekyll-theme-minimal` scheme, explicit landing-page navigation and the supported Pages build action.
- Replace theme-dependent header navigation with content-led entry points for the specification, implementation guidance, profiles, schemas, vocabularies, conformance and releases.
- Replace oblique references to an external governance metamodel with explicit attribution to the ToIP Governance Metamodel Specification v1.0 and Companion Guide v1.0.
- Reframe the TSMM crosswalk as a GAAM source-adoption and architectural-differentiation record.
- Remove residual language implying that GAAM is a successor "v2" of the ToIP specification.
- Add repository-level source attribution and a GitHub Pages landing page for mappings.

## [0.9.0] - 2026-07-16

### Added

- Feature-complete normative requirements for canonical artifacts, lifecycle, assurance, profiles, decisions, safety, remedy, systemic harm and market integrity.
- Eight exhaustive profile manifests, canonical JSON Schemas and controlled vocabularies.
- Three end-to-end implementation patterns with positive and negative fixtures.
- Executable validation, generated evidence, threat model, ADRs and GitHub workflows.
- Full GitHub Pages navigation and `AI_USAGE.md` disclosure.
- Candidate stability and artifact-precedence governance.
- Canonical schema catalogue, behavioural vectors, threat register and traceability matrices.
- Modular validation evidence, CI workflow and reproducible v0.9.0 governance package.

### Changed

- Replaced open markers with v0.9.0 decision dispositions.
- Reframed unexplained predecessor-version language as independent architectural provenance.
- Expanded conformance, implementation and lifecycle guidance.
- Corrected the normative specification identity from v0.1.0 to v0.9.0.
- Updated active profiles, manifests, schemas, vocabularies, examples and claims to v0.9.0.
- Corrected TSMM references to the canonical repository.
- Operationalised L0–L4 conformance evidence and independence boundaries.

### Documentation

- Published canonical schemas and controlled vocabularies through GitHub Pages.
- Added stable permalinks, shared layouts, status metadata and full documentation navigation.
- Added human-readable schema, vocabulary and traceability catalogues.
- Added production-equivalent strict Jekyll build and rendered-site validation.
- Added least-privilege GitHub Pages deployment workflow.

## [0.1.0] - 2026-07-15

### Added

- Initial public draft of the Governance, Authority and Assurance Metamodel.
- Core concepts for authority, delegation, evidence, assurance, trust decisions, effects and accountability.
- Normative governance for agentic systems, runtime evaluation, registries and decentralised trust graphs.
- Composable conformance profiles.
- Requirements, relationship and conformance matrices.
- Implementation, conformance and reviewer guidance.
- Initial examples and architecture diagrams.
- Repository governance, contribution, security and release hygiene.
