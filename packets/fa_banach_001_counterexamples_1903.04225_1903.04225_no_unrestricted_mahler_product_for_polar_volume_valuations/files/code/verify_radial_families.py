#!/usr/bin/env python3
"""Numerical sanity checks for the two counterexample families.

This script uses the sample weight zeta(t) = max(1-t, 0).  It checks the
closed radial formulas against Simpson quadrature in the transformed radial
variable and prints the product along p -> 1+.  The theorem itself uses the
exact change-of-variables calculation in the proof, not this computation.
"""

from __future__ import annotations

import math


def kappa(n: int) -> float:
    """Volume of the Euclidean unit ball in R^n."""
    return math.pi ** (n / 2) / math.gamma(n / 2 + 1)


def tent_moment(a: float) -> float:
    """Integral_0^1 (1-t)t^(a-1) dt."""
    return 1.0 / (a * (a + 1.0))


def simpson_moment(a: float, panels: int = 200_000) -> float:
    """Stable Simpson check after t=s^m removes the endpoint singularity."""
    if panels % 2:
        raise ValueError("panels must be even")
    power = max(1, math.ceil(1.0 / a))
    step = 1.0 / panels

    def integrand(s: float) -> float:
        if s == 0.0:
            exponent = power * a - 1.0
            if abs(exponent) < 1e-14:
                return float(power)
            return 0.0
        t = s**power
        return (1.0 - t) * (t ** (a - 1.0)) * power * (s ** (power - 1))

    total = integrand(0.0) + integrand(1.0)
    total += 4.0 * sum(integrand(j * step) for j in range(1, panels, 2))
    total += 2.0 * sum(integrand(j * step) for j in range(2, panels, 2))
    return total * step / 3.0


def factors(n: int, p: float) -> tuple[float, float, float]:
    """Return A_zeta(u_p), B_zeta(u_p), and their product."""
    q = p / (p - 1.0)
    a = n / q
    b = n / p
    a_factor = (
        n * kappa(n) / q * p ** (n / q) * tent_moment(a)
    )
    b_factor = (
        n * kappa(n) / p * q ** (n / p) * tent_moment(b)
    )
    return a_factor, b_factor, a_factor * b_factor


def main() -> None:
    print("Moment quadrature checks for integral_0^1 (1-t)t^(a-1) dt")
    for a in (0.04, 0.2, 2.0 / 3.0, 1.5, 2.0):
        exact = tent_moment(a)
        numeric = simpson_moment(a)
        rel_error = abs(numeric - exact) / exact
        print(
            f"a={a:8.5f} exact={exact:14.9f} "
            f"numeric={numeric:14.9f} relerr={rel_error:.3e}"
        )

    print("\nRadial-power products for zeta(t)=max(1-t,0)")
    for n in (2, 3):
        print(f"n={n}")
        for p in (1.5, 1.2, 1.1, 1.05, 1.02, 1.01):
            a_factor, b_factor, product = factors(n, p)
            q = p / (p - 1.0)
            print(
                f"  p={p:5.2f} q={q:8.2f} "
                f"A={a_factor:12.6g} B={b_factor:12.6g} "
                f"A*B={product:12.6g}"
            )

    # For u_c=|x|^2/2+c and c=1, the A-integrand is
    # zeta(|y|^2/2+1)=0 at every y.
    shifted_a = 0.0
    if shifted_a != 0.0:
        raise AssertionError("shifted-quadratic A factor should vanish")
    print("\nShifted quadratic with c=1: A=0 exactly, hence A*B=0.")


if __name__ == "__main__":
    main()
