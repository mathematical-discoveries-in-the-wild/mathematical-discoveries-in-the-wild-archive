#!/usr/bin/env python3
"""Render source-evidence crops for the 2302.04506 duality packet."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
FIGURES = ROOT / "figures"


def render_crop(page_index: int, rect: tuple[float, float, float, float], name: str) -> None:
    doc = fitz.open(PDF)
    page = doc[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=fitz.Rect(rect), alpha=False)
    FIGURES.mkdir(exist_ok=True)
    pix.save(FIGURES / name)


def main() -> None:
    render_crop(
        2,
        (60, 350, 552, 625),
        "open_problem_crop.png",
    )
    render_crop(
        7,
        (60, 145, 552, 330),
        "source_duality_proposition_crop.png",
    )
    render_crop(
        5,
        (60, 160, 552, 370),
        "phic_open_problem_crop.png",
    )


if __name__ == "__main__":
    main()
