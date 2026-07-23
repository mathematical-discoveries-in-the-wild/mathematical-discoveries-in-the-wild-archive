#!/usr/bin/env python3
"""Render source PDF page 26 and crop Questions 4.7--4.9."""

from pathlib import Path

import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_questions_crop.png"


def main() -> None:
    doc = pdfium.PdfDocument(PDF)
    page = doc[25]  # zero-based: PDF page 26
    image = page.render(scale=2.5).to_pil()
    left = 65
    right = image.width - 65
    top = int(image.height * 0.39)
    bottom = int(image.height * 0.94)
    image.crop((left, top, right, bottom)).save(OUT)
    print(f"wrote {OUT} ({right-left}x{bottom-top})")


if __name__ == "__main__":
    main()

