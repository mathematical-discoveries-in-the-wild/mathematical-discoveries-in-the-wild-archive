"""Scalar sanity check for the second-order lower-bound asymptotic.

This is not part of the proof.  It checks the model case
g(z)=(1+z)^(-1), for which a[g]=(g''(0)-1)/2=1/2, along z_n=i sqrt(n).
"""

from __future__ import annotations

import cmath
import math


def g(z: complex) -> complex:
    return 1.0 / (1.0 + z)


def residual(n: int, rho: float = 1.0) -> complex:
    a = 0.5
    z = 1j * rho * math.sqrt(n)
    return g(z / n) ** n - cmath.exp(-z) - a * (z * z / n) * cmath.exp(-z)


def main() -> None:
    a = 0.5
    rho = 1.0
    predicted = math.exp(-a * rho * rho) - 1.0 + a * rho * rho
    print(f"predicted_scalar_limit={predicted:.12f}")
    for n in [100, 400, 1600, 6400, 25600]:
        value = abs(residual(n, rho))
        print(f"n={n:5d} abs_residual={value:.12f} error={abs(value - predicted):.3e}")


if __name__ == "__main__":
    main()
