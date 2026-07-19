from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    target_page = None
    target_y = None
    for page_index, page in enumerate(doc):
        text = page.get_text()
        if "The following four questions are left open" in text:
            target_page = page
            hits = page.search_for("The following four questions are left open")
            target_y = hits[0].y0 if hits else page.rect.height * 0.55
            break
    if target_page is None or target_y is None:
        raise RuntimeError("Could not locate open-question passage")

    rect = target_page.rect
    crop = fitz.Rect(
        rect.x0 + 45,
        max(rect.y0, target_y - 25),
        rect.x1 - 45,
        min(rect.y1, target_y + 155),
    )
    pix = target_page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
