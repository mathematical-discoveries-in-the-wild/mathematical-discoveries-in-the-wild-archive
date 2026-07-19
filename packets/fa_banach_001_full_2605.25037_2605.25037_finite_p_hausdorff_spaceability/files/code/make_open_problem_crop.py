from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[23]  # PDF page 24, where Question 3.19 appears.
    page_rect = page.rect

    hits = page.search_for("Question 3.19")
    if not hits:
        raise RuntimeError("Could not locate Question 3.19 on source page 24")

    y0 = max(0, hits[0].y0 - 42)
    y1 = min(page_rect.height, hits[0].y1 + 58)
    crop = fitz.Rect(54, y0, page_rect.width - 54, y1)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=crop, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
