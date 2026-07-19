#!/usr/bin/env python3
"""Numerical sanity check for the cubic free-cumulant perturbation packet."""

from __future__ import annotations

import cmath
import math

import numpy as np


def branch_g(z: complex, a: float) -> complex:
    """Root of aG^3 + G^2/2 - zG + 1 = 0 with Cauchy branch behavior."""
    roots = np.roots([a, 0.5, -z, 1.0])
    lower = [r for r in roots if r.imag < 0]
    if lower:
        return min(lower, key=lambda r: abs(r))
    return min(roots, key=lambda r: abs(r - 1 / z))


def main() -> None:
    a = 0.02
    eta = 1e-8
    xs = np.linspace(-1.8, 1.8, 1601)
    gs = np.array([branch_g(complex(x, eta), a) for x in xs])
    density = -gs.imag / math.pi
    support_mask = density > 1e-3
    support_x = xs[support_mask]
    interior = density > 0.02
    vp = 2 * gs.real
    dv = np.gradient(vp[interior], xs[interior])

    print(f"a = {a}")
    print(f"approx support = [{support_x[0]:.6f}, {support_x[-1]:.6f}]")
    print(f"max density = {density.max():.6f}")
    print(f"min sampled d/dx(2 Re G) on interior = {dv.min():.6f}")
    print(f"R_+(z)+R_-(z) = z exactly by construction")
    print(f"third free cumulants are +a and -a, so the factors are nonsemicircular")


if __name__ == "__main__":
    main()
