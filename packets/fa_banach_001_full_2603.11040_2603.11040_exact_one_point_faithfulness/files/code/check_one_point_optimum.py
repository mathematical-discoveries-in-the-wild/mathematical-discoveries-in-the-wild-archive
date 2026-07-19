"""Numerical smoke test for the exact one-point faithfulness formula.

This is not used in the proof.  It scans a finite range of Gegenbauer degrees,
reports the minimizing degree, and verifies that the two-mode optimizer has
unit coefficient mass and vanishes at the requested threshold.
"""

from __future__ import annotations

from scipy.special import eval_gegenbauer


def normalized_gegenbauer(degree: int, dimension: int, value: float) -> float:
    alpha = (dimension - 2) / 2
    return float(
        eval_gegenbauer(degree, alpha, value)
        / eval_gegenbauer(degree, alpha, 1.0)
    )


def check(dimension: int, epsilon: float, max_degree: int = 500) -> None:
    values = {
        degree: normalized_gegenbauer(degree, dimension, epsilon)
        for degree in range(max_degree + 1)
        if degree != 1
    }
    minimizing_degree = min(values, key=values.get)
    minimum = values[minimizing_degree]
    linear_mass = -minimum / (epsilon - minimum)
    other_mass = epsilon / (epsilon - minimum)
    residual = linear_mass * epsilon + other_mass * minimum
    assert minimum < 0
    assert abs(linear_mass + other_mass - 1.0) < 1e-12
    assert abs(residual) < 1e-12
    print(
        f"n={dimension:2d} eps={epsilon:5.3f} "
        f"degree={minimizing_degree:3d} m={minimum: .10f} "
        f"tau={linear_mass: .10f} residual={residual: .2e}"
    )


if __name__ == "__main__":
    for n in range(3, 11):
        for eps in (0.001, 0.01, 0.05, 0.1, 0.25, 0.5, 0.8):
            check(n, eps)
