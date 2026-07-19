#!/usr/bin/env python3
"""Exact finite-dimensional checks for the expectation-semigroup packet.

The counterexample itself is infinite-dimensional.  This script checks the
algebraic identities on finite weighted models using fractions; it is a sanity
check, not a proof of the density-character argument.
"""

from fractions import Fraction
from math import exp


def matmul(left, right):
    rows = len(left)
    inner = len(right)
    cols = len(right[0])
    return [
        [sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def add(left, right):
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def scale(value, matrix):
    return [[value * entry for entry in row] for row in matrix]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def identity(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def expectation_matrix(n):
    raw = [Fraction(1, 2 ** k) for k in range(1, n + 1)]
    total = sum(raw)
    weights = [entry / total for entry in raw]
    expectation = [weights[:] for _ in range(n)]
    return weights, expectation


def diagonal(values):
    n = len(values)
    return [[values[i] if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def verify_size(n):
    weights, expectation = expectation_matrix(n)
    ident = identity(n)
    generator = add(ident, scale(Fraction(-1), expectation))

    assert sum(weights) == 1
    assert all(sum(row) == 1 for row in expectation)  # E(1)=1
    assert matmul(expectation, expectation) == expectation
    assert matmul(generator, generator) == generator

    # Trace preservation: w^T E = w^T.
    weighted_after = [
        sum(weights[i] * expectation[i][j] for i in range(n)) for j in range(n)
    ]
    assert weighted_after == weights

    # Self-adjointness for the weighted L2 inner product: D E = E^T D.
    density = diagonal(weights)
    assert matmul(density, expectation) == matmul(transpose(expectation), density)

    # With q=e^{-t}, T(q)=E+q(I-E) and T(q)T(r)=T(qr).
    for q, r in [(Fraction(1, 2), Fraction(2, 3)), (Fraction(3, 5), Fraction(4, 7))]:
        tq = add(expectation, scale(q, generator))
        tr = add(expectation, scale(r, generator))
        tqr = add(expectation, scale(q * r, generator))
        assert matmul(tq, tr) == tqr


def main():
    sizes = [2, 3, 5, 8, 16]
    for size in sizes:
        verify_size(size)
        print(f"N={size}: exact Markov/projection/semigroup checks passed")

    for alpha in [0.25, 0.5, 0.75]:
        critical = 1.0 - alpha
        coefficient = critical ** critical * exp(-critical)
        print(
            f"alpha={alpha:.2f}: maximizing s=1-alpha={critical:.2f}, "
            f"c_alpha={coefficient:.12f}"
        )

    print("all checks passed")


if __name__ == "__main__":
    main()
