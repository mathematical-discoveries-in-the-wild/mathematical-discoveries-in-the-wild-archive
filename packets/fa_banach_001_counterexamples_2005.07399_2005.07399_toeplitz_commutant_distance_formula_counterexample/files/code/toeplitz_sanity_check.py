"""Finite-section sanity check for the Toeplitz counterexample packet.

This does not prove the theorem. It checks the finite-dimensional shadow of
the analytic mechanism: the alternating diagonal has commutator norm 2 with the
unilateral shift truncations.
"""

import numpy as np


def op_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False)[0])


def shift(n: int) -> np.ndarray:
    s = np.zeros((n, n), dtype=complex)
    for j in range(n - 1):
        s[j + 1, j] = 1.0
    return s


def alternating_diagonal(n: int) -> np.ndarray:
    return np.diag([(-1) ** j for j in range(n)]).astype(complex)


def main() -> None:
    for n in [4, 8, 16, 32, 64]:
        s = shift(n)
        d = alternating_diagonal(n)
        comm = d @ s - s @ d
        print(f"n={n:2d} ||DS-SD||={op_norm(comm):.12f}")


if __name__ == "__main__":
    main()
