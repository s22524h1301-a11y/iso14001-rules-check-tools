from pathlib import Path


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.index(marker) + len(marker)
    tail = text[start:]
    next_heading = tail.find("\n## ")
    return tail[:next_heading] if next_heading != -1 else tail


def test_readme_mentions_v040_and_csv():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "v0.4.0" in readme
    assert "CSV" in readme
    assert "catalog" in readme.lower()
    assert "coverage" in readme.lower()


def test_changelog_mentions_v040():
    changelog = Path("CHANGELOG.md").read_text(encoding="utf-8")
    assert "v0.4.0" in changelog


def test_versioning_doc_mentions_v040():
    versioning = Path("docs/VERSIONING.md").read_text(encoding="utf-8")
    assert "v0.4.0" in versioning
