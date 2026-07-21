#!/usr/bin/env python3
"""Crop page 4 of the source rendering to concluding Remark 1.7(iv)."""

from pathlib import Path
import sys

from PIL import Image


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: crop_source.py INPUT_PNG OUTPUT_PNG")
    source = Path(sys.argv[1])
    output = Path(sys.argv[2])
    image = Image.open(source)
    # Coordinates for the 180-dpi, 1488 x 2105 rendering of source page 4.
    crop = image.crop((170, 850, 1320, 1420))
    output.parent.mkdir(parents=True, exist_ok=True)
    crop.save(output)


if __name__ == "__main__":
    main()
