from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-31.png"
OUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    # Crop the conclusion paragraph containing the SEP/simplicial-cone conjecture.
    crop = image.crop((65, 850, 970, 1025))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    crop.save(OUT)


if __name__ == "__main__":
    main()
