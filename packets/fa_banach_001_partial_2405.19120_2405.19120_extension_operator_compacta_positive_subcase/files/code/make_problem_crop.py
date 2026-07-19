from __future__ import annotations

import json
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"
META = ROOT / "figures" / "open_problem_crop.json"


def main() -> None:
    doc = fitz.open(PDF)
    needle = "Does C(βω × βω) contain a complemented isomorphic copy"
    fallback = "Does C(βω"

    match_page = None
    match_rects = []
    for page_index, page in enumerate(doc):
        rects = page.search_for(needle)
        if not rects:
            rects = page.search_for(fallback)
        if rects:
            match_page = page_index
            match_rects = rects
            break

    if match_page is None:
        raise SystemExit("Problem text was not found in the PDF")

    page = doc[match_page]
    union = match_rects[0]
    for rect in match_rects[1:]:
        union |= rect

    # Full readable width; enough vertical context for the preceding paragraph,
    # the problem label, and the following one-sentence general variant.
    crop = fitz.Rect(
        48,
        max(0, union.y0 - 95),
        page.rect.width - 48,
        min(page.rect.height, union.y1 + 95),
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)

    META.write_text(
        json.dumps(
            {
                "source_pdf": str(PDF),
                "output": str(OUT),
                "page_index_zero_based": match_page,
                "page_number_one_based": match_page + 1,
                "crop": [crop.x0, crop.y0, crop.x1, crop.y1],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
