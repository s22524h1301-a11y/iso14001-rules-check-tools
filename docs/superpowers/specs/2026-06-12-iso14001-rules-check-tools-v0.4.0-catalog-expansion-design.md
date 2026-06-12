# ISO 14001 Rules Check Tools v0.4.0 Design Spec

**Goal:** Expand the ISO 14001:2015 clause catalog across the core management system chapters so the matcher can recognize more realistic wording for `4.x`, `5.x`, `6.x`, `9.x`, and `10.x` sections without changing the PDF/OCR pipeline or the existing report formats.

**Architecture:** Keep the current pipeline intact: PDF intake, selectable-text extraction with OCR fallback, section splitting, clause matching, and reporting. `v0.4.0` is a catalog-growth release, so the main work happens in the clause catalog and the tests that prove the new coverage behaves as expected. The matcher should remain deterministic and explainable, and the reporting layer should continue to use the same text, JSON, and CSV contracts.

**Tech Stack:** Python 3.12, `pypdf`, OCR adapter layer, standard library `csv` and `json`, and `pytest`.

---

## 1. Product Summary

`ISO 14001 Rules Check Tools` remains a standalone CLI for ISO 14001:2015 document analysis. `v0.4.0` should make the tool feel more complete when it reads real-world management-system documents by recognizing a broader set of normal clause phrasings.

The release should improve coverage in the clauses users are most likely to see in policy, planning, monitoring, audit, and improvement documents:
- `4.x` context and scope language
- `5.x` leadership, policy, and responsibilities
- `6.x` planning, risks, objectives, and obligations
- `9.x` monitoring, evaluation, audit, and review
- `10.x` nonconformity and continual improvement

This is not a rewrite of the matcher. It is a catalog expansion with regression tests that keep the current explainable scoring model honest.

## 2. Versioning Intent

`v0.4.0` is a minor release after the false-positive tuning release.

- `v0.3.x`: false-positive reduction and reporting clarity
- `v0.4.0`: broader clause catalog coverage for real-world ISO 14001 documents

This release should stay backward-compatible for the current pipeline:
- selectable-text extraction remains primary
- OCR fallback remains unchanged
- text, JSON, and CSV output remain available

## 3. Functional Scope

### In scope for `v0.4.0`
- Expand clause coverage for `4.x`, `5.x`, `6.x`, `9.x`, and `10.x`
- Add or refine high-signal keywords and descriptions for those clauses
- Keep clause IDs stable and human-readable
- Add regression tests for the newly strengthened clauses
- Preserve the current CLI behavior and report formats

### Out of scope for `v0.4.0`
- New input formats such as Word, Excel, or HTML
- OCR changes
- PDF parsing changes
- Major matcher architecture changes
- Semantic search or AI-based matching
- Report schema redesign
- Compliance judgment or certification logic

## 4. Catalog Expansion Strategy

`v0.4.0` should improve coverage without making the catalog noisy.

The catalog update should focus on the kinds of text that appear in normal ISO 14001 documents:

### `4.x` focus
- organization context and external/internal issues
- interested parties and their requirements
- documented scope and EMS boundaries
- EMS process interaction language

### `5.x` focus
- leadership commitment and top management language
- environmental policy statements
- responsibilities and authorities language

### `6.x` focus
- risks and opportunities
- environmental aspects and impacts
- compliance obligations
- environmental objectives and planning actions

### `9.x` focus
- monitoring and measurement
- evaluation of compliance
- internal audit
- management review

### `10.x` focus
- nonconformity
- corrective action
- continual improvement

The catalog should remain transparent:
- keyword lists stay explicit
- descriptions should explain what kind of document wording each clause is looking for
- additions should prefer high-signal terms over generic ones that create false positives

## 5. Matching Strategy

The matcher should continue to rank clause suggestions deterministically.

No structural matcher rewrite is planned. The desired outcome is:
- more realistic wording should now match the right clause more often
- the existing false-positive improvements from `v0.3.0` should remain intact
- higher coverage should not reintroduce broad noisy matches

If a small ranking adjustment is needed to support the broader catalog, it should remain explainable and test-driven. The matcher should still surface why a clause was suggested through the existing `reason` text.

## 6. Reporting Strategy

No reporting format changes are planned for `v0.4.0`.

The current behavior should remain:
- plain text remains the default
- `--json` continues to work
- `--csv` continues to work

The reporting layer may benefit indirectly from the richer catalog because more sections will produce more meaningful matches, but the report schema itself should not change in this release.

## 7. CLI Contract

The CLI should keep the current output modes and help text behavior.

No new flags are required for `v0.4.0`.

The visible improvement should be broader clause coverage on real documents, not a new command surface.

## 8. README and Changelog

The README should be updated to describe:
- the current version as `v0.4.0`
- broader clause catalog coverage
- the continued support for selectable-text PDFs and scanned PDFs
- the continued availability of text, JSON, and CSV output

The changelog should note:
- broader clause catalog coverage across the core ISO 14001 chapters
- any narrow matcher or keyword refinements needed to support that coverage
- no change to the PDF/OCR pipeline or output contracts

## 9. Testing Strategy

Tests should prove that the expanded catalog improves coverage without breaking the current false-positive controls.

Required coverage:
- a `4.x` clause that should now match a realistic context or scope section
- a `5.x` clause that should now match leadership or policy language
- a `6.x` clause that should now match a planning, obligation, or objective section
- a `9.x` clause that should now match monitoring, audit, or review language
- a `10.x` clause that should now match corrective action or continual improvement language
- regression coverage showing the existing high-false-positive behavior stays controlled
- text, JSON, and CSV reporting still render after the catalog changes

Testing guidance:
- use small, readable section examples that reflect real clause language
- prefer positive controls that are obvious to a human reviewer
- keep at least one regression test focused on the noise that `v0.3.0` removed

## 10. Risks and Constraints

- Expanding the catalog too aggressively could bring back broad false positives
- A larger keyword set can become hard to maintain if it is not kept explicit and narrow
- The release should improve coverage, not become a rewrite of the scoring model

## 11. Acceptance Criteria

`v0.4.0` is acceptable when:
- the catalog covers more of the core ISO 14001 clause families
- the new coverage matches realistic document wording
- the previously tuned false-positive cases remain controlled
- text, JSON, and CSV outputs still work as before
- the test suite passes
- the release stays within the intended catalog-expansion boundary
