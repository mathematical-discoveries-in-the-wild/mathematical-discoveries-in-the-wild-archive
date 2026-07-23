#!/usr/bin/env python3
"""Create readable full-text-width crops of the source target passages.

Run from the packet directory after rendering source PDF pages 29 and 31 at
180 dpi as tmp/source_page-29.png and tmp/source_page-31.png.
"""

from pathlib import Path

from PIL import Image


PACKET_DIR = Path(__file__).resolve().parent.parent


def crop(source_name: str, box: tuple[int, int, int, int], output_name: str) -> None:
    source_path = PACKET_DIR / "tmp" / source_name
    output_path = PACKET_DIR / "figures" / output_name
    with Image.open(source_path) as image:
        image.crop(box).save(output_path)


def main() -> None:
    # The x-coordinates retain margins beyond the complete source text block.
    crop(
        "source_page-29.png",
        (170, 110, 1320, 660),
        "theorem1_negative_moment_context_page29.png",
    )
    crop(
        "source_page-31.png",
        (170, 0, 1320, 675),
        "open_problem_crop.png",
    )


if __name__ == "__main__":
    main()
