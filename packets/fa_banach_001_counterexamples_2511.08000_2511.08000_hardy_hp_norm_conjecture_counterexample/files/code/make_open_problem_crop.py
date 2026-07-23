#!/usr/bin/env python3
"""Crop the full-width Conjecture 4.3 region from a 300-dpi page render."""

from pathlib import Path

from PIL import Image


packet = Path(__file__).resolve().parents[1]
source = packet / "tmp" / "pdfs" / "source_page300-12.png"
destination = packet / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Preserve both text margins and the complete conjecture plus its immediate
    # introduction and following continuity sentence.
    crop = image.crop((190, 680, 2360, 1055))
    crop.save(destination)

print(destination)
