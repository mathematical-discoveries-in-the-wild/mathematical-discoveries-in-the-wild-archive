from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    # Page 25 in the arXiv PDF contains the paragraph asking for the exact
    # constants c_n, c and for dichotomy of S_{L_p}.
    page = doc[24]
    # Full-width crop around the open-question paragraph and the following
    # explanatory note.
    rect = fitz.Rect(55, 315, 557, 420)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
