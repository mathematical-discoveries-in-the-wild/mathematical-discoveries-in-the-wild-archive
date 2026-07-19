from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    # Page 7 of the source PDF contains Section 5 and Conjectures 5.1--5.2.
    page = doc[6]
    clip = fitz.Rect(55, 70, 535, 515)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.6, 2.6), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
