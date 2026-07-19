from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(SOURCE)
    page = doc[45]  # rendered page 46, where the final question/goal appears
    clip = fitz.Rect(72, 230, 552, 452)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)


if __name__ == "__main__":
    main()
