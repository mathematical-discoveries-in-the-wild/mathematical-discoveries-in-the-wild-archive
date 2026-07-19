#!/usr/bin/env python3
"""Crop the general-case open-problem paragraph from PDF page 4."""

from pathlib import Path
import sys

from PIL import Image


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: make_open_problem_crop.py INPUT_PNG OUTPUT_PNG")
    source = Path(sys.argv[1])
    output = Path(sys.argv[2])
    with Image.open(source) as image:
        crop = image.crop((185, 1225, 1515, 1680))
        output.parent.mkdir(parents=True, exist_ok=True)
        crop.save(output)


if __name__ == "__main__":
    main()
