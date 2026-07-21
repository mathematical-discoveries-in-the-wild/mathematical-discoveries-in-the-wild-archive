#!/usr/bin/env python3
"""Render and crop the source question and its referenced formula."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image


def render_page(pdftoppm: str, pdf: Path, page: int, dpi: int, out: Path) -> Path:
    prefix = out / f"source_page_{page}"
    subprocess.run(
        [
            pdftoppm,
            "-f",
            str(page),
            "-l",
            str(page),
            "-r",
            str(dpi),
            "-png",
            str(pdf),
            str(prefix),
        ],
        check=True,
    )
    return out / f"source_page_{page}-{page}.png"


def scaled_box(box: tuple[int, int, int, int], dpi: int) -> tuple[int, int, int, int]:
    scale = dpi / 200
    return tuple(round(value * scale) for value in box)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dpi", type=int, default=200)
    args = parser.parse_args()

    packet = Path(__file__).resolve().parents[1]
    pdf = packet / "source_paper.pdf"
    figures = packet / "figures"
    tmp = packet / "tmp" / "source_render"
    figures.mkdir(parents=True, exist_ok=True)
    tmp.mkdir(parents=True, exist_ok=True)

    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        raise SystemExit("pdftoppm is required; put bundled Poppler on PATH")

    question_page = render_page(pdftoppm, pdf, 43, args.dpi, tmp)
    formula_page = render_page(pdftoppm, pdf, 35, args.dpi, tmp)

    with Image.open(question_page) as image:
        image.crop(scaled_box((205, 625, 1515, 900), args.dpi)).save(
            figures / "open_problem_crop.png"
        )
    with Image.open(formula_page) as image:
        image.crop(scaled_box((215, 1445, 1515, 1715), args.dpi)).save(
            figures / "spectral_mapping_formula_crop.png"
        )

    print("WROTE", figures / "open_problem_crop.png")
    print("WROTE", figures / "spectral_mapping_formula_crop.png")


if __name__ == "__main__":
    main()
