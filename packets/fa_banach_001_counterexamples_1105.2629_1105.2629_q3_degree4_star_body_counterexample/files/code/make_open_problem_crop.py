"""Render and crop Question 3 from the source PDF."""

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main():
    doc = fitz.open(SOURCE)
    hit_page = None
    hit_rect = None
    for page_index, page in enumerate(doc):
        hits = page.search_for("Question 3")
        if hits:
            hit_page = page_index
            hit_rect = hits[-1]
    if hit_page is None:
        raise RuntimeError("Could not find Question 3 in source_paper.pdf")

    page = doc[hit_page]
    rect = page.rect
    top = max(0, hit_rect.y0 - 80)
    bottom = min(rect.y1, hit_rect.y1 + 130)
    crop = fitz.Rect(24, top, rect.x1 - 24, bottom)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.6, 2.6), clip=crop, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT} from page {hit_page + 1}")


if __name__ == "__main__":
    main()
