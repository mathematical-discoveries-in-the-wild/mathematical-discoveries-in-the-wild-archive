"""Crop the Section 5 open question from source PDF page 17.

Render the page first from the packet directory with:

    /opt/homebrew/bin/gs -q -dNOPAUSE -dBATCH -sDEVICE=pngalpha \
      -r180 -dFirstPage=17 -dLastPage=17 \
      -sOutputFile=tmp/open_problem_page.png source_paper.pdf
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "open_problem_page.png"
TARGET = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Full text width, with the Section 5 heading, condition (5), and the
    # complete two-line open-question statement. Coordinates are for 180 dpi.
    crop = image.crop((245, 1280, 1290, 1558))
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    crop.save(TARGET)
    print(f"wrote {TARGET}")


if __name__ == "__main__":
    main()
