#!/usr/bin/env python3
"""Render the decisive source pages and make full-width evidence crops."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


def render_page(pdf: Path, page: int, dpi: int, output_prefix: Path) -> Path:
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise RuntimeError("pdftoppm was not found on PATH")
    subprocess.run(
        [
            renderer,
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-png",
            "-r",
            str(dpi),
            str(pdf),
            str(output_prefix),
        ],
        check=True,
    )
    return output_prefix.with_suffix(".png")


def save_fractional_crop(
    source: Path, destination: Path, top: float, bottom: float
) -> None:
    with Image.open(source) as image:
        width, height = image.size
        crop = image.crop((0, int(top * height), width, int(bottom * height)))
        destination.parent.mkdir(parents=True, exist_ok=True)
        crop.save(destination, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_pdf", type=Path)
    parser.add_argument("figures_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=240)
    args = parser.parse_args()

    args.figures_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="hardy_source_crops_") as tmp_name:
        tmp = Path(tmp_name)
        question_page = render_page(
            args.source_pdf, page=17, dpi=args.dpi, output_prefix=tmp / "page17"
        )
        theorem_page = render_page(
            args.source_pdf, page=5, dpi=args.dpi, output_prefix=tmp / "page05"
        )

        # Full page width is retained. The first crop includes the preceding
        # classical inequality and all lines of the open-question paragraph.
        save_fractional_crop(
            question_page,
            args.figures_dir / "open_problem_crop.png",
            top=0.055,
            bottom=0.390,
        )
        # This crop includes the complete statement and barrier of Theorem 3.1,
        # giving enough context for the cross-reference in the question.
        save_fractional_crop(
            theorem_page,
            args.figures_dir / "theorem_3_1_crop.png",
            top=0.255,
            bottom=0.625,
        )


if __name__ == "__main__":
    main()
