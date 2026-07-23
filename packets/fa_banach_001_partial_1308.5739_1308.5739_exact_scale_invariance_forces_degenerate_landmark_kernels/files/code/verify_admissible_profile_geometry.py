"""Stress tests for the admissible-profile adaptive landmark theorems.

The tests cover a non-TRI matrix-valued positive-definite Gaussian mixture,
the full scalar two-landmark hyperbolic-times-sphere identification, and the
fixed-center product for an anisotropic TRI curl-free mixture.  They check
finite-dimensional identities used by the proofs, not completeness itself.
"""

from __future__ import annotations

import math
import numpy as np


TOL = 2.0e-11


def rms_scale(q: np.ndarray) -> tuple[float, np.ndarray]:
    centered = q - q.mean(axis=0, keepdims=True)
    rho = math.sqrt(float(np.sum(centered * centered)) / q.shape[0])
    return rho, centered


def matrix_mixture_data(d: int) -> list[tuple[np.ndarray, np.ndarray]]:
    """Return input precision/output PSD pairs for a strict matrix kernel."""
    axis = np.arange(1.0, d + 1.0)
    direction = axis / np.linalg.norm(axis)
    return [
        (0.55 * np.eye(d), np.eye(d)),
        (
            np.diag(np.linspace(0.25, 1.15, d)),
            0.31 * np.outer(direction, direction),
        ),
    ]


def matrix_profile(z: np.ndarray) -> np.ndarray:
    value = np.zeros((z.size, z.size))
    for precision, output in matrix_mixture_data(z.size):
        value += math.exp(-float(z @ precision @ z)) * output
    return value


def feature_lipschitz_constant_sq(d: int) -> float:
    # 2(1-exp(-z^T A z))M <= 2||A|| ||M|| |z|^2 I.
    return 2.0 * sum(
        np.linalg.norm(precision, 2) * np.linalg.norm(output, 2)
        for precision, output in matrix_mixture_data(d)
    )


def adaptive_matrix_gram(q: np.ndarray) -> np.ndarray:
    n, d = q.shape
    rho, _ = rms_scale(q)
    gram = np.empty((n * d, n * d))
    for a in range(n):
        for b in range(n):
            block = rho**2 * matrix_profile((q[a] - q[b]) / rho)
            gram[a * d : (a + 1) * d, b * d : (b + 1) * d] = block
    return gram


def check_all_n_matrix_profile_completeness_bounds() -> None:
    rng = np.random.default_rng(20260723)
    pair_count = 0
    for n in (2, 3, 5, 8):
        for d in (1, 2, 3, 4):
            q = rng.normal(size=(n, d))
            q += np.linspace(-0.7, 0.9, n)[:, None]
            rho, centered = rms_scale(q)
            gram = adaptive_matrix_gram(q)
            phi0 = matrix_profile(np.zeros(d))
            eig = np.linalg.eigvalsh(gram)
            assert eig[0] > 0.0

            op_bound = n * np.trace(phi0) * rho**2
            assert eig[-1] <= op_bound * (1.0 + TOL)

            grad_rho = centered / (n * rho)
            dual_rho_sq = float(grad_rho.ravel() @ gram @ grad_rho.ravel())
            assert dual_rho_sq <= np.trace(phi0) * rho**2 * (1.0 + TOL)

            c_sq = feature_lipschitz_constant_sq(d)
            for a in range(n):
                for b in range(a + 1, n):
                    selector = np.zeros((d, n * d))
                    selector[:, a * d : (a + 1) * d] = np.eye(d)
                    selector[:, b * d : (b + 1) * d] = -np.eye(d)
                    pair_cometric = selector @ gram @ selector.T
                    radius_sq = float(np.sum((q[a] - q[b]) ** 2))
                    remainder = c_sq * radius_sq * np.eye(d) - pair_cometric
                    assert np.linalg.eigvalsh(remainder)[0] >= -TOL
                    pair_count += 1

            lam = 1.91
            np.testing.assert_allclose(
                adaptive_matrix_gram(lam * q),
                lam**2 * gram,
                rtol=TOL,
                atol=TOL,
            )
            print(
                f"matrix profile N={n}, d={d}: min eig={eig[0]:.4e}, "
                f"rho dual ratio={dual_rho_sq/(np.trace(phi0)*rho**2):.6f}"
            )
    print(f"matrix-profile pair inequalities checked: {pair_count}")


def scalar_profile(radius: float) -> float:
    return 0.72 * math.exp(-0.31 * radius**2) + 0.28 * math.exp(
        -1.27 * radius**2
    )


def check_full_scalar_hyperbolic_sphere_product() -> None:
    rng = np.random.default_rng(510091)
    for d in (1, 2, 3, 5):
        a = scalar_profile(0.0)
        b = scalar_profile(2.0)
        hyperbolic_scale = 2.0 / (a - b)
        center_rescale = 2.0 * math.sqrt((a - b) / (a + b))

        for _ in range(20):
            z = rng.normal(size=d)
            r = np.linalg.norm(z)
            omega = z / r
            c = rng.normal(size=d)
            q = np.stack((c + z / 2.0, c - z / 2.0))
            rho, _ = rms_scale(q)
            assert abs(rho - r / 2.0) < TOL

            block = rho**2 * np.block(
                [
                    [a * np.eye(d), b * np.eye(d)],
                    [b * np.eye(d), a * np.eye(d)],
                ]
            )
            metric = np.linalg.inv(block)

            dc = rng.normal(size=d)
            dz = rng.normal(size=d)
            tangent_q = np.concatenate((dc + dz / 2.0, dc - dz / 2.0))
            direct_sq = float(tangent_q @ metric @ tangent_q)

            dr = float(omega @ dz)
            domega = (dz - omega * dr) / r
            dx = center_rescale * dc
            product_sq = hyperbolic_scale * (
                (dr**2 + float(dx @ dx)) / r**2 + float(domega @ domega)
            )
            np.testing.assert_allclose(direct_sq, product_sq, rtol=TOL, atol=TOL)

        first_conjugate = math.pi * math.sqrt(hyperbolic_scale)
        assert abs(math.sin(first_conjugate / math.sqrt(hyperbolic_scale))) < TOL
        print(
            f"scalar full product d={d}: B={hyperbolic_scale:.12f}, "
            f"K_H={-1/hyperbolic_scale:.12f}, "
            f"K_S={1/hyperbolic_scale:.12f}"
        )


def tri_profile(z: np.ndarray, sigma: float = 1.35) -> np.ndarray:
    """Strict scalar Gaussian plus a positive curl-free Gaussian kernel."""
    d = z.size
    scalar_weight = 0.83
    curl_free_weight = 0.24
    radius_sq = float(z @ z)
    h = math.exp(-radius_sq / (2.0 * sigma**2))
    hessian_kernel = (
        np.eye(d) / sigma**2 - np.outer(z, z) / sigma**4
    ) * h
    return scalar_weight * h * np.eye(d) + curl_free_weight * hessian_kernel


def check_matrix_tri_fixed_center_product() -> None:
    rng = np.random.default_rng(77881)
    sigma = 1.35
    for d in (2, 3, 5):
        omega = rng.normal(size=d)
        omega /= np.linalg.norm(omega)
        z_normalized = 2.0 * omega
        phi0 = tri_profile(np.zeros(d), sigma)
        phi2 = tri_profile(z_normalized, sigma)
        a = float(phi0[0, 0])
        k_parallel = float(omega @ phi2 @ omega)
        tangent = rng.normal(size=d)
        tangent -= omega * float(omega @ tangent)
        tangent /= np.linalg.norm(tangent)
        k_perp = float(tangent @ phi2 @ tangent)
        delta_parallel = a - k_parallel
        delta_perp = a - k_perp
        assert delta_parallel > 0.0 and delta_perp > 0.0
        radial_scale = 2.0 / delta_parallel
        sphere_scale = 2.0 / delta_perp

        for _ in range(20):
            r = float(rng.uniform(0.3, 4.0))
            rho = r / 2.0
            gram = rho**2 * np.block([[phi0, phi2], [phi2, phi0]])
            metric = np.linalg.inv(gram)

            dr = float(rng.normal())
            domega = rng.normal(size=d)
            domega -= omega * float(omega @ domega)
            dz = omega * dr + r * domega
            tangent_q = np.concatenate((dz / 2.0, -dz / 2.0))
            direct_sq = float(tangent_q @ metric @ tangent_q)
            product_sq = (
                radial_scale * (dr / r) ** 2
                + sphere_scale * float(domega @ domega)
            )
            np.testing.assert_allclose(direct_sq, product_sq, rtol=TOL, atol=TOL)

        print(
            f"matrix TRI sector d={d}: A={radial_scale:.12f}, "
            f"B={sphere_scale:.12f}, first sector conjugate="
            f"{math.pi*math.sqrt(sphere_scale):.12f}"
        )


if __name__ == "__main__":
    check_all_n_matrix_profile_completeness_bounds()
    check_full_scalar_hyperbolic_sphere_product()
    check_matrix_tri_fixed_center_product()
    print("ALL ADMISSIBLE-PROFILE GEOMETRY CHECKS PASSED")
