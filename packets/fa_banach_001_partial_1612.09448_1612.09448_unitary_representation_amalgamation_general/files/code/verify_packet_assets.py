"""Reproduce the source-question crop for the packet.

This script is an asset verifier, not a proof checker.
Run from the repository root:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/partial/1612.09448_unitary_representation_amalgamation_general/code/verify_packet_assets.py
"""

from pathlib import Path

import fitz


PACKET = Path(
    "runs/fa_banach_001/solutions/partial/"
    "1612.09448_unitary_representation_amalgamation_general"
)
PDF = PACKET / "source_paper.pdf"
CROP = PACKET / "figures" / "open_problem_crop.png"

NEEDLES = [
    "Of special interest is whether one can amalgamate unitary representations",
    "Does there exist an amalgam of these",
    "Does this problem have a positive answer",
]


def main() -> None:
    doc = fitz.open(PDF)
    matches = []
    for index, page in enumerate(doc):
        text = page.get_text()
        if all(needle in text for needle in NEEDLES):
            matches.append(index)
    if matches != [20]:
        raise SystemExit(f"expected one match on PDF page 21, got {matches}")

    page = doc[20]
    clip = fitz.Rect(36, 348, 566, 482)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False)
    pix.save(CROP)
    print(f"verified question text on page 21 and wrote {CROP}")


if __name__ == "__main__":
    main()
