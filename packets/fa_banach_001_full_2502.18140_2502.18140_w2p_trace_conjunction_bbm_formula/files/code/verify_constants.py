#!/usr/bin/env python3
"""Independent checks for the constants in the W^{2,p} BBM packet.

These checks are diagnostic only; the packet contains analytic proofs.
"""

from __future__ import annotations

import math

from scipy.integrate import quad


def sphere_area(dimension: int) -> float:
    """Surface area of the unit sphere S^dimension."""
    return 2.0 * math.pi ** ((dimension + 1) / 2) / math.gamma(
        (dimension + 1) / 2
    )


def angular_formula(n: int, p: float) -> float:
    """Integral over a hemisphere of |e dot omega|^p."""
    return (
        math.pi ** ((n - 1) / 2)
        * math.gamma((p + 1) / 2)
        / math.gamma((n + p) / 2)
    )


def angular_quadrature(n: int, p: float) -> float:
    """Half of the full-sphere polar-coordinate integral."""
    integral, _ = quad(
        lambda theta: abs(math.cos(theta)) ** p
        * math.sin(theta) ** (n - 2),
        0.0,
        math.pi,
        epsabs=1e-12,
        epsrel=1e-12,
    )
    return 0.5 * sphere_area(n - 2) * integral


def mellin_exact(p: float, a0: float, q: float, s: float) -> float:
    """(1-s) integral_0^1 r^{p(1-s)-1}(a0+r^q) dr."""
    return a0 / p + (1 - s) / (p * (1 - s) + q)


def main() -> None:
    cases = [(2, 1.0), (2, 2.0), (3, 1.5), (4, 3.25), (7, 4.5)]
    for n, p in cases:
        lhs = angular_quadrature(n, p)
        rhs = angular_formula(n, p)
        error = abs(lhs - rhs)
        print(
            f"angular N={n} p={p:g}: quadrature={lhs:.15g} "
            f"formula={rhs:.15g} abs_error={error:.3e}"
        )
        assert error <= 2e-11 * max(1.0, abs(rhs))

    p, a0, q = 2.75, 1.3, 0.8
    target = a0 / p
    values = [mellin_exact(p, a0, q, s) for s in (0.9, 0.99, 0.999, 0.9999)]
    errors = [abs(value - target) for value in values]
    print(f"mellin target A0/p={target:.15g}")
    for s, value, error in zip((0.9, 0.99, 0.999, 0.9999), values, errors):
        print(f"mellin s={s}: value={value:.15g} abs_error={error:.3e}")
    assert all(later < earlier for earlier, later in zip(errors, errors[1:]))
    assert errors[-1] < 2e-4

    print("all constant checks passed")


if __name__ == "__main__":
    main()

