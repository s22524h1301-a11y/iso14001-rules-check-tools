from pathlib import Path

from iso14001_rules_check_tools.ocr import extract_pdf_text


def test_extract_pdf_text_from_ocr_adapter_combines_page_text(tmp_path: Path, monkeypatch):
    pdf_path = tmp_path / "scanned.pdf"
    pdf_path.write_bytes(b"%PDF-1.4")

    monkeypatch.setattr(
        "iso14001_rules_check_tools.ocr._open_pdf",
        lambda path: ["page-one", "page-two"],
    )
    monkeypatch.setattr(
        "iso14001_rules_check_tools.ocr._render_page",
        lambda page: f"image:{page}",
    )
    monkeypatch.setattr(
        "iso14001_rules_check_tools.ocr._image_to_text",
        lambda image: image.removeprefix("image:").upper(),
    )

    result = extract_pdf_text(pdf_path)

    assert result == "PAGE-ONE\n\nPAGE-TWO"
