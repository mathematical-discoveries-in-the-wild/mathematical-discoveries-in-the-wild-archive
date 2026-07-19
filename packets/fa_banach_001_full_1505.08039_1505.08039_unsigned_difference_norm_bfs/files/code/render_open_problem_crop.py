"""Render the open-problem crop for the 1505.08039 packet.

Run from the repository root with:
    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/full/1505.08039_unsigned_difference_norm_bfs/code/render_open_problem_crop.py
"""

from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[6]
PDF = ROOT / "data/raw/arxiv/1505.08039/paper.pdf"
OUT = (
    ROOT
    / "runs/fa_banach_001/solutions/full/1505.08039_unsigned_difference_norm_bfs/figures/open_problem_crop.png"
)

doc = fitz.open(PDF)
page = doc[23]  # PDF page 24, where Corollary 4.9 and Remark 4.10 appear.
rect = fitz.Rect(36, 350, 576, 690)
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
pix.save(OUT)
print(f"wrote {OUT} ({pix.width}x{pix.height})")
