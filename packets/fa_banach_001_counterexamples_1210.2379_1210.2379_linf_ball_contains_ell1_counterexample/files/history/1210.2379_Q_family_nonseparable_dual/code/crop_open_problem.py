"""Render the Problem 1 crop from arXiv:1210.2379.

Run from the repository root:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/1210.2379_linf_ball_contains_ell1_counterexample/history/1210.2379_Q_family_nonseparable_dual/code/crop_open_problem.py
"""

from pathlib import Path

import fitz


ROOT = Path("runs/fa_banach_001/solutions/counterexamples/1210.2379_linf_ball_contains_ell1_counterexample/history/1210.2379_Q_family_nonseparable_dual")
PDF = ROOT / "source_paper.pdf"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    doc = fitz.open(PDF)
    # The paper has 47 PDF pages; Problem 1 appears on displayed page 45.
    page = doc[44]
    # Points in the original 612 x 792 page. This keeps the full text width and
    # enough vertical height for Problem 1 and the following ball-family remark.
    clip = fitz.Rect(45, 94, 567, 318)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pix.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
