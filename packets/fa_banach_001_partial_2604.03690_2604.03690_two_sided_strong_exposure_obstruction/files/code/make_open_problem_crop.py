from pathlib import Path

import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[6]  # PDF page 7, where the complex-reflexive open problem appears.
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    tmp = ROOT / "tmp" / "page7_full.png"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    pix.save(tmp)

    image = Image.open(tmp)
    # Full page width, covering the preceding LMP proposition and the open problem.
    crop = image.crop((0, 90, image.width, 520))
    crop.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
