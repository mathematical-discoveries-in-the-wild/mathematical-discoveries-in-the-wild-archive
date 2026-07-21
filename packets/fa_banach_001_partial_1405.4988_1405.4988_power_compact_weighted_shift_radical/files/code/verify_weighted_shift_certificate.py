#!/usr/bin/env python3
"""Finite audits for the weighted-shift tail-nest certificate.

The proof is analytic.  This script checks the combinatorial propagation of
forced zeros and several finite matrix identities used in the proof.
"""

from __future__ import annotations

import numpy as np


def forced_positions(n: int) -> set[tuple[int, int]]:
    """Positions b[i,k] forced to zero by the boundary recursion."""
    forced = {(0, k) for k in range(1, n)}
    for i in range(1, n):
        for k in range(i + 1, n):
            if (i - 1, k - 1) not in forced:
                raise AssertionError("induction predecessor was not forced")
            forced.add((i, k))
    return forced


def sample_audit(n: int, seed: int) -> tuple[float, float, int]:
    rng = np.random.default_rng(seed)
    alpha = 0.2 + rng.random(n - 1)
    a = np.zeros((n, n))
    for j, weight in enumerate(alpha):
        a[j + 1, j] = weight

    # A decreasing positive diagonal B gives a nonzero positive commutator.
    drops = 0.1 + rng.random(n)
    diagonal = np.cumsum(drops[::-1])[::-1]
    b = np.diag(diagonal)
    c = a @ b - b @ a

    min_entry = float(c.min())
    max_diagonal = float(np.max(np.abs(np.diag(c))))
    nonzero_entries = int(np.count_nonzero(np.abs(c) > 1e-12))
    if min_entry < -1e-12:
        raise AssertionError("sample commutator is not positive")
    if max_diagonal > 1e-12:
        raise AssertionError("sample commutator diagonal is not zero")
    if nonzero_entries == 0:
        raise AssertionError("sample commutator should be nonzero")
    return min_entry, max_diagonal, nonzero_entries


def main() -> None:
    for n in (3, 5, 10, 25):
        forced = forced_positions(n)
        expected = {(i, k) for i in range(n) for k in range(i + 1, n)}
        if forced != expected:
            raise AssertionError(f"forced-zero set mismatch at n={n}")
        min_entry, max_diagonal, nonzero = sample_audit(n, 1000 + n)
        print(
            f"n={n:2d} forced={len(forced):3d} "
            f"min(C)={min_entry:.3e} max|diag(C)|={max_diagonal:.3e} "
            f"nnz(C)={nonzero}"
        )
    print("all weighted-shift certificate audits passed")


if __name__ == "__main__":
    main()

