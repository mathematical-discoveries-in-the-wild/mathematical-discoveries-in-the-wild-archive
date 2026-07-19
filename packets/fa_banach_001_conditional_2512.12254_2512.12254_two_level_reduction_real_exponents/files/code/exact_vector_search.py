"""Exact-formula random search for the Hunter exponential moment conjecture.

For distinct positive coefficients a_i and non-integer q,

    E(sum a_i X_i)^q / Gamma(q+1)

is the divided difference of x -> x^(q+n-1) at the nodes a_i.  This script uses
that formula for fast arbitrary-vector screening and validates the best rows
with high-precision mpmath divided differences.
"""

from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np
from scipy.special import gammaln


def log_rho(m: int, q: float) -> float:
    return gammaln(m + q) - gammaln(m) - 0.5 * q * math.log(m)


def log_min_rho(n: int, q: float) -> tuple[float, int]:
    vals = [(log_rho(m, q), m) for m in range(1, n + 1)]
    return min(vals)


def divided_difference(nodes: np.ndarray, power: float) -> float:
    dd = np.power(nodes.astype(float), power)
    work = dd.copy()
    n = len(nodes)
    for k in range(1, n):
        work[: n - k] = (work[1 : n - k + 1] - work[: n - k]) / (nodes[k:] - nodes[: n - k])
    return float(work[0])


def log_moment_fast(a: np.ndarray, q: float) -> float:
    a = np.sort(a[a > 1e-14])
    n = len(a)
    if n == 1:
        return gammaln(q + 1.0) + q * math.log(float(a[0]))
    val = divided_difference(a, q + n - 1.0)
    if not math.isfinite(val) or val <= 0.0:
        return float("nan")
    return gammaln(q + 1.0) + math.log(val)


def log_moment_mp(a: np.ndarray, q: float, dps: int) -> mp.mpf:
    nodes = [mp.mpf(str(x)) for x in sorted(float(y) for y in a if y > 1e-14)]
    n = len(nodes)
    mp.mp.dps = dps
    if n == 1:
        return mp.loggamma(q + 1) + q * mp.log(nodes[0])
    power = mp.mpf(str(q + n - 1.0))
    work = [x**power for x in nodes]
    for k in range(1, n):
        work = [(work[i + 1] - work[i]) / (nodes[i + k] - nodes[i]) for i in range(n - k)]
    return mp.loggamma(q + 1) + mp.log(work[0])


def random_masses(n: int, count: int, rng: np.random.Generator) -> np.ndarray:
    rows = []
    for m in range(1, n + 1):
        p = np.zeros(n)
        p[:m] = 1.0 / m
        rows.append(p)
    for alpha in [0.03, 0.06, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 12.0]:
        take = max(1, count // 9)
        rows.extend(rng.dirichlet(np.full(n, alpha), size=take))
    out = np.asarray(rows)
    return out[:count]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", default="5,6,8,10,12,16,20,30")
    ap.add_argument("--q", default="5.05,5.2,5.35,5.5,5.8,6.2,6.5,7,8,10,15,20,30,50")
    ap.add_argument("--count", type=int, default=20000)
    ap.add_argument("--validate", type=int, default=5)
    ap.add_argument("--dps", type=int, default=100)
    args = ap.parse_args()

    rng = np.random.default_rng(8675309)
    for n in [int(x) for x in args.n.split(",") if x]:
        masses = random_masses(n, args.count, rng)
        # Jitter the exact equal-support rows very slightly for the distinct-node formula.
        jitter = rng.normal(scale=1e-9, size=masses.shape)
        masses = np.maximum(masses + jitter, 0.0)
        masses = masses / masses.sum(axis=1, keepdims=True)
        coeffs = np.sqrt(masses)
        for q in [float(x) for x in args.q.split(",") if x]:
            target, target_m = log_min_rho(n, q)
            gaps = []
            for a in coeffs:
                lm = log_moment_fast(a, q)
                gaps.append(lm - target)
            gaps_arr = np.asarray(gaps)
            finite = np.isfinite(gaps_arr)
            order = np.argsort(gaps_arr[finite])[: args.validate]
            finite_coeffs = coeffs[finite]
            best_rows = []
            for idx in order:
                a = finite_coeffs[int(idx)]
                lm_mp = log_moment_mp(a, q, args.dps)
                gap_mp = lm_mp - mp.mpf(str(target))
                best_rows.append(
                    {
                        "log_gap_mp": float(gap_mp),
                        "ratio_mp": float(mp.e**gap_mp),
                        "support_rough": int(np.sum(a > 1e-5)),
                        "top_coeffs": sorted([float(x) for x in a if x > 1e-5], reverse=True)[:10],
                    }
                )
            print({"n": n, "q": q, "target_m": target_m, "best": best_rows[0], "validated": best_rows}, flush=True)


if __name__ == "__main__":
    main()
