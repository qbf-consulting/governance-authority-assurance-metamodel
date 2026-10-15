---
title: "GitHub Pages Publication Model"
permalink: /docs/github-pages-publication/
parent: Project & Evolution
artifact_type: Publication architecture
normative_status: Informative
nav_order: 7
---
# GitHub Pages Publication Model

{% include gaam-meta.html %}

The GitHub Pages site is a versioned publication surface for both human-readable and machine-readable GAAM artifacts.

## Presentation model

The site uses [Just the Docs](https://just-the-docs.com), a documentation-focused Jekyll theme with built-in search, nested sidebar navigation and breadcrumbs. GAAM adds one small extension point on top of the theme -- `_includes/gaam-meta.html`, which renders `artifact_type`, `normative_status`, `version` and a source link from a page's front matter -- included explicitly from the body of pages that declare that front matter. Everything else (page structure, the single `h1` derived from `title`, navigation, search, breadcrumbs) is owned by the theme; GAAM does not override any of the theme's own layouts or includes. Custom styling lives entirely in `_sass/custom/custom.scss`, the theme's documented extension point for adding rules without ejecting or forking it.

Just the Docs' own bundled templates unconditionally reference several `_includes/*_custom.html` files (`head_custom.html`, `header_custom.html`, `footer_custom.html`, `nav_footer_custom.html`) as customization hooks, and the theme gem does not ship default/empty versions of them -- the build fails with a Liquid "could not locate the included file" error until the site provides them. GAAM's repo provides all four as empty (comment-only) stubs, since none currently need custom content.

The repository root is the Pages source. GitHub Actions builds the complete site into `_site` with GitHub's supported Jekyll build action, mirrors `schemas/*.json` into the versioned path declared by each schema's `$id` (`scripts/publish_versioned_schemas.py`; see Canonical identifier publication below), and deploys the resulting Pages artifact.

## Navigation

Section index pages (`profiles/index.md`, `schemas/index.md`, `docs/index.md`, `matrices/index.md`, and so on) declare `has_children: true` and a `nav_order`, and appear as top-level sidebar entries. Pages within a section declare `parent: "<Section Title>"`, matching that section's index-page title exactly, which nests them under it in the sidebar and in the theme's automatic breadcrumbs. Repository `README.md` files are excluded from the Jekyll build and remain GitHub-rendered source documents. Published landing pages use `index.md`, including each implementation pattern, so GitHub Pages exposes one canonical directory URL per landing page. A small number of pages (`VALIDATION_REPORT.md`, `implementation-reports/TEMPLATE.md`) declare `nav_exclude: true` -- reachable by direct link, but not cluttering primary navigation.

## Page-title contract

Every page derives its sole level-one heading from the front-matter `title`, rendered once by the theme's own layout. Markdown bodies begin below that title and MUST NOT declare another level-one heading. Rendered-site validation (`scripts/validate_pages.py`) checks every built page for exactly one `h1`.

## Canonical identifier publication

Every file in `schemas/*.schema.json` declares a canonical `$id` under `release.json`'s `schemaBase`, which includes a version segment (for example `v0.9.0/schemas/authority.schema.json`). Jekyll publishes `schemas/` verbatim to `_site/schemas/` for human browsing and relative links from `schemas/index.md`, but that path has no version segment. `scripts/publish_versioned_schemas.py` runs after the Jekyll build and copies each schema into `_site/<version>/schemas/`, so the `$id` a schema declares is also the URL at which it is actually published. The script fails the build if any schema's `$id` does not start with `schemaBase`, keeping the two in lockstep.

## Publication guarantees

- The normative specification and supporting guidance render as HTML with stable permalinks.
- Every schema and controlled vocabulary remains available as its original JSON media type.
- Canonical schema identifiers are tested against the generated `_site`.
- Traceability CSV files remain downloadable and receive human-readable table views.
- CI parses every Mermaid block with the pinned Mermaid 11.16.0 runtime before publication.
- CI performs a production-equivalent strict Jekyll build before publication.
- Built-in search indexes every page except those marked `search_exclude`.
- The GFM parser is an explicit dependency, preventing dependency-resolution drift.
- GitHub-hosted workflows use Node 24-compatible first-party action releases without insecure runtime overrides.
- Deployment uses GitHub's official Pages build, artifact and deployment actions with least-privilege permissions.
- Scripts, tests, generated packages, validation internals and local build files are excluded from the public site.

## Information architecture

The landing page provides direct routes to:

1. the Candidate Specification;
2. architecture and implementation guidance;
3. implementation and conformance profiles;
4. machine-readable schemas and vocabularies;
5. conformance, evidence and threat traceability;
6. examples, releases and migration guidance.

Section index pages remain the authoritative navigation surfaces for their respective artifact families; the theme's sidebar and search are the two supported ways to reach any page from any other page.

## Authority boundary

Rendering does not alter normative meaning. Where presentation and source differ, the repository source and the artifact-precedence rules govern.

## Publication integrity gates

The Pages build is accepted only when:

- every rendered Markdown page contains exactly one H1 matching its front-matter title;
- required landing pages, stylesheets and the Just the Docs search index are present;
- repository JSON artifacts are copied without semantic transformation;
- every canonical schema `$id` resolves under the versioned `/v0.9.0/schemas/` path; and
- internal documentation links resolve from repository source; and
- every Mermaid block parses successfully using the version pinned in `_config.yml`.

Both workflows run `npm run validate:mermaid` before Jekyll. `scripts/validate_mermaid.mjs` recursively extracts fenced Mermaid blocks, parses them with Mermaid 11.16.0, fails on any syntax error and writes machine-readable evidence to `validation/mermaid-validation.json`. The validation workflow then builds the site, publishes the versioned schema mirror and runs `scripts/validate_pages.py`. The deployment workflow performs the same Mermaid gate, build and mirror sequence before uploading the Pages artifact.

## Implementation-pattern publication boundary

Each pattern uses `index.md` as its canonical published landing page. The corresponding `README.md` remains available in the repository but is excluded from Jekyll. Supporting pattern pages declare `nav_exclude: true`: they remain directly addressable and searchable without creating repetitive top-level sidebar entries.
