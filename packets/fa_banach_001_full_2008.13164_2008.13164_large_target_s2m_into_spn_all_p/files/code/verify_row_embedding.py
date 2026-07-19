"""Numerical sanity check for the row embedding S_2^m -> S_p^n.

This is not part of the proof.  It samples complex matrices A, embeds vec(A)
as the first row of an n x n matrix, and checks that the Schatten p norms
agree with the Hilbert-Schmidt norm.
"""

from __future__ import annotations

import math

import numpy as np


def schatten_norm(matrix: np.ndarray, p: float | str) -> float:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    if p == "inf":
        return float(singular_values[0])
    return float(np.sum(singular_values**float(p)) ** (1.0 / float(p)))


def row_embed(matrix: np.ndarray, n: int) -> np.ndarray:
    vector = matrix.reshape(-1)
    if n < vector.size:
        raise ValueError("n must be at least m^2")
    out = np.zeros((n, n), dtype=complex)
    out[0, : vector.size] = vector
    return out


def main() -> None:
    rng = np.random.default_rng(200813164)
    ps: list[float | str] = [1.0, 1.3, 2.0, 3.0, 4.7, "inf"]
    for m in [1, 2, 3, 5]:
        n = m * m
        for _ in range(25):
            a = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
            hs = float(np.linalg.norm(a.reshape(-1)))
            embedded = row_embed(a, n)
            for p in ps:
                got = schatten_norm(embedded, p)
                if not math.isclose(got, hs, rel_tol=5e-12, abs_tol=5e-12):
                    raise AssertionError((m, n, p, got, hs))
    print("row embedding sanity checks passed")


if __name__ == "__main__":
    main()
