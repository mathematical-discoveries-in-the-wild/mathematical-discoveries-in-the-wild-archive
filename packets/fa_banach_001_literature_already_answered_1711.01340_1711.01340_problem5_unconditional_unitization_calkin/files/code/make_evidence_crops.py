#!/usr/bin/env python3
"""Reproduce the evidence crops for this packet."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PACKET = Path(__file__).resolve().parents[1]
CROP = ROOT / "scripts" / "crop_open_problem_from_pdf.py"


def run_crop(*args: str) -> None:
    subprocess.run(
        [
            sys.executable,
            str(CROP),
            *args,
        ],
        check=True,
    )


def main() -> None:
    run_crop(
        "--pdf",
        str(PACKET / "source_paper.pdf"),
        "--output",
        str(PACKET / "figures" / "open_problem_crop.png"),
        "--needle",
        "Problem 5",
        "--needle",
        "unit vector basis of c0",
        "--needle",
        "unitization of X",
        "--pad-x",
        "38",
        "--pad-y",
        "110",
        "--zoom",
        "2.6",
    )
    run_crop(
        "--pdf",
        str(PACKET / "supporting_paper_2401.18037.pdf"),
        "--output",
        str(PACKET / "figures" / "supporting_theorem_crop.png"),
        "--needle",
        "Let U be a Banach space",
        "--needle",
        "unitization of U",
        "--needle",
        "coordinate-wise multiplication",
        "--pad-x",
        "190",
        "--pad-y",
        "145",
        "--zoom",
        "2.2",
    )
    run_crop(
        "--pdf",
        str(PACKET / "supporting_paper_2401.18037.pdf"),
        "--output",
        str(PACKET / "figures" / "supporting_problem5_crop.png"),
        "--needle",
        "Problem 5",
        "--needle",
        "which is indeed true",
        "--needle",
        "Theorem",
        "--pad-x",
        "200",
        "--pad-y",
        "95",
        "--zoom",
        "2.4",
    )


if __name__ == "__main__":
    main()
