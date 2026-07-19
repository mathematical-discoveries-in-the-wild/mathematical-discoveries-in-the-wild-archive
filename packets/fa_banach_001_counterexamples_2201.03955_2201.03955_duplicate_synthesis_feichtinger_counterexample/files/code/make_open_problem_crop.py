#!/usr/bin/env python3
"""Render and crop Conjectures 7.1--7.2 from arXiv:2201.03955."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from PIL import Image


PACKET_DIR = Path(__file__).resolve().parents[1]
SOURCE_PDF = PACKET_DIR / "source_paper.pdf"
TMP_DIR = PACKET_DIR / "tmp"
FIGURES_DIR = PACKET_DIR / "figures"
OUTPUT = FIGURES_DIR / "open_problem_crop.png"
BUNDLED_PDFTOPPM = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm"
)


def find_pdftoppm() -> str:
    env_path = os.environ.get("PDFTOPPM")
    if env_path:
        return env_path
    path = shutil.which("pdftoppm")
    if path:
        return path
    if BUNDLED_PDFTOPPM.exists():
        return str(BUNDLED_PDFTOPPM)
    raise RuntimeError("pdftoppm not found; set PDFTOPPM to a Poppler pdftoppm binary")


def main() -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    prefix = TMP_DIR / "source_page"
    subprocess.run(
        [
            find_pdftoppm(),
            "-f",
            "24",
            "-l",
            "24",
            "-r",
            "180",
            "-png",
            str(SOURCE_PDF),
            str(prefix),
        ],
        check=True,
    )

    rendered = TMP_DIR / "source_page-24.png"
    image = Image.open(rendered)
    # Page 24 at 180 dpi is 1530 x 1980. This full-width crop covers
    # Conjectures 7.1 and 7.2 without clipping the displayed norm bounds.
    crop = image.crop((100, 80, 1435, 615))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
