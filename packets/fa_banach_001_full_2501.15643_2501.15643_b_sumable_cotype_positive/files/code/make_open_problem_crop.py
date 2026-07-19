from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[11]  # Source PDF page 12, containing Question 3.9.
    rects = page.search_for("Question 3.9")
    if not rects:
        raise RuntimeError("Question 3.9 not found on page 12")
    q = rects[0]
    clip = fitz.Rect(42, q.y0 - 42, 570, q.y1 + 46)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()
