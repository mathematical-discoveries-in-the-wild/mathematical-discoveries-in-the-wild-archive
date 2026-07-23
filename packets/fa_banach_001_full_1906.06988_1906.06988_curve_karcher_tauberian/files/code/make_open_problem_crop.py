#!/usr/bin/env python3
"""Render and crop Remark 3.1 (PDF page 14) from the source paper."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
TMP = PACKET / "tmp" / "pdfs"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise RuntimeError("pdftoppm is required")
    prefix = TMP / "source_page"
    subprocess.run(
        [
            renderer,
            "-f",
            "14",
            "-l",
            "14",
            "-png",
            "-r",
            "180",
            str(PDF),
            str(prefix),
        ],
        check=True,
    )
    page = Image.open(TMP / "source_page-14.png")
    width, _ = page.size
    # Retain both page margins and all of Remark 3.1, including the displayed
    # definitions and the final open-question sentence.
    crop = page.crop((120, 200, width - 120, 1370))
    crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
