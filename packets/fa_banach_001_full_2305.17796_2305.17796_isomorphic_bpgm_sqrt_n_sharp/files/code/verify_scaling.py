#!/usr/bin/env python3
"""Finite sanity checks for the Euclidean-ball scaling in the proof packet.

This is not part of the proof. It checks the gamma-function identity for
omega_n/omega_(n-1) and a uniform bound over a broad finite range. The packet
uses only the standard analytic gamma-ratio estimate.
"""

from math import exp, lgamma, log, pi, sqrt


def unit_ball_ratio(n: int) -> float:
    """Return |B_2^n|/|B_2^(n-1)| without overflow."""
    return exp(0.5 * log(pi) + lgamma((n + 1) / 2) - lgamma(n / 2 + 1))


def main() -> None:
    worst = (0.0, 0)
    for n in range(5, 10_001):
        ratio = unit_ball_ratio(n)
        scaled = sqrt(n) * ratio
        if scaled > worst[0]:
            worst = (scaled, n)
        assert ratio <= 3.0 / sqrt(n), (n, ratio)

        # Normalizing M=R=1, the proof bounds comparison mass by 4*ratio.
        normalized_comparison_mass = 4.0 * ratio
        assert normalized_comparison_mass <= 12.0 / sqrt(n)

    print("checked dimensions: 5..10000")
    print(f"max sqrt(n)*omega_n/omega_(n-1): {worst[0]:.12f} at n={worst[1]}")
    print("verified comparison mass <= 12*M*R/sqrt(n) on this range")


if __name__ == "__main__":
    main()

