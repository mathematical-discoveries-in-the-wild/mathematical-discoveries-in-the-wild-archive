#!/usr/bin/env python3
"""Numerical sanity checks for the unit-disk Fourier witness.

This script is not part of the proof.  It compares a long odd Fourier partial
sum with the exact radial-derivative formula and samples the smooth-family
growth asserted in the packet.
"""

from __future__ import annotations

import math


def partial_radial_derivative(r: float, terms: int = 200_000) -> float:
    total = 0.0
    power = 1.0
    r2 = r * r
    for m in range(terms):
        total += power / (2 * m + 1)
        power *= r2
    return -(8.0 / math.pi**2) * total


def exact_radial_derivative(r: float) -> float:
    return -(4.0 / (math.pi**2 * r)) * math.log((1.0 + r) / (1.0 - r))


def smooth_boundary_radial_derivative(rho: float) -> float:
    return (4.0 / math.pi**2) * math.log((1.0 + rho) / (1.0 - rho))


def main() -> None:
    radii = (0.2, 0.5, 0.9, 0.99, 0.999)
    previous_growth = -math.inf
    for r in radii:
        partial = partial_radial_derivative(r)
        exact = exact_radial_derivative(r)
        error = abs(partial - exact)
        tolerance = 2e-10 if r < 0.999 else 2e-8
        assert error < tolerance, (r, partial, exact, error)

        growth = smooth_boundary_radial_derivative(r)
        assert growth > previous_growth
        previous_growth = growth
        print(
            f"r={r:.3f} partial={partial:.12f} exact={exact:.12f} "
            f"error={error:.3e} smooth_growth={growth:.12f}"
        )

    print("Verified the derivative identity and monotone logarithmic growth.")


if __name__ == "__main__":
    main()
