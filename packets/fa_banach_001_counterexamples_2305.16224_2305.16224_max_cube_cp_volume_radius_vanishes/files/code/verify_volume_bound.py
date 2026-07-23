#!/usr/bin/env python3
"""Evaluate the explicit max-cube volume-radius upper bound.

This checks arithmetic in the packet's closed formula. It is not part of the
proof of the elliptope recursion.
"""

from __future__ import annotations

import math


def log_unit_ball_volume(k: int) -> float:
    return 0.5 * k * math.log(math.pi) - math.lgamma(0.5 * k + 1.0)


def log_radius_upper_bound(n: int) -> float:
    if n < 2:
        raise ValueError("n must be at least 2")
    dimension = n * (n + 1) / 2
    log_elliptope_bound = sum(log_unit_ball_volume(k) for k in range(1, n))
    return (
        -dimension * math.log(2.0)
        + n * math.log(2.0 / (n + 1.0))
        + log_elliptope_bound
    ) / dimension


def main() -> None:
    print(" n    radius upper bound    sqrt(n) * bound")
    for n in (2, 4, 8, 16, 32, 64, 128, 256):
        radius = math.exp(log_radius_upper_bound(n))
        print(f"{n:3d}    {radius:18.12f}    {math.sqrt(n) * radius:16.12f}")


if __name__ == "__main__":
    main()
