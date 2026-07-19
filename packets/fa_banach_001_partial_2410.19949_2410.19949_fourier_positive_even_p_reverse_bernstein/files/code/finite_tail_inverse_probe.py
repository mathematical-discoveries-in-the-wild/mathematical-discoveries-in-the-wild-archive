#!/usr/bin/env python3
"""Numerically probe the inverse Laplacian on scalar hypercube tail spaces.

For the normalization used in arXiv:2410.19949, Delta has eigenvalue 2|S|
on the Walsh character W_S.  The script maximizes

    ||Delta^{-1} g||_p / ||g||_p

over g whose Walsh support lies on levels at least d.  A growing value of
d times this ratio would be evidence against the reverse Bernstein estimate.
The optimization is nonconvex, so the output is only a lower bound on the
operator norm and cannot certify the inequality.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.linalg import hadamard
from scipy.optimize import minimize


def duality_map(values: np.ndarray, p: float) -> np.ndarray:
    return np.sign(values) * np.abs(values) ** (p - 1.0)


def probe(n: int, d: int, p: float, starts: int, seed: int, maxiter: int) -> dict:
    if not (1.0 < p < np.inf):
        raise ValueError("p must lie in (1, infinity)")
    if not (1 <= d <= n):
        raise ValueError("d must lie in {1,...,n}")

    size = 1 << n
    degrees = np.fromiter((j.bit_count() for j in range(size)), dtype=int)
    keep = degrees >= d
    tail_degrees = degrees[keep].astype(float)
    walsh_tail = hadamard(size, dtype=float)[:, keep] / np.sqrt(size)
    inverse_eigenvalues = 1.0 / (2.0 * tail_degrees)
    rng = np.random.default_rng(seed)

    def objective_and_gradient(coefficients: np.ndarray) -> tuple[float, np.ndarray]:
        g = walsh_tail @ coefficients
        f = walsh_tail @ (inverse_eigenvalues * coefficients)
        f_power = float(np.sum(np.abs(f) ** p))
        g_power = float(np.sum(np.abs(g) ** p))
        if f_power == 0.0 or g_power == 0.0:
            return np.inf, np.zeros_like(coefficients)

        log_ratio = (np.log(f_power) - np.log(g_power)) / p
        gradient = (
            inverse_eigenvalues
            * (walsh_tail.T @ duality_map(f, p))
            / f_power
            - (walsh_tail.T @ duality_map(g, p)) / g_power
        )
        return -log_ratio, -gradient

    initial_points: list[np.ndarray] = []
    for level in sorted(set(tail_degrees.astype(int))):
        point = np.zeros(tail_degrees.size)
        point[int(np.flatnonzero(tail_degrees == level)[0])] = 1.0
        initial_points.append(point)
    for _ in range(starts):
        point = rng.standard_normal(tail_degrees.size)
        point /= np.linalg.norm(point)
        initial_points.append(point)

    best_ratio = 0.0
    best_result = None
    for point in initial_points:
        result = minimize(
            fun=lambda x: objective_and_gradient(x),
            x0=point,
            jac=True,
            method="L-BFGS-B",
            options={"maxiter": maxiter, "ftol": 1e-13, "gtol": 1e-9},
        )
        ratio = float(np.exp(-result.fun))
        if ratio > best_ratio:
            best_ratio = ratio
            best_result = result

    assert best_result is not None
    return {
        "n": n,
        "d": d,
        "p": p,
        "tail_dimension": int(tail_degrees.size),
        "starts": starts,
        "inverse_norm_lower_bound": best_ratio,
        "scaled_d_inverse_norm_lower_bound": d * best_ratio,
        "reverse_constant_upper_bound": 1.0 / (d * best_ratio),
        "optimizer_success": bool(best_result.success),
        "optimizer_message": str(best_result.message),
        "iterations": int(best_result.nit),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--d", type=int, required=True)
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--starts", type=int, default=12)
    parser.add_argument("--seed", type=int, default=241019949)
    parser.add_argument("--maxiter", type=int, default=1000)
    args = parser.parse_args()
    print(json.dumps(probe(args.n, args.d, args.p, args.starts, args.seed, args.maxiter)))


if __name__ == "__main__":
    main()
