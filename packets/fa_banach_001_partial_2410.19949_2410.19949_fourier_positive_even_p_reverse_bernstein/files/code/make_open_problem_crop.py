#!/usr/bin/env python3
"""Crop the full-width Section 1.3 excerpt from rendered source-paper page 3."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_page-03.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        # Keep the complete horizontal page width.  The vertical interval contains
        # all of Section 1.3, including the definition, Corollary 3, and the exact
        # open-problem sentence; the next section heading is retained as context.
        crop = image.crop((0, 120, image.width, 890))
        crop.save(OUTPUT)


if __name__ == "__main__":
    main()
