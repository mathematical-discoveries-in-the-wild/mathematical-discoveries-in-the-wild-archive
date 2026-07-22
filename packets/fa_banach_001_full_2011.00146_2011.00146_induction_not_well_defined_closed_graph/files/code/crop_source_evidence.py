#!/usr/bin/env python3
"""Crop Remark 19 and its induction-map context from 144-dpi source pages."""

import argparse
from pathlib import Path

from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("page9_png")
    parser.add_argument("page10_png")
    parser.add_argument("output_dir")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    page9 = Image.open(args.page9_png)
    page10 = Image.open(args.page10_png)

    # Coordinates are for 1224 x 1584 letter pages rendered at 144 dpi.
    page9.crop((235, 480, 1005, 1220)).save(
        output_dir / "induction_and_unboundedness_crop.png"
    )
    page10.crop((235, 545, 1005, 755)).save(
        output_dir / "open_problem_crop.png"
    )


if __name__ == "__main__":
    main()
