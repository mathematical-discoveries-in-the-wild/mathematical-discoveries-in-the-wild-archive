#!/usr/bin/env python3
"""Crop the closing finite-p question from rendered source PDF page 24."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "source-page-24.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Full readable text width, including comfortable left/right margins.
    crop = image.crop((95, 1178, 1395, 1336))
    crop.save(target)

print(target)
