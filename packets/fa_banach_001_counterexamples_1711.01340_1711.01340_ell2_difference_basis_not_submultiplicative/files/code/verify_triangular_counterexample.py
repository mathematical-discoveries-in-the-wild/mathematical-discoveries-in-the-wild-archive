#!/usr/bin/env python3
"""Numerical check for the triangular-sequence counterexample.

This is not needed for the proof; it simply prints the growth of
||sum a_i^2 d_i||_2 / ||sum a_i d_i||_2^2 for the finite sequences used in
the packet.
"""

from __future__ import annotations

import math


def diff_norm_sq(coeffs: list[float]) -> float:
    total = 0.0
    for i, value in enumerate(coeffs):
        nxt = coeffs[i + 1] if i + 1 < len(coeffs) else 0.0
        total += (value - nxt) ** 2
    return total


def triangular_coeffs(n: int) -> list[float]:
    return [i / math.sqrt(n) for i in range(1, n + 1)] + [
        (2 * n - i) / math.sqrt(n) for i in range(n + 1, 2 * n + 1)
    ]


def main() -> None:
    print("n norm_u norm_square ratio")
    for n in [4, 8, 16, 32, 64, 128, 256]:
        a = triangular_coeffs(n)
        norm_u = math.sqrt(diff_norm_sq(a))
        norm_square = math.sqrt(diff_norm_sq([x * x for x in a]))
        ratio = norm_square / (norm_u * norm_u)
        print(f"{n:3d} {norm_u:.6f} {norm_square:.6f} {ratio:.6f}")


if __name__ == "__main__":
    main()
