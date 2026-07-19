#!/usr/bin/env python3
"""Reproduce the two source-evidence crops from rendered source pages."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
TMP = PACKET / "tmp" / "pdfs"
FIGURES = PACKET / "figures"


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)

    page3 = Image.open(TMP / "source_page_3.png").convert("RGB")
    question = page3.crop((125, 980, 1365, 1410))
    question.save(FIGURES / "open_problem_crop.png", quality=95)

    page29 = Image.open(TMP / "source_endpoint-29.png").convert("RGB")
    page30 = Image.open(TMP / "source_endpoint-30.png").convert("RGB")
    bottom29 = page29.crop((125, 1495, 1365, 1635))
    top30 = page30.crop((315, 330, 1310, 660))

    gap = 22
    width = max(bottom29.width, top30.width)
    stitched = Image.new("RGB", (width, bottom29.height + gap + top30.height), "white")
    stitched.paste(bottom29, (0, 0))
    stitched.paste(top30, ((width - top30.width) // 2, bottom29.height + gap))
    stitched.save(FIGURES / "same_hypotheses_remark_crop.png", quality=95)


if __name__ == "__main__":
    main()
