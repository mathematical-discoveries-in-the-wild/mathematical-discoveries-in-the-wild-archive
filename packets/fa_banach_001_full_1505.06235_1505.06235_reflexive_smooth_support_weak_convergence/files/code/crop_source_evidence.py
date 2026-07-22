#!/usr/bin/env python3
"""Crop concluding open question C from rendered source-paper page 8."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--top", type=int, default=845)
    parser.add_argument("--bottom", type=int, default=1180)
    args = parser.parse_args()

    with Image.open(args.input) as page:
        if not (0 <= args.top < args.bottom <= page.height):
            raise ValueError(
                f"invalid crop ({args.top}, {args.bottom}) for height {page.height}"
            )
        crop = page.crop((0, args.top, page.width, args.bottom))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        crop.save(args.output)
        print(f"saved {args.output} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
