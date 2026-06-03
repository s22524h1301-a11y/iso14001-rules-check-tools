import subprocess
import sys
from io import StringIO
from pathlib import Path
import csv

from reportlab.pdfgen import canvas


def _write_text_pdf(path: Path, text: str) -> None:
    c = canvas.Canvas(str(path))
    text_object = c.beginText(72, 720)
    for line in text.splitlines():
        text_object.textLine(line)
    c.drawText(text_object)
    c.save()


def test_cli_csv_outputs_csv_header(tmp_path: Path):
    pdf_path = tmp_path / "policy.pdf"
    _write_text_pdf(
        pdf_path,
        "1. Environmental policy\nThe organization shall establish an environmental policy and communicate it.",
    )

    result = subprocess.run(
        [sys.executable, "-m", "iso14001_rules_check_tools", "--csv", str(pdf_path)],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    header = next(csv.reader(StringIO(result.stdout)))
    assert "section_id" in header
    assert "clause_id" in header
