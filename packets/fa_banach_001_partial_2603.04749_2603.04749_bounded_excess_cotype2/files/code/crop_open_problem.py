from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "tmp" / "open_problem_page-08.png"
dst = ROOT / "figures" / "open_problem_crop.png"

im = Image.open(src)
im.crop((120, 585, 1415, 1188)).save(dst)
print(dst)
