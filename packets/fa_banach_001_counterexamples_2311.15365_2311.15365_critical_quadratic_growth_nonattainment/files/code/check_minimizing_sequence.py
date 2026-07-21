#!/usr/bin/env python3
"""Exact-arithmetic smoke test for the minimizing sequence in the packet."""

from fractions import Fraction


def values(M: int) -> tuple[Fraction, Fraction, Fraction]:
    r = Fraction(1, 2)
    R = r
    A = r * M * M / (1 + M * M)
    J = (A - 1) ** 2 + R
    return A, R, J


def main() -> None:
    lower_bound = Fraction(3, 4)
    previous = None
    for M in (1, 2, 5, 10, 100, 1000):
        A, R, J = values(M)
        assert A < R
        assert J > lower_bound
        if previous is not None:
            assert J < previous
        previous = J
        print(
            f"M={M:4d}  A={float(A):.12f}  R={float(R):.12f}  "
            f"J={float(J):.12f}  J-3/4={float(J-lower_bound):.12e}"
        )


if __name__ == "__main__":
    main()

