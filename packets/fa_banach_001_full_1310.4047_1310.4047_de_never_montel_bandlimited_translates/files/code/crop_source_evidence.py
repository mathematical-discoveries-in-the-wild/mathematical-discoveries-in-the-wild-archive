#!/usr/bin/env python3
"""Crop Remark 6 from a rendered image of source-paper page 17.

Render page 17 at 180 dpi before running this script.  The default crop keeps
the full page width and enough vertical context to include all of Remark 6.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--top", type=int, default=1260)
    parser.add_argument("--bottom", type=int, default=1645)
    args = parser.parse_args()

    with Image.open(args.input) as page:
        if not (0 <= args.top < args.bottom <= page.height):
            raise ValueError(
                f"invalid vertical crop ({args.top}, {args.bottom}) "
                f"for image height {page.height}"
            )
        crop = page.crop((0, args.top, page.width, args.bottom))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        crop.save(args.output)
        print(f"saved {args.output} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
