from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

import iso14001_rules_check_tools.ocr as ocr
from iso14001_rules_check_tools.ocr import (
    OcrEmptyOutputError,
    OcrMissingSupportError,
    OcrRuntimeError,
    OcrUnreadablePdfError,
    extract_ocr_text,
)


class _FakePixmap:
    width = 1
    height = 1
    samples = b"\x00\x00\x00"


class _FakePage:
    def get_pixmap(self, matrix, alpha: bool = False):  # noqa: ARG002
        return _FakePixmap()


class _FakeDocument:
    def __init__(self, pages: list[_FakePage]):
        self._pages = pages
        self.closed = False

    def __iter__(self):
        return iter(self._pages)

    def close(self) -> None:
        self.closed = True


def _install_support(monkeypatch: pytest.MonkeyPatch, *, image_text=None, image_error=None):
    fake_fitz = SimpleNamespace(Matrix=lambda *_args: object(), open=lambda _path: _FakeDocument([]))
    fake_pytesseract = SimpleNamespace(
        image_to_string=(lambda _image: image_error() if callable(image_error) else image_error)
        if image_error is not None
        else (lambda _image: image_text)
    )
    fake_image = SimpleNamespace(frombytes=lambda *_args, **_kwargs: object())

    monkeypatch.setattr(ocr, "fitz", fake_fitz)
    monkeypatch.setattr(ocr, "pytesseract", fake_pytesseract)
    monkeypatch.setattr(ocr, "Image", fake_image)
    return fake_fitz, fake_pytesseract, fake_image


def test_extract_ocr_text_raises_when_support_is_missing(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(ocr, "fitz", None)
    monkeypatch.setattr(ocr, "pytesseract", None)
    monkeypatch.setattr(ocr, "Image", None)

    with pytest.raises(OcrMissingSupportError, match="OCR support is not installed"):
        extract_ocr_text(Path("sample.pdf"))


def test_extract_ocr_text_raises_for_unreadable_pdf(monkeypatch: pytest.MonkeyPatch):
    _install_support(monkeypatch, image_text="unused")
    monkeypatch.setattr(
        ocr.fitz,
        "open",
        lambda _path: (_ for _ in ()).throw(OSError("cannot open")),
    )

    with pytest.raises(OcrUnreadablePdfError, match="Unable to read PDF for OCR"):
        extract_ocr_text(Path("sample.pdf"))


def test_extract_ocr_text_raises_for_runtime_failure(monkeypatch: pytest.MonkeyPatch):
    _install_support(monkeypatch, image_error=lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    monkeypatch.setattr(ocr.fitz, "open", lambda _path: _FakeDocument([_FakePage()]))

    with pytest.raises(OcrRuntimeError, match="OCR runtime failure"):
        extract_ocr_text(Path("sample.pdf"))


def test_extract_ocr_text_raises_for_empty_output(monkeypatch: pytest.MonkeyPatch):
    _install_support(monkeypatch, image_text="")
    monkeypatch.setattr(ocr.fitz, "open", lambda _path: _FakeDocument([_FakePage()]))

    with pytest.raises(OcrEmptyOutputError, match="OCR produced no readable text"):
        extract_ocr_text(Path("sample.pdf"))
