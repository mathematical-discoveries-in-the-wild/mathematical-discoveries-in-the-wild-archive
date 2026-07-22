#!/usr/bin/env python3
"""Deterministic sanity checks for the analytic scale-obstruction proof."""

from fractions import Fraction
from math import exp


def exact_rank(matrix):
    """Row-reduction rank over the rationals."""
    a = [[Fraction(value) for value in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((row for row in range(rank, rows) if a[row][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [value / pivot_value for value in a[rank]]
        for row in range(rows):
            if row != rank and a[row][col]:
                factor = a[row][col]
                a[row] = [
                    a[row][j] - factor * a[rank][j] for j in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def constant_block_gram(kappa_zero, landmarks):
    """The block Gram matrix 1_N 1_N^T tensor kappa(0)."""
    dimension = len(kappa_zero)
    return [
        [
            kappa_zero[row % dimension][col % dimension]
            for col in range(landmarks * dimension)
        ]
        for row in range(landmarks * dimension)
    ]


def check_constant_kernel_degeneracy():
    kappa_zero = [[2, 1], [1, 3]]
    assert exact_rank(kappa_zero) == 2
    for landmarks in (2, 3, 4):
        gram = constant_block_gram(kappa_zero, landmarks)
        rank = exact_rank(gram)
        assert rank == 2
        assert rank < 2 * landmarks
        print(
            f"N={landmarks}: constant block Gram rank {rank} "
            f"< ambient dimension {2 * landmarks}"
        )


def check_gaussian_ratio_failure():
    dilation = 2.0
    ratio_at_zero = 1.0
    ratio_at_unit = exp(-(dilation * dilation - 1.0))
    assert ratio_at_zero == 1.0
    assert abs(ratio_at_unit - ratio_at_zero) > 0.9
    print(
        "Gaussian test: kappa(2x)/kappa(x) equals "
        f"{ratio_at_zero:.6f} at x=0 but {ratio_at_unit:.6f} at |x|=1"
    )


def check_zero_diagonal_cross_term_obstruction():
    # A scalar 2-point Gram matrix with zero diagonal and nonzero cross
    # term has eigenvalues +1 and -1, hence cannot be positive semidefinite.
    gram = [[0, 1], [1, 0]]
    positive_vector = [1, 1]
    negative_vector = [1, -1]

    def quadratic(vector):
        return sum(
            vector[i] * gram[i][j] * vector[j]
            for i in range(2)
            for j in range(2)
        )

    assert quadratic(positive_vector) == 2
    assert quadratic(negative_vector) == -2
    print("Zero diagonal/nonzero cross test: quadratic values +2 and -2")


if __name__ == "__main__":
    check_constant_kernel_degeneracy()
    check_gaussian_ratio_failure()
    check_zero_diagonal_cross_term_obstruction()
    print("ALL SCALE-INVARIANCE OBSTRUCTION CHECKS PASSED")
