#!/usr/bin/env python3
"""Crop the open-question paragraph from the 144-dpi rendering of PDF page 4."""

import argparse

from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_png")
    parser.add_argument("output_png")
    args = parser.parse_args()

    image = Image.open(args.input_png)
    # Coordinates are for the 1224 x 1584 page rendered at 144 dpi.
    crop = image.crop((245, 1060, 1005, 1235))
    crop.save(args.output_png)


if __name__ == "__main__":
    main()
