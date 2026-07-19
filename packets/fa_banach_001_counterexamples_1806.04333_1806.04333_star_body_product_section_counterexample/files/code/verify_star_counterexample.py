#!/usr/bin/env python3
"""Exact verifier for the thin-cross star-body counterexample."""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def interval_area(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    """Integral of 1_|u|<=a 1_|v|<=b 1_|u+v|<=c."""
    t, s, r = sorted((a, b, c))
    if r >= s + t:
        return 4 * s * t
    return 2 * (r * s + r * t + s * t) - (r * r + s * s + t * t)


def exact_integral(delta: Fraction) -> Fraction:
    # Rectangles are (x radius, y radius, inclusion-exclusion sign).
    rectangles = {
        "H": (Fraction(1), delta, Fraction(1)),
        "V": (delta, Fraction(1), Fraction(1)),
        "S": (delta, delta, Fraction(-1)),
    }
    total = Fraction(0)
    for ax, ay, sign_a in rectangles.values():
        for bx, by, sign_b in rectangles.values():
            for cx, cy, sign_c in rectangles.values():
                total += (
                    sign_a * sign_b * sign_c
                    * interval_area(ax, bx, cx)
                    * interval_area(ay, by, cy)
                )
    return total


def ratio_value(delta: np.ndarray) -> np.ndarray:
    integral = 18 * delta**2 + 24 * delta**3 - 39 * delta**4
    area = 8 * delta - 4 * delta**2
    return 3 * integral / area**2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", required=True, type=Path)
    args = parser.parse_args()

    delta = Fraction(1, 100)
    integral = exact_integral(delta)
    closed_form = 18 * delta**2 + 24 * delta**3 - 39 * delta**4
    area = 8 * delta - 4 * delta**2
    section = 3 * integral
    ratio = section / area**2

    assert integral == closed_form
    assert integral == Fraction(182361, 100000000)
    assert area == Fraction(199, 2500)
    assert ratio == Fraction(547083, 633616)
    assert ratio < 1

    args.figure.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.3))

    d = float(delta)
    axes[0].add_patch(Rectangle((-1, -d), 2, 2 * d,
                                facecolor="#2f6690", alpha=0.72,
                                edgecolor="#173b57"))
    axes[0].add_patch(Rectangle((-d, -1), 2 * d, 2,
                                facecolor="#70a65b", alpha=0.72,
                                edgecolor="#315628"))
    axes[0].set_xlim(-1.08, 1.08)
    axes[0].set_ylim(-1.08, 1.08)
    axes[0].set_aspect("equal")
    axes[0].set_title(r"Thin cross $K$, $\delta=1/100$")
    axes[0].set_xlabel("first coordinate")
    axes[0].set_ylabel("second coordinate")
    axes[0].grid(alpha=0.18)

    ds = np.linspace(0.001, 0.5, 1000)
    rs = ratio_value(ds)
    axes[1].plot(ds, rs, color="#245985", linewidth=2.3)
    axes[1].axhline(1, color="#b7352d", linestyle="--", linewidth=1.6,
                    label="proposed lower bound")
    axes[1].scatter([d], [float(ratio)], color="#1f7a35", s=55, zorder=4,
                    label=r"$\delta=1/100$: ratio $0.86343$")
    axes[1].set_xlim(0, 0.5)
    axes[1].set_ylim(0.8, 1.75)
    axes[1].set_xlabel(r"cross thickness $\delta$")
    axes[1].set_ylabel(r"$|K^3\cap H_{\rm diag}|/|K|^2$")
    axes[1].set_title("Exact diagonal-section ratio")
    axes[1].grid(alpha=0.2)
    axes[1].legend(loc="lower right")

    fig.tight_layout()
    fig.savefig(args.figure, dpi=180)
    plt.close(fig)

    print(f"delta={delta}")
    print(f"area={area} ({float(area):.12f})")
    print(f"convolution_integral={integral} ({float(integral):.12f})")
    print(f"section_volume={section} ({float(section):.12f})")
    print(f"ratio={ratio} ({float(ratio):.12f})")
    print(f"closed_form_match={integral == closed_form}")
    print(f"figure={args.figure}")
    print("PASS")


if __name__ == "__main__":
    main()

