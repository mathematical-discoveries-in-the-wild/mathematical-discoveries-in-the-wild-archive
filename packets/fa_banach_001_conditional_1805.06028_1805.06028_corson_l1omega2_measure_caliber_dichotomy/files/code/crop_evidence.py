#!/usr/bin/env python3
"""Reproduce the source open-problem crop for the packet."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page_index = None
    for index, page in enumerate(doc):
        text = page.get_text()
        if "Is the existence of a Corson compact" in text:
            page_index = index
            break
    if page_index is None:
        page_index = 10

    page = doc[page_index]
    rects = page.search_for("Is the existence of a Corson compact")
    clip = rects[0] if rects else fitz.Rect(60, 250, 560, 470)
    clip = fitz.Rect(50, max(0, clip.y0 - 80), 562, min(page.rect.height, clip.y1 + 120))
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT} from page {page_index + 1}")


if __name__ == "__main__":
    main()
