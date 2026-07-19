#!/usr/bin/env python3
"""Numerically audit the exact balanced-simplex-join formula.

This is a consistency check, not part of the proof.
"""

from __future__ import annotations

import math


def balanced_dimensions(n: int, r: int) -> list[int]:
    q, s = divmod(n, r)
    return [q + 1] * s + [q] * (r - s)


def log_isoperimetric_quotient(n: int, r: int) -> float:
    blocks = balanced_dimensions(n, r)
    assert len(blocks) == r
    assert sum(blocks) == n
    assert sum(b + 1 for b in blocks) == n + r
    log_product = 0.5 * sum((b + 1) * math.log(b + 1) for b in blocks)
    return math.log(n) + 0.5 * math.log(n) + (log_product - math.lgamma(n + 1)) / n


def main() -> None:
    ratios: list[tuple[float, int, int]] = []
    for n in range(1, 501):
        for r in range(1, n + 1):
            iq = math.exp(log_isoperimetric_quotient(n, r))
            scale = n / math.sqrt(r)
            ratios.append((iq / scale, n, r))

    low = min(ratios)
    high = max(ratios)
    print(f"checked {len(ratios)} pairs with 1 <= r <= n <= 500")
    print(f"min iq/(n/sqrt(r)) = {low[0]:.12f} at n={low[1]}, r={low[2]}")
    print(f"max iq/(n/sqrt(r)) = {high[0]:.12f} at n={high[1]}, r={high[2]}")

    for n in (2, 5, 10, 50, 100):
        simplex = math.exp(log_isoperimetric_quotient(n, 1))
        cross_polytope = math.exp(log_isoperimetric_quotient(n, n))
        print(
            f"n={n:3d}: r=1 iq/n={simplex/n:.8f}; "
            f"r=n iq/sqrt(n)={cross_polytope/math.sqrt(n):.8f}"
        )


if __name__ == "__main__":
    main()
