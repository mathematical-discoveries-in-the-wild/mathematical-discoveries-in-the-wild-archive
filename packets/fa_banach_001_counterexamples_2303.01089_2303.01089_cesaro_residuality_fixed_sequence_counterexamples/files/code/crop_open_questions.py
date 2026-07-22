#!/usr/bin/env python3
"""Crop the two source-page regions used in the review packet."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"


def crop(source: str, box: tuple[int, int, int, int], target: str) -> None:
    image = Image.open(TMP / source)
    image.crop(box).save(FIGURES / target)


# Full readable text width is retained. Page 28 gives the definition of
# G''_{p,(c_n)}; page 29 contains Questions 5.6 and 5.9 and the definition of
# G''_{A,B}.
crop(
    "source_page-28.png",
    (135, 1400, 1405, 1935),
    "question_5_6_definition_crop.png",
)
crop(
    "source_page-29.png",
    (135, 185, 1405, 1535),
    "questions_5_6_5_9_crop.png",
)

