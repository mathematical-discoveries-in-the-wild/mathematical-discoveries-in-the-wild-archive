"""Numerical checks from the 2026-07-18 full-push attempt.

This script does not prove a new theorem.  It records reproducible evidence for
two observations:

1. even moments p=8,10,12,16,20 appear Schur-concave in x_i=a_i^2 for the
   exp(-|x|^q), q>2, coordinate law;
2. the Malliaris Fourier-transform criterion does not apply directly because
   exp(-|x|^q), q>2, has a Fourier transform with negative values.
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial, gamma
import random

import numpy as np
from scipy.integrate import quad


@lru_cache(maxsize=None)
def compositions(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    if parts == 1:
        return ((total,),)
    out: list[tuple[int, ...]] = []
    for k in range(total + 1):
        for rest in compositions(total - k, parts - 1):
            out.append((k,) + rest)
    return tuple(out)


def even_moments(q: float, m: int) -> list[float]:
    return [gamma((2 * k + 1) / q) / gamma(1 / q) for k in range(m + 1)]


def moment_and_gradient(q: float, m: int, x: list[float]) -> tuple[float, list[float]]:
    """Return F_m(x)=E(sum sqrt(x_i)Y_i)^(2m) and its gradient."""

    n = len(x)
    mu = even_moments(q, m)
    prefactor = factorial(2 * m)
    value = 0.0
    grad = [0.0] * n
    for ks in compositions(m, n):
        coef = float(prefactor)
        term = 1.0
        for i, k in enumerate(ks):
            coef *= mu[k] / factorial(2 * k)
            if k:
                term *= x[i] ** k
        value += coef * term
        for i, k in enumerate(ks):
            if k:
                grad[i] += coef * term * k / x[i]
    return value, grad


def max_sampled_schur_bracket(q: float, p: int, n: int, samples: int = 5000) -> float:
    """Sample max of (partial_i-partial_j)/(x_i-x_j).

    Schur concavity requires this bracket to be <= 0 whenever x_i > x_j.
    """

    m = p // 2
    best = -float("inf")
    for _ in range(samples):
        raw = [random.random() for _ in range(n)]
        total = sum(raw)
        x = [r / total for r in raw]
        _, grad = moment_and_gradient(q, m, x)
        for i in range(n):
            for j in range(n):
                if x[i] > x[j] + 1e-12:
                    bracket = (grad[i] - grad[j]) / (x[i] - x[j])
                    best = max(best, bracket)
    return best


def p8_auxiliary_quantities(q: float) -> tuple[float, float, float, float]:
    """Return the two endpoint deficits and two still-unproved derivative terms."""

    m2, m4, m6, m8 = even_moments(q, 4)[1:]
    u = m4 / m2**2
    v = m6 / m2**3
    w = m8 / m2**4
    return (
        7 * v - w,
        35 * u * u - 3 * w,
        2 * w - 35 * v + 105 * u,
        3 * w - 42 * v + 210 * u - 35 * u * u,
    )


def fourier_exp_power(q: float, t: float) -> float:
    """Unnormalised Fourier transform of exp(-|x|^q), convention exp(-2 pi i t x)."""

    integrand = lambda x: np.exp(-(x**q)) * np.cos(2 * np.pi * t * x)
    value, _ = quad(integrand, 0.0, np.inf, epsabs=1e-11, epsrel=1e-11, limit=300)
    return 2.0 * value


def main() -> None:
    random.seed(20260718)
    for p in (8, 10, 12, 16, 20):
        print(f"p={p}")
        for q in (2.01, 2.1, 3.0, 4.0, 10.0, 1000.0):
            bracket = max_sampled_schur_bracket(q=q, p=p, n=4, samples=3000)
            print(f"  q={q:7g} max_sampled_schur_bracket={bracket:.6g}")

    print("\np=8 auxiliary quantities")
    for q in (2.01, 2.1, 3.0, 4.0, 10.0, 1000.0):
        endpoint1, endpoint2, deriv1, deriv2 = p8_auxiliary_quantities(q)
        print(
            f"  q={q:7g} 7v-w={endpoint1:.6g} "
            f"35u^2-3w={endpoint2:.6g} "
            f"D1={deriv1:.6g} D2={deriv2:.6g}"
        )

    print("\nFourier sign check")
    for q, t in ((3.0, 0.58), (4.0, 0.56), (6.0, 0.54), (10.0, 0.53)):
        print(f"  q={q:4g} t={t:.2f} hat_phi={fourier_exp_power(q, t):.6g}")


if __name__ == "__main__":
    main()

