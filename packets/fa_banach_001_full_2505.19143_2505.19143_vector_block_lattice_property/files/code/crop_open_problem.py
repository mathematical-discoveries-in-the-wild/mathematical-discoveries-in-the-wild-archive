from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
page = ROOT / "tmp" / "source_page-26.png"
out = ROOT / "figures" / "open_problem_crop.png"

im = Image.open(page)
crop = im.crop((115, 135, 1085, 705))
out.parent.mkdir(parents=True, exist_ok=True)
crop.save(out)
print(out)
