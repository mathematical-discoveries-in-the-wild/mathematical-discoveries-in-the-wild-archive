"""Crop the source theorem and the final relaxation remark from rendered pages."""

from pathlib import Path

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]


def crop(source_name: str, box: tuple[int, int, int, int], output_name: str) -> None:
    source = PACKET / "tmp" / source_name
    output = PACKET / "figures" / output_name
    with Image.open(source) as image:
        cropped = image.crop(box).convert("RGBA")
        flattened = Image.new("RGB", cropped.size, "white")
        flattened.paste(cropped, mask=cropped.getchannel("A"))
        flattened.save(output)


crop(
    "source-theorem-page-01.png",
    (105, 1200, 1225, 1845),
    "source_theorem_crop.png",
)
crop(
    "source-page-01.png",
    (105, 1350, 1225, 1625),
    "open_problem_crop.png",
)
