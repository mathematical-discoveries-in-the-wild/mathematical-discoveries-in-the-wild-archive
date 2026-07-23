#!/usr/bin/env python3
"""Render PDF page 14 and crop the complete concluding open question."""

from pathlib import Path

import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = pdfium.PdfDocument(PDF)
    page = doc[13]  # zero-based: PDF page 14
    image = page.render(scale=2.5).to_pil()
    # Full readable width; retain the end of the preceding proof, the complete
    # Section 6 heading/question, and enough following context to show closure.
    left = 55
    right = image.width - 55
    top = int(image.height * 0.48)
    bottom = int(image.height * 0.88)
    image.crop((left, top, right, bottom)).save(OUT)
    print(f"wrote {OUT} ({right-left}x{bottom-top})")


if __name__ == "__main__":
    main()
