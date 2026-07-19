#!/usr/bin/env python3
"""Sanity checks for the planar dual log-BM equality counterexample."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import e, isclose


Point = tuple[Fraction, Fraction]


def det(a: Point, b: Point) -> Fraction:
    return a[0] * b[1] - a[1] * b[0]


def scaled(point: Point, factor: float) -> tuple[float, float]:
    return (float(point[0]) * factor, float(point[1]) * factor)


def det_float(a: tuple[float, float], b: tuple[float, float]) -> float:
    return a[0] * b[1] - a[1] * b[0]


def main() -> None:
    x1: Point = (Fraction(2), Fraction(0))
    x2: Point = (Fraction(0), Fraction(1))
    x3: Point = (Fraction(-1), Fraction(1, 2))
    x4: Point = (Fraction(0), Fraction(-1))
    points = [x1, x2, x3, x4]

    # For q > 0, the vertices are x1, q x2, x3, q x4.
    edge_coefficients = [
        det(x1, x2),
        det(x2, x3),
        det(x3, x4),
        det(x4, x1),
    ]
    area_coeff = sum(edge_coefficients) / 2

    print("edge determinant coefficients:", [str(c) for c in edge_coefficients])
    print("area(P_q) =", f"{area_coeff} * q")
    assert edge_coefficients == [Fraction(2), Fraction(1), Fraction(1), Fraction(2)]
    assert area_coeff == Fraction(3)

    area_p0 = float(area_coeff)
    area_p1 = float(area_coeff) * e
    print("area(P_0) =", area_p0)
    print("area(P_1) =", area_p1)
    assert isclose(area_p1, e * area_p0)

    # Product-style planar equality would force K^circ to split into two
    # pairs of vertices on lines through the origin.  This P_0 does not.
    collinear_pairs = [
        (i + 1, j + 1)
        for i, j in combinations(range(4), 2)
        if det(points[i], points[j]) == 0
    ]
    print("origin-collinear vertex pairs in P_0:", collinear_pairs)
    assert collinear_pairs == [(2, 4)]

    # No scalar homothety P_1 = c P_0 is possible.
    p1 = [scaled(x1, 1.0), scaled(x2, e), scaled(x3, 1.0), scaled(x4, e)]
    p0 = [scaled(p, 1.0) for p in points]
    print("P_0 vertices:", p0)
    print("P_1 vertices:", p1)
    assert p1[0] == p0[0]
    assert p1[2] == p0[2]
    assert p1[1] != p0[1]

    print("verdict: PASS")


if __name__ == "__main__":
    main()
