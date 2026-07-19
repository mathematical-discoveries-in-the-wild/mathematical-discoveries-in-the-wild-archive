"""Sanity checks for the c0 inside ell_infty radius counterexample.

The proof is exact. This script just illustrates the radius computations for
finite prefixes and the limiting obstruction in c0.
"""

from __future__ import annotations


def sup_distance_to_basis(center: list[float], n: int) -> float:
    """Max distance from center to e_1,...,e_n in l_infty^n."""
    worst = 0.0
    for j in range(n):
        dist = 0.0
        for k, value in enumerate(center):
            target = 1.0 if k == j else 0.0
            dist = max(dist, abs(value - target))
        worst = max(worst, dist)
    return worst


def main() -> None:
    for n in [2, 3, 5, 10]:
        center = [0.5] * n
        print(f"finite prefix n={n}: radius at constant 1/2 center = {sup_distance_to_basis(center, n):.3f}")

    tail_centers = {
        "zero": [0.0] * 20,
        "decay_1_over_n": [1.0 / (k + 1) for k in range(20)],
        "first_ten_half_then_zero": [0.5 if k < 10 else 0.0 for k in range(20)],
    }
    for name, center in tail_centers.items():
        print(f"20-point sample for c0-like center {name}: radius = {sup_distance_to_basis(center, 20):.3f}")

    print("Exact infinite result: rad_{ell_infty}({e_n}) = 1/2 and rad_{c0}({e_n}) = 1.")


if __name__ == "__main__":
    main()

