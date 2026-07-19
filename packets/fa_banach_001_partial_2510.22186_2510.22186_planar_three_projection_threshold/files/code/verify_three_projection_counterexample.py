"""Verify sample cases of the n=3, D=2d-1 sorting-embedding obstruction.

The proof packet gives a symbolic construction for normalized keys
A = [I_d | B] in R^{d x (2d-1)}.  If c spans ker(B^T), then the construction
chooses row permutations P_i and column vectors x_i so that

    sum_i b_{ij} (P_i - I) x_i = 0

for every extra column b_j of B, while the P_i are not all compatible with a
single common row permutation.  This script checks representative normalized
full-support and singleton-support cases, including the original d=2 case.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def beta(A: np.ndarray, X: np.ndarray) -> np.ndarray:
    """Columnwise sorted projection matrix."""
    return np.sort(X @ A, axis=0)


def same_orbit(X: np.ndarray, Y: np.ndarray, tol: float = 1e-10) -> bool:
    for perm in itertools.permutations(range(X.shape[0])):
        if np.allclose(X[list(perm), :], Y, atol=tol, rtol=0):
            return True
    return False


def full_spark_counterexample(lam: float, mu: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abs(lam * mu) == 0:
        raise ValueError("full-spark normalized case requires lambda*mu != 0")

    r = lam / mu
    x = np.array([0.0, 1.0, 3.0])
    y = np.array([0.0, 2.0 * r, -r])
    cycle = [1, 2, 0]
    inv_cycle = [2, 0, 1]
    X = np.column_stack([x, y])
    Y = np.column_stack([x[cycle], y[inv_cycle]])
    A = np.array([[1.0, 0.0, lam], [0.0, 1.0, mu]])
    return A, X, Y


def redundant_planar_counterexample(horizontal: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]])
    Y = np.array([[0.0, 1.0], [1.0, 2.0], [2.0, 0.0]])
    if horizontal:
        A = np.array([[1.0, 0.0, 2.0], [0.0, 1.0, 0.0]])
    else:
        A = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, -3.0]])
    return A, X, Y


def cycle_matrix(kind: str) -> np.ndarray:
    if kind == "C":
        return np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]])
    if kind == "Ci":
        return np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    if kind == "I":
        return np.eye(3)
    raise ValueError(kind)


def solve_difference(P: np.ndarray, u: np.ndarray) -> np.ndarray:
    """Solve (P-I)x=u with the normalization sum(x)=0."""
    M = np.vstack([P - np.eye(3), np.ones((1, 3))])
    rhs = np.concatenate([u, [0.0]])
    x, *_ = np.linalg.lstsq(M, rhs, rcond=None)
    if not np.allclose((P - np.eye(3)) @ x, u, atol=1e-9, rtol=0):
        raise AssertionError("failed to solve cycle difference equation")
    return x


def kernel_vector(B: np.ndarray) -> np.ndarray:
    _, _, vh = np.linalg.svd(B.T)
    return vh[-1, :]


def general_normalized_counterexample(B: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Construct X,Y for A=[I|B], following the packet proof."""
    d = B.shape[0]
    c = kernel_vector(B)
    support = [i for i, value in enumerate(c) if abs(value) > 1e-9]
    if not support:
        raise AssertionError("empty support for kernel vector")

    P_kinds = ["I"] * d
    x_cols = [np.zeros(3) for _ in range(d)]

    if len(support) == 1:
        p = support[0]
        q = 0 if p != 0 else 1
        P_kinds[p] = "C"
        x_cols[p] = np.array([0.0, 1.0, 3.0])
        x_cols[q] = np.array([0.0, 2.0, 5.0])
    else:
        p, q = support[:2]
        for i in support:
            P_kinds[i] = "C"
        P_kinds[q] = "Ci"

        candidates = [
            np.array([1.0, -1.0, 0.0]),
            np.array([2.0, -1.0, -1.0]),
            np.array([1.0, 2.0, -3.0]),
            np.array([3.0, -5.0, 2.0]),
        ]
        for w in candidates:
            trial = list(x_cols)
            ok = True
            for i in support:
                P = cycle_matrix(P_kinds[i])
                trial[i] = solve_difference(P, c[i] * w)
                if min(abs(trial[i][a] - trial[i][b]) for a in range(3) for b in range(a + 1, 3)) < 1e-8:
                    ok = False
                    break
            if ok:
                x_cols = trial
                break
        else:
            raise AssertionError("candidate w choices all produced repeated coordinates")

    X = np.column_stack(x_cols)
    Y = np.column_stack([cycle_matrix(kind) @ x for kind, x in zip(P_kinds, x_cols)])
    A = np.column_stack([np.eye(d), B])
    return A, X, Y


def check_case(A: np.ndarray, X: np.ndarray, Y: np.ndarray) -> None:
    bx = beta(A, X)
    by = beta(A, Y)
    if not np.allclose(bx, by, atol=1e-10, rtol=0):
        raise AssertionError(f"sorted projections differ:\n{bx}\n{by}")
    if same_orbit(X, Y):
        raise AssertionError("constructed point sets are in the same row-permutation orbit")


def main() -> None:
    samples = [
        (1.0, 1.0),
        (2.0, 5.0),
        (-3.0, 7.0),
        (math.sqrt(2.0), -math.pi),
    ]
    for lam, mu in samples:
        check_case(*full_spark_counterexample(lam, mu))

    check_case(*redundant_planar_counterexample(horizontal=True))
    check_case(*redundant_planar_counterexample(horizontal=False))

    rng = np.random.default_rng(20260718)
    for d in range(2, 9):
        for _ in range(5):
            B = rng.normal(size=(d, d - 1))
            check_case(*general_normalized_counterexample(B))

        singleton = rng.normal(size=(d, d - 1))
        singleton[0, :] = 0.0
        singleton[1:, :] += np.eye(d - 1)
        check_case(*general_normalized_counterexample(singleton))

    print("verified sample normalized n=3, D=2d-1 obstruction cases")


if __name__ == "__main__":
    main()
