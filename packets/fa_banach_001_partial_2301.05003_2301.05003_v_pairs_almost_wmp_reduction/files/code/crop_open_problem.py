#!/usr/bin/env python3
"""Render and crop Question 3.7 from the source PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
TMP_PREFIX = PACKET / "tmp" / "source_page"
PAGE_IMAGE = PACKET / "tmp" / "source_page-08.png"
OUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            "8",
            "-l",
            "8",
            "-png",
            "-r",
            "160",
            str(PDF),
            str(TMP_PREFIX),
        ],
        check=True,
    )
    image = Image.open(PAGE_IMAGE)
    # Full text-width crop around Question 3.7 and the immediate obstruction.
    crop = image.crop((245, 730, 1145, 970))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUT)


if __name__ == "__main__":
    main()
