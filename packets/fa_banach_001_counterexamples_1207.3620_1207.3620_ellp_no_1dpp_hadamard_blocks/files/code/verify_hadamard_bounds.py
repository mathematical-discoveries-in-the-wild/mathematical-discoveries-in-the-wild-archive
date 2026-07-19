#!/usr/bin/env python3
"""Sanity checks for the Hadamard estimates used in the packet.

The proof is analytic. This script only verifies the elementary finite
identities for small Sylvester matrices and prints the lower/upper estimates.
"""

from __future__ import annotations

import math


def sylvester(n: int) -> list[list[int]]:
    if n == 1:
        return [[1]]
    half = sylvester(n // 2)
    top = [row + row for row in half]
    bottom = [row + [-entry for entry in row] for row in half]
    return top + bottom


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(col) for col in zip(*matrix)]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(x * y for x, y in zip(row, col)) for col in transpose(b)]
        for row in a
    ]


def identity_scaled(n: int) -> list[list[int]]:
    return [[n if i == j else 0 for j in range(n)] for i in range(n)]


def estimates(n: int, p: float) -> tuple[float, float, float]:
    pi_lower = n ** (2 - 1 / p)
    if p <= 2:
        op_upper = n
    else:
        op_upper = n ** (1.5 - 1 / p)
    return pi_lower, op_upper, pi_lower / op_upper


def main() -> None:
    for n in [2, 4, 8, 16]:
        h = sylvester(n)
        assert matmul(transpose(h), h) == identity_scaled(n)
        column_l1 = [sum(abs(h[row][col]) for row in range(n)) for col in range(n)]
        assert column_l1 == [n] * n

    for p in [1.25, 1.5, 2.0, 3.0, 6.0]:
        print(f"p={p:g}")
        for n in [2, 4, 8, 16, 32, 64]:
            pi_lower, op_upper, ratio_lower = estimates(n, p)
            print(
                f"  N={n:2d}  pi1_lower={pi_lower:9.3f}  "
                f"op_upper={op_upper:9.3f}  ratio_lower={ratio_lower:7.3f}"
            )
        print()


if __name__ == "__main__":
    main()
