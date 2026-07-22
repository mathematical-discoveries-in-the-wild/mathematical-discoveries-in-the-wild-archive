#!/usr/bin/env python3
"""Render the two-page Remark 6.4 statement and make readable full-width crops."""

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

    prefix = TMP / "source_page"
    subprocess.run(
        [
            pdftoppm,
            "-f",
            "11",
            "-l",
            "12",
            "-r",
            "200",
            "-png",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )

    page11 = Image.open(TMP / "source_page-11.png")
    page12 = Image.open(TMP / "source_page-12.png")
    if page11.size != (1700, 2200) or page12.size != (1700, 2200):
        raise RuntimeError(f"unexpected render size: {page11.size}, {page12.size}")

    # Keep the complete page width (including margins) and the full statement.
    page11.crop((0, 1690, 1700, 2180)).save(
        FIGURES / "open_problem_crop_page11.png"
    )
    page12.crop((0, 0, 1700, 330)).save(
        FIGURES / "open_problem_crop_page12.png"
    )


if __name__ == "__main__":
    main()
