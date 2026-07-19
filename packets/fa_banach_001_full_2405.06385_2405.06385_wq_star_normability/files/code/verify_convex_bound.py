"""Finite-dimensional sanity check for the convex-hull normability packet.

The proof is analytic. This script only verifies the scalar Hilbert-space
inequality behind the current estimate and the resulting levelwise bound for
random finite convex combinations.
"""

from __future__ import annotations

import random


def random_simplex(n: int) -> list[float]:
    xs = [random.random() for _ in range(n)]
    s = sum(xs)
    return [x / s for x in xs]


def check_jensen(trials: int = 1000) -> None:
    for _ in range(trials):
        n = random.randint(2, 8)
        weights = random_simplex(n)
        vectors = [complex(random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(n)]
        lhs = abs(sum(w * z for w, z in zip(weights, vectors))) ** 2
        rhs = sum(w * abs(z) ** 2 for w, z in zip(weights, vectors))
        assert lhs <= rhs + 1e-12


def check_level_bound(q: int, trials: int = 1000) -> None:
    for _ in range(trials):
        n = random.randint(2, 8)
        weights = random_simplex(n)
        masses = []
        for _i in range(n):
            row = []
            remaining = random.random()
            for j in range(1, q + 1):
                term = remaining * random.random()
                row.append(term ** (2**j))
            masses.append(row)
        combined_terms = []
        for j in range(q):
            combined_mass = sum(weights[i] * masses[i][j] for i in range(n))
            combined_terms.append(combined_mass ** (1 / (2 ** (j + 1))))
        assert sum(combined_terms) <= q + 1e-12


def main() -> None:
    random.seed(240506385)
    check_jensen()
    for q in range(1, 8):
        check_level_bound(q)
        print(f"q={q}: convex-hull quasinorm bound <= q verified in samples")


if __name__ == "__main__":
    main()

