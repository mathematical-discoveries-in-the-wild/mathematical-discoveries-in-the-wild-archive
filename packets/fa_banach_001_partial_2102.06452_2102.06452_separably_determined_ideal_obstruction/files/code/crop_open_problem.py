from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(PDF)
page = doc[7]  # PDF page 8
rect = fitz.Rect(55, 475, 545, 680)
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
pix.save(OUT)
print(OUT)

