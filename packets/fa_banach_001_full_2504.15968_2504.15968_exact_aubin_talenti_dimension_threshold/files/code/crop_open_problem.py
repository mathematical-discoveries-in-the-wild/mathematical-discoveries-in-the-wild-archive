#!/usr/bin/env python3
"""Render and crop the open-question passage from page 7 of the source PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
PDF = PACKET / "source_paper.pdf"
TMP_PREFIX = PACKET / "tmp" / "source_page_7"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"
PDFTOPPM = Path(
    "/Users/pacuaviva/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/bin/override/pdftoppm"
)


def main() -> None:
    subprocess.run(
        [
            str(PDFTOPPM),
            "-f",
            "7",
            "-l",
            "7",
            "-r",
            "300",
            "-png",
            "-singlefile",
            str(PDF),
            str(TMP_PREFIX),
        ],
        check=True,
    )
    page_path = TMP_PREFIX.with_suffix(".png")
    with Image.open(page_path) as page:
        width, height = page.size
        # Full page width is retained.  The vertical crop includes all of
        # Remark 1.1(1), its lead-in, and enough of item (2) to show the end.
        crop = page.crop((0, int(0.56 * height), width, int(0.93 * height)))
        crop.save(OUTPUT, dpi=(300, 300))
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
