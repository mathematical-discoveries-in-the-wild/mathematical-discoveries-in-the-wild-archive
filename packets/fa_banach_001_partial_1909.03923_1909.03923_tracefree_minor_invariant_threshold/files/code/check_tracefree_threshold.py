#!/usr/bin/env python3
"""Exact sanity check for the trace-free scalar-shift minor threshold."""

from fractions import Fraction
from itertools import combinations


def rank_matrix(matrix):
    matrix = [list(map(Fraction, row)) for row in matrix]
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if matrix[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][col]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for row in range(rows):
            if row == rank or not matrix[row][col]:
                continue
            factor = matrix[row][col]
            matrix[row] = [
                matrix[row][j] - factor * matrix[rank][j] for j in range(cols)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def derivative_kernel_dim(n, s):
    domain = [
        (rows, cols)
        for rows in combinations(range(n), s)
        for cols in combinations(range(n), s)
    ]
    codomain = [
        (rows, cols)
        for rows in combinations(range(n), s - 1)
        for cols in combinations(range(n), s - 1)
    ]
    row_index = {item: i for i, item in enumerate(codomain)}
    matrix = [[0 for _ in domain] for __ in codomain]
    for col, (rows, cols) in enumerate(domain):
        rows = list(rows)
        cols = list(cols)
        for a in set(rows).intersection(cols):
            sign = -1 if (rows.index(a) + cols.index(a)) % 2 else 1
            reduced_rows = tuple(item for item in rows if item != a)
            reduced_cols = tuple(item for item in cols if item != a)
            matrix[row_index[(reduced_rows, reduced_cols)]][col] += sign
    return len(domain) - rank_matrix(matrix)


def main():
    for n in range(3, 8):
        for s in range(2, n):
            kernel = derivative_kernel_dim(n, s)
            expected_nonzero = 2 * s <= n
            observed_nonzero = kernel > 0
            print(f"n={n} s={s} kernel={kernel}")
            assert observed_nonzero == expected_nonzero


if __name__ == "__main__":
    main()
