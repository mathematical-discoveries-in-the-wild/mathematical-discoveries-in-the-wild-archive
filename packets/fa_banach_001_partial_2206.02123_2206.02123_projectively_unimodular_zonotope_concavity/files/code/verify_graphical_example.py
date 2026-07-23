#!/usr/bin/env python3
"""Exact check of the K5 graphical-zonotope example in the packet."""

from itertools import combinations

import sympy as sp


def reduced_incidence_matrix(vertex_count: int):
    edges = list(combinations(range(vertex_count), 2))
    columns = []
    for i, j in edges:
        column = [0] * (vertex_count - 1)
        if i < vertex_count - 1:
            column[i] = 1
        if j < vertex_count - 1:
            column[j] = -1
        columns.append(column)
    matrix = sp.Matrix(
        vertex_count - 1,
        len(edges),
        lambda row, col: columns[col][row],
    )
    return edges, matrix


def assert_totally_unimodular(matrix: sp.Matrix) -> None:
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for row_set in combinations(range(rows), size):
            for col_set in combinations(range(cols), size):
                minor = matrix.extract(row_set, col_set).det()
                assert minor in (-1, 0, 1), (row_set, col_set, minor)


def zonotope_polynomial_by_bases(matrix, edge_weights):
    rank, edge_count = matrix.shape
    total = 0
    for basis in combinations(range(edge_count), rank):
        determinant = abs(matrix[:, basis].det())
        monomial = sp.prod(edge_weights[index] for index in basis)
        total += determinant * monomial
    return sp.expand(total)


def main() -> None:
    t = sp.symbols("t", nonnegative=True)
    edges, matrix = reduced_incidence_matrix(5)
    assert_totally_unimodular(matrix)

    distinguished = {(0, 1), (0, 2), (0, 3)}
    weights = [t if edge in distinguished else 1 for edge in edges]
    diagonal = sp.diag(*weights)

    by_determinant = sp.expand((matrix * diagonal * matrix.T).det())
    by_bases = zonotope_polynomial_by_bases(matrix, weights)
    assert by_determinant == by_bases
    assert by_determinant == 4 * t**3 + 33 * t**2 + 72 * t + 16
    assert sp.factor(by_determinant) == (t + 4) ** 2 * (4 * t + 1)

    concavity_numerator = sp.expand(
        3 * by_determinant * sp.diff(by_determinant, t, 2)
        - 2 * sp.diff(by_determinant, t) ** 2
    )
    assert sp.factor(concavity_numerator) == -450 * (t + 4) ** 2

    print("P(t) =", by_determinant)
    print("factorization =", sp.factor(by_determinant))
    print("3 P P'' - 2(P')^2 =", sp.factor(concavity_numerator))
    print("all exact checks passed")


if __name__ == "__main__":
    main()
