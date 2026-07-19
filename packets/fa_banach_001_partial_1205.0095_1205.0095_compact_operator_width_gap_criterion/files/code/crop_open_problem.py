from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
pdf_path = ROOT / "source_paper.pdf"
out_path = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(pdf_path)
page = doc[17]  # printed page 18, where Problem 8.1 starts
clip = fitz.Rect(0, 600, 612, 790)
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
pix.save(out_path)
print(out_path)
