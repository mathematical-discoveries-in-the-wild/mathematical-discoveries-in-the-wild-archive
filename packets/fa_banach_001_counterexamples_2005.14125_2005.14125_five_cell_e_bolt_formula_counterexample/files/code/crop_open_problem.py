#!/usr/bin/env python3
"""Crop Theorem 3.8 and the e-bolt conjecture from rendered source pages."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
TMP = PACKET / "tmp"
FIGURES = PACKET / "figures"


def crop(source: str, box: tuple[int, int, int, int], target: str) -> None:
    image = Image.open(TMP / source)
    image.crop(box).save(FIGURES / target)


# The source pages were rendered at 160 dpi. Both crops retain the full
# readable text width. The first contains all of Theorem 3.8 and the start of
# Definition 3.2; the second contains the continuation, the exact e-bolt
# enumeration, and the complete conjecture.
crop(
    "source_page-141.png",
    (180, 380, 1210, 1590),
    "theorem_3_8_crop.png",
)
crop(
    "source_page-142.png",
    (180, 170, 1210, 870),
    "e_bolt_conjecture_crop.png",
)

