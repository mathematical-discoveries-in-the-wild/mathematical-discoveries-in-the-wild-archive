"""Render the open-problem crop from the source PDF.

Run from the packet directory:

    python code/crop_open_problem.py
"""

from pathlib import Path

import fitz


PACKET_DIR = Path(__file__).resolve().parents[1]
SOURCE = PACKET_DIR / "source_paper.pdf"
OUTPUT = PACKET_DIR / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    # PDF page 24 contains the paragraph immediately after Theorem 5.2.
    page = doc[23]
    # Full readable width, enough vertical height to include the complete
    # open-problem paragraph and the following transition line.
    clip = fitz.Rect(52, 525, 560, 653)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()
