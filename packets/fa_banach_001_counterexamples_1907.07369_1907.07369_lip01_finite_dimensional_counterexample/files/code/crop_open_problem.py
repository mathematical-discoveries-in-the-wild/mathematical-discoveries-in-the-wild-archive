from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
pdf_path = ROOT / "source_paper.pdf"
out_path = ROOT / "figures" / "problem_4_5_crop.png"

doc = fitz.open(pdf_path)
page = doc[7]  # PDF page 8, where Problems 4 and 5 appear.
clip = fitz.Rect(85, 220, 550, 305)
pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
pix.save(out_path)
print(out_path)
