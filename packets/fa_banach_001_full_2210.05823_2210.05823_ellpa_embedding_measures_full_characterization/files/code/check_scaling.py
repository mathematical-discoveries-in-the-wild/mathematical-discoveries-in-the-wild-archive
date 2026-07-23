#!/usr/bin/env python3
"""Finite scaling checks for the Dirichlet-kernel and Bergman exponents.

These checks are diagnostics only.  The packet proof is analytic.
"""

from __future__ import annotations

import cmath
import math


def dirichlet_box_minimum(p: float, n: int, samples: int = 101) -> float:
    """Sample the normalized Dirichlet polynomial on a small Carleson box."""
    h = 1.0 / (16.0 * n)
    minimum = math.inf
    for radial_index in range(samples):
        r = 1.0 - h * radial_index / (samples - 1)
        for angle_index in range(samples):
            t = h * (angle_index / (samples - 1) - 0.5)
            z = r * cmath.exp(1j * t)
            value = sum(z**k for k in range(n)) / (n ** (1.0 / p))
            scaled = abs(value) / (n ** (1.0 - 1.0 / p))
            minimum = min(minimum, scaled)
    return minimum


def main() -> None:
    for p in (2.2, 2.5, 3.0, 4.0, 6.0):
        print(f"p={p}")
        for n in (8, 16, 32, 64, 128):
            minimum = dirichlet_box_minimum(p, n, samples=31)
            # The critical Bergman shell factor is
            # n^(p-2) * (1/n)^(p-2) = 1.
            cancellation = n ** (p - 2.0) * (1.0 / n) ** (p - 2.0)
            print(
                f"  N={n:3d} normalized_box_min={minimum:.6f} "
                f"critical_cancellation={cancellation:.6f}"
            )


if __name__ == "__main__":
    main()

