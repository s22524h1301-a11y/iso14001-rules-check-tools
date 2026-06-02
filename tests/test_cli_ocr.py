from __future__ import annotations

from unittest.mock import Mock

import iso14001_rules_check_tools.cli as cli
from iso14001_rules_check_tools.pdf_reader import PdfTextExtractionError


def test_cli_preserves_pdf_reader_error_message(monkeypatch, capsys):
    monkeypatch.setattr(cli, "extract_pdf_text", Mock(side_effect=PdfTextExtractionError("OCR runtime failure: sample.pdf")))

    result = cli.main(["sample.pdf"])

    captured = capsys.readouterr()
    assert result == 1
    assert "OCR runtime failure: sample.pdf" in captured.err
