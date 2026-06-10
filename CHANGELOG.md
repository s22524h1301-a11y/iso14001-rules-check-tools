# Changelog

All notable changes to this project will be documented in this file.

## [v0.3.0] - 2026-06-10

### Added

- Top-match summary lines in the plain-text report
- Slightly more compact CSV reason strings for easier review
- Regression coverage for high-false-positive clause matches

### Changed

- Tightened the clause catalog for `6.1.3` and `8.1`
- Reduced noisy keyword hits that caused generic policy or process text to match too broadly
- Updated README, versioning, and release metadata for the new release

### Notes

- JSON output remains available and structurally stable
- The project remains a standalone ISO 14001 tool, separate from the ISO 9001 repository

## [v0.2.0] - 2026-06-03

### Added

- CSV report output for section-level analysis
- Match evidence surfaced to the reporting layer
- Better spreadsheet-friendly review flow for ISO 14001 results

### Changed

- Improved clause catalog coverage for high-value ISO 14001 topics
- Refined clause ranking and report payloads
- Updated CLI help and docs for `--csv`

### Notes

- JSON and plain text output remain available
- The project remains a standalone ISO 14001 tool, separate from the ISO 9001 repository

## [v0.1.0] - 2026-06-02

### Added

- Initial ISO 14001 project scaffold
- CLI entry point
- PDF text extraction pipeline
- Section splitting pipeline
- Text and JSON reporting pipeline
- Initial ISO 14001 clause catalog structure
- Basic automated tests

### Notes

- This is the first starting version of the ISO 14001 project
- The clause catalog will continue to be refined for environmental management use cases
