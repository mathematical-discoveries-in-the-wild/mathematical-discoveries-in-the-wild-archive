#!/usr/bin/env python3
"""Recreate the two source-question crops after rendering PDF pages 4--5.

First run pdftoppm at 220 DPI as documented in the packet README. The input
PNGs should be tmp/pdfs/source-4.png and tmp/pdfs/source-5.png.
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp" / "pdfs"
FIG = ROOT / "figures"


def main() -> None:
    page4 = Image.open(TMP / "source-4.png")
    page5 = Image.open(TMP / "source-5.png")
    page4.crop((0, 1400, 1870, 2420)).save(FIG / "open_problem_crop_page4.png")
    page5.crop((0, 150, 1870, 500)).save(FIG / "open_problem_crop_page5.png")
    print("Wrote source-question crops")


if __name__ == "__main__":
    main()
