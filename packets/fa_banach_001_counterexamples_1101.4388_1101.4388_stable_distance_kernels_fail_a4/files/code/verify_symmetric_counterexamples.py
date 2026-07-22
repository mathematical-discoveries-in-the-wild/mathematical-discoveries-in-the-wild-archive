#!/usr/bin/env python3
"""Deterministic sanity checks for the analytic A4 counterexamples.

The proof is symbolic.  This script checks its closed formulas at high
precision, reports concrete witness sizes, and directly solves one Gram
system as an independent numerical check.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 80


def best_small_u_ratio(numerator, denominator):
    """Return the largest ratio on a fixed decreasing small-u grid."""
    candidates = []
    for k in range(2, 13):
        u = mp.mpf(10) ** (-k)
        candidates.append((numerator(u) / denominator(u), u))
    return max(candidates)


def p1_cross_polytope(gamma):
    c = mp.power(2, gamma)
    d = 1
    while (2 * d - 1) * c <= 2 * d:
        d += 1
    n = 2 * d
    derivative = (n - 1) * c - n
    ratio, u = best_small_u_ratio(
        lambda z: n * mp.exp(-z),
        lambda z: 1 + (n - 1) * mp.exp(-c * z),
    )
    assert derivative > 0 and ratio > 1
    return d, derivative, u, ratio


def p2_cross_polytope(gamma):
    antipodal = mp.power(2, gamma)
    orthogonal = mp.power(2, gamma / 2)
    d = 1
    while antipodal + (2 * d - 2) * orthogonal <= 2 * d:
        d += 1
    n = 2 * d
    derivative = antipodal + (n - 2) * orthogonal - n
    ratio, u = best_small_u_ratio(
        lambda z: n * mp.exp(-z),
        lambda z: (
            1
            + mp.exp(-antipodal * z)
            + (n - 2) * mp.exp(-orthogonal * z)
        ),
    )
    assert derivative > 0 and ratio > 1
    return d, derivative, u, ratio


N_SCHEDULE = [
    3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 32, 40, 50, 64, 80, 100,
    128, 160, 200, 256, 320, 400, 512, 640, 800, 1024, 1280,
    1600, 2048, 2560, 3200, 4096, 5120, 6400, 8192, 10000,
    12800, 16000, 20000, 25600, 32000, 40000, 50000, 65536,
]


def p2_circle(gamma):
    selected = None
    average = None
    for n in N_SCHEDULE:
        j = np.arange(n, dtype=float)
        average = float(np.mean((2 * np.sin(np.pi * j / n)) ** gamma))
        if average > 1:
            selected = n
            break
    assert selected is not None and average is not None and average > 1
    n = selected
    distances = [
        2 * mp.sin(mp.pi * j / n)
        for j in range(n)
    ]
    derivative = mp.fsum(x**gamma for x in distances) - n
    u = mp.mpf("0.0001")
    ratio = (
        n * mp.exp(-u)
        / mp.fsum(mp.exp(-u * x**gamma) for x in distances)
    )
    assert derivative > 0 and ratio > 1
    return n, average, derivative, u, ratio


def direct_circle_solve():
    gamma = 0.5
    n = 6
    u = 1e-2
    radius = u ** (1 / gamma)
    angles = 2 * np.pi * np.arange(n) / n
    points = radius * np.column_stack([np.cos(angles), np.sin(angles)])
    gram = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            gram[i, j] = math.exp(
                -(np.linalg.norm(points[i] - points[j]) ** gamma)
            )
    rhs = np.full(n, math.exp(-u))
    coeff = np.linalg.solve(gram, rhs)
    residual = np.linalg.norm(gram @ coeff - rhs, ord=np.inf)
    row_spread = np.ptp(coeff)
    norm1 = np.linalg.norm(coeff, ord=1)
    min_eigenvalue = np.linalg.eigvalsh(gram)[0]
    assert min_eigenvalue > 0
    assert residual < 1e-11
    assert row_spread < 1e-10
    assert norm1 > 1
    return min_eigenvalue, residual, row_spread, norm1


def main():
    gammas = [0.05, 0.10, 0.25, 0.50, 0.75, 0.95]
    print("Cross-polytope witnesses")
    for gamma in gammas:
        d1, der1, u1, ratio1 = p1_cross_polytope(mp.mpf(str(gamma)))
        d2, der2, u2, ratio2 = p2_cross_polytope(mp.mpf(str(gamma)))
        print(
            f"gamma={gamma:0.2f}  "
            f"p=1: d={d1}, derivative={mp.nstr(der1, 8)}, "
            f"u={mp.nstr(u1, 3)}, A4_norm={mp.nstr(ratio1, 14)};  "
            f"p=2: d={d2}, derivative={mp.nstr(der2, 8)}, "
            f"u={mp.nstr(u2, 3)}, A4_norm={mp.nstr(ratio2, 14)}"
        )

    print("\nPlanar regular-polygon witnesses")
    for gamma in gammas:
        n, avg, derivative, u, ratio = p2_circle(mp.mpf(str(gamma)))
        print(
            f"gamma={gamma:0.2f}  n={n}, chord_average={avg:.12f}, "
            f"derivative={mp.nstr(derivative, 9)}, u={mp.nstr(u, 3)}, "
            f"A4_norm={mp.nstr(ratio, 14)}"
        )

    mineig, residual, spread, norm1 = direct_circle_solve()
    print("\nDirect six-by-six Gram solve (gamma=1/2)")
    print(f"min_eigenvalue={mineig:.12e}")
    print(f"solve_residual_inf={residual:.12e}")
    print(f"coefficient_spread={spread:.12e}")
    print(f"A4_norm={norm1:.12f}")
    print("\nALL SYMMETRIC COUNTEREXAMPLE CHECKS PASSED")


if __name__ == "__main__":
    main()
