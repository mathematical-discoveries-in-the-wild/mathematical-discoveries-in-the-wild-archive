from pathlib import Path

import fitz


PACKET = Path(__file__).resolve().parents[1]
PDF = PACKET / "source_paper.pdf"
OUT = PACKET / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[5]  # PDF page 6, introduction, low distortion regime.
    hits = page.search_for("Question 1.3 at distortion 2 remains open")
    if not hits:
        raise SystemExit("open-problem sentence not found")
    rect = hits[0]
    crop = fitz.Rect(45, max(0, rect.y0 - 120), page.rect.width - 45, min(page.rect.height, rect.y1 + 115))
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=crop, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
