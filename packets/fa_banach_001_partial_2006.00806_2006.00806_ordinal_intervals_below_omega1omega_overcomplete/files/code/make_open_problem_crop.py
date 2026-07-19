from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "tmp" / "source_page-25.png"
dst = ROOT / "figures" / "open_problem_crop.png"

im = Image.open(src)
# Full-width crop around Question 48 and the following source context.
crop = im.crop((245, 1368, 1135, 1738))
crop.save(dst)
print(dst)
