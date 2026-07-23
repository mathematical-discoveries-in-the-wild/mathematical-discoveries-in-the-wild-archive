#!/usr/bin/env python3
"""Deterministic checks for the arbitrary-matrix shape quotient and N=2 laws."""

from __future__ import annotations

import math
import numpy as np


RNG = np.random.default_rng(20260723)
RTOL = 2.0e-10
ATOL = 2.0e-11


def assert_close(name: str, lhs, rhs, rtol: float = RTOL, atol: float = ATOL):
    if not np.allclose(lhs, rhs, rtol=rtol, atol=atol):
        err = np.max(np.abs(np.asarray(lhs) - np.asarray(rhs)))
        raise AssertionError(f"{name}: max error {err:.3e}")


def spd_matrix(d: int, shift: float = 0.35) -> np.ndarray:
    raw = RNG.normal(size=(d, d))
    return raw @ raw.T + shift * np.eye(d)


class EvenGaussianMixture:
    """A strict, generally non-TRI, even matrix-valued stationary kernel."""

    def __init__(self, d: int):
        self.d = d
        self.spatial = [spd_matrix(d, 0.7), spd_matrix(d, 1.1)]
        self.output = [spd_matrix(d, 0.9), spd_matrix(d, 0.15)]
        self.output[1] *= 0.22

    def __call__(self, z: np.ndarray) -> np.ndarray:
        ans = np.zeros((self.d, self.d))
        for spatial, output in zip(self.spatial, self.output):
            ans += math.exp(-float(z @ spatial @ z)) * output
        return ans


def skew_spectral_kernel(z: np.ndarray, epsilon: float = 0.8, a: float = 0.55):
    """A strict real stationary 2x2 kernel with a nonzero odd skew part.

    Its spectral density is a positive Gaussian scalar times
    v(xi)v(xi)^* + epsilon I, with v=(1,-i a xi_1).
    """

    z1 = float(z[0])
    phi = math.exp(-0.5 * float(z @ z))
    d1_phi = -z1 * phi
    minus_d11_phi = (1.0 - z1 * z1) * phi
    return np.array(
        [
            [(1.0 + epsilon) * phi, a * d1_phi],
            [-a * d1_phi, epsilon * phi + a * a * minus_d11_phi],
        ]
    )


def gram(points: np.ndarray, profile) -> np.ndarray:
    n, d = points.shape
    ans = np.empty((n * d, n * d))
    for i in range(n):
        for j in range(n):
            ans[i * d : (i + 1) * d, j * d : (j + 1) * d] = profile(
                points[i] - points[j]
            )
    return ans


def normalized_shape(n: int, d: int) -> np.ndarray:
    while True:
        x = RNG.normal(size=(n, d))
        x -= np.mean(x, axis=0)
        rho = math.sqrt(float(np.sum(x * x)) / n)
        x /= rho
        separations = [
            np.linalg.norm(x[i] - x[j])
            for i in range(n)
            for j in range(i)
        ]
        if min(separations) > 0.2:
            return x


def shape_tangent(x: np.ndarray) -> np.ndarray:
    v = RNG.normal(size=x.shape)
    v -= np.mean(v, axis=0)
    v -= x * (float(np.sum(x * v)) / float(np.sum(x * x)))
    assert np.linalg.norm(np.sum(v, axis=0)) < 2.0e-12
    assert abs(float(np.sum(x * v))) < 2.0e-12
    return v


def vertical_matrix(x: np.ndarray) -> np.ndarray:
    n, d = x.shape
    ans = np.zeros((n * d, d + 1))
    for i in range(n):
        ans[i * d : (i + 1) * d, :d] = np.eye(d)
    ans[:, d] = x.reshape(-1)
    return ans


def verify_shape_quotient():
    cases = [(3, 2), (4, 2), (5, 3), (7, 3)]
    checks = 0
    for n, d in cases:
        profile = EvenGaussianMixture(d)
        for _ in range(25):
            x = normalized_shape(n, d)
            v = shape_tangent(x).reshape(-1)
            k = gram(x, profile)
            eig = np.linalg.eigvalsh(k)
            if eig[0] <= 1.0e-10:
                raise AssertionError(f"shape Gram not positive: {eig[0]:.3e}")
            metric = np.linalg.inv(k)
            vertical = vertical_matrix(x)
            normal = vertical.T @ metric @ vertical
            coefficient = -np.linalg.solve(normal, vertical.T @ metric @ v)
            horizontal = v + vertical @ coefficient
            h_min = float(horizontal @ metric @ horizontal)

            shorted = metric - metric @ vertical @ np.linalg.solve(
                normal, vertical.T @ metric
            )
            h_formula = float(v @ shorted @ v)
            assert_close("shape Schur formula", h_formula, h_min)
            assert_close(
                "horizontal orthogonality",
                vertical.T @ metric @ horizontal,
                np.zeros(d + 1),
            )

            # The horizontal lift q=a+r x with
            # a_dot/r=coefficient[:d], r_dot/r=coefficient[d]
            # has exactly the quotient speed.
            r = math.exp(RNG.uniform(-2.0, 2.0))
            a0 = RNG.normal(size=d)
            q = a0 + r * x
            qdot_matrix = r * horizontal.reshape(n, d)
            qdot = qdot_matrix.reshape(-1)
            gq = (r * r) * k
            lift_speed = float(qdot @ np.linalg.solve(gq, qdot))
            assert_close("horizontal lift speed", lift_speed, h_min)

            # Translation and positive dilation do not change the metric
            # pairing after the tangent is dilated.
            lam = math.exp(RNG.uniform(-1.5, 1.5))
            shift = RNG.normal(size=d)
            q2 = lam * q + shift
            rho2 = lam * r
            x2 = (q2 - np.mean(q2, axis=0)) / rho2
            assert_close("normalized shape invariance", x2, x)
            gq2 = (rho2 * rho2) * gram(x2, profile)
            lift_speed2 = float((lam * qdot) @ np.linalg.solve(gq2, lam * qdot))
            assert_close("quotient isometry", lift_speed2, lift_speed)

            # A nonhorizontal vertical choice can only increase the speed.
            perturb = RNG.normal(size=d + 1)
            trial = horizontal + vertical @ perturb
            trial_speed = float(trial @ metric @ trial)
            if trial_speed + 2.0e-10 < h_min:
                raise AssertionError("horizontal lift did not minimize")
            checks += 1
    print(f"shape quotient: {checks} random non-TRI cases passed")


def center_relative_cometric(a0: np.ndarray, b: np.ndarray) -> np.ndarray:
    bsym = 0.5 * (b + b.T)
    cskew = 0.5 * (b - b.T)
    return np.block(
        [
            [0.5 * (a0 + bsym), -cskew],
            [cskew, 2.0 * (a0 - bsym)],
        ]
    )


def verify_general_two_landmark_blocks():
    checks = 0
    a0 = skew_spectral_kernel(np.zeros(2))
    for _ in range(160):
        e = RNG.normal(size=2)
        e /= np.linalg.norm(e)
        b = skew_spectral_kernel(2.0 * e)
        k = np.block([[a0, b], [b.T, a0]])
        if np.linalg.eigvalsh(k)[0] <= 1.0e-10:
            raise AssertionError("strict skew spectral Gram lost positivity")
        j = center_relative_cometric(a0, b)

        p1 = RNG.normal(size=2)
        p2 = RNG.normal(size=2)
        p = np.concatenate([p1, p2])
        total = p1 + p2
        relative = 0.5 * (p1 - p2)
        canonical = np.concatenate([total, relative])
        assert_close(
            "general N=2 cotangent block",
            float(p @ k @ p),
            float(canonical @ j @ canonical),
        )

        dc = RNG.normal(size=2)
        dz = RNG.normal(size=2)
        dq = np.concatenate([dc + 0.5 * dz, dc - 0.5 * dz])
        tangent = np.concatenate([dc, dz])
        assert_close(
            "general N=2 tangent block",
            float(dq @ np.linalg.solve(k, dq)),
            float(tangent @ np.linalg.solve(j, tangent)),
        )

        # With total momentum zero, the center drift is precisely the
        # skew-profile block -C pi.
        pi = RNG.normal(size=2)
        p_zero = np.concatenate([pi, -pi])
        qdot = k @ p_zero
        center_drift_direct = 0.5 * (qdot[:2] + qdot[2:])
        cskew = 0.5 * (b - b.T)
        center_drift_formula = -cskew @ pi
        assert_close(
            "zero-total-momentum center drift",
            center_drift_direct,
            center_drift_formula,
        )
        checks += 1
    print(f"general N=2 block geometry: {checks} skew-profile cases passed")


def verify_even_relative_kaluza_klein():
    checks = 0
    profile = EvenGaussianMixture(3)
    a0 = profile(np.zeros(3))
    for _ in range(180):
        e = RNG.normal(size=3)
        e /= np.linalg.norm(e)
        de = RNG.normal(size=3)
        de -= e * float(e @ de)
        ds = float(RNG.normal())
        b = profile(2.0 * e)
        assert_close("even profile", b, b.T)
        dgap = a0 - b
        hmat = np.linalg.inv(dgap)
        tangent = e * ds + de
        direct = 2.0 * float(tangent @ hmat @ tangent)

        radial = float(e @ hmat @ e)
        theta = float(e @ hmat @ de) / radial
        sphere = 2.0 * (
            float(de @ hmat @ de)
            - float(e @ hmat @ de) ** 2 / radial
        )
        kk = 2.0 * radial * (ds + theta) ** 2 + sphere
        assert_close("Kaluza-Klein completion", direct, kk)
        if sphere < -2.0e-11:
            raise AssertionError("sphere quotient metric is not positive")
        checks += 1
    print(f"even N=2 Kaluza-Klein reduction: {checks} cases passed")


def main():
    verify_shape_quotient()
    verify_general_two_landmark_blocks()
    verify_even_relative_kaluza_klein()
    print("ALL SHAPE-QUOTIENT AND GENERAL N=2 CHECKS PASSED")


if __name__ == "__main__":
    main()
