#!/usr/bin/env python3
"""Finite exact/numerical sanity checks for the three-point construction.

This script is not part of the proof.  It checks the displayed coordinate
identities exactly for the first 40 coordinates and illustrates the divergent
lower bound on any putative global witness.
"""

from fractions import Fraction


def main() -> None:
    for i in range(1, 41):
        alpha = Fraction(1, 2**i)
        d_ab_sq = 1 + alpha * alpha / 4
        d_c_sq = 1 - alpha * alpha + alpha**4
        assert d_ab_sq - d_c_sq == alpha * alpha * (Fraction(5, 4) - alpha * alpha)
        assert d_ab_sq > d_c_sq

        threshold = Fraction(3, 8) + alpha * alpha / 2
        # At t=threshold, A_i, B_i, and C_i are exactly equidistant.
        d_a_threshold = threshold * threshold + alpha * alpha / 4
        d_c_threshold = alpha * alpha + (threshold - alpha * alpha) ** 2
        assert d_a_threshold == d_c_threshold
        assert threshold >= Fraction(3, 8)

    for p in (1.0, 1.5, 2.0, 4.0, 10.0):
        lower_bound_n_1000 = (1000 * (3 / 8) ** p) ** (1 / p)
        assert lower_bound_n_1000 > 0
        print(f"p={p:>4}: first-1000-coordinate witness norm >= {lower_bound_n_1000:.6f}")

    print("exact coordinate identities verified for i=1,...,40")


if __name__ == "__main__":
    main()
