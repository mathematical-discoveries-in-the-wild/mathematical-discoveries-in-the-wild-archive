from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp" / "pdfs"
FIGURES = ROOT / "figures"


def crop(path: Path, box: tuple[int, int, int, int]) -> Image.Image:
    image = Image.open(path).convert("RGB")
    return image.crop(box)


def bordered(image: Image.Image) -> Image.Image:
    return ImageOps.expand(image, border=10, fill="white")


def stack(images: list[Image.Image], gap: int = 18) -> Image.Image:
    width = max(image.width for image in images)
    height = sum(image.height for image in images) + gap * (len(images) - 1)
    out = Image.new("RGB", (width, height), "white")
    y = 0
    for image in images:
        out.paste(image, ((width - image.width) // 2, y))
        y += image.height + gap
    return out


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)

    page15 = TMP / "source_page-15.png"
    page16 = TMP / "source_page-16.png"
    page17 = TMP / "source_page-17.png"

    conjecture_bottom = crop(page15, (105, 1015, 845, 1166))
    conjecture_top = crop(page16, (105, 82, 850, 300))
    open_problem = stack([bordered(conjecture_bottom), bordered(conjecture_top)])
    open_problem.save(FIGURES / "open_problem_crop.png")

    semidirect = crop(page17, (105, 122, 850, 1168))
    bordered(semidirect).save(FIGURES / "semidirect_obstruction_crop.png")


if __name__ == "__main__":
    main()
