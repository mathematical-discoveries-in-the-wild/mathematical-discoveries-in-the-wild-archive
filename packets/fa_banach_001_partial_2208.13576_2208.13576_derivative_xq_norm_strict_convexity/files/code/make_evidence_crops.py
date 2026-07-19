from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp"
FIGURES = ROOT / "figures"


def crop(src_name: str, box: tuple[int, int, int, int], out_name: str) -> None:
    image = Image.open(TMP / src_name)
    FIGURES.mkdir(parents=True, exist_ok=True)
    image.crop(box).save(FIGURES / out_name)


def main() -> None:
    crop(
        "source_page-06.png",
        (170, 705, 880, 1095),
        "open_problem_crop.png",
    )
    crop(
        "source_page-08.png",
        (165, 380, 920, 735),
        "self_adjoint_modification_crop.png",
    )


if __name__ == "__main__":
    main()
