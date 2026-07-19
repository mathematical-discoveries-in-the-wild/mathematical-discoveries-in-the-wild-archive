"""Finite-dimensional sanity check for the orbit formulas in the packet.

This does not prove the c0 theorem.  It checks the algebraic identities in
M_n that underlie the Banach-algebra computation:

    (S circledast phi)(T) = first_row(T) dot first_column(S)
    (phi circledast S)(T) = first_row(S) dot first_column(T)

where phi(T) is the (1,1)-entry.
"""

from __future__ import annotations

import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def phi(t: list[list[float]]) -> float:
    return t[0][0]


def main() -> None:
    random.seed(260214317)
    n = 6
    for _ in range(100):
        s = [[random.randint(-3, 3) for _ in range(n)] for _ in range(n)]
        t = [[random.randint(-3, 3) for _ in range(n)] for _ in range(n)]

        left = phi(matmul(t, s))
        left_formula = sum(t[0][k] * s[k][0] for k in range(n))
        assert left == left_formula

        right = phi(matmul(s, t))
        right_formula = sum(s[0][k] * t[k][0] for k in range(n))
        assert right == right_formula

    print("orbit formulas verified in finite-dimensional matrix samples")


if __name__ == "__main__":
    main()
