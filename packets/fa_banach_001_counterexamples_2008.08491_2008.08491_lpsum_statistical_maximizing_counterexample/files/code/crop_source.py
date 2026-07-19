#!/usr/bin/env python3
"""Crop the full-width Corollary 3.6 / Remark 3.7 region from source page 5."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "pdfs" / "source_page-05.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as page:
        width, height = page.size
        if (width, height) != (1700, 2200):
            raise RuntimeError(f"unexpected source render size: {(width, height)}")
        # Preserve the original full page width, including both margins.
        crop = page.crop((0, 490, width, 700))
        crop.save(OUTPUT)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
