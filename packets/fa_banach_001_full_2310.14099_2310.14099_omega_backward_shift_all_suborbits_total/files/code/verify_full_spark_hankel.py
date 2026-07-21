#!/usr/bin/env python3
"""Exact finite audit of the Hankel-minor certificate in the proof packet."""

from itertools import combinations


def bareiss_det(matrix):
    """Return an exact integer determinant using fraction-free elimination."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 1:
        return a[0][0]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        previous = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def vandermonde_certificate(q, rows):
    size = len(rows)
    row_factor = q ** sum(n * n for n in rows)
    column_factor = q ** sum(j * j for j in range(size))
    nodes = [q ** (2 * n) for n in rows]
    vandermonde = 1
    for i in range(size):
        for k in range(i + 1, size):
            vandermonde *= nodes[k] - nodes[i]
    return row_factor * column_factor * vandermonde


def main():
    q = 2
    tested = 0
    for size in range(1, 6):
        for rows in combinations(range(8), size):
            matrix = [
                [q ** ((n + j) ** 2) for j in range(size)] for n in rows
            ]
            determinant = bareiss_det(matrix)
            expected = vandermonde_certificate(q, rows)
            assert determinant == expected
            assert determinant != 0
            tested += 1
    print(f"PASS: {tested} Hankel minors checked in exact integer arithmetic.")
    print("PASS: each determinant equals its row/column factors times Vandermonde.")
    print("PASS: every tested finite family of shift projections has full rank.")


if __name__ == "__main__":
    main()

