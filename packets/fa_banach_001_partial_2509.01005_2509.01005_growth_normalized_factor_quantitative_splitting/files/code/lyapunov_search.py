"""Numerical stress test for the quantitative tensor-splitting question.

For a finite-dimensional generator A, the optimal similarity constant is
the minimum of sqrt(cond(P)) over P>0 satisfying A^*P+PA<=0.  We optimize
this scale-invariant problem over P=exp(H), trace(H)=0, and compare the
tensor-product generator with the best zero-sum scalar splitting.

This is exploratory only; durable mathematical claims must be proved
independently of the numerical output.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.linalg import expm, logm, solve_continuous_lyapunov
from scipy.optimize import minimize, minimize_scalar


def sym_from_x(x: np.ndarray, n: int) -> np.ndarray:
    """Trace-zero real symmetric matrix from n(n+1)/2-1 coordinates."""
    h = np.zeros((n, n), dtype=float)
    k = 0
    for i in range(n):
        for j in range(i, n):
            if i == n - 1 and j == n - 1:
                continue
            h[i, j] = x[k]
            h[j, i] = x[k]
            k += 1
    h[-1, -1] = -np.trace(h)
    return h


def x_from_sym(h: np.ndarray) -> np.ndarray:
    n = h.shape[0]
    h = (h + h.T) / 2
    h = h - np.trace(h) * np.eye(n) / n
    out = []
    for i in range(n):
        for j in range(i, n):
            if i == n - 1 and j == n - 1:
                continue
            out.append(h[i, j])
    return np.asarray(out)


def similarity_constant(a: np.ndarray, restarts: int = 2) -> tuple[float, float]:
    n = a.shape[0]
    spectral = np.max(np.real(np.linalg.eigvals(a)))
    if spectral > 1e-9:
        return math.inf, spectral
    if np.max(np.linalg.eigvalsh((a + a.T) / 2)) <= 1e-10:
        return 1.0, spectral
    if spectral >= -1e-9:
        # Boundary cases are deliberately excluded from this exploratory search.
        return math.inf, spectral

    p0 = solve_continuous_lyapunov(a.T, -np.eye(n))
    p0 = (p0 + p0.T) / 2
    h0 = np.real(logm(p0))
    x0 = x_from_sym(h0)

    def unpack(x: np.ndarray) -> np.ndarray:
        return expm(sym_from_x(x, n))

    def objective(x: np.ndarray) -> float:
        ev = np.linalg.eigvalsh(sym_from_x(x, n))
        return 0.5 * (ev[-1] - ev[0])

    def constraint(x: np.ndarray) -> float:
        p = unpack(x)
        lyap = a.T @ p + p @ a
        return -np.max(np.linalg.eigvalsh((lyap + lyap.T) / 2))

    best = math.inf
    rng = np.random.default_rng(137)
    starts = [x0]
    starts.extend(x0 + 0.15 * rng.normal(size=x0.shape) for _ in range(restarts))
    for start in starts:
        result = minimize(
            objective,
            start,
            method="SLSQP",
            constraints={"type": "ineq", "fun": constraint},
            options={"maxiter": 1200, "ftol": 2e-10, "disp": False},
        )
        if result.success and constraint(result.x) >= -2e-7:
            best = min(best, math.exp(objective(result.x)))
    return best, spectral


def operator_similarity_constant(t: np.ndarray, restarts: int = 2) -> tuple[float, float]:
    """Optimal contraction-similarity constant via the Stein inequality."""
    n = t.shape[0]
    radius = np.max(np.abs(np.linalg.eigvals(t)))
    if radius > 1 + 1e-9:
        return math.inf, radius
    if np.linalg.norm(t, 2) <= 1 + 1e-10:
        return 1.0, radius
    if radius >= 1 - 1e-9:
        return math.inf, radius

    # Convergent observability Gramian sum_{k>=0} (T*)^k T^k.
    p0 = np.eye(n)
    term = np.eye(n)
    for _ in range(10000):
        term = t.T @ term @ t
        p0 += term
        if np.linalg.norm(term, 2) < 1e-13:
            break
    h0 = np.real(logm((p0 + p0.T) / 2))
    x0 = x_from_sym(h0)

    def unpack(x: np.ndarray) -> np.ndarray:
        return expm(sym_from_x(x, n))

    def objective(x: np.ndarray) -> float:
        ev = np.linalg.eigvalsh(sym_from_x(x, n))
        return 0.5 * (ev[-1] - ev[0])

    def constraint(x: np.ndarray) -> float:
        p = unpack(x)
        stein = t.T @ p @ t - p
        return -np.max(np.linalg.eigvalsh((stein + stein.T) / 2))

    best = math.inf
    rng = np.random.default_rng(421)
    starts = [x0]
    starts.extend(x0 + 0.15 * rng.normal(size=x0.shape) for _ in range(restarts))
    for start in starts:
        result = minimize(
            objective,
            start,
            method="SLSQP",
            constraints={"type": "ineq", "fun": constraint},
            options={"maxiter": 1200, "ftol": 2e-10, "disp": False},
        )
        if result.success and constraint(result.x) >= -2e-7:
            best = min(best, math.exp(objective(result.x)))
    return best, radius


def operator_split_constant(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    ra = np.max(np.abs(np.linalg.eigvals(a)))
    rb = np.max(np.abs(np.linalg.eigvals(b)))
    lo = math.log(rb) + 2e-4
    hi = -math.log(ra) - 2e-4
    if not lo < hi:
        return math.inf, math.nan
    cache: dict[float, float] = {}

    def f(log_alpha: float) -> float:
        key = round(float(log_alpha), 8)
        if key not in cache:
            alpha = math.exp(log_alpha)
            c1, _ = operator_similarity_constant(alpha * a, restarts=0)
            c2, _ = operator_similarity_constant(b / alpha, restarts=0)
            cache[key] = max(c1, c2)
        return cache[key]

    result = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 2e-4})
    return float(result.fun), math.exp(float(result.x))


def kron_sum(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, np.eye(b.shape[0])) + np.kron(np.eye(a.shape[0]), b)


def split_constant(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    wa = np.max(np.real(np.linalg.eigvals(a)))
    wb = np.max(np.real(np.linalg.eigvals(b)))
    lo = wb + 2e-4
    hi = -wa - 2e-4
    if not lo < hi:
        return math.inf, math.nan

    cache: dict[float, float] = {}

    def f(d: float) -> float:
        key = round(float(d), 8)
        if key not in cache:
            c1, _ = similarity_constant(a + d * np.eye(a.shape[0]), restarts=0)
            c2, _ = similarity_constant(b - d * np.eye(b.shape[0]), restarts=0)
            cache[key] = max(c1, c2)
        return cache[key]

    result = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 2e-4})
    return float(result.fun), float(result.x)


def random_triangular(rng: np.random.Generator) -> np.ndarray:
    rates = rng.uniform(0.08, 1.6, size=2)
    off = rng.uniform(-5.0, 5.0)
    return np.array([[-rates[0], off], [0.0, -rates[1]]])


def random_stable_operator(rng: np.random.Generator) -> np.ndarray:
    diag = rng.uniform(-0.9, 0.9, size=2)
    off = rng.uniform(-3.5, 3.5)
    return np.array([[diag[0], off], [0.0, diag[1]]])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=12)
    parser.add_argument("--discrete", action="store_true")
    args = parser.parse_args()
    rng = np.random.default_rng(250901005)
    records = []
    for j in range(args.samples):
        if args.discrete:
            a = random_stable_operator(rng)
            b = random_stable_operator(rng)
            cp, _ = operator_similarity_constant(np.kron(a, b), restarts=1)
            cs, d = operator_split_constant(a, b)
        else:
            a = random_triangular(rng)
            b = random_triangular(rng)
            cp, _ = similarity_constant(kron_sum(a, b), restarts=1)
            cs, d = split_constant(a, b)
        ratio = cs / cp
        records.append((ratio, cp, cs, d, a, b))
        print(f"{j:03d} ratio={ratio:.6f} product={cp:.6f} split={cs:.6f} d={d:.6f}")
    print("\nLargest ratios")
    for ratio, cp, cs, d, a, b in sorted(records, reverse=True, key=lambda z: z[0])[:5]:
        print(f"ratio={ratio:.8f} product={cp:.8f} split={cs:.8f} d={d:.8f}")
        print("A=", repr(a))
        print("B=", repr(b))


if __name__ == "__main__":
    main()
