from pathlib import Path

from reportlab.pdfgen import canvas

from iso14001_rules_check_tools import cli


def _write_blank_pdf(path: Path) -> None:
    c = canvas.Canvas(str(path))
    c.showPage()
    c.save()


def test_cli_prints_ocr_fallback_text(tmp_path: Path, monkeypatch, capsys):
    pdf_path = tmp_path / "scanned.pdf"
    _write_blank_pdf(pdf_path)

    monkeypatch.setattr(
        "iso14001_rules_check_tools.pdf_reader.extract_text_with_ocr",
        lambda path: "OCR fallback text",
    )

    exit_code = cli.main([str(pdf_path)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "OCR fallback text" in captured.out
