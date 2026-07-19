#!/usr/bin/env python3
"""Render and crop the lattice-isomorphism question from the source PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
TMP_PREFIX = PACKET / "tmp" / "source_page"
PAGE_IMAGE = PACKET / "tmp" / "source_page-09.png"
OUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            "9",
            "-l",
            "9",
            "-png",
            "-r",
            "200",
            str(PDF),
            str(TMP_PREFIX),
        ],
        check=True,
    )
    image = Image.open(PAGE_IMAGE)
    # Full text width around Corollary 3.3 and Question 3.4 on page 9.
    crop = image.crop((110, 1120, 1595, 1625))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUT)


if __name__ == "__main__":
    main()
