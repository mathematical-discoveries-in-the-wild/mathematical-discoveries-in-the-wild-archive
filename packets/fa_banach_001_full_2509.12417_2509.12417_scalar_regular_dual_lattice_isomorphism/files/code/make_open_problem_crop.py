from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[0]

    # Page 1 contains the lattice version of the Diaz-Dineen question and the
    # source paper's order-continuous-dual sufficient condition.
    clip = fitz.Rect(48, 500, 565, 735)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
