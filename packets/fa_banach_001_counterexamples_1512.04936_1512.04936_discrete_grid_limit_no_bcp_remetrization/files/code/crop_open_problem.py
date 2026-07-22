#!/usr/bin/env python3
"""Crop the Section 8.3 open problem from a rendered source page."""

from pathlib import Path
import argparse

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    image = Image.open(args.input)
    # Coordinates for page 55 rendered at 180 dpi (1530 x 1980 pixels).
    crop = image.crop((120, 510, 1390, 1180))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    crop.save(args.output)


if __name__ == "__main__":
    main()
