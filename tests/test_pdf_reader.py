from pathlib import Path

import pytest
from reportlab.pdfgen import canvas

import iso14001_rules_check_tools.pdf_reader as pdf_reader
from iso14001_rules_check_tools.pdf_reader import PdfTextExtractionError, extract_pdf_text


def _write_text_pdf(path: Path, text: str) -> None:
    c = canvas.Canvas(str(path))
    c.drawString(72, 720, text)
    c.save()


def _write_blank_pdf(path: Path) -> None:
    c = canvas.Canvas(str(path))
    c.showPage()
    c.save()


def test_extract_pdf_text_returns_combined_text(tmp_path: Path):
    pdf_path = tmp_path / "sample.pdf"
    _write_text_pdf(pdf_path, "Hello ISO 14001")

    result = extract_pdf_text(pdf_path)

    assert "Hello ISO 14001" in result


def test_extract_pdf_text_uses_ocr_when_direct_extraction_is_empty(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    pdf_path = tmp_path / "blank.pdf"
    _write_blank_pdf(pdf_path)
    monkeypatch.setattr(pdf_reader, "extract_ocr_text", lambda _path: "Recovered via OCR")

    result = extract_pdf_text(pdf_path)

    assert result == "Recovered via OCR"


def test_extract_pdf_text_raises_for_unreadable_pdf(tmp_path: Path):
    pdf_path = tmp_path / "broken.pdf"
    pdf_path.write_text("not a pdf", encoding="utf-8")

    with pytest.raises(PdfTextExtractionError, match="Unable to read PDF"):
        extract_pdf_text(pdf_path)

