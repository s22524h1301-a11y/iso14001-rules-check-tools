from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_release_docs_mention_ocr_stability_and_fallback_scope() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8").lower()
    versioning = (ROOT / "docs" / "VERSIONING.md").read_text(encoding="utf-8").lower()

    english_intro = _section(readme, "## english", "### what it does")
    english_scope = _section(readme, "### scope", "### installation")
    chinese_intro = _section(readme, "## 繁體中文", "### 這個工具會做什麼")
    chinese_scope = _section(readme, "### 支援範圍", "### 安裝")
    release_status = _section(readme, "### release status", "<a id=\"")
    changelog_v011 = _section(changelog, "## [v0.1.1]", "## [v0.1.0]")
    versioning_starting_point = _section(versioning, "## starting point", "")

    assert "v0.1.1" in english_intro
    assert "ocr stability patch" in english_intro
    assert "scanned pdfs with ocr fallback" in english_intro

    assert "selectable-text electronic pdfs and scanned pdfs with ocr fallback" in english_scope
    assert "stable, explainable mvp with ocr fallback reliability" in english_scope

    assert "繁體中文" in readme
    assert "掃描式 pdf" in chinese_intro
    assert "ocr 備援" in chinese_intro
    assert "可選取文字的電子檔與需要 ocr 備援的掃描式 pdf" in chinese_scope
    assert "ocr fallback 穩定性" in chinese_scope

    assert "v0.1.1" in release_status
    assert "first ocr stability patch" in release_status

    assert "v0.1.1" in changelog_v011
    assert "ocr stability patch" in changelog_v011
    assert "fallback-focused scope" in changelog_v011

    assert "v0.1.1" in versioning_starting_point
    assert "first ocr stability patch" in versioning_starting_point
    assert "iso 14001-only scope" in versioning_starting_point


def _section(text: str, start_marker: str, end_marker: str) -> str:
    start = text.index(start_marker)
    if end_marker:
        end = text.index(end_marker, start + len(start_marker))
        return text[start:end]
    return text[start:]
