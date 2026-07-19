#!/usr/bin/env python3
"""Generate evidence crops for the Halbeisen--Odell literature-status packet."""

from __future__ import annotations

from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"


def crop(pdf_name: str, page_index: int, rect: tuple[float, float, float, float], out_name: str) -> None:
    doc = fitz.open(ROOT / pdf_name)
    page = doc.load_page(page_index)
    clip = fitz.Rect(*rect)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=clip, alpha=False)
    out = FIGURES / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    pix.save(out)
    print(f"{out_name}: page={page_index + 1}, crop_points={tuple(round(v, 2) for v in clip)}")


def main() -> None:
    crop(
        "source_paper.pdf",
        30,
        (40, 410, 572, 535),
        "open_problem_crop.png",
    )
    crop(
        "supporting_paper_2106.12323.pdf",
        0,
        (95, 195, 520, 305),
        "supporting_abstract_complete_answer_crop.png",
    )
    crop(
        "supporting_paper_2106.12323.pdf",
        1,
        (85, 112, 530, 250),
        "supporting_problem_restatement_crop.png",
    )
    crop(
        "supporting_paper_2106.12323.pdf",
        2,
        (75, 675, 545, 755),
        "supporting_theorem_1_4_crop.png",
    )


if __name__ == "__main__":
    main()
