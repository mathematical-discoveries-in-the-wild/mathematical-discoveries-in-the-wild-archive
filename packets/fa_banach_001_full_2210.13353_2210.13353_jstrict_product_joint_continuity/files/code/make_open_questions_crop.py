#!/usr/bin/env python3
"""Render source page 25 and crop the exact Q1--Q2 statement."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp" / "pdfs"
FIGURES = PACKET / "figures"


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError("pdftoppm was not found")

    prefix = TMP / "source_page25"
    subprocess.run(
        [
            pdftoppm,
            "-f",
            "25",
            "-singlefile",
            "-r",
            "200",
            "-png",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )

    page = Image.open(TMP / "source_page25.png")
    if page.size != (1700, 2200):
        raise RuntimeError(f"unexpected render size: {page.size}")

    # Full text width, including the lead-in sentence and both questions.
    page.crop((300, 1138, 1400, 1298)).save(
        FIGURES / "open_questions_crop.png"
    )


if __name__ == "__main__":
    main()
