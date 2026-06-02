from __future__ import annotations

import os
from pathlib import Path


def pytest_configure() -> None:
    src_path = Path(__file__).resolve().parents[1] / "src"
    current = os.environ.get("PYTHONPATH")
    if current:
        os.environ["PYTHONPATH"] = f"{src_path}{os.pathsep}{current}"
    else:
        os.environ["PYTHONPATH"] = str(src_path)
