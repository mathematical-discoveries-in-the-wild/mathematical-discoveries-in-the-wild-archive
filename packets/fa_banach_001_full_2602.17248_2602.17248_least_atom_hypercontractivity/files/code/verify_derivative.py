#!/usr/bin/env python3
"""Algebraic and numerical checks for the least-atom proof packet.

The symbolic checks guard the two displayed algebraic identities in the
proof.  The numerical checks are not proof: they stress-test the coordinate
crossing and independently optimize the two-point constant at nearby biases.
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar


def symbolic_checks() -> None:
    a, t, s = sp.symbols("a t s", positive=True)
    fa = 1 / (s * (a + t**s)) - 1 / (a + t) + (1 - 1 / s) / (1 + a)
    b = (1 - t) * (1 - t ** (s - 1)) / (a + t**s)
    k = (1 - s * t ** (s - 1) + (s - 1) * t**s) / (
        s * (1 - t) * (1 - t ** (s - 1))
    )
    identity = sp.factor(fa + a * b / ((a + 1) * (a + t)) - b * k / (a + 1))
    assert identity == 0

    u = sp.symbols("u", positive=True)
    exp = sp.exp
    t_exp = exp(-u)
    k_exp = (1 - s * t_exp ** (s - 1) + (s - 1) * t_exp**s) / (
        s * (1 - t_exp) * (1 - t_exp ** (s - 1))
    )
    h_u = u * (exp(u) + 1) / (2 * (exp(u) - 1))
    z = (s - 1) * u
    h_z = z * (exp(z) + 1) / (2 * (exp(z) - 1))
    transformed = sp.simplify(sp.together(k_exp - (sp.Rational(1, 2) + (h_u - h_z) / (s * u))))
    assert transformed == 0


def b_value(exponent: float, t: float, a: float) -> float:
    return (1.0 - t) * (1.0 - t ** (exponent - 1.0)) / (a + t**exponent)


def k_value(exponent: float, t: float) -> float:
    numerator = 1.0 - exponent * t ** (exponent - 1.0) + (exponent - 1.0) * t**exponent
    denominator = exponent * (1.0 - t) * (1.0 - t ** (exponent - 1.0))
    return numerator / denominator


def coordinate_crossing_checks(samples: int = 1000) -> None:
    rng = np.random.default_rng(260217248)
    checked = 0
    for _ in range(samples):
        p = rng.uniform(2.0, 12.0)
        q = p + rng.uniform(0.01, 12.0)
        a = 10.0 ** rng.uniform(-3.0, -0.01)
        x = rng.uniform(1e-4, 0.995)
        target = b_value(p, x, a)
        left = b_value(q, x, a) - target
        right = b_value(q, 1.0 - 1e-10, a) - target
        # Skip the numerically degenerate root y=x when p and q are large
        # and x is extremely small; the nontrivial critical root has y>x.
        if not (left > 1e-9 and right < 0.0):
            continue
        y = brentq(lambda z: b_value(q, z, a) - target, x, 1.0 - 1e-10)
        A, B = -math.log(x), -(p - 1.0) * math.log(x)
        C, D = -math.log(y), -(q - 1.0) * math.log(y)
        assert A > C and B < D
        assert k_value(p, x) > k_value(q, y) - 2e-10
        checked += 1
    assert checked >= samples // 2
    print(f"coordinate_crossing_checks={checked}")


def log_ratio(lam: float, p: float, q: float, r: float, x: float) -> float:
    weights = np.array([lam, 1.0 - lam])
    values = np.array([1.0, x])
    mean = float(weights @ values)
    image = mean + r * (values - mean)
    return math.log(float(weights @ image**q)) / q - math.log(float(weights @ values**p)) / p


def sigma_two_point(lam: float, p: float, q: float) -> float:
    def crossing(x: float) -> float:
        return brentq(lambda r: log_ratio(lam, p, q, r, x), 0.0, 1.0, xtol=2e-13, rtol=2e-13)

    result = minimize_scalar(
        crossing,
        bounds=(1e-8, 1.0 - 1e-7),
        method="bounded",
        options={"xatol": 2e-10, "maxiter": 1000},
    )
    assert result.success
    return float(result.fun)


def finite_difference_checks() -> None:
    pairs = [(1.2, 1.8), (1.2, 4.0), (1.5, 2.5), (2.0, 5.0), (2.5, 4.0), (3.0, 6.0), (8.0, 13.0)]
    biases = [0.01, 0.04, 0.1, 0.2, 0.35, 0.47]
    checked = 0
    for p, q in pairs:
        for lam in biases:
            delta = min(2e-5, lam / 20.0, (0.5 - lam) / 20.0)
            lower = sigma_two_point(lam - delta, p, q)
            upper = sigma_two_point(lam + delta, p, q)
            assert upper > lower
            checked += 1
    print(f"finite_difference_checks={checked}")


def main() -> None:
    symbolic_checks()
    print("symbolic_identities=2")
    coordinate_crossing_checks()
    finite_difference_checks()
    print("status=PASS")


if __name__ == "__main__":
    main()
