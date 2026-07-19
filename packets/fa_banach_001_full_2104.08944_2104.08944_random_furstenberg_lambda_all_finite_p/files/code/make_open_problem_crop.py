#!/usr/bin/env python3
"""Crop the open-question paragraph from rendered PDF page 9."""

from pathlib import Path
import sys

from PIL import Image


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: make_open_problem_crop.py INPUT_PAGE.png OUTPUT.png")
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    image = Image.open(source)
    if image.size != (1530, 1980):
        raise SystemExit(f"unexpected rendered-page size: {image.size}")
    # Keep the full text width plus generous margins.  The crop includes
    # Theorem 1.7 and the complete paragraph stating the Lambda(p) question.
    crop = image.crop((170, 480, 1360, 930))
    destination.parent.mkdir(parents=True, exist_ok=True)
    crop.save(destination)


if __name__ == "__main__":
    main()
