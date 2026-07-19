#!/usr/bin/env python3
"""Deterministic sanity checks for the Hilbert-ball fiber packet.

The packet proof is analytic.  This script only audits the formulas in
finite-dimensional Euclidean proxies and the constants in the escaping-well
construction.
"""

from __future__ import annotations

import math
import random


def norm(x: list[float]) -> float:
    return math.sqrt(sum(v * v for v in x))


def sub(x: list[float], y: list[float]) -> list[float]:
    return [a - b for a, b in zip(x, y)]


def scale(a: float, x: list[float]) -> list[float]:
    return [a * v for v in x]


def random_ball_vector(rng: random.Random, dim: int, radius: float) -> list[float]:
    x = [rng.uniform(-1.0, 1.0) for _ in range(dim)]
    nx = norm(x)
    if nx == 0.0:
        x[0] = 1.0
        nx = 1.0
    return scale(radius * rng.random() ** (1.0 / dim) / nx, x)


def check_exact_distance() -> None:
    rng = random.Random(190202363)
    r = 3.0
    m_dim = 4
    n_dim = 5
    for _ in range(1000):
        zs = random_ball_vector(rng, m_dim, 0.97 * r)
        zt = random_ball_vector(rng, m_dim, 0.97 * r)
        rs = math.sqrt(r * r - norm(zs) ** 2)
        rt = math.sqrt(r * r - norm(zt) ** 2)
        dz = norm(sub(zs, zt))
        exact = math.hypot(dz, abs(rs - rt))

        # Audit the point-to-section formula on random points of A_s.
        for _ in range(10):
            n = random_ball_vector(rng, n_dim, rs)
            point_dist = math.hypot(dz, max(norm(n) - rt, 0.0))
            assert point_dist <= exact + 1e-12

        # Boundary points in a fixed kernel direction attain the asymmetric
        # radii, and the maximum of the two directions gives the exact value.
        asym_st = math.hypot(dz, max(rs - rt, 0.0))
        asym_ts = math.hypot(dz, max(rt - rs, 0.0))
        assert abs(max(asym_st, asym_ts) - exact) < 1e-12


def check_moduli() -> None:
    rng = random.Random(512)
    r = 2.5
    operator_inverse_norm = 1.7
    b = 1.8
    local_constant = r * operator_inverse_norm / math.sqrt(r * r - b * b)
    for _ in range(1000):
        zs = random_ball_vector(rng, 4, b)
        zt = random_ball_vector(rng, 4, b)
        d = norm(sub(zs, zt))
        rs = math.sqrt(r * r - norm(zs) ** 2)
        rt = math.sqrt(r * r - norm(zt) ** 2)
        hausdorff = math.hypot(d, abs(rs - rt))

        # Use a parameter displacement large enough that
        # d <= ||G|| ||s-t||.
        parameter_distance = d / operator_inverse_norm
        assert hausdorff <= local_constant * parameter_distance + 1e-11

        holder_rhs = 2.0 * math.sqrt(r * d)
        assert hausdorff <= holder_rhs + 1e-11


def check_escaping_wells() -> None:
    data: list[tuple[float, float, float]] = []
    for n in range(1, 80):
        t = 2.0 ** (-(n + 2))
        rho = math.sqrt(1.0 - t * t)
        delta = t / 3.0
        assert t > delta  # support misses A_0
        assert abs(t * t + rho * rho - 1.0) < 1e-15  # y_n is on C
        data.append((t, rho, delta))

    minimum_gap = math.inf
    for i, (ti, rhoi, di) in enumerate(data):
        for tj, rhoj, dj in data[i + 1 :]:
            center_distance = math.sqrt((ti - tj) ** 2 + rhoi**2 + rhoj**2)
            gap = center_distance - di - dj
            minimum_gap = min(minimum_gap, gap)
            assert gap > 1.0
    assert minimum_gap > 1.0


def main() -> None:
    check_exact_distance()
    check_moduli()
    check_escaping_wells()
    print("all Hilbert-ball fiber checks passed")


if __name__ == "__main__":
    main()
