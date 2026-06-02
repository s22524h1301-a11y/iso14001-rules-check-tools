# ISO 14001 Rules Check Tools v0.1.1 OCR Stability Design

**Goal:** Improve OCR fallback reliability for scanned PDFs by making failure modes explicit, diagnosable, and testable without changing the existing text/JSON output format or expanding the overall feature scope.

**Architecture:** Keep the existing pipeline intact: selectable-text PDF extraction first, OCR fallback only when needed, then section splitting, clause matching, and report rendering. The `v0.1.1` change is a narrow reliability layer around the OCR boundary: classify failures precisely, preserve user-facing context, and make the CLI emit actionable messages instead of a generic fallback failure.

**Tech Stack:** Python 3.12, `pypdf`, `pymupdf`, `pytesseract`, `Pillow`, and `pytest`.

---

## 1. Product Summary

This release is a patch-level improvement to the existing ISO 14001 MVP. It does not add new input formats, new report formats, or semantic matching. The only goal is to make scanned PDF handling more predictable and easier to debug when OCR fails.

The current OCR path already exists. `v0.1.1` hardens it by:
- distinguishing direct PDF read failures from OCR failures
- making the absence of OCR support explicit
- making OCR-empty results explicit
- surfacing the failure reason in the CLI

## 2. Versioning

`v0.1.1` is a patch release.

- `v0.1.0` remains the first MVP release
- `v0.1.1` is a stability release focused on OCR diagnostics
- Future `v0.1.x` releases should stay compatible with the current CLI and output shape unless a patch-level bug fix requires a narrow behavior correction

Release hygiene:
- Update `pyproject.toml` version if the release is cut
- Update `CHANGELOG.md` with a short note describing OCR stability improvements
- Keep the README scope summary aligned with actual behavior

## 3. Recommended Approach

Recommended: explicit failure classification with direct CLI propagation.

Why this approach:
- It preserves the current pipeline and keeps the change small
- It makes OCR issues easy to diagnose in scripts and manual use
- It avoids pretending a broken OCR run succeeded

Alternatives considered:
- Best-effort silent fallback: too ambiguous for troubleshooting
- Recover-and-hide errors: convenient short term, but it can mask broken OCR setup and create false confidence

The release should keep the conservative default: if OCR cannot produce text, the command should fail with a clear reason rather than returning an empty or misleading analysis.

## 4. Error Model

The OCR boundary should distinguish these cases:

- unreadable PDF file
  - the PDF cannot be opened or parsed at all
- OCR dependency missing
  - OCR support is not installed in the environment
- OCR execution failure
  - the OCR engine or render path raised an unexpected error
- OCR empty output
  - the OCR path ran, but it did not recover usable text

The CLI should show a concise, actionable message for each case. The underlying exception chain should remain available for debugging, but the user-facing error should stay short.

## 5. Behavioral Scope

### In scope for `v0.1.1`
- Preserve selectable-text PDF extraction as the primary path
- Keep OCR as fallback for scanned PDFs
- Distinguish OCR support missing from OCR runtime failure
- Treat empty OCR output as a failure, not a success
- Emit clear CLI error messages for OCR failures
- Add or update tests for each failure class

### Out of scope for `v0.1.1`
- New file types such as Word, Excel, or HTML
- New output formats
- Changes to section splitting
- Changes to clause catalog structure
- Semantic or ML-based matching
- OCR tuning for multilingual or layout-heavy documents beyond basic robustness

## 6. Component Boundaries

### `pdf_reader`
Responsibility:
- manage direct PDF extraction
- invoke OCR fallback only when needed
- translate low-level exceptions into the project-level `PdfTextExtractionError`

Inputs:
- a PDF path

Outputs:
- extracted text, or a clear project-level error

### `ocr`
Responsibility:
- open and render scanned PDFs
- run OCR on rendered pages
- raise `OcrTextExtractionError` with a specific reason when OCR cannot complete successfully

Inputs:
- a PDF path

Outputs:
- extracted OCR text, or a classified OCR error

### CLI
Responsibility:
- call the document reader
- print section reports on success
- print a short error message on OCR or PDF failure

## 7. Reporting and UX

No report format changes are planned.

The user-facing behavior should be:
- successful text extraction or OCR fallback still produces the same text and JSON outputs as `v0.1.0`
- failure cases produce a clear error message and a non-zero exit code

The error text should point to the cause, not just the symptom. For example, it should be obvious whether the user needs to install OCR support, replace a broken PDF, or investigate OCR runtime issues.

## 8. Testing Strategy

Tests should focus on deterministic behavior and failure classification.

Required coverage:
- direct text extraction still works
- OCR fallback is used when direct extraction yields no text
- OCR dependency missing is reported clearly
- OCR runtime failure is reported clearly
- OCR-empty output is reported clearly
- CLI surfaces the failure message and exits non-zero

Testing guidance:
- mock the OCR boundary so tests do not require local OCR software for the unit suite
- keep a small integration-style test only if it stays deterministic and easy to skip when OCR tooling is unavailable

## 9. Risks and Constraints

- OCR environments vary widely across machines, so the design should prefer explicit failures over silent recovery
- A better error message is more valuable than a broader fallback
- The release must not accidentally widen scope into general OCR feature work

## 10. Acceptance Criteria

`v0.1.1` is acceptable when:
- selectable-text PDFs still work as before
- scanned PDFs either OCR successfully or fail with a clear, classified error
- CLI users can tell why OCR failed
- the unit and CLI tests pass
- no report format or matcher behavior changed
- the release remains a small, patch-level stability update


