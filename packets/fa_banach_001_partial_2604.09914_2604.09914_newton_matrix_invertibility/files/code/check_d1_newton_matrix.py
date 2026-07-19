"""Sanity checks for the 1D semidiscrete MMP Newton matrix.

This script is not part of the proof.  It uses the explicit one-dimensional
Laguerre interval formula to sample full-cell configurations and verifies that
the regularized matrix M is positive definite up to numerical tolerance, while
the Hessian has exactly the affine two-dimensional kernel.
"""

from __future__ import annotations

import math

import numpy as np


def hessian_d1(y: np.ndarray, phi: np.ndarray) -> np.ndarray | None:
    """Return the Hessian from the source formula for sorted 1D sites.

    The return value is None if the Laguerre cells are not all intervals with
    nonempty interior or if the exponential integral is not finite.
    """

    n = len(y)
    cuts = np.array(
        [(phi[i + 1] - phi[i]) / (y[i + 1] - y[i]) for i in range(n - 1)]
    )
    if not np.all(np.diff(cuts) > 1e-10):
        return None

    bounds = [-math.inf, *cuts.tolist(), math.inf]
    masses: list[float] = []
    for i in range(n):
        left, right = bounds[i], bounds[i + 1]
        yi = y[i]
        if abs(yi) < 1e-12:
            if not math.isfinite(left) or not math.isfinite(right):
                return None
            mass = math.exp(phi[i]) * (right - left)
        else:

            def primitive(x: float) -> float:
                return -(1.0 / yi) * math.exp(-yi * x)

            if math.isinf(left) and left < 0:
                if yi >= 0:
                    return None
                left_value = 0.0
            else:
                left_value = primitive(left)

            if math.isinf(right) and right > 0:
                if yi <= 0:
                    return None
                right_value = 0.0
            else:
                right_value = primitive(right)

            mass = math.exp(phi[i]) * (right_value - left_value)

        if not math.isfinite(mass) or mass <= 0:
            return None
        masses.append(mass)

    z = sum(masses)
    q = np.array(masses) / z
    facet = np.zeros((n, n))
    for i, cut in enumerate(cuts):
        weight = math.exp(phi[i] - y[i] * cut) / (abs(y[i + 1] - y[i]) * z)
        facet[i, i + 1] = facet[i + 1, i] = weight

    hessian = np.zeros((n, n))
    for i in range(n):
        hessian[i, i] = q[i] * q[i] - q[i] + facet[i].sum()
        for j in range(n):
            if i != j:
                hessian[i, j] = q[i] * q[j] - facet[i, j]
    return hessian


def main() -> None:
    rng = np.random.default_rng(20260718)
    failures = 0
    trials = 0
    min_regularized = math.inf
    for n in range(3, 9):
        y = np.linspace(-1.0, 1.0, n)
        for _ in range(250):
            cuts = np.sort(rng.normal(size=n - 1))
            phi = np.zeros(n)
            for i, cut in enumerate(cuts):
                phi[i + 1] = phi[i] + (y[i + 1] - y[i]) * cut

            hessian = hessian_d1(y, phi)
            if hessian is None:
                continue

            u = np.ones(n)
            regularized = hessian + np.outer(u, u) + np.outer(y, y)
            eig_hessian = np.linalg.eigvalsh((hessian + hessian.T) / 2)
            eig_regularized = np.linalg.eigvalsh((regularized + regularized.T) / 2)
            trials += 1
            min_regularized = min(min_regularized, float(eig_regularized[0]))
            if eig_regularized[0] <= 1e-8 or abs(eig_hessian[2]) <= 1e-8:
                failures += 1
                print("failure", n, eig_hessian, eig_regularized)
                break

    print(f"trials={trials}")
    print(f"failures={failures}")
    print(f"minimum_regularized_eigenvalue={min_regularized:.6g}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
