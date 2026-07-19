from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[8]  # page 9, Remark 1.14
    clip = fitz.Rect(55, 555, 560, 688)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pix.save(OUT)
    print(f"wrote {OUT} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()
