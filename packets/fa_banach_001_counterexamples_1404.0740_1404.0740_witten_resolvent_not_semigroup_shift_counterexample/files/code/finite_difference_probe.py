#!/usr/bin/env python3
"""Numerical probe for the log-kernel separation used in the packet.

This is not part of the proof.  It checks one high-order finite-difference
block for the heat step E(x)=1-exp(-exp(x)) and the resolvent step
R(x)=1/(1+exp(-x)).
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def heat_step(x: np.ndarray) -> np.ndarray:
    out = np.ones_like(x, dtype=float)
    mask = x < 50
    out[mask] = 1.0 - np.exp(-np.exp(x[mask]))
    return out


def resolvent_step(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, 1.0 / (1.0 + np.exp(-x)), np.exp(x) / (1.0 + np.exp(x)))


def finite_difference_values(kind: str, order: int, spacing: float, grid: np.ndarray) -> np.ndarray:
    kernel = heat_step if kind == "heat" else resolvent_step
    values = np.zeros_like(grid)
    for j in range(order + 1):
        coeff = (-1) ** (order - j) * math.comb(order, j)
        values += coeff * kernel(grid - j * spacing)
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=33)
    parser.add_argument("--spacing", type=float, default=0.178)
    parser.add_argument("--points", type=int, default=120_001)
    args = parser.parse_args()

    left = -10.0
    right = args.order * args.spacing + 10.0
    grid = np.linspace(left, right, args.points)
    heat = finite_difference_values("heat", args.order, args.spacing, grid)
    resolvent = finite_difference_values("resolvent", args.order, args.spacing, grid)
    heat_sup = float(np.max(np.abs(heat)))
    resolvent_sup = float(np.max(np.abs(resolvent)))
    heat_arg = float(grid[int(np.argmax(np.abs(heat)))])

    print(f"order={args.order}")
    print(f"spacing={args.spacing}")
    print(f"heat_sup={heat_sup:.12g}")
    print(f"heat_argmax={heat_arg:.12g}")
    print(f"resolvent_sup={resolvent_sup:.12g}")
    print(f"ratio_heat_to_resolvent={heat_sup / resolvent_sup:.12g}")


if __name__ == "__main__":
    main()
