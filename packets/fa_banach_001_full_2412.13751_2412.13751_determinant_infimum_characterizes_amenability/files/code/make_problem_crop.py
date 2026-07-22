from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tmp" / "source-page-36.png"
target = ROOT / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Keep the full page width and both margins.  The vertical window contains
    # the section context, equation (3.8), and all of Problem 3.7.
    crop = image.crop((0, 250, image.width, 915))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
