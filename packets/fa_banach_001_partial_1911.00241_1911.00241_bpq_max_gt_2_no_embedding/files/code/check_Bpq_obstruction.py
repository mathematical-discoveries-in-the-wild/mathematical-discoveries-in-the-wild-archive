#!/usr/bin/env python3
"""Sanity checks for the B_{p,q} partial non-embedding packet."""

from __future__ import annotations

import math


def witness_non_contraction(p: float, q: float, c: float) -> tuple[float, float, float]:
    """Return (x,y,value) with x^p+y^q=1 and x^2+c^2 y^2>1."""
    for k in range(1, 80):
        y = 10.0 ** (-k / 4)
        x = (1.0 - y**q) ** (1.0 / p)
        value = x * x + c * c * y * y
        if value > 1.0:
            return x, y, value
    raise AssertionError(f"no witness found for p={p}, q={q}, c={c}")


def triangular_norm(a: float, b: float) -> float:
    """Operator norm of [[b,a],[0,b]] for a,b >= 0."""
    largest_eigenvalue = b * b + a * a / 2 + 0.5 * a * math.sqrt(a * a + 4 * b * b)
    return math.sqrt(largest_eigenvalue)


def check_positive_B12_grid() -> None:
    """Check ||bI+a e12||=1 on the boundary a+b^2=1."""
    worst = 0.0
    for i in range(101):
        b = i / 100
        a = 1 - b * b
        worst = max(worst, abs(triangular_norm(a, b) - 1.0))
    if worst > 1e-12:
        raise AssertionError(f"unexpected triangular norm error {worst}")


def main() -> None:
    # These are only floating-point sanity checks.  The proof covers every
    # q>2, but q very close to 2 can require witnesses too small to display
    # reliably in double precision.
    for p, q in [(1, 3), (2, 3), (1.5, 4), (10, 5)]:
        for c in [1.0, 0.5, 0.1]:
            x, y, value = witness_non_contraction(p, q, c)
            print(f"p={p:4g} q={q:4g} c={c:4g}: y={y:.3e}, x={x:.12f}, x^2+c^2y^2={value:.12f}")
    check_positive_B12_grid()
    print("triangular B_{1,2} sanity check passed")


if __name__ == "__main__":
    main()
