#!/usr/bin/env python3
"""Render PDF page 55 and crop the full-width Problem 9 context."""

from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP_PREFIX = PACKET / "tmp" / "pdfs" / "source-page-55"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    pdftoppm = sys.argv[1] if len(sys.argv) > 1 else shutil.which("pdftoppm")
    if pdftoppm is None:
        raise SystemExit("pdftoppm was not found on PATH")
    TMP_PREFIX.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            pdftoppm,
            "-f",
            "55",
            "-l",
            "55",
            "-png",
            "-r",
            "180",
            "-singlefile",
            str(SOURCE),
            str(TMP_PREFIX),
        ],
        check=True,
    )
    rendered = TMP_PREFIX.with_suffix(".png")
    with Image.open(rendered) as image:
        width, height = image.size
        crop = image.crop((0, round(0.20 * height), width, round(0.56 * height)))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
