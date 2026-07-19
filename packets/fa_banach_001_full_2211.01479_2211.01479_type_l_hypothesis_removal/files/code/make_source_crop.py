"""Render the open-question passage from page 16 of the source PDF."""

from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE)
    page = document[15]  # one-based PDF page 16
    clip = fitz.Rect(60, 122, 538, 246)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(OUTPUT)
    print(f"wrote {OUTPUT} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()
