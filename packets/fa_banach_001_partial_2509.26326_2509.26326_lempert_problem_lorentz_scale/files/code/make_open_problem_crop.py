from pathlib import Path

import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = pdfium.PdfDocument(str(PDF))
    page = doc[27]  # PDF page 28, zero-indexed.
    image = page.render(scale=2.5).to_pil()
    width, height = image.size
    crop = image.crop(
        (
            int(0.06 * width),
            int(0.08 * height),
            int(0.95 * width),
            int(0.35 * height),
        )
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUT)


if __name__ == "__main__":
    main()
