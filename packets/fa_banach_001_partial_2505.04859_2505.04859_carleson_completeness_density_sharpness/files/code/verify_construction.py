#!/usr/bin/env python3
"""Numerical sanity checks for the exact two-ray phase diagram.

The packet proof is analytic.  This script only checks representative finite
truncations and the formulas used in that proof.
"""

from __future__ import annotations

import cmath
import math


def pseudohyperbolic(z: complex, w: complex) -> float:
    return abs((z - w) / (1.0 - w * z.conjugate()))


def minimum_finite_carleson_product(points: list[complex]) -> float:
    products = []
    for index, z in enumerate(points):
        log_product = 0.0
        for other_index, w in enumerate(points):
            if index == other_index:
                continue
            rho = pseudohyperbolic(z, w)
            assert 0.0 < rho < 1.0
            log_product += math.log(rho)
        products.append(math.exp(log_product))
    return min(products)


def main() -> None:
    c = math.pi / 3.0
    d = 0.2
    theta = math.pi * d
    spacing = 0.4
    count = 20

    assert 0.0 < d <= c / math.pi
    radii = [math.tanh(spacing * (n + 1)) for n in range(count)]
    plus = [r * cmath.exp(1j * theta) for r in radii]
    minus = [r * cmath.exp(-1j * theta) for r in radii]
    points = plus + minus

    # Exact within-ray formula, checked at machine precision.
    same_ray_error = 0.0
    for m in range(count):
        for n in range(count):
            if m == n:
                continue
            expected = math.tanh(spacing * abs(m - n))
            actual = pseudohyperbolic(plus[m], plus[n])
            same_ray_error = max(same_ray_error, abs(actual - expected))
    # Direct evaluation loses digits once both radii are extremely close to
    # one, so the test deliberately uses a moderate truncation.
    assert same_ray_error < 1e-8

    # Finite Carleson products.  They decrease toward the infinite products;
    # positivity here is only a sanity check, not a proof of a limiting bound.
    minimum_finite_product = minimum_finite_carleson_product(points)
    assert minimum_finite_product > 0.0

    # Cross-ray lower bound and loss estimate from the proof.
    r0 = radii[0]
    sine = math.sin(theta)
    q = r0 * sine
    sum_defects = sum(1.0 - r * r for r in radii)
    worst_cross_ratio = math.inf
    for m, z in enumerate(plus):
        for n, w in enumerate(minus):
            rho = pseudohyperbolic(z, w)
            assert rho + 1e-14 >= q
            loss = 1.0 - rho * rho
            bound = (
                (1.0 - radii[m] ** 2)
                * (1.0 - radii[n] ** 2)
                / (4.0 * r0 * r0 * sine * sine)
            )
            assert loss <= bound + 2e-14
            if bound > 0.0:
                worst_cross_ratio = min(worst_cross_ratio, loss / bound)

    # Principal-phase collision for several powers and every tested pair.
    maximum_alias_error = 0.0
    for k in range(25):
        lam = k / d
        for z_plus, z_minus in zip(plus, minus):
            power_plus = cmath.exp(
                lam * (math.log(abs(z_plus)) + 1j * cmath.phase(z_plus))
            )
            power_minus = cmath.exp(
                lam * (math.log(abs(z_minus)) + 1j * cmath.phase(z_minus))
            )
            maximum_alias_error = max(
                maximum_alias_error, abs(power_plus - power_minus)
            )
    assert maximum_alias_error < 2e-12

    # Nonresonant powered spectrum and the diagonal frame-transfer weights.
    nonresonant_alpha = 1.3
    assert abs(math.sin(nonresonant_alpha * theta)) > 0.1
    powered_plus = [z**nonresonant_alpha for z in plus]
    # Python's complex power also uses the principal logarithm here because
    # the original phases lie in (-pi, pi).
    powered_minus = [z**nonresonant_alpha for z in minus]
    minimum_powered_product = minimum_finite_carleson_product(
        powered_plus + powered_minus
    )
    assert minimum_powered_product > 0.0

    weight_ratios = [
        math.sqrt(
            (1.0 - r * r) / (1.0 - r ** (2.0 * nonresonant_alpha))
        )
        for r in radii
    ]
    assert min(weight_ratios) > 0.0
    assert max(weight_ratios) < math.inf

    # At resonance alpha*theta=pi, every powered radial pair collides.
    resonant_alpha = 1.0 / d
    assert abs(resonant_alpha * theta - math.pi) < 1e-14
    maximum_powered_collision = max(
        abs(z_plus**resonant_alpha - z_minus**resonant_alpha)
        for z_plus, z_minus in zip(plus, minus)
    )
    assert maximum_powered_collision < 2e-12

    # Finite-window approximation to L({k/d}) = d.
    mu = 2.7
    t = 50_000.0
    lower = math.ceil(d * t)
    upper = math.floor(d * mu * t)
    block_sum = d * sum(1.0 / k for k in range(lower, upper + 1))
    density_approximation = block_sum / math.log(mu)
    assert abs(density_approximation - d) < 5e-5

    print(f"parameters: c={c:.12g}, d={d:.12g}, theta={theta:.12g}")
    print(f"tested spectral pairs: {count}")
    print(f"maximum within-ray identity error: {same_ray_error:.3e}")
    print(f"minimum {2 * count}-point Carleson product: "
          f"{minimum_finite_product:.12g}")
    print(f"cross-ray common lower bound q: {q:.12g}")
    print(f"truncated sum of radial defects: {sum_defects:.12g}")
    print(f"minimum loss/bound ratio observed: {worst_cross_ratio:.12g}")
    print(f"maximum phase-alias error: {maximum_alias_error:.3e}")
    print(f"nonresonant alpha: {nonresonant_alpha:.12g}")
    print(f"minimum powered-spectrum Carleson product: "
          f"{minimum_powered_product:.12g}")
    print(
        "frame-transfer weight-ratio range: "
        f"[{min(weight_ratios):.12g}, {max(weight_ratios):.12g}]"
    )
    print(f"resonant alpha: {resonant_alpha:.12g}")
    print(f"maximum powered-pair collision error: "
          f"{maximum_powered_collision:.3e}")
    print(f"logarithmic block-density approximation: "
          f"{density_approximation:.12g}")
    print("all numerical sanity checks passed")


if __name__ == "__main__":
    main()
