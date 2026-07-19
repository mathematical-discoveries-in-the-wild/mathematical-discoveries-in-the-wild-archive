"""Crop the open-question passage from rendered page 148 of the source PDF."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "tmp" / "source_page-148.png"
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


with Image.open(SOURCE) as image:
    # Includes the multi-cycle motivation, proposed repair statement, and the
    # sentence declaring the question open.
    crop = image.crop((105, 805, 1225, 1515))
    crop.save(OUTPUT)

print(OUTPUT)
