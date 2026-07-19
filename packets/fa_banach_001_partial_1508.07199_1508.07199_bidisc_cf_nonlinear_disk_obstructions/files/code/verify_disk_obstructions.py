#!/usr/bin/env python3
"""Numerical sanity checks for the nonlinear-disk CF obstructions.

This script is not part of the proof.  It checks two elementary numerical
claims used in the packet:

1. Maximizing |a10 alpha + a02 beta^2| over phases gives |a10|+|a02|.
2. The source example and nearby two-term examples satisfy the source
   D-slice condition but fail the nonlinear-disk condition exactly when
   |a|+|b|>1.
"""

from __future__ import annotations

import cmath
import math
import random


def phase_grid_max(a: complex, b: complex, samples: int = 720) -> float:
    best = 0.0
    for i in range(samples):
        alpha = cmath.exp(2j * math.pi * i / samples)
        for j in range(samples):
            beta = cmath.exp(2j * math.pi * j / samples)
            best = max(best, abs(a * alpha + b * beta * beta))
    return best


def check_phase_maxima() -> None:
    rng = random.Random(150807199)
    for _ in range(20):
        a = (rng.random() - 0.5) + 1j * (rng.random() - 0.5)
        b = (rng.random() - 0.5) + 1j * (rng.random() - 0.5)
        numeric = phase_grid_max(a, b, samples=180)
        exact = abs(a) + abs(b)
        if numeric + 1e-3 < exact:
            raise AssertionError((a, b, numeric, exact))
    print("phase maxima sanity check passed")


def check_two_term_boundary() -> None:
    examples = [
        (1 / math.sqrt(2), 1 / 2),
        (0.4, 0.55),
        (0.4, 0.60),
        (0.8, 0.20),
        (0.8, 0.30),
    ]
    for a, b in examples:
        source_condition = b + a * a <= 1 + 1e-12
        nonlinear_condition = a + b <= 1 + 1e-12
        print(
            f"a={a:.6f} b={b:.6f} "
            f"source={source_condition} nonlinear={nonlinear_condition}"
        )
    assert examples[0][1] + examples[0][0] ** 2 <= 1 + 1e-12
    assert examples[0][0] + examples[0][1] > 1
    print("two-term boundary sanity check passed")


if __name__ == "__main__":
    check_phase_maxima()
    check_two_term_boundary()
