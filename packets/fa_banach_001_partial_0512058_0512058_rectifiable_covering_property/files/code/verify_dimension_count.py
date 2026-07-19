"""Sanity checks for the rectifiable covering-property packet.

The packet proof is geometric-measure theoretic. This script only checks the
dimension identity for the incidence space and samples the elementary tangent
estimate |A theta| <= ||A||_HS used behind the uniform Jacobian bound.
"""

from __future__ import annotations

import math
import random


def hs_norm(matrix: list[list[float]]) -> float:
    return math.sqrt(sum(x * x for row in matrix for x in row))


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def euclidean_norm(vector: list[float]) -> float:
    return math.sqrt(sum(x * x for x in vector))


def random_unit_vector(dim: int) -> list[float]:
    values = [random.gauss(0.0, 1.0) for _ in range(dim)]
    norm = euclidean_norm(values)
    return [x / norm for x in values]


def main() -> None:
    random.seed(512058)
    for n in range(3, 12):
        for k in range(1, n):
            m = n - k
            incidence_dim = k + (m - 1)
            assert incidence_dim == n - 1
            for _ in range(100):
                theta = random_unit_vector(m)
                matrix = [[random.gauss(0.0, 1.0) for _ in range(m)] for _ in range(k)]
                assert euclidean_norm(mat_vec(matrix, theta)) <= hs_norm(matrix) + 1e-12
        print(f"n={n}: incidence dimension and tangent estimate checked")


if __name__ == "__main__":
    main()

