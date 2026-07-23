#!/usr/bin/env python3
"""Render and crop the two decisive pages from source_paper.pdf."""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"


def render(page: int, stem: str) -> Path:
    TMP.mkdir(parents=True, exist_ok=True)
    prefix = TMP / stem
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            str(page),
            "-l",
            str(page),
            "-r",
            "220",
            "-png",
            str(SOURCE),
            str(prefix),
        ],
        check=True,
    )
    return TMP / f"{stem}-{page}.png"


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)

    gap_page = Image.open(render(20, "source_gap_page"))
    gap_page.crop((145, 625, 1725, 1900)).save(
        FIGURES / "open_problem_crop.png"
    )

    criterion_page = Image.open(render(16, "source_criterion_page"))
    criterion_page.crop((145, 470, 1725, 1685)).save(
        FIGURES / "rank_one_criterion_crop.png"
    )

    print("wrote figures/open_problem_crop.png")
    print("wrote figures/rank_one_criterion_crop.png")


if __name__ == "__main__":
    main()
