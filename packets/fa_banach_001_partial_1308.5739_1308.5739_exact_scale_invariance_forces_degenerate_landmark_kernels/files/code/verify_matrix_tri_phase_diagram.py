#!/usr/bin/env python3
"""Checks for the longitudinal matrix-TRI completeness criterion."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 180


def rms_scale(x: list[mp.mpf]) -> mp.mpf:
    mean = mp.fsum(x) / len(x)
    return mp.sqrt(mp.fsum((y - mean) ** 2 for y in x) / len(x))


def sites(n: int, eps: mp.mpf) -> list[mp.mpf]:
    return [-eps, eps] + [mp.mpf(2 * j - 3) / 2 for j in range(3, n + 1)]


def longitudinal_value(t: mp.mpf, beta: mp.mpf, eta: mp.mpf) -> mp.mpf:
    """Longitudinal coefficient of exp(-|z|^beta)I+eta(-Hess exp(-|z|^2))."""
    return mp.exp(-(abs(t) ** beta)) + eta * (2 - 4 * t**2) * mp.exp(-(t**2))


def transverse_value(t: mp.mpf, beta: mp.mpf, eta: mp.mpf) -> mp.mpf:
    return mp.exp(-(abs(t) ** beta)) + 2 * eta * mp.exp(-(t**2))


def full_matrix_gram(
    n: int, d: int, beta: mp.mpf, eta: mp.mpf, eps: mp.mpf
) -> tuple[mp.matrix, mp.matrix, mp.mpf, mp.mpf]:
    x = sites(n, eps)
    rho = rms_scale(x)
    full = mp.matrix(n * d)
    longitudinal = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            t = (x[i] - x[j]) / rho
            kp = longitudinal_value(t, beta, eta)
            kt = transverse_value(t, beta, eta)
            longitudinal[i, j] = kp
            full[i * d, j * d] = kp
            for a in range(1, d):
                full[i * d + a, j * d + a] = kt
    return full, longitudinal, rho, 2 * eps / rho


def longitudinal_schur(k: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    n = k.rows
    transform = mp.eye(n)
    root2 = mp.sqrt(2)
    transform[0, 0], transform[1, 0] = 1 / root2, -1 / root2
    transform[0, 1], transform[1, 1] = 1 / root2, 1 / root2
    kb = transform.T * k * transform
    a = kb[0, 0]
    b = kb[1:n, 0]
    c = kb[1:n, 1:n]
    schur = a - (b.T * c**-1 * b)[0]
    return a, schur


def collision_case(
    n: int, d: int, beta: mp.mpf, eta: mp.mpf, eps: mp.mpf
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    full, longitudinal, rho, t = full_matrix_gram(n, d, beta, eta, eps)
    a, schur = longitudinal_schur(longitudinal)
    velocity = mp.matrix(n * d, 1)
    velocity[0], velocity[d] = -1, 1
    direct = (velocity.T * full**-1 * velocity)[0] / rho**2
    reduced = 2 / (rho**2 * schur)
    delta_parallel = longitudinal_value(mp.mpf(0), beta, eta) - longitudinal_value(
        t, beta, eta
    )
    return a, schur, direct, reduced, delta_parallel


def assert_close(x: mp.mpf, y: mp.mpf, tol: mp.mpf, label: str) -> None:
    rel = abs(x - y) / max(mp.mpf(1), abs(x), abs(y))
    if rel > tol:
        raise AssertionError(f"{label}: relative error {mp.nstr(rel, 12)}")


def gaussian_matrix_profile(z: np.ndarray) -> np.ndarray:
    """A strict, non-TRI stationary matrix Gaussian mixture."""
    d = z.size
    matrices = [
        np.diag(np.linspace(0.7, 1.6, d)),
        np.diag(np.linspace(1.4, 0.5, d)),
    ]
    vectors = [
        np.linspace(0.4, 1.2, d),
        np.array([(-1.0) ** j * (j + 1) / d for j in range(d)]),
    ]
    value = math.exp(-float(z @ z)) * np.eye(d)
    for a, v in zip(matrices, vectors):
        value += 0.35 * math.exp(-float(z @ a @ z)) * np.outer(v, v)
    return value


def check_two_landmark_uniform_model() -> tuple[float, float]:
    """Sample the universal N=2 quasi-isometry with H^(d+1) times S^(d-1)."""
    rng = np.random.default_rng(20260723)
    d = 4
    ratios: list[float] = []
    for _ in range(240):
        e = rng.normal(size=d)
        e /= np.linalg.norm(e)
        r = float(np.exp(rng.uniform(-8, 8)))
        phi0 = gaussian_matrix_profile(np.zeros(d))
        phi2 = gaussian_matrix_profile(2 * e)
        k = np.block([[phi0, phi2], [phi2.T, phi0]])
        rho = r / 2
        g = np.linalg.inv(rho**2 * k)

        dc = rng.normal(size=d)
        dr = float(rng.normal())
        de = rng.normal(size=d)
        de -= float(de @ e) * e
        dz = e * dr + r * de
        dq = np.concatenate([dc + dz / 2, dc - dz / 2])
        metric_sq = float(dq @ g @ dq)
        model_sq = (float(dc @ dc) + dr**2) / r**2 + float(de @ de)
        ratio = metric_sq / model_sq
        if not (ratio > 0 and np.isfinite(ratio)):
            raise AssertionError("N=2 model comparison lost positivity")
        ratios.append(ratio)
    return min(ratios), max(ratios)


def main() -> None:
    eta = mp.mpf("0.13")
    betas = [mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("1.5"), mp.mpf("1.9")]
    cases = [(3, 2), (4, 3), (6, 4), (8, 5)]
    eps1, eps2 = mp.mpf("1e-20"), mp.mpf("1e-50")
    tol = mp.mpf("1e-80")
    checks = 0

    for n, d in cases:
        for beta in betas:
            a1, s1, direct1, reduced1, delta1 = collision_case(
                n, d, beta, eta, eps1
            )
            a2, s2, direct2, reduced2, delta2 = collision_case(
                n, d, beta, eta, eps2
            )
            if not min(a1, s1, a2, s2, delta1, delta2) > 0:
                raise AssertionError("matrix-TRI collision block lost positivity")
            assert_close(direct1, reduced1, tol, "full inverse/longitudinal Schur")
            assert_close(direct2, reduced2, tol, "full inverse/longitudinal Schur")
            assert_close(a1, delta1, tol, "antisymmetric block/gap eps1")
            assert_close(a2, delta2, tol, "antisymmetric block/gap eps2")

            ratio = s2 / a2
            slope = mp.log(s2 / s1) / mp.log(eps2 / eps1)
            if abs(ratio - 1) > mp.mpf("2e-3"):
                raise AssertionError(f"longitudinal S/a failed: {mp.nstr(ratio, 12)}")
            if abs(slope - beta) > mp.mpf("5e-3"):
                raise AssertionError(
                    f"longitudinal exponent failed: beta={beta}, "
                    f"slope={mp.nstr(slope, 12)}"
                )
            scaled_speed = mp.sqrt(direct2) * eps2 ** (beta / 2)
            if not (scaled_speed > 0 and mp.isfinite(scaled_speed)):
                raise AssertionError("scaled longitudinal speed was not finite")
            print(
                f"N={n}, d={d}, beta={mp.nstr(beta, 3)}: "
                f"S/a={mp.nstr(ratio, 10)}, "
                f"slope={mp.nstr(slope, 10)}, "
                f"scaled-speed={mp.nstr(scaled_speed, 10)}"
            )
            checks += 1

    beta_two = mp.mpf(2)
    for n, d in cases:
        _, _, speed1, _, _ = collision_case(n, d, beta_two, eta, eps1)
        _, _, speed2, _, _ = collision_case(n, d, beta_two, eta, eps2)
        slope = mp.log(mp.sqrt(speed2 / speed1)) / mp.log(eps2 / eps1)
        if abs(slope + 1) > mp.mpf("2e-8"):
            raise AssertionError("quadratic longitudinal gap lost logarithmic threshold")

    minimum, maximum = check_two_landmark_uniform_model()
    print(
        "N=2 non-TRI model comparison over 240 cases: "
        f"min={minimum:.8g}, max={maximum:.8g}"
    )
    print(f"rough matrix-TRI collision cases checked: {checks}")
    print("ALL MATRIX-TRI PHASE-DIAGRAM CHECKS PASSED")


if __name__ == "__main__":
    main()
