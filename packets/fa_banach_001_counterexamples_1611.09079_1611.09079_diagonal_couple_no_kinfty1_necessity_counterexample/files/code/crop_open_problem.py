from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(PDF)
page = doc[17]
rect = page.search_for("We do not know whether")[0]
clip = fitz.Rect(35, max(0, rect.y0 - 55), page.rect.width - 35, min(page.rect.height, rect.y1 + 85))
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
pix.save(OUT)
print(OUT)
