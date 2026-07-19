"""Search pair-splitting slices for the 2512.12254 Hunter moment conjecture.

The slice tested here has a background block of r equal coefficients carrying
l2 mass p0, and two single coordinates sharing the remaining l2 mass c.
For fixed q this computes

    Phi(s) = E (b * (X_1+...+X_r) + sqrt(s) Y + sqrt(c-s) Z)^q

exactly up to Gauss-Jacobi quadrature through the Gamma/Dirichlet
representation.  The pair-splitting proof route would require the minimum on
0 <= s <= c to occur at an endpoint or at s=c/2.
"""

from __future__ import annotations

import argparse
import math
from functools import lru_cache

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import betaln, gammaln, logsumexp, roots_jacobi


@lru_cache(maxsize=None)
def beta_nodes(alpha: int, beta: int, order: int) -> tuple[np.ndarray, np.ndarray]:
    """Nodes/weights for E f(U), U ~ Beta(alpha,beta), alpha,beta positive ints."""
    x, w = roots_jacobi(order, beta - 1, alpha - 1)
    u = (x + 1.0) / 2.0
    log_factor = -(alpha + beta - 1) * math.log(2.0) - betaln(alpha, beta)
    return u, w * math.exp(log_factor)


def log_group3_moment(r: int, q: float, p0: float, s: float, order: int) -> float:
    """Log moment for groups of sizes (r,1,1) and masses (p0,s,c-s)."""
    c = 1.0 - p0
    if p0 < 0.0 or c < 0.0 or s < 0.0 or s > c:
        return float("inf")
    masses = np.array([p0, s, c - s], dtype=float)
    sizes = np.array([r, 1.0, 1.0], dtype=float)
    coeff = np.sqrt(masses / sizes)
    n = r + 2
    u, wu = beta_nodes(r, 2, order)
    v, wv = beta_nodes(1, 1, order)
    uu = u[:, None]
    vv = v[None, :]
    values = coeff[0] * uu + (1.0 - uu) * (coeff[1] * vv + coeff[2] * (1.0 - vv))
    log_w = np.log(wu)[:, None] + np.log(wv)[None, :]
    log_dir = logsumexp(log_w.ravel() + q * np.log(values.ravel()))
    return gammaln(n + q) - gammaln(n) + log_dir


def log_group4_moment(
    r1: int,
    r2: int,
    q: float,
    p1: float,
    p2: float,
    s: float,
    order: int,
) -> float:
    """Log moment for groups of sizes (r1,r2,1,1)."""
    c = 1.0 - p1 - p2
    if p1 < 0.0 or p2 < 0.0 or c < 0.0 or s < 0.0 or s > c:
        return float("inf")
    masses = np.array([p1, p2, s, c - s], dtype=float)
    sizes = np.array([r1, r2, 1.0, 1.0], dtype=float)
    coeff = np.sqrt(masses / sizes)
    n = r1 + r2 + 2

    u, wu = beta_nodes(r1, r2 + 2, order)
    v, wv = beta_nodes(r2, 2, order)
    z, wz = beta_nodes(1, 1, order)
    uu = u[:, None, None]
    vv = v[None, :, None]
    zz = z[None, None, :]
    rest = coeff[2] * zz + coeff[3] * (1.0 - zz)
    values = coeff[0] * uu + (1.0 - uu) * (coeff[1] * vv + (1.0 - vv) * rest)
    log_w = np.log(wu)[:, None, None] + np.log(wv)[None, :, None] + np.log(wz)[None, None, :]
    log_dir = logsumexp(log_w.ravel() + q * np.log(values.ravel()))
    return gammaln(n + q) - gammaln(n) + log_dir


def scan(q_values: list[float], r_values: list[int], p_values: list[float], order: int) -> list[dict]:
    rows: list[dict] = []
    for q in q_values:
        for r in r_values:
            for p0 in p_values:
                c = 1.0 - p0
                if c <= 0.0:
                    continue

                def objective(s: float) -> float:
                    return log_group3_moment(r, q, p0, s, order)

                res = minimize_scalar(
                    objective,
                    bounds=(0.0, c),
                    method="bounded",
                    options={"xatol": 1e-13, "maxiter": 300},
                )
                candidates = [
                    (objective(0.0), 0.0, "endpoint"),
                    (objective(c), c, "endpoint"),
                    (objective(0.5 * c), 0.5 * c, "equal"),
                    (res.fun, float(res.x), "interior"),
                ]
                best_log, best_s, best_kind = min(candidates)
                allowed_log = min(candidates[0][0], candidates[1][0], candidates[2][0])
                gain = allowed_log - best_log
                # Symmetry can return c-s.  Store the canonical distance from the equal split.
                off_center = abs(best_s - 0.5 * c) / c
                if best_kind == "interior" and gain > 1e-8 and off_center > 1e-5:
                    rows.append(
                        {
                            "q": q,
                            "r": r,
                            "p0": p0,
                            "c": c,
                            "s": best_s,
                            "s_over_c": best_s / c,
                            "off_center": off_center,
                            "log_gain_vs_allowed": gain,
                            "ratio_vs_allowed": math.exp(-gain),
                        }
                    )
    rows.sort(key=lambda row: row["log_gain_vs_allowed"], reverse=True)
    return rows


def scan_two_background_blocks(
    q_values: list[float],
    r_values: list[int],
    p_values: list[float],
    order: int,
) -> list[dict]:
    rows: list[dict] = []
    for q in q_values:
        for r1 in r_values:
            for r2 in r_values:
                for p1 in p_values:
                    for p2 in p_values:
                        c = 1.0 - p1 - p2
                        if c <= 1e-10:
                            continue

                        def objective(s: float) -> float:
                            return log_group4_moment(r1, r2, q, p1, p2, s, order)

                        res = minimize_scalar(
                            objective,
                            bounds=(0.0, c),
                            method="bounded",
                            options={"xatol": 1e-12, "maxiter": 300},
                        )
                        candidates = [
                            (objective(0.0), 0.0, "endpoint"),
                            (objective(c), c, "endpoint"),
                            (objective(0.5 * c), 0.5 * c, "equal"),
                            (res.fun, float(res.x), "interior"),
                        ]
                        best_log, best_s, best_kind = min(candidates)
                        allowed_log = min(candidates[0][0], candidates[1][0], candidates[2][0])
                        gain = allowed_log - best_log
                        off_center = abs(best_s - 0.5 * c) / c
                        if best_kind == "interior" and gain > 1e-8 and off_center > 1e-5:
                            rows.append(
                                {
                                    "q": q,
                                    "r1": r1,
                                    "r2": r2,
                                    "p1": p1,
                                    "p2": p2,
                                    "c": c,
                                    "s": best_s,
                                    "s_over_c": best_s / c,
                                    "off_center": off_center,
                                    "log_gain_vs_allowed": gain,
                                    "ratio_vs_allowed": math.exp(-gain),
                                }
                            )
    rows.sort(key=lambda row: row["log_gain_vs_allowed"], reverse=True)
    return rows


def parse_float_list(text: str) -> list[float]:
    return [float(x) for x in text.split(",") if x.strip()]


def parse_int_list(text: str) -> list[int]:
    return [int(x) for x in text.split(",") if x.strip()]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["one-background", "two-background"], default="one-background")
    ap.add_argument("--q", default="5.05,5.2,5.35,5.5,5.8,6.2,6.5,7,8,10,15,20,30,50")
    ap.add_argument("--r", default="1,2,3,4,5,6,8,10,12,16,20,30,40,60")
    ap.add_argument("--p0", default="0,0.01,0.03,0.05,0.08,0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.98,0.99")
    ap.add_argument("--order", type=int, default=128)
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    if args.mode == "one-background":
        rows = scan(parse_float_list(args.q), parse_int_list(args.r), parse_float_list(args.p0), args.order)
    else:
        rows = scan_two_background_blocks(
            parse_float_list(args.q),
            parse_int_list(args.r),
            parse_float_list(args.p0),
            args.order,
        )
    if not rows:
        print("NO_OFF_CENTER_PAIR_SPLIT_MINIMA_FOUND")
        return
    for row in rows[: args.limit]:
        print(row)
    print("COUNT", len(rows))


if __name__ == "__main__":
    main()
