#!/usr/bin/env python3
"""Finite sanity checks for bandwidth arithmetic.

This is not a proof; it checks the finite-dimensional shadow of the packet's
two algebraic rules: adjoints preserve bandwidth and products add bandwidth.
"""

from __future__ import annotations

import random


def band_matrix(n: int, width: int) -> list[list[complex]]:
    out: list[list[complex]] = []
    for i in range(n):
        row: list[complex] = []
        for j in range(n):
            if abs(i - j) <= width:
                row.append(complex(random.randint(-3, 3), random.randint(-3, 3)))
            else:
                row.append(0j)
        out.append(row)
    return out


def adjoint(a: list[list[complex]]) -> list[list[complex]]:
    n = len(a)
    return [[a[j][i].conjugate() for j in range(n)] for i in range(n)]


def product(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def bandwidth(a: list[list[complex]]) -> int:
    width = 0
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value != 0:
                width = max(width, abs(i - j))
    return width


def main() -> None:
    random.seed(14081164)
    for n in (8, 13, 21):
        for r in range(4):
            for s in range(4):
                a = band_matrix(n, r)
                b = band_matrix(n, s)
                assert bandwidth(adjoint(a)) <= r
                assert bandwidth(product(a, b)) <= r + s
    print("bandwidth arithmetic sanity checks passed")


if __name__ == "__main__":
    main()

