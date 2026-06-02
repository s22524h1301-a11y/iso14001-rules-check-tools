import subprocess
import sys
from pathlib import Path

from reportlab.pdfgen import canvas


def _write_text_pdf(path: Path, text: str) -> None:
    c = canvas.Canvas(str(path))
    text_object = c.beginText(72, 720)
    for line in text.splitlines():
        text_object.textLine(line)
    c.drawText(text_object)
    c.save()


def test_cli_prints_section_headings_and_bodies(tmp_path: Path):
    pdf_path = tmp_path / "sample.pdf"
    _write_text_pdf(
        pdf_path,
        "1. Introduction\nThis is the intro.\n\n2. Environmental policy\nThe organization shall establish an environmental policy.",
    )

    result = subprocess.run(
        [sys.executable, "-m", "iso14001_rules_check_tools", str(pdf_path)],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "[1] 1. Introduction" in result.stdout
    assert "[2] 2. Environmental policy" in result.stdout


def test_cli_prints_matched_clause_ids(tmp_path: Path):
    pdf_path = tmp_path / "policy.pdf"
    _write_text_pdf(
        pdf_path,
        "1. Environmental policy\nThe organization shall establish an environmental policy and communicate it.",
    )

    result = subprocess.run(
        [sys.executable, "-m", "iso14001_rules_check_tools", str(pdf_path)],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "5.2" in result.stdout



