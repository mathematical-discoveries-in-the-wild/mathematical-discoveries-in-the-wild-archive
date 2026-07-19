#!/usr/bin/env python3
"""Crop the exact unresolved two-dimensional weak L-P paragraph."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source-page-08.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Includes the end of Theorem 2.10 for context, the complete open paragraph,
    # and the start of the higher-dimensional contrast.
    crop = image.crop((235, 735, 1315, 1045))
    crop.save(target, optimize=True)

print(target)
