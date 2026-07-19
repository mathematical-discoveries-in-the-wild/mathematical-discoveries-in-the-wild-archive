#!/usr/bin/env python3
"""Render the Question 3.7 source crop from page 18 of the arXiv PDF."""

from pathlib import Path

import fitz


PACKET_DIR = Path(__file__).resolve().parents[1]
SOURCE_PDF = PACKET_DIR / "source_paper.pdf"
OUTPUT_PNG = PACKET_DIR / "figures" / "open_problem_crop.png"


def main() -> None:
    document = fitz.open(SOURCE_PDF)
    page = document[17]  # PDF page 18, one-based.
    text = page.get_text()
    if "Question 3.7" not in text or "Does there exists" not in text:
        raise RuntimeError("Question 3.7 was not found on the expected source page")

    # Retain the complete readable text width and the lead-in explaining why
    # the question matters, while excluding the unrelated footnote below it.
    clip = fitz.Rect(52, 549, 560, 691)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUTPUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(OUTPUT_PNG)
    print(f"wrote {OUTPUT_PNG} ({pixmap.width}x{pixmap.height})")


if __name__ == "__main__":
    main()
