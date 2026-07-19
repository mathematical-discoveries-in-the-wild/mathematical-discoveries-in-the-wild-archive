"""Numerical probes for the U(d,a) modulus in two-dimensional l_p spaces.

This is exploratory only.  It tries to minimize over pairs on the l_p^2
unit sphere and maximize over perturbations in the l_p^2 ball.  The output
is intended to suggest proof targets, not to certify any statement.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import differential_evolution, minimize


def lp_norm(v: np.ndarray, p: float) -> float:
    return float(np.sum(np.abs(v) ** p) ** (1.0 / p))


def sphere_point(theta: float, p: float) -> np.ndarray:
    v = np.array([math.cos(theta), math.sin(theta)], dtype=float)
    return v / lp_norm(v, p)


def ball_point(rho: float, theta: float, a: float, p: float) -> np.ndarray:
    direction = sphere_point(theta, p)
    return a * rho * direction


def pair_distance(theta1: float, theta2: float, p: float) -> float:
    return lp_norm(sphere_point(theta1, p) - sphere_point(theta2, p), p)


def u_pair(theta1: float, theta2: float, a: float, p: float) -> float:
    x = sphere_point(theta1, p)
    y = sphere_point(theta2, p)

    def objective(params: np.ndarray) -> float:
        rho, theta = params
        z = ball_point(rho, theta, a, p)
        return -abs(lp_norm(x + z, p) - lp_norm(y + z, p))

    result = differential_evolution(
        objective,
        bounds=[(0.0, 1.0), (0.0, 2.0 * math.pi)],
        tol=1e-8,
        polish=True,
        seed=1234,
        workers=1,
        updating="immediate",
        maxiter=120,
        popsize=12,
    )
    return -float(result.fun)


def approximate_u(d: float, a: float, p: float) -> tuple[float, tuple[float, float, float]]:
    penalty = 1e3

    def objective(params: np.ndarray) -> float:
        theta1, theta2 = params
        dist = pair_distance(theta1, theta2, p)
        if dist < d:
            return penalty * (d - dist) ** 2 + 10.0
        return u_pair(theta1, theta2, a, p)

    starts = [
        (0.1, 0.1 + d),
        (0.0, math.pi / 2),
        (math.pi / 4, math.pi / 4 + d),
        (math.pi / 8, math.pi / 8 + d),
        (math.pi / 2 - d, math.pi / 2),
    ]
    best_value = math.inf
    best_params = (0.0, 0.0, 0.0)
    for start in starts:
        result = minimize(
            objective,
            x0=np.array(start, dtype=float),
            method="Nelder-Mead",
            options={"maxiter": 160, "xatol": 1e-4, "fatol": 1e-5},
        )
        theta1, theta2 = result.x
        dist = pair_distance(theta1, theta2, p)
        if dist >= d * 0.999 and result.fun < best_value:
            best_value = float(result.fun)
            best_params = (float(theta1), float(theta2), float(dist))
    return best_value, best_params


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ps", default="1.2,1.5,1.8,2,3,4")
    parser.add_argument("--ds", default="0.02,0.05,0.1,0.2,0.5")
    parser.add_argument("--a-factor", type=float, default=0.25)
    args = parser.parse_args()

    ps = [float(item) for item in args.ps.split(",")]
    ds = [float(item) for item in args.ds.split(",")]
    for p in ps:
        print(f"p={p:g}")
        for d in ds:
            a = min(0.01, args.a_factor * d)
            value, params = approximate_u(d, a, p)
            ratio = value / (a * d)
            print(
                f"  d={d:g} a={a:g} U~{value:.6g} "
                f"U/(ad)~{ratio:.6g} dist~{params[2]:.6g} "
                f"theta=({params[0]:.4g},{params[1]:.4g})"
            )


if __name__ == "__main__":
    main()
