"""Numerical sanity checks for the affine Hilbert-sphere approximants.

Run from the packet directory with:
    python code/check_approximants.py

This is not part of the proof; it samples scalar inner products t in [-1, 1].
"""

from __future__ import annotations

import math

from mpmath import mp


mp.dps = 80
GRID_SIZE = 2_001
GRID = [mp.mpf(-1) + mp.mpf(2) * i / (GRID_SIZE - 1) for i in range(GRID_SIZE)]


def n_r(r, t):
    return mp.sqrt(1 + r * t)


def cubic(r, t):
    return 8 * (n_r(r, t) - n_r(-r, t) - r * t) / (r**3)


def generalized_binomial_half(k: int):
    value = mp.mpf(1)
    for j in range(k):
        value *= (mp.mpf("0.5") - j) / (j + 1)
    return value


def power_difference(k: int, h, t):
    delta = mp.mpf(0)
    for j in range(k + 1):
        delta += (-1) ** (k - j) * math.comb(k, j) * n_r(j * h, t)
    scale = math.factorial(k) * generalized_binomial_half(k) * h**k
    return delta / scale


def max_grid_error(approx, exact):
    return max(abs(approx(t) - exact(t)) for t in GRID)


def main() -> None:
    print(f"grid_size={GRID_SIZE}")
    for r_text in ("0.4", "0.2", "0.1", "0.05"):
        r = mp.mpf(r_text)
        error = max_grid_error(lambda t, r=r: cubic(r, t), lambda t: t**3)
        print(f"cubic r={float(r):.5f} max_error={float(error):.8e}")

    for k in range(1, 7):
        h = mp.mpf("0.001")
        error = max_grid_error(
            lambda t, k=k, h=h: power_difference(k, h, t),
            lambda t, k=k: t**k,
        )
        print(f"power k={k} h={float(h):.5f} max_error={float(error):.8e}")


if __name__ == "__main__":
    main()
