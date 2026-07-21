#!/usr/bin/env python3
"""Print finite-dimensional Haar lower bounds converging to the sharp constants."""

from math import gamma, pi


def complex_haar_mean(d: int) -> float:
    return gamma(d) * gamma(1.5) / gamma(d + 0.5)


def real_haar_mean(d: int) -> float:
    return gamma(d / 2) / (pi**0.5 * gamma((d + 1) / 2))


print("d  complex lower bound  real lower bound")
for dimension in (2, 4, 8, 16, 32, 64, 128):
    complex_mean = complex_haar_mean(dimension)
    real_mean = real_haar_mean(dimension)
    complex_bound = 1 / (dimension * complex_mean**2)
    real_bound = 1 / (dimension * real_mean**2)
    print(f"{dimension:3d} {complex_bound:19.12f} {real_bound:17.12f}")

print(f"limits: complex={4 / pi:.12f} real={pi / 2:.12f}")

