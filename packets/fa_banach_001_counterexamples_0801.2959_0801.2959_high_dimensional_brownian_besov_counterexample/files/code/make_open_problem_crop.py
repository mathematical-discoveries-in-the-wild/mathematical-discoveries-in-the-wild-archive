#!/usr/bin/env python3
"""Crop Theorem 6.1 and Remark 6.1 from rendered source page 15."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source-page-hi-15.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        # Full text width plus margins; includes the complete theorem and remark.
        crop = image.crop((275, 250, 1595, 760))
        crop.save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
