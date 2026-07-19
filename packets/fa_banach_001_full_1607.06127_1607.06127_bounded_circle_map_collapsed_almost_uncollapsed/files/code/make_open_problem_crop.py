#!/usr/bin/env python3
"""Render the source-paper crop containing Problem 2.6."""

from pathlib import Path

import fitz


PACKET_DIR = Path(__file__).resolve().parents[1]
PDF_PATH = PACKET_DIR / "source_paper.pdf"
OUT_PATH = PACKET_DIR / "figures" / "open_problem_crop.png"
TMP_PAGE = PACKET_DIR / "tmp" / "source_page8_full.png"


def main() -> None:
    doc = fitz.open(PDF_PATH)
    page = doc[7]
    problem_hits = page.search_for("Problem 2.6")
    next_hits = page.search_for("3. Preservation of cotype")
    if not problem_hits or not next_hits:
        raise RuntimeError("Could not locate Problem 2.6 crop anchors")

    rect = page.rect
    top = max(rect.y0, problem_hits[0].y0 - 18)
    bottom = min(rect.y1, next_hits[0].y0 - 8)
    clip = fitz.Rect(rect.x0 + 34, top, rect.x1 - 34, bottom)
    matrix = fitz.Matrix(2.4, 2.4)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    (PACKET_DIR / "tmp").mkdir(parents=True, exist_ok=True)
    page.get_pixmap(matrix=matrix).save(TMP_PAGE)
    page.get_pixmap(matrix=matrix, clip=clip).save(OUT_PATH)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
