"""Numerical sanity check for the sharp p=4 example in the packet.

This script samples the l_4^2 unit sphere and checks that the Hadamard
operator H(x, y) = (x + y, x - y) reaches its sampled maximum only near the
four sign choices with |x| = |y| = 2^(-1/4).  The proof in main.tex is exact;
this file is only a regression-style check for arithmetic mistakes.
"""

from __future__ import annotations

import math


def lp4_unit(theta: float) -> tuple[float, float]:
    c = math.cos(theta)
    s = math.sin(theta)
    denom = (abs(c) ** 4 + abs(s) ** 4) ** 0.25
    return c / denom, s / denom


def h_norm4_power(x: float, y: float) -> float:
    return (x + y) ** 4 + (x - y) ** 4


def main() -> None:
    n = 200_000
    vals: list[tuple[float, float, float]] = []
    max_val = -1.0
    for i in range(n):
        theta = 2.0 * math.pi * i / n
        x, y = lp4_unit(theta)
        val = h_norm4_power(x, y)
        vals.append((val, x, y))
        max_val = max(max_val, val)

    expected = 8.0
    if abs(max_val - expected) > 1e-8:
        raise AssertionError(f"sampled max {max_val} differs from {expected}")

    tol = 1e-5
    near = [(x, y) for val, x, y in vals if val > expected - tol]
    target_abs = 2 ** (-0.25)
    for x, y in near:
        if abs(abs(x) - target_abs) > 2e-3 or abs(abs(y) - target_abs) > 2e-3:
            raise AssertionError((x, y))

    print(f"sampled max = {max_val:.12f}")
    print(f"near-max samples = {len(near)}")
    print(f"target absolute coordinate = {target_abs:.12f}")


if __name__ == "__main__":
    main()
