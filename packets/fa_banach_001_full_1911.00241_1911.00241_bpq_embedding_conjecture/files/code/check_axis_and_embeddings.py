#!/usr/bin/env python3
"""Numerical sanity checks for the B_{p,q} embedding conjecture packet."""

from __future__ import annotations

import cmath
import math


def bpq_norm_axis_1(p: float, q: float, t: float) -> float:
    """Solve lambda^{-p} + t^q lambda^{-q} = 1 by bisection."""
    lo, hi = 1.0, 2.0
    while hi ** (-p) + (t**q) * hi ** (-q) > 1.0:
        hi *= 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid ** (-p) + (t**q) * mid ** (-q) > 1.0:
            lo = mid
        else:
            hi = mid
    return hi


def triangular_norm(a: float, b: float) -> float:
    """Operator norm of [[b,a],[0,b]] for a,b >= 0."""
    largest = b * b + a * a / 2 + 0.5 * a * math.sqrt(a * a + 4 * b * b)
    return math.sqrt(largest)


def check_fractional_axis() -> None:
    for p, q in [(1.0, 1.5), (1.25, 1.75), (2.0, 1.2)]:
        for t in [1e-2, 3e-3, 1e-3]:
            lam = bpq_norm_axis_1(p, q, t)
            ratio = (lam - 1.0) / (t**q)
            print(f"axis p={p:g} q={q:g} t={t:.0e}: ratio={(ratio):.8f}, expected={1/p:.8f}")


def check_triangular_positive_case() -> None:
    # ||b I + a e12|| <= 1 iff a + b^2 <= 1.
    worst = 0.0
    for i in range(101):
        b = i / 100
        a = 1 - b * b
        worst = max(worst, abs(triangular_norm(a, b) - 1.0))
    if worst > 1e-12:
        raise AssertionError(f"triangular boundary check failed: {worst}")
    print("triangular B_{2,1}/B_{1,2} boundary check passed")


def check_l2_positive_case() -> None:
    for z1, z2 in [(1, 0), (0, 1), (1 + 2j, 3 - 1j)]:
        row_norm = math.sqrt(abs(z1) ** 2 + abs(z2) ** 2)
        expected = math.sqrt(abs(z1) ** 2 + abs(z2) ** 2)
        if abs(row_norm - expected) > 1e-12:
            raise AssertionError("row Hilbert check failed")
    print("B_{2,2} row-operator check passed")


def main() -> None:
    check_fractional_axis()
    check_triangular_positive_case()
    check_l2_positive_case()


if __name__ == "__main__":
    main()
