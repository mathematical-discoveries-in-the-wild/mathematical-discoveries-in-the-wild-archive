#!/usr/bin/env python3
"""Verify the scalar inequality used in the monotonicity check.

For m >= n+2 the proof uses

    2*(2**(-n) - 2**(-m)) >= 2**(-n) + 2**(-m).

This script is only a sanity check for representative finite ranges; the
paper proof gives the exact argument.
"""

from fractions import Fraction


def main() -> None:
    for n in range(1, 80):
        for m in range(n + 2, 80):
            lhs = 2 * (Fraction(1, 2**n) - Fraction(1, 2**m))
            rhs = Fraction(1, 2**n) + Fraction(1, 2**m)
            assert lhs >= rhs, (n, m, lhs, rhs)
    print("scalar inequality verified for 1 <= n < m < 80 with m >= n+2")


if __name__ == "__main__":
    main()
