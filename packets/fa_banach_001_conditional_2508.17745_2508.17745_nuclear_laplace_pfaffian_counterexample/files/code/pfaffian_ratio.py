#!/usr/bin/env python3
"""Exact de Bruijn Pfaffians for the real nuclear-Laplace ensemble."""

from fractions import Fraction
from math import factorial


def ordered_two_moment(a: int, b: int) -> Fraction:
    """Integral over 0<x<y of exp(-x-y) x^a y^b dx dy."""
    return factorial(b) * sum(
        Fraction(factorial(a + k), factorial(k) * 2 ** (a + k + 1))
        for k in range(b + 1)
    )


def skew_moment(a: int, b: int) -> Fraction:
    return ordered_two_moment(a, b) - ordered_two_moment(b, a)


def pfaffian(matrix: list[list[Fraction]]) -> Fraction:
    """Fraction-preserving skew elimination with pivoting."""
    a = [row[:] for row in matrix]
    size = len(a)
    if size % 2:
        raise ValueError("Pfaffian needs even size")
    value = Fraction(1)
    for k in range(0, size, 2):
        pivot = next((j for j in range(k + 1, size) if a[k][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k + 1:
            for row in range(size):
                a[row][k + 1], a[row][pivot] = a[row][pivot], a[row][k + 1]
            a[k + 1], a[pivot] = a[pivot], a[k + 1]
            value = -value
        p = a[k][k + 1]
        value *= p
        for i in range(k + 2, size):
            for j in range(i + 1, size):
                updated = a[i][j] - (
                    a[k][i] * a[k + 1][j] - a[k][j] * a[k + 1][i]
                ) / p
                a[i][j] = updated
                a[j][i] = -updated
    return value


def chamber_integral(exponents: list[int]) -> Fraction:
    n = len(exponents)
    size = n if n % 2 == 0 else n + 1
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for i, ai in enumerate(exponents):
        for j in range(i + 1, n):
            entry = skew_moment(ai, exponents[j])
            matrix[i][j] = entry
            matrix[j][i] = -entry
        if n % 2:
            moment = Fraction(factorial(ai))
            matrix[i][n] = moment
            matrix[n][i] = -moment
    return pfaffian(matrix)


def ratio(n: int) -> Fraction:
    z = chamber_integral([2 * j for j in range(n)])
    boundary = chamber_integral([2 * j for j in range(1, n)])
    return boundary / z


def main() -> None:
    print("n\tratio\tratio/log(n)\texact")
    for n in range(1, 41):
        value = ratio(n)
        import math
        scaled = float(value) / math.log(n) if n > 1 else float("nan")
        print(f"{n}\t{float(value):.12g}\t{scaled:.12g}\t{value}")


def normalized_skew_matrix(n: int) -> list[list[Fraction]]:
    """Skew moments after factoring one factorial from every row/column."""
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            entry = skew_moment(2 * i, 2 * j) / (
                factorial(2 * i) * factorial(2 * j)
            )
            matrix[i][j] = entry
            matrix[j][i] = -entry
    return matrix


if __name__ == "__main__":
    main()
