"""Render a crop of the final open-question list from the source PDF."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_question_i_crop.png"
NEEDLE = "Is it possible to find an infinite compact set"


def main() -> None:
    doc = fitz.open(PDF)
    for page_index, page in enumerate(doc):
        matches = page.search_for(NEEDLE)
        if not matches:
            continue
        rect = matches[0]
        crop = fitz.Rect(40, max(0, rect.y0 - 90), page.rect.width - 40, min(page.rect.height, rect.y1 + 170))
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
        pix.save(OUT)
        print(f"saved {OUT} from page {page_index + 1}")
        return
    raise SystemExit(f"could not find question text: {NEEDLE!r}")


if __name__ == "__main__":
    main()
