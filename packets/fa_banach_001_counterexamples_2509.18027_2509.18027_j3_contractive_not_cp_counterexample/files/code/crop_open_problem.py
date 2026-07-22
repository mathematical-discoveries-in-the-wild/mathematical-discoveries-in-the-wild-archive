from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
source = PACKET / "tmp" / "pdfs" / "source_page-21.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Keep the complete lead-in, Conjecture 6.10, and extension formulation.
    crop = image.crop((110, 90, image.width - 110, 930))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
