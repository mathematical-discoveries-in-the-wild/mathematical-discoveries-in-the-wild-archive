import fitz
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[7]  # Source PDF page 8, Remark 3.8.
    clip = fitz.Rect(72, 205, 540, 292)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pix.save(OUT)


if __name__ == "__main__":
    main()
