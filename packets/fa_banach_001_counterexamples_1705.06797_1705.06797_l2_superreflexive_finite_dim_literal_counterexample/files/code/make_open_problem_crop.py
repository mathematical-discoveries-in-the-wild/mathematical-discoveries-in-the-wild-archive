#!/usr/bin/env python3
"""Render and crop the Problem 5.1 source page.

Requires Ghostscript on PATH and Pillow in the active Python environment.
Run from the packet directory:

    python3 code/make_open_problem_crop.py
"""

from pathlib import Path
import subprocess

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"
PAGE_PNG = TMP / "page19.png"
OUT = FIGURES / "open_problem_crop.png"


def main() -> None:
    TMP.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    subprocess.run(
        [
            "gs",
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE=pngalpha",
            "-r220",
            "-dFirstPage=19",
            "-dLastPage=19",
            f"-sOutputFile={PAGE_PNG}",
            str(PDF),
        ],
        check=True,
    )
    image = Image.open(PAGE_PNG)
    crop = image.crop((235, 500, 1585, 1135))
    crop.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
