"""Finite sanity checks for the L2 constant computation.

The proof in the packet is analytic. This script only verifies, for small
finite cubes and overlap patterns, that the operator norm behind c_n is
sqrt(2) by building the corresponding quadratic form.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def cube(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((0, 1), repeat=n))


def coupling_matrix(n: int, shared: tuple[int, ...]) -> np.ndarray:
    pts = cube(n)
    index = {x: i for i, x in enumerate(pts)}
    N = len(pts)
    mat = np.zeros((N, N), dtype=float)
    count = 0
    for x in pts:
        for y in pts:
            if all(x[i] == y[i] for i in shared):
                mat[index[x], index[y]] += 1.0
                count += 1
    return mat / count


def max_distance_squared(n: int, shared: tuple[int, ...]) -> float:
    N = 2**n
    joint = coupling_matrix(n, shared)
    # E[(F(X)-F(Y))^2] = 2 E[F^2] - 2 E[F(X)F(Y)].
    # With uniform L2 norm E[F^2]=1, this is the largest generalized
    # eigenvalue of the quadratic form below relative to (1/N) I.
    q = (2.0 / N) * np.eye(N) - 2.0 * joint
    gram = (1.0 / N) * np.eye(N)
    eigs = np.linalg.eigvalsh(np.linalg.solve(gram, q))
    return float(eigs[-1])


def main() -> None:
    for n in range(1, 6):
        values = []
        for r in range(n + 1):
            for shared in itertools.combinations(range(n), r):
                values.append(max_distance_squared(n, shared))
        top = max(values)
        print(f"n={n}: max squared distance {top:.12f}, max distance {math.sqrt(top):.12f}")
        assert abs(top - 2.0) < 1e-9


if __name__ == "__main__":
    main()
