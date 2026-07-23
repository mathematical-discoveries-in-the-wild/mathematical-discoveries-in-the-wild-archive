"""Numerical checks for the full geodesic-geometry extension of arXiv:1308.5739.

The script checks finite-dimensional identities behind the analytic proofs. It
does not attempt to replace completeness or Jacobi-field arguments.
"""

from __future__ import annotations

import math
import numpy as np


TOL = 3.0e-12


def rms_scale(q: np.ndarray) -> tuple[float, np.ndarray]:
    centered = q - q.mean(axis=0, keepdims=True)
    rho = math.sqrt(float(np.sum(centered * centered)) / q.shape[0])
    return rho, centered


def adaptive_gram(q: np.ndarray, alpha: float = 2.0) -> np.ndarray:
    n, d = q.shape
    rho, _ = rms_scale(q)
    diff = q[:, None, :] - q[None, :, :]
    scalar = rho**alpha * np.exp(-np.sum(diff * diff, axis=2) / rho**2)
    return np.kron(scalar, np.eye(d))


def check_adaptive_bounds() -> None:
    rng = np.random.default_rng(20260722)
    for n in (2, 3, 5, 8):
        for d in (1, 2, 3):
            q = rng.normal(size=(n, d)) + np.linspace(-0.4, 0.7, n)[:, None]
            rho, centered = rms_scale(q)
            gram = adaptive_gram(q)
            eig = np.linalg.eigvalsh(gram)
            assert eig[0] > 0.0
            assert eig[-1] <= n * rho**2 * (1.0 + TOL)

            grad_rho = centered / (n * rho)
            dual_rho_sq = float(grad_rho.ravel() @ gram @ grad_rho.ravel())
            assert dual_rho_sq <= rho**2 * (1.0 + TOL)

            for a in range(n):
                for b in range(a + 1, n):
                    selector = np.zeros((d, n * d))
                    selector[:, a * d : (a + 1) * d] = np.eye(d)
                    selector[:, b * d : (b + 1) * d] = -np.eye(d)
                    pair_cometric = selector @ gram @ selector.T
                    radius_sq = float(np.sum((q[a] - q[b]) ** 2))
                    bound = 2.0 * radius_sq * np.eye(d)
                    assert np.linalg.eigvalsh(bound - pair_cometric)[0] >= -TOL

            lam = 1.73
            scaled = adaptive_gram(lam * q)
            np.testing.assert_allclose(scaled, lam**2 * gram, rtol=TOL, atol=TOL)
            print(
                f"N={n}, d={d}: min eig={eig[0]:.5e}, "
                f"dual(d rho)^2/rho^2={dual_rho_sq/rho**2:.8f}"
            )


def check_two_landmark_product_and_conjugacy() -> None:
    off = math.exp(-4.0)
    constant = 2.0 / (1.0 - off)
    first_conjugate = math.pi * math.sqrt(constant)

    # The normal Jacobi scalar on the sphere factor is sin(t/sqrt(C)).
    jacobi_at_endpoint = math.sin(first_conjugate / math.sqrt(constant))
    jacobi_before = math.sin(0.999 * first_conjugate / math.sqrt(constant))
    assert abs(jacobi_at_endpoint) < TOL
    assert jacobi_before > 0.0

    # Check the relative cometric obtained from the two-by-two Gaussian Gram.
    r = 2.4
    rho = r / 2.0
    relative_cometric = 2.0 * rho**2 * (1.0 - off)
    relative_metric = 1.0 / relative_cometric
    np.testing.assert_allclose(relative_metric, constant / r**2, rtol=TOL)
    print(
        f"two-landmark product: C={constant:.12f}, "
        f"first conjugate length={first_conjugate:.12f}"
    )


def gaussian_relative_curvature(r: float, sigma: float = 1.0) -> float:
    t = r * r / (2.0 * sigma * sigma)
    return (2.0 / sigma**2) * (
        math.exp(t) * (1.0 - t) - 1.0
    ) / (math.exp(t) * math.expm1(t))


def check_stationary_relative_curvature() -> None:
    values = [gaussian_relative_curvature(r) for r in np.geomspace(1.0e-3, 6.0, 80)]
    assert max(values) < 0.0
    print(
        "stationary Gaussian relative curvature: "
        f"max={max(values):.5e}, min={min(values):.5e}"
    )


def check_radial_exponent_threshold() -> None:
    # Truncated exact integrals of r^(-alpha/2) illustrate the two ends.
    eps = 1.0e-8
    big = 1.0e8
    for alpha in (0.0, 1.0, 2.0, 3.0, 4.0):
        if abs(alpha - 2.0) < 1.0e-14:
            near_zero = -math.log(eps)
            near_infinity = math.log(big)
        else:
            power = 1.0 - alpha / 2.0
            near_zero = (1.0 - eps**power) / power
            near_infinity = (big**power - 1.0) / power
        print(
            f"alpha={alpha:.1f}: truncated collapse={near_zero:.6e}, "
            f"escape={near_infinity:.6e}"
        )


if __name__ == "__main__":
    check_adaptive_bounds()
    check_two_landmark_product_and_conjugacy()
    check_stationary_relative_curvature()
    check_radial_exponent_threshold()
    print("ALL FULL-GEOMETRY IDENTITY CHECKS PASSED")
