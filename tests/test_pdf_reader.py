from pathlib import Path

import pytest
from reportlab.pdfgen import canvas

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


def test_extract_pdf_text_falls_back_to_ocr_when_no_text_is_available(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    pdf_path = tmp_path / "blank.pdf"
    _write_blank_pdf(pdf_path)

    monkeypatch.setattr(
        "iso14001_rules_check_tools.pdf_reader.extract_text_with_ocr",
        lambda path: "OCR extracted text",
    )

    result = extract_pdf_text(pdf_path)

    assert result == "OCR extracted text"


def test_extract_pdf_text_raises_when_pdf_cannot_be_read(tmp_path: Path):
    pdf_path = tmp_path / "missing.pdf"

    with pytest.raises(PdfTextExtractionError, match="Unable to read PDF"):
        extract_pdf_text(pdf_path)

