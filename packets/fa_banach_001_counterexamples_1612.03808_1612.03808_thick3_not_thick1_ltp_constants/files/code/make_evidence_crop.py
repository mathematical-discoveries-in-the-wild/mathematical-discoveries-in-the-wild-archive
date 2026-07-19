from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    page = doc[5]
    rect = fitz.Rect(38, 265, 574, 720)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
