"""Audit the scalar inequality used in the packet proof.

The proof uses, for r,s >= 0 with r+s <= a,

    r**N + s**N <= (r+s)**N <= a**N.

This script is not part of the proof; it is a small reproducibility check for
the numerical constants used in the packet.
"""

from __future__ import annotations

import random


def check_grid(max_n: int = 12, grid: int = 1000) -> None:
    for n in range(1, max_n + 1):
        worst = 0.0
        for i in range(grid + 1):
            r = i / grid
            for j in range(grid + 1 - i):
                s = j / grid
                lhs = r**n + s**n
                rhs = (r + s) ** n
                worst = max(worst, lhs - rhs)
        assert worst <= 1e-12, (n, worst)


def check_random(max_n: int = 20, samples: int = 100_000) -> None:
    rng = random.Random(160207090)
    for _ in range(samples):
        n = rng.randint(1, max_n)
        a = 1.0 + rng.random()
        r = a * rng.random()
        s = (a - r) * rng.random()
        lhs = r**n + s**n
        rhs = a**n
        assert lhs <= rhs + 1e-12, (n, a, r, s, lhs, rhs)


if __name__ == "__main__":
    check_grid()
    check_random()
    print("scalar inequality checks passed")
