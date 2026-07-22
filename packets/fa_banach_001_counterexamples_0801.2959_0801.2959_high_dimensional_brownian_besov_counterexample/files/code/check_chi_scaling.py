#!/usr/bin/env python3
"""Numerical sanity check for the high-dimensional Gaussian scaling.

This is not part of the proof.  It evaluates the exact chi-distribution
moments used by the counterexample family.
"""

from math import exp, lgamma, log, sqrt


def chi_moment(dimension: int, exponent: float) -> float:
    """Return (E ||g_d||_2^exponent)^(1/exponent) for g_d standard Gaussian."""
    log_moment = (
        0.5 * exponent * log(2.0)
        + lgamma(0.5 * (dimension + exponent))
        - lgamma(0.5 * dimension)
    )
    return exp(log_moment / exponent)


def chi_mean(dimension: int) -> float:
    return sqrt(2.0) * exp(
        lgamma(0.5 * (dimension + 1)) - lgamma(0.5 * dimension)
    )


def main() -> None:
    previous = float("inf")
    print(" n      L^n(chi_n)/(sqrt(n) E chi_n)")
    for n in (4, 16, 64, 256, 1024, 4096):
        ratio = chi_moment(n, n) / (sqrt(n) * chi_mean(n))
        print(f"{n:4d}    {ratio:.10f}")
        assert ratio < previous
        previous = ratio
    assert previous < 0.03
    print("PASS: the exact ratio decreases toward zero along d=p=n.")


if __name__ == "__main__":
    main()
