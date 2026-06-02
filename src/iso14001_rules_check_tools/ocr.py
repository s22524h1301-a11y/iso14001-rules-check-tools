from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import fitz  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised via missing-support tests
    fitz = None

try:
    import pytesseract  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised via missing-support tests
    pytesseract = None

try:
    from PIL import Image  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised via missing-support tests
    Image = None


class OcrTextExtractionError(RuntimeError):
    pass


class OcrUnreadablePdfError(OcrTextExtractionError):
    pass


class OcrMissingSupportError(OcrTextExtractionError):
    pass


class OcrRuntimeError(OcrTextExtractionError):
    pass


class OcrEmptyOutputError(OcrTextExtractionError):
    pass


def _require_ocr_support() -> None:
    if fitz is None or pytesseract is None or Image is None:
        raise OcrMissingSupportError("OCR support is not installed")


def _page_to_text(page: Any) -> str:
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    return (pytesseract.image_to_string(image) or "").strip()


def extract_ocr_text(pdf_path: str | Path) -> str:
    path = Path(pdf_path)
    _require_ocr_support()

    try:
        document = fitz.open(str(path))
    except OcrTextExtractionError:
        raise
    except Exception as exc:
        raise OcrUnreadablePdfError(f"Unable to read PDF for OCR: {path}") from exc

    try:
        pages: list[str] = []
        for page in document:
            try:
                text = _page_to_text(page)
            except Exception as exc:
                raise OcrRuntimeError(f"OCR runtime failure: {path}") from exc
            if text:
                pages.append(text)
    finally:
        close = getattr(document, "close", None)
        if callable(close):
            close()

    combined = "\n\n".join(pages).strip()
    if not combined:
        raise OcrEmptyOutputError("OCR produced no readable text")
    return combined
