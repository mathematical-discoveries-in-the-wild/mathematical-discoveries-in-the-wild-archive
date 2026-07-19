"""Sanity checks for the 0611160 Rademacher partial packet.

The proof packet is deterministic.  This script only checks the two finite
matrix inequalities used in the proof on random small examples.
"""

from __future__ import annotations

import itertools

import numpy as np


def trace_norm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False).sum())


def row_trace_norm(xs: list[np.ndarray]) -> float:
    row = np.concatenate(xs, axis=1)
    return trace_norm(row)


def two_term_average(x: np.ndarray, y: np.ndarray) -> float:
    return 0.5 * (trace_norm(x + y) + trace_norm(x - y))


def diagonal_norm_formula(diag_entries: np.ndarray) -> float:
    # diag_entries has shape (d, n); row k is the coefficient vector at the
    # kth diagonal point.
    return float(np.sqrt(np.sum(np.abs(diag_entries) ** 2, axis=0)).sum())


def diagonal_rademacher_average(diag_entries: np.ndarray) -> float:
    d, _ = diag_entries.shape
    total = 0.0
    for signs in itertools.product([-1.0, 1.0], repeat=d):
        signed = np.tensordot(np.array(signs), diag_entries, axes=(0, 0))
        total += float(np.abs(signed).sum())
    return total / (2**d)


def main() -> None:
    rng = np.random.default_rng(611160)
    sqrt2 = np.sqrt(2.0)

    for n in range(1, 6):
        for _ in range(200):
            x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            lhs = row_trace_norm([x, y])
            rhs = sqrt2 * two_term_average(x, y)
            if lhs > rhs + 1e-8:
                raise AssertionError((n, lhs, rhs))

    for d in range(1, 7):
        for n in range(1, 7):
            for _ in range(100):
                entries = rng.normal(size=(d, n)) + 1j * rng.normal(size=(d, n))
                norm = diagonal_norm_formula(entries)
                avg = diagonal_rademacher_average(entries)
                if avg + 1e-8 < norm / sqrt2:
                    raise AssertionError((d, n, avg, norm / sqrt2))

    print("sanity checks passed")


if __name__ == "__main__":
    main()
