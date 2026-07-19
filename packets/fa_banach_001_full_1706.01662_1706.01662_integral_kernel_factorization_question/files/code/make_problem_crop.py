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
    needles = [
        "It is a natural question whether this implies",
        "However we haven",
    ]

    match_page = None
    rects = []
    for page_index, page in enumerate(doc):
        found = []
        for needle in needles:
            found.extend(page.search_for(needle))
        if len(found) >= 2:
            match_page = page_index
            rects = found
            break

    if match_page is None:
        raise SystemExit("Could not find the source question in the PDF")

    page = doc[match_page]
    union = rects[0]
    for rect in rects[1:]:
        union |= rect

    crop = fitz.Rect(
        42,
        max(0, union.y0 - 130),
        page.rect.width - 42,
        min(page.rect.height, union.y1 + 105),
    )
    pix = page.get_pixmap(matrix=fitz.Matrix(2.8, 2.8), clip=crop, alpha=False)
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
