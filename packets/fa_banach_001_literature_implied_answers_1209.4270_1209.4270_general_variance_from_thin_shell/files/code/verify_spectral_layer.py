#!/usr/bin/env python3
"""Seeded smoke test for the deterministic spectral-layer identities."""

from __future__ import annotations

import numpy as np


def check_once(rng: np.random.Generator, dimension: int) -> None:
    mu = np.sort(rng.exponential(size=dimension))[::-1]
    centered_squares = rng.normal(size=dimension)

    direct = float(mu @ centered_squares)
    extended = np.concatenate((mu, [0.0]))
    increments = extended[:-1] - extended[1:]
    abel = float(increments @ np.cumsum(centered_squares))
    if not np.isclose(direct, abel, rtol=2.0e-13, atol=2.0e-13):
        raise AssertionError((direct, abel))

    spectral_sum = float(increments @ np.sqrt(np.arange(1, dimension + 1)))
    bound = float(np.sqrt(mu[0] * np.sum(mu)))
    if spectral_sum > bound * (1.0 + 2.0e-13):
        raise AssertionError((spectral_sum, bound, mu))


def main() -> None:
    rng = np.random.default_rng(12094270)
    checks = 0
    for dimension in range(1, 101):
        for _ in range(200):
            check_once(rng, dimension)
            checks += 1
    print(f"spectral-layer checks passed: {checks}")


if __name__ == "__main__":
    main()

