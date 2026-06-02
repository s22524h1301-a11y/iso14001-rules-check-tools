from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from .ocr import OcrTextExtractionError, extract_ocr_text


class PdfTextExtractionError(RuntimeError):
    pass


def extract_pdf_text(pdf_path: str | Path) -> str:
    path = Path(pdf_path)
    try:
        reader = PdfReader(str(path))
    except (FileNotFoundError, PdfReadError, OSError) as exc:
        raise PdfTextExtractionError(f"Unable to read PDF: {path}") from exc

    pages: list[str] = []
    for page in reader.pages:
        text = (page.extract_text() or "").strip()
        if text:
            pages.append(text)

    combined = "\n\n".join(pages).strip()
    if combined:
        return combined

    try:
        return extract_ocr_text(path)
    except OcrTextExtractionError as exc:
        raise PdfTextExtractionError(str(exc)) from exc
