"""Numerical sanity check for the scalar estimate in the packet.

The proof uses: eta = min(2, C ** (-1/(1-alpha))) and 2r <= eta**alpha.
Then min(C*d, 2r) <= d**alpha for every d in [0,2].
"""

from __future__ import annotations

import math


def check(alpha: float, C: float, samples: int = 200_000) -> float:
    eta = min(2.0, C ** (-1.0 / (1.0 - alpha)))
    r = 0.49 * eta**alpha / 2.0
    worst = 0.0
    for i in range(1, samples + 1):
        d = 2.0 * i / samples
        lhs = min(C * d, 2.0 * r)
        rhs = d**alpha
        worst = max(worst, lhs / rhs)
    return worst


def main() -> None:
    cases = [
        (0.1, 0.25),
        (0.25, 1.0),
        (0.5, 2.0),
        (0.75, 10.0),
        (0.9, 100.0),
    ]
    for alpha, C in cases:
        worst = check(alpha, C)
        print(f"alpha={alpha:.2f} C={C:.2f} worst_ratio={worst:.6f}")
        assert worst <= 1.000001


if __name__ == "__main__":
    main()
