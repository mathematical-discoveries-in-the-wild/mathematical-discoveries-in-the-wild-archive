#!/usr/bin/env python3
"""Exact arithmetic check for the affine-surface-area parameter map."""

from fractions import Fraction


def main() -> None:
    tested = 0
    for n in range(2, 21):
        for k in range(1, 31):
            p_k = Fraction(-2 * k * n, 2 * k - 1)
            exponent = p_k / (n + p_k)
            assert p_k < -n
            assert p_k != -n
            assert exponent == 2 * k
            tested += 1

    print("PARAMETER DOMAIN CHECK: PASS")
    print("EXPONENT IDENTITY CHECK: PASS")
    print(f"tested exact parameter pairs = {tested}")
    print("ALL VERIFICATION CHECKS: PASS")


if __name__ == "__main__":
    main()
