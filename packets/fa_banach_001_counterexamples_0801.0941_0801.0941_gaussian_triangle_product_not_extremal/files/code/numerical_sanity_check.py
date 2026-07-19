#!/usr/bin/env python3
"""Finite-grid sanity checks for the packet; this is not a proof.

The proof only needs existence of a sufficiently small epsilon.  This script
samples the Fourier transforms of q and x^2 q, checks the exact Gaussian
refactorization at representative points, and reports the observed margins for
epsilon=1 on a finite frequency grid.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad


PI = math.pi
EPSILON = 1.0


def triangle(x: float) -> float:
    return max(1.0 - abs(x), 0.0)


def gaussian(x: float, rate: float = 1.0) -> float:
    return math.exp(-rate * PI * x * x)


def q(x: float) -> float:
    return max(1.0 - 2.0 * abs(x), 0.0) * gaussian(x, 2.0)


def cosine_transform(power: int, xi: float) -> float:
    integrand = lambda x: (
        2.0
        * (x**power)
        * (1.0 - 2.0 * x)
        * gaussian(x, 2.0)
        * math.cos(2.0 * PI * xi * x)
    )
    return quad(integrand, 0.0, 0.5, epsabs=2e-12, epsrel=2e-12, limit=200)[0]


def source_product(x: float) -> float:
    convolution = quad(
        lambda t: triangle(t) * gaussian(x - t),
        -1.0,
        1.0,
        epsabs=2e-12,
        epsrel=2e-12,
        limit=200,
    )[0]
    return gaussian(x) * convolution


def refactorized_product(x: float) -> float:
    return 2.0 * quad(
        lambda s: q(s) * gaussian(x - s, 2.0),
        -0.5,
        0.5,
        epsabs=2e-12,
        epsrel=2e-12,
        limit=200,
    )[0]


def main() -> None:
    identity_errors = [
        abs(source_product(x) - refactorized_product(x))
        for x in np.linspace(-3.0, 3.0, 25)
    ]

    minimum_qhat = math.inf
    minimum_relative_margin = math.inf
    maximum_ratio = 0.0
    ratio_location = 0.0
    for xi in np.linspace(0.0, 100.0, 2001):
        qhat = cosine_transform(0, float(xi))
        uhat = cosine_transform(2, float(xi))
        minimum_qhat = min(minimum_qhat, qhat)
        ratio = abs(uhat / qhat)
        if ratio > maximum_ratio:
            maximum_ratio = ratio
            ratio_location = float(xi)
        minimum_relative_margin = min(
            minimum_relative_margin,
            (qhat - EPSILON * abs(uhat)) / qhat,
        )

    print(f"max refactorization error: {max(identity_errors):.3e}")
    print(f"minimum sampled qhat: {minimum_qhat:.3e}")
    print(
        "maximum sampled |uhat/qhat|: "
        f"{maximum_ratio:.6f} at xi={ratio_location:.3f}"
    )
    print(
        f"minimum relative Fourier margin for epsilon={EPSILON:g}: "
        f"{minimum_relative_margin:.6f}"
    )
    print("Finite sampling supports the formulas but does not prove positivity on R.")


if __name__ == "__main__":
    main()

