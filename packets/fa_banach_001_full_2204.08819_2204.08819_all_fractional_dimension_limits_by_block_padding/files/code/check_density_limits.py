"""Numerical sanity checks for the density formula in the solution packet."""

from __future__ import annotations

from math import floor, sqrt


def density(r: int, k: int) -> float:
    if r < 1 or k < 0:
        raise ValueError("require r >= 1 and k >= 0")
    return (7 * r + k * k) / (4 * r + k) ** 2


def approximant(theta: float, r: int) -> tuple[int, float]:
    if not 0.0 < theta < 1.0:
        raise ValueError("require 0 < theta < 1")
    lam = 4.0 * sqrt(theta) / (1.0 - sqrt(theta))
    k = floor(lam * r)
    return k, density(r, k)


def main() -> None:
    print("Endpoint checks")
    for r in (10, 100, 10_000):
        print(f"  r={r:>5}, k=0:       density={density(r, 0):.10f}")
    for k in (10, 100, 10_000):
        print(f"  r=1, k={k:>5}: density={density(1, k):.10f}")

    print("\nInterior targets (r=10000)")
    for theta in (0.01, 0.10, 0.25, 0.50, 0.90, 0.99):
        k, value = approximant(theta, 10_000)
        print(
            f"  theta={theta:.2f}, k={k:>8}: "
            f"density={value:.10f}, error={abs(value - theta):.3e}"
        )


if __name__ == "__main__":
    main()

