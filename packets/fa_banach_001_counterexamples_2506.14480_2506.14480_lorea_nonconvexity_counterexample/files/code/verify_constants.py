#!/usr/bin/env python3
"""Verify the scalar inequality used in the LorEA nonconvexity packet.

The paper's Appendix C criterion uses

    alpha(phi) = max(||phi_1 + phi_2||, ||phi_1 - phi_2||,
                     sqrt(||phi H phi^T||_1) for H in Hset).

For a real 2x2 matrix M, ||M||_1^2 = ||M||_F^2 + 2 |det M|.
This script computes the relevant quantities for the two rational matrices
appearing in the source paper.
"""

from fractions import Fraction
from math import sqrt


HSET = [
    ((-1, 1), (1, 1)),
    ((1, -1), (1, 1)),
    ((1, 1), (-1, 1)),
    ((1, 1), (1, -1)),
]


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def transpose(a):
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def frob2(a):
    return sum(a[i][j] * a[i][j] for i in range(2) for j in range(2))


def vec_norm(v):
    return sqrt(float(sum(x * x for x in v)))


def trace_norm_2x2(a):
    return sqrt(float(frob2(a) + 2 * abs(det2(a))))


def alpha(phi):
    c1 = (phi[0][0], phi[1][0])
    c2 = (phi[0][1], phi[1][1])
    candidates = [
        vec_norm((c1[0] + c2[0], c1[1] + c2[1])),
        vec_norm((c1[0] - c2[0], c1[1] - c2[1])),
    ]
    for h in HSET:
        h = tuple(tuple(Fraction(x) for x in row) for row in h)
        m = matmul(matmul(phi, h), transpose(phi))
        candidates.append(sqrt(trace_norm_2x2(m)))
    return max(candidates), candidates


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def main():
    phi1 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, 5)))
    phi2 = ((Fraction(1), Fraction(3, 10)), (Fraction(0), Fraction(1, 2)))
    phi12 = add(phi1, phi2)

    a1, vals1 = alpha(phi1)
    a2, vals2 = alpha(phi2)
    a12, vals12 = alpha(phi12)

    print(f"alpha(phi1) = {a1:.15f}")
    print(f"  candidates = {[round(x, 15) for x in vals1]}")
    print(f"alpha(phi2) = {a2:.15f}")
    print(f"  candidates = {[round(x, 15) for x in vals2]}")
    print(f"alpha(phi1+phi2) = {a12:.15f}")
    print(f"  candidates = {[round(x, 15) for x in vals12]}")
    print(f"alpha(phi1)+alpha(phi2) = {a1 + a2:.15f}")
    assert a1 + a2 < a12
    print("verified: alpha(phi1)+alpha(phi2) < alpha(phi1+phi2)")


if __name__ == "__main__":
    main()
