"""Render source crops for the tau_infty density question.

Run from the packet directory:

    python code/crop_open_problem.py
"""

from pathlib import Path

import fitz


PACKET_DIR = Path(__file__).resolve().parents[1]
SOURCE = PACKET_DIR / "source_paper.pdf"
FIGURES = PACKET_DIR / "figures"


def render(page, rect, name):
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    out = FIGURES / name
    out.parent.mkdir(parents=True, exist_ok=True)
    pix.save(out)
    print(f"wrote {out} ({pix.width}x{pix.height})")


def main() -> None:
    doc = fitz.open(SOURCE)
    # PDF page 10: Theorem 3.8 statement and its tau_cc density condition.
    render(doc[9], fitz.Rect(50, 535, 562, 742), "theorem_context_crop.png")
    # PDF page 12: the explicit tau_infty open question after Theorem 3.8.
    render(doc[11], fitz.Rect(50, 72, 562, 162), "open_problem_crop.png")
    # PDF page 8: the source's quoted existence of spaces without p-OAP.
    render(doc[7], fitz.Rect(50, 503, 562, 590), "source_non_poap_crop.png")


if __name__ == "__main__":
    main()
