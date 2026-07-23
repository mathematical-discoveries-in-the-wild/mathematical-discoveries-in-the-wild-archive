#!/usr/bin/env python3
"""Check the scalar cancellation and asymptotic reserve in the packet.

This script verifies only algebraic identities and finite numerical samples.
It does not prove the regularized-distance lemma or the analytic estimates.
"""

from __future__ import annotations

import math

import sympy as sp


def check_symbolic_identity() -> None:
    k, f, inv_g_sq = sp.symbols("k f inv_g_sq", real=True)

    # The identity uses t f'(t) = f(t)^2 for f=1/log(1/t).
    divergence_main = sp.Rational(1, 2) * (k * (k + f) + f**2)
    inverse_metric_term = sp.Rational(1, 4) * (k + f) ** 2 * inv_g_sq
    geometric_error = (
        sp.Rational(1, 4) * (k + f) ** 2 * (1 - inv_g_sq)
    )
    claimed = sp.Rational(1, 4) * (k**2 + f**2) + geometric_error

    remainder = sp.simplify(divergence_main - inverse_metric_term - claimed)
    if remainder != 0:
        raise AssertionError(f"central identity failed: {remainder}")
    print("symbolic cancellation: PASS")


def check_derivative_identity() -> None:
    t = sp.symbols("t", positive=True)
    f = 1 / sp.log(1 / t)
    remainder = sp.simplify(t * sp.diff(f, t) - f**2)
    if remainder != 0:
        raise AssertionError(f"t f'(t)=f(t)^2 failed: {remainder}")
    print("derivative identity t*f'(t)=f(t)^2: PASS")


def check_asymptotic_samples() -> None:
    # E/f^2 is bounded by a constant times
    # t^theta (1+log(1/t)) log(1/t)^2.
    exponents = (0.10, 0.25, 0.50, 0.80)
    powers = (8, 16, 32, 64, 128)
    print("sample ratios for t^theta(1+L)/L^-2, L=log(1/t):")
    for theta in exponents:
        ratios = []
        for power in powers:
            log_t_inverse = power * math.log(10.0)
            ratio = math.exp(-theta * log_t_inverse)
            ratio *= (1.0 + log_t_inverse) * log_t_inverse**2
            ratios.append(ratio)
        if not ratios[-1] < ratios[-2]:
            raise AssertionError(
                f"tail sanity check did not decrease for theta={theta}: {ratios}"
            )
        formatted = ", ".join(f"{value:.3e}" for value in ratios)
        print(f"  theta={theta:.2f}: {formatted}")

    # The exact anisotropic t/delta conversion uses
    # delta^epsilon = o(log(1/delta)^-2), equivalently
    # delta^epsilon * log(1/delta)^2 -> 0.
    print("sample ratios for delta^epsilon/L^-2, L=log(1/delta):")
    for epsilon in exponents:
        ratios = []
        for power in powers:
            log_delta_inverse = power * math.log(10.0)
            ratio = math.exp(-epsilon * log_delta_inverse)
            ratio *= log_delta_inverse**2
            ratios.append(ratio)
        if not ratios[-1] < ratios[-2]:
            raise AssertionError(
                "delta reserve tail did not decrease for "
                f"epsilon={epsilon}: {ratios}"
            )
        formatted = ", ".join(f"{value:.3e}" for value in ratios)
        print(f"  epsilon={epsilon:.2f}: {formatted}")
    print("regularized-to-Euclidean anisotropic reserve: PASS")


if __name__ == "__main__":
    check_derivative_identity()
    check_symbolic_identity()
    check_asymptotic_samples()
    print("all checks: PASS")
