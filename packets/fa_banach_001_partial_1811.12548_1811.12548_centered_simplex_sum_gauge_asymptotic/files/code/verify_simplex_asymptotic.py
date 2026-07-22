#!/usr/bin/env python3
"""Numerical sanity checks for the centered-simplex gauge asymptotic.

The analytic proof does not depend on this script.  It checks two quantities:
1. the exact scaled minimum of m iid Gamma(2,1) variables by quadrature;
2. m^(3/2) min_i(P_i+Q_i) for independent flat Dirichlet vectors.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln


RAYLEIGH_MEAN = math.sqrt(math.pi / 2.0)


def gamma_min_scaled_mean(m: int) -> float:
    """Return E[sqrt(m) min_{i<=m} Z_i], Z_i iid Gamma(2,1)."""

    def survival(t: float) -> float:
        z = t / math.sqrt(m)
        return math.exp(m * (-z + math.log1p(z)))

    value, _ = quad(survival, 0.0, math.inf, epsabs=2e-11, epsrel=2e-11)
    return value


def simplex_scaled_mean(m: int, samples: int, seed: int) -> tuple[float, float]:
    """Monte Carlo mean and standard error of m^(3/2) min(P_i+Q_i)."""

    rng = np.random.default_rng(seed)
    batch = min(4096, samples)
    total = 0.0
    total_sq = 0.0
    done = 0
    while done < samples:
        count = min(batch, samples - done)
        e = rng.exponential(size=(count, m))
        f = rng.exponential(size=(count, m))
        p = e / e.sum(axis=1, keepdims=True)
        q = f / f.sum(axis=1, keepdims=True)
        values = (m ** 1.5) * np.min(p + q, axis=1)
        total += float(values.sum())
        total_sq += float(values @ values)
        done += count
    mean = total / samples
    variance = max(0.0, total_sq / samples - mean * mean)
    return mean, math.sqrt(variance / samples)


def cube_scaled_deficit(n: int) -> float:
    """Return sqrt(n) times the exact cube deficit."""

    log_ratio = n * math.log(4.0) - (
        gammaln(2 * n + 1) - 2.0 * gammaln(n + 1)
    )
    deficit = 2.0 * math.exp(log_ratio) / (2 * n + 1)
    return math.sqrt(n) * deficit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=40000)
    parser.add_argument("--seed", type=int, default=181112548)
    args = parser.parse_args()

    print(f"Rayleigh limiting mean: {RAYLEIGH_MEAN:.9f}")
    print("\nExact unnormalized Gamma-min check")
    last = None
    for m in (16, 64, 256, 1024, 4096):
        value = gamma_min_scaled_mean(m)
        print(f"m={m:4d}  scaled_mean={value:.9f}  error={value-RAYLEIGH_MEAN:+.3e}")
        last = value
    assert last is not None and abs(last - RAYLEIGH_MEAN) < 0.02

    print("\nNormalized Dirichlet Monte Carlo check")
    for index, m in enumerate((32, 128, 512)):
        value, se = simplex_scaled_mean(m, args.samples, args.seed + index)
        print(
            f"m={m:4d}  scaled_mean={value:.9f}  se={se:.3e}  "
            f"error={value-RAYLEIGH_MEAN:+.3e}"
        )
        if m == 512:
            assert abs(value - RAYLEIGH_MEAN) < 0.08

    print("\nCube comparison")
    cube_value = cube_scaled_deficit(4096)
    print(f"sqrt(n) cube deficit at n=4096: {cube_value:.9f}")
    print(f"limit sqrt(pi): {math.sqrt(math.pi):.9f}")
    print(f"simplex/cube limiting deficit ratio: {1/math.sqrt(2):.9f}")
    assert abs(cube_value - math.sqrt(math.pi)) < 0.03
    print("\nPASS")


if __name__ == "__main__":
    main()

