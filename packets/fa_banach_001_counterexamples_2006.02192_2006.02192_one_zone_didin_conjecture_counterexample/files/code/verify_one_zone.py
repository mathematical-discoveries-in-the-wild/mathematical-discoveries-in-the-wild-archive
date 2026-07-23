#!/usr/bin/env python3
"""Exact sanity checks for the one-zone counterexample."""

from fractions import Fraction


def normalized_sum(beta_over_pi: Fraction) -> Fraction:
    """Return (beta + 2 gamma) / pi with gamma=(pi-beta)/2."""
    gamma_over_pi = (1 - beta_over_pi) / 2
    return beta_over_pi + 2 * gamma_over_pi


def main() -> None:
    samples = (
        Fraction(1, 12),
        Fraction(1, 6),
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(11, 12),
    )
    for beta_over_pi in samples:
        assert 0 < beta_over_pi < 1
        gamma_over_pi = (1 - beta_over_pi) / 2
        assert 0 < gamma_over_pi < Fraction(1, 2)
        lhs_over_pi = normalized_sum(beta_over_pi)
        assert lhs_over_pi == 1
        assert lhs_over_pi < 2
        print(
            f"beta/pi={beta_over_pi}, gamma/pi={gamma_over_pi}, "
            f"LHS/pi={lhs_over_pi} < 2"
        )
    print("PASS: every sampled nondegenerate one-zone instance has LHS=pi<2pi.")


if __name__ == "__main__":
    main()
