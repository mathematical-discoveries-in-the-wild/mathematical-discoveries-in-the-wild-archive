#!/usr/bin/env python3
"""Exact arithmetic check of the two-island perturbation counterexample."""

from fractions import Fraction


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def determinant_2x2(matrix: list[list[Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> None:
    epsilon = Fraction(1, 100)
    analysis = [
        [Fraction(1), epsilon],
        [Fraction(0), Fraction(1)],
    ]
    x = [Fraction(0), Fraction(1)]
    z = [-2 * epsilon, Fraction(1)]

    mx = matvec(analysis, x)
    mz = matvec(analysis, z)
    assert [abs(value) for value in mx] == [abs(value) for value in mz]
    assert [abs(value) for value in mx] == [epsilon, Fraction(1)]

    quotient_distance_squared = sum(
        (abs(left) - abs(right)) ** 2 for left, right in zip(x, z)
    )
    assert quotient_distance_squared == 4 * epsilon**2 > 0
    assert determinant_2x2(analysis) == 1
    assert epsilon**2 == Fraction(1, 10_000)

    print("epsilon =", epsilon)
    print("|Theta_Y x| =", [abs(value) for value in mx])
    print("|Theta_Y z| =", [abs(value) for value in mz])
    print("d_island(x,z)^2 =", quotient_distance_squared)
    print("PASS: arbitrarily scalable exact counterexample verified")


if __name__ == "__main__":
    main()
