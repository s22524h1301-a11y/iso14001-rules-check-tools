from __future__ import annotations

from pathlib import Path


class OcrTextExtractionError(RuntimeError):
    pass


def _open_pdf(path: Path):
    try:
        import fitz

        return fitz.open(str(path))
    except ImportError as exc:
        raise OcrTextExtractionError("OCR support is not available") from exc
    except (FileNotFoundError, OSError, RuntimeError, ValueError) as exc:
        raise OcrTextExtractionError(f"Unable to read PDF: {path}") from exc


def _render_page(page):
    from PIL import Image

    pixmap = page.get_pixmap(dpi=300, alpha=False)
    mode = "RGBA" if getattr(pixmap, "alpha", False) else "RGB"
    return Image.frombytes(mode, [pixmap.width, pixmap.height], pixmap.samples)


def _image_to_text(image) -> str:
    import pytesseract

    return pytesseract.image_to_string(image)


def extract_pdf_text(pdf_path: str | Path) -> str:
    path = Path(pdf_path)
    document = _open_pdf(path)
    pages: list[str] = []

    try:
        for page in document:
            text = _image_to_text(_render_page(page)).strip()
            if text:
                pages.append(text)
    except OcrTextExtractionError:
        raise
    except Exception as exc:
        raise OcrTextExtractionError(f"Unable to OCR PDF: {path}") from exc
    finally:
        close = getattr(document, "close", None)
        if callable(close):
            close()

    return "\n\n".join(pages).strip()
