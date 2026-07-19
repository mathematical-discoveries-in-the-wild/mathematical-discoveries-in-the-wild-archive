"""Finite Walsh/Rademacher sanity check for the packet theorem.

This is not a proof. It verifies numerically, in finite Walsh models, the
two mechanisms used in the proof:

1. The Rademacher map e_k -> r_k is contractive from ell_2^n to L_q for
   sample q in (1, 2].
2. Positive sums of |r_k| have exactly ell_1 growth.
"""

from __future__ import annotations

import itertools
import math
import random


def sign_table(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n))


def lq_norm(values: list[float], q: float) -> float:
    return (sum(abs(v) ** q for v in values) / len(values)) ** (1.0 / q)


def unit_random_vector(n: int) -> list[float]:
    values = [random.gauss(0.0, 1.0) for _ in range(n)]
    norm = math.sqrt(sum(v * v for v in values))
    return [v / norm for v in values]


def check_contraction(n: int, q: float, trials: int = 5000) -> float:
    signs = sign_table(n)
    worst = 0.0
    for _ in range(trials):
        x = unit_random_vector(n)
        values = [sum(x_i * eps_i for x_i, eps_i in zip(x, eps)) for eps in signs]
        worst = max(worst, lq_norm(values, q))
    return worst


def positive_growth(coeffs: list[float], q: float) -> tuple[float, float]:
    n = len(coeffs)
    signs = sign_table(n)
    values = [sum(a * abs(eps_i) for a, eps_i in zip(coeffs, eps)) for eps in signs]
    return lq_norm(values, q), sum(coeffs)


def main() -> None:
    random.seed(20260608)
    for q in (1.1, 1.5, 1.9, 2.0):
        for n in (2, 4, 6):
            worst = check_contraction(n, q)
            lhs, rhs = positive_growth([1.0 + k / 10.0 for k in range(n)], q)
            print(
                f"q={q:.1f} n={n}: sampled operator norm <= {worst:.6f}; "
                f"positive growth {lhs:.6f} vs ell1 {rhs:.6f}"
            )


if __name__ == "__main__":
    main()
