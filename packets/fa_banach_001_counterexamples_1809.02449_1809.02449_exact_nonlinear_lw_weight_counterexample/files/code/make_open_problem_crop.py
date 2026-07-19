"""Crop the determinant-weight question from rendered source PDF page 48."""

from pathlib import Path
from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "pdfs" / "source-page-48.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Keep the complete text width and enough vertical context for the full
    # question, including the lead-in and its displayed inequality.
    crop = image.crop((145, 135, 1235, 420))
    crop.save(target)

print(target)
