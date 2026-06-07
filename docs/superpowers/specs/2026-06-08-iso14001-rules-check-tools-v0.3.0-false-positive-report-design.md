# ISO 14001 Rules Check Tools v0.3.0 Design Spec

**Goal:** Reduce high-value false positives in clause matching, especially around `6.1.3` and `8.1`, while making the plain-text and CSV reports easier to scan without changing the overall PDF/OCR pipeline or the existing output formats.

**Architecture:** Keep the current linear flow intact: PDF intake, selectable-text extraction with OCR fallback, section splitting, clause matching, and reporting. `v0.3.0` only adjusts the matcher/catalog boundary and the presentation of match reasoning. The release should remain explainable and deterministic, with small additive reporting improvements rather than a schema rewrite.

**Tech Stack:** Python 3.12, `pypdf`, OCR adapter layer, standard library `csv` and `json`, and `pytest`.

---

## 1. Product Summary

`ISO 14001 Rules Check Tools` remains a standalone CLI for ISO 14001:2015 document analysis. `v0.3.0` is a focused quality release: it should make the tool less eager to mislabel sections as `6.1.3` or `8.1` when the text is only broadly related to compliance or operational control.

The release should also make the output easier to review:
- the text report should surface why a section matched a clause a little more clearly
- the CSV report should stay spreadsheet-friendly and reflect the improved reasoning
- the JSON output should remain stable and continue to expose structured match data

## 2. Versioning Intent

`v0.3.0` is a minor release after the CSV reporting update.

- `v0.2.x`: reporting growth, catalog expansion, and CSV output
- `v0.3.0`: matching refinement plus small reporting clarity improvements

This release should stay backward-compatible for the current pipeline:
- selectable-text extraction remains primary
- OCR fallback remains unchanged
- text, JSON, and CSV output remain available

## 3. Functional Scope

### In scope for `v0.3.0`
- Tighten matching for a small number of high-false-positive clauses
- Focus first on `6.1.3` and `8.1`
- Adjust keyword lists or ranking weights only where they reduce obvious noise
- Improve the readability of the text and CSV report explanations
- Add regression tests that capture the false-positive cases being fixed
- Keep the current CLI contract intact

### Out of scope for `v0.3.0`
- New input formats such as Word, Excel, or HTML
- OCR changes
- PDF parsing changes
- Full semantic search or AI-based matching
- Major output schema redesign
- Compliance judgment or pass/fail certification logic

## 4. Matching Strategy

The matcher should remain deterministic and explainable.

Planned refinement areas:
- review keyword overlap that is too broad for `6.1.3`
- review operational-control phrasing that is too generic for `8.1`
- reduce false positives caused by common management language that appears in many sections
- preserve the current title-hit and keyword-hit model, but adjust the scoring or keyword sets where needed

Design constraints:
- keyword additions must be narrow and explicit
- ranking changes must be justified by tests
- any reduction in false positives should not break obviously correct matches

## 5. Reporting Strategy

The reporting layer should become easier to scan without changing the core output contracts.

Recommended improvements:
- text output should add a short top-match summary line for each section when matches exist
- CSV output should continue to expose section-level detail and matched keyword evidence, with a more compact and readable `reason` string
- JSON output should remain structured and stable

This release should prefer additive clarity over format churn:
- no removal of existing fields
- no rename of current report modes
- no new mandatory columns

## 6. Clause Catalog Strategy

`v0.3.0` should refine the existing clause catalog rather than replace it.

Catalog work should focus on:
- narrowing keywords that are too generic
- adding only high-signal keywords that help distinguish true matches from false positives
- keeping clause IDs and titles stable
- preserving transparency so the output still explains why a clause was suggested

Primary attention:
- `6.1.3` compliance obligations
- `8.1` operational planning and control

Secondary attention:
- any nearby clauses that become over-eager after the tuning above

## 7. CLI Contract

The CLI should keep the current output modes:
- default plain text
- `--json`
- `--csv`

No new flags are required for `v0.3.0`.

The only user-visible change should be clearer, less noisy matches and easier-to-read reasoning in the existing reports.

## 8. README and Changelog

The README should be updated to describe:
- the current version as `v0.3.0`
- the improved match precision for the most noisy clauses
- the continued support for selectable-text PDFs and scanned PDFs
- the continued availability of text, JSON, and CSV output

The changelog should note:
- high-false-positive tuning for the clause matcher
- small reporting clarity improvements
- no change to the PDF/OCR pipeline

## 9. Testing Strategy

Tests should prove that the tuning reduced noise without breaking useful matches.

Required coverage:
- a false-positive regression for `6.1.3`
- a false-positive regression for `8.1`
- a positive case that should still match each tuned clause
- text and CSV reporting still render after the matcher changes
- the full CLI/test suite remains green

Testing guidance:
- write regression tests around small, readable section examples
- prefer deterministic wording that isolates the false-positive trigger
- keep the test surface focused on the clauses being tuned, not on broad catalog reshaping

## 10. Risks and Constraints

- Over-tuning could make the tool miss legitimate `6.1.3` or `8.1` sections
- A small report improvement should not require a schema migration
- The release should remain a conservative step, not a redesign

## 11. Acceptance Criteria

`v0.3.0` is acceptable when:
- the targeted false-positive cases are reduced or removed
- the targeted true-positive cases still match
- text and CSV output remain readable and stable
- the JSON output remains compatible with the current structure
- the test suite passes
- the release stays within the intended small-scope tuning boundary
