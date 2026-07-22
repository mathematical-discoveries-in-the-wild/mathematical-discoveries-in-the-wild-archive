"""Floating-point sanity checks for the exact radial-twist counterexample.

The mathematical proof in main.tex is exact and does not depend on this file.
"""

from __future__ import annotations

import cmath
import math


A = math.sqrt(7.0) / 5.0
B = 3.0 / 5.0


def phi(radius: float) -> float:
    if radius <= A:
        return 0.0
    if radius < B:
        return (math.pi / 3.0) * (radius - A) / (B - A)
    return math.pi / 3.0


def h(z: complex) -> complex:
    return (1.0 - 2.0 * cmath.exp(1j * phi(abs(z)))) * z


def t(alpha: float, z: complex) -> complex:
    return z - alpha * h(z)


def main() -> None:
    phase = (2.0 + 1j * math.sqrt(3.0)) / math.sqrt(7.0)
    z1 = A
    z2 = B / phase
    target = 3.0 * math.sqrt(7.0) / 10.0

    assert 0.5 < A < B < 1.0
    assert abs(t(0.5, z1) - target) < 1e-12
    assert abs(t(0.5, z2) - target) < 1e-12
    assert abs(z1 - z2) > 1e-3
    assert abs(target) < 1.0

    for k in range(1, 10_000):
        radius = k / 10_000.0
        assert 1.0 - 2.0 * math.cos(phi(radius)) <= 1e-12
        z = radius * cmath.exp(0.731j)
        assert abs(abs(t(1.0, z)) - 2.0 * radius) < 1e-12

    print("all radial-twist counterexample checks passed")


if __name__ == "__main__":
    main()

