from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)


def main() -> None:
    doc = fitz.open(ROOT / "source_paper.pdf")
    page = doc[9]  # printed page 10, Remark 3.15
    clip = fitz.Rect(0, 535, page.rect.width, 635)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pix.save(FIGURES / "open_problem_crop.png")
    print("Wrote", FIGURES / "open_problem_crop.png")


if __name__ == "__main__":
    main()
