from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
pdf_path = ROOT / "source_paper.pdf"
out_path = ROOT / "figures" / "open_problem_crop.png"

doc = fitz.open(pdf_path)
page = doc[2]  # PDF page 3, source Remark 1.7.

# Crop the paragraph beginning "One major dissemblance..." through the
# commutant question. Coordinates are PDF points.
clip = fitz.Rect(55, 410, 555, 488)
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
pix.save(out_path)
print(out_path)
