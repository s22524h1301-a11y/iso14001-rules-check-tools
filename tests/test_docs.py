from __future__ import annotations

from pathlib import Path


def test_readme_mentions_v010_scope_keywords() -> None:
    readme_path = Path(__file__).resolve().parents[1] / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme_lower = readme.lower()

    english_index = readme.index("## English")
    chinese_index = readme.index("## 繁體中文")

    assert english_index < chinese_index
    assert "### v0.1.0 scope" in readme
    assert "### 發佈狀態" in readme

    required_phrases = [
        "selectable-text pdfs",
        "scanned pdfs",
        "ocr fallback",
        "iso 14001:2015",
        "text and json output",
    ]

    for phrase in required_phrases:
        assert phrase in readme_lower
