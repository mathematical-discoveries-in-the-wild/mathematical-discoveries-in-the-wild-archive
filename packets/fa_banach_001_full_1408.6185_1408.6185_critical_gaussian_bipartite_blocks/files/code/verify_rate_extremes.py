#!/usr/bin/env python3
"""Deterministic checks for the critical Gaussian bipartite-block packet."""

from __future__ import annotations

import math


def rate(t: float) -> float:
    if t < 2.0:
        raise ValueError("rate formula is used only on [2,infinity)")
    return 0.5 * (t * math.sqrt(t * t - 4.0) - 4.0 * math.acosh(t / 2.0))


def root_for_a(a: float) -> float:
    target = 1.0 / a
    lo, hi = 2.0, 3.0
    while rate(hi) < target:
        hi *= 2.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if rate(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    assert abs(rate(2.0)) < 1e-14
    grid = [2.0 + j / 20.0 for j in range(61)]
    vals = [rate(t) for t in grid]
    assert all(y > x for x, y in zip(vals, vals[1:]))

    print("a        t_a          J(t_a)      lower exponent   upper exponent")
    for a in (0.25, 1.0, 4.0, 10.0, 100.0):
        t = root_for_a(a)
        eps = min(0.05, (t - 2.0) / 4.0)
        lower_exp = 1.0 / a - rate(t - eps)
        upper_exp = 1.0 / a - rate(t + eps)
        assert t > 2.0
        assert abs(rate(t) - 1.0 / a) < 1e-11
        assert lower_exp > 0.0 > upper_exp
        print(
            f"{a:<7g}  {t:11.8f}  {rate(t):11.8f}"
            f"  {lower_exp:14.8g}  {upper_exp:14.8g}"
        )

    for a in (1e3, 1e4, 1e5):
        t = root_for_a(a)
        leading = (3.0 / (4.0 * a)) ** (2.0 / 3.0)
        ratio = (t - 2.0) / leading
        assert abs(ratio - 1.0) < 0.02
        print(f"large-a check a={a:g}: asymptotic ratio={ratio:.10f}")

    for a in (0.5, 2.0, 20.0):
        for k in (100, 1000, 10000):
            log_n = math.log(2.0 * k) + k / a
            ratio = k / log_n
            assert ratio < a and ratio > 0.0
        print(
            f"dimension check a={a:g}: k/log(2k exp(k/a))="
            f"{ratio:.10f} -> {a:g}"
        )

    print("all deterministic checks passed")


if __name__ == "__main__":
    main()
