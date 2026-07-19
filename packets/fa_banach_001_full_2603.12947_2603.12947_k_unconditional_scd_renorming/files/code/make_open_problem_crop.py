#!/usr/bin/env python3
"""Reproduce the open-question screenshot crop for arXiv:2603.12947."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
PACKET = ROOT / "runs/fa_banach_001/solutions/full/2603.12947_k_unconditional_scd_renorming"


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/crop_open_problem_from_pdf.py"),
            "--pdf",
            str(PACKET / "source_paper.pdf"),
            "--output",
            str(PACKET / "figures/open_problem_crop.png"),
            "--needle",
            "Question 5.4",
            "--needle",
            "k-unconditional",
            "--zoom",
            "3",
            "--pad-x",
            "300",
            "--pad-y",
            "145",
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
