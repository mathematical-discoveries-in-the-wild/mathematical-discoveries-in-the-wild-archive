#!/usr/bin/env python3
"""Numerically check the critical point in the logarithmic example.

This script is only a reproducibility check.  The packet proves uniqueness
analytically from the derivative of q(t)=2t/(1+t)-log(1+t).
"""

from math import log


def q(t: float) -> float:
    return 2.0 * t / (1.0 + t) - log(1.0 + t)


left, right = 1.0, 10.0
for _ in range(100):
    mid = (left + right) / 2.0
    if q(mid) > 0.0:
        left = mid
    else:
        right = mid

t_star = (left + right) / 2.0
print(f"t_star={t_star:.12f}")
print(f"q(t_star)={q(t_star):.3e}")
print(f"q(t_star/2)={q(t_star / 2.0):.6f}")
print(f"q(2*t_star)={q(2.0 * t_star):.6f}")

