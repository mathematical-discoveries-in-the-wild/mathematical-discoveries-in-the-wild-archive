"""Render the source-page crop used in the solution packet.

Run from the repository root:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/full/2104.05330_separable_range_auerbach_system/code/render_open_problem_crop.py
"""

from pathlib import Path

import fitz


PACKET = Path(
    "runs/fa_banach_001/solutions/full/"
    "2104.05330_separable_range_auerbach_system"
)
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[2]  # PDF page 3.
    clip = fitz.Rect(50, 185, 562, 365)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pix.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()
