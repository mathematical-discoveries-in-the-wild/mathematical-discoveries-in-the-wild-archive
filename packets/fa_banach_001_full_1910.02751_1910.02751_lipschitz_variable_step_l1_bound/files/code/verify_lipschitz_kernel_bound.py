#!/usr/bin/env python3
"""Sanity checks for the one-dimensional Lipschitz-step kernel bound."""

from __future__ import annotations

import math


def linear_kernel_mass(lipschitz: float, n: int, y: float) -> float:
    """Exact integral of n/(Lx) 1_{|x-y| < Lx/n} over x in (0,1)."""
    if not 0 < y < 1:
        raise ValueError("y must lie in (0,1)")
    if not lipschitz > 0:
        raise ValueError("lipschitz must be positive")
    lower = y / (1.0 + lipschitz / n)
    if lipschitz < n:
        upper = y / (1.0 - lipschitz / n)
    else:
        upper = 1.0
    upper = min(upper, 1.0)
    if lower >= upper:
        return 0.0
    return (n / lipschitz) * math.log(upper / lower)


def theorem_bound_1d(lipschitz: float) -> float:
    """The N=1 theorem bound with omega_1=2."""
    return 2.0 * (1.0 + lipschitz) / (1.0 - lipschitz)


def main() -> None:
    print("L<1 exact one-dimensional linear-step checks")
    for lipschitz in [0.25, 0.5, 0.9]:
        worst = 0.0
        worst_case = None
        for n in [1, 2, 3, 10, 100]:
            for y in [10.0 ** (-k) for k in range(1, 8)]:
                value = linear_kernel_mass(lipschitz, n, y)
                if value > worst:
                    worst = value
                    worst_case = (n, y)
        print(
            f"L={lipschitz:.2f} worst_sample={worst:.6f} "
            f"case={worst_case} theorem_bound={theorem_bound_1d(lipschitz):.6f}"
        )

    print("\nBorderline L=1, n=1 grows as y approaches the boundary")
    for y in [1e-1, 1e-2, 1e-4, 1e-8]:
        print(f"y={y:g} mass={linear_kernel_mass(1.0, 1, y):.6f}")


if __name__ == "__main__":
    main()
