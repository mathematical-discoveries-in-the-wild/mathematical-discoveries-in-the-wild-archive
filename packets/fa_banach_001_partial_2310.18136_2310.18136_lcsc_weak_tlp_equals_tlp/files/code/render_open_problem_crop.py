from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
pdf = ROOT / "source_paper.pdf"
out = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(pdf)
page = doc[14]
rect = fitz.Rect(40, 610, 555, 715)
pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect, alpha=False)
pix.save(out)
print(out)
