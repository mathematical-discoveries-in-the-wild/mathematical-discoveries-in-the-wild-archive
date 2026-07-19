"""Finite-dimensional sanity check for the d=1 residue circuit.

This is not part of the proof. On the connected cubic y^2 = x^3 + x, the
product of two real lines cuts six distinct real points. Their quadratic
evaluation vectors have a unique signed relation with three positive and three
negative coefficients, giving two equal positive-definite moment matrices.
"""

import numpy as np


def line_intersections(slope: float, intercept: float) -> list[tuple[float, float]]:
    # Substitute y = slope*x + intercept into y^2 = x^3 + x.
    coefficients = [
        1.0,
        -(slope**2),
        1.0 - 2.0 * slope * intercept,
        -(intercept**2),
    ]
    roots = np.roots(coefficients)
    assert np.max(np.abs(roots.imag)) < 1.0e-10
    return [(float(x), float(slope * x + intercept)) for x in roots.real]


points = line_intersections(-4.0, 0.5) + line_intersections(-3.5, 1.0)

# Quadratic evaluation basis: z^2, xz, yz, x^2, xy, y^2 with z=1.
evaluation = np.array(
    [[1.0, x, y, x * x, x * y, y * y] for x, y in points],
    dtype=float,
)

# A relation among point evaluations is a null vector of evaluation.T.
_, singular_values, vh = np.linalg.svd(evaluation.T)
coefficients = vh[-1]
coefficients /= np.max(np.abs(coefficients))

positive = coefficients > 1.0e-9
negative = coefficients < -1.0e-9
relation_residual = np.linalg.norm(evaluation.T @ coefficients)


def linear_evaluation_vector(point: tuple[float, float]) -> np.ndarray:
    x, y = point
    return np.array([1.0, x, y])


moment_positive = sum(
    coefficient
    * np.outer(linear_evaluation_vector(point), linear_evaluation_vector(point))
    for point, coefficient in zip(points, coefficients)
    if coefficient > 0.0
)
moment_negative = sum(
    -coefficient
    * np.outer(linear_evaluation_vector(point), linear_evaluation_vector(point))
    for point, coefficient in zip(points, coefficients)
    if coefficient < 0.0
)

curve_residual = max(abs(y * y - x * x * x - x) for x, y in points)
matrix_residual = np.linalg.norm(moment_positive - moment_negative)
minimum_eigenvalue = np.min(np.linalg.eigvalsh(moment_positive))

print(f"maximum cubic residual: {curve_residual:.3e}")
print(f"smallest singular value: {singular_values[-1]:.3e}")
print(f"evaluation-relation residual: {relation_residual:.3e}")
print(f"positive/negative coefficient counts: {positive.sum()}/{negative.sum()}")
print(f"moment-matrix equality residual: {matrix_residual:.3e}")
print(f"minimum moment-matrix eigenvalue: {minimum_eigenvalue:.6f}")

assert curve_residual < 1.0e-8
assert relation_residual < 1.0e-8
assert positive.sum() == 3 and negative.sum() == 3
assert matrix_residual < 1.0e-8
assert minimum_eigenvalue > 0.0

