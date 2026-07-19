"""Arithmetic checks for the ell_4^2 counterexamples in the packet."""

from __future__ import annotations

import cmath
import math


def norm4(z: tuple[complex, complex]) -> float:
    return (abs(z[0]) ** 4 + abs(z[1]) ** 4) ** 0.25


def J_eval(x: tuple[complex, complex], y: tuple[complex, complex]) -> complex:
    """Evaluate the normalized duality functional J(x) at y."""
    n2 = norm4(x) ** 2
    return (abs(x[0]) ** 2 * x[0].conjugate() * y[0] + abs(x[1]) ** 2 * x[1].conjugate() * y[1]) / n2


def swap(x: tuple[complex, complex]) -> tuple[complex, complex]:
    return (x[1], x[0])


def diag12(x: tuple[complex, complex]) -> tuple[complex, complex]:
    return (x[0], 2 * x[1])


def J_vector(x: tuple[complex, complex]) -> tuple[complex, complex]:
    """Coefficient vector for J(x) in the standard linear-dual pairing."""
    n2 = norm4(x) ** 2
    return (abs(x[0]) ** 2 * x[0].conjugate() / n2, abs(x[1]) ** 2 * x[1].conjugate() / n2)


def main() -> None:
    x = (1 + 0j, 2j)
    print("J_x(Ux) =", J_eval(x, swap(x)))
    print("expected =", -6j / math.sqrt(17))
    y = tuple(v / norm4(x) for v in x)
    print("unit numerical-range value =", J_eval(y, swap(y)))
    print("expected =", -6j / 17)

    z = (1 + 0j, 1 + 0j)
    d_prime_jz = (J_vector(z)[0], 2 * J_vector(z)[1])
    j_dz = J_vector(diag12(z))
    print("D'Jz =", d_prime_jz)
    print("J(Dz) =", j_dz)
    print("vectors differ =", any(abs(a - b) > 1e-12 for a, b in zip(d_prime_jz, j_dz)))


if __name__ == "__main__":
    main()
