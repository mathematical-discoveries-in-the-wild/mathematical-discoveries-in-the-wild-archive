from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(src: str, box: tuple[int, int, int, int], dst: str) -> None:
    image = Image.open(TMP / src)
    image.crop(box).save(FIGURES / dst)


FIGURES.mkdir(exist_ok=True)

# Full readable text width around Carbery's Section 3.3, article p. 106.
crop(
    "carbery_page_106_hi.png",
    (300, 300, 1580, 1265),
    "open_problem_crop.png",
)

# The supporting paper's explicit affirmative answer and Theorem 1.1.
crop(
    "support_page_3_hi.png",
    (320, 380, 1585, 1430),
    "supporting_answer_crop.png",
)
