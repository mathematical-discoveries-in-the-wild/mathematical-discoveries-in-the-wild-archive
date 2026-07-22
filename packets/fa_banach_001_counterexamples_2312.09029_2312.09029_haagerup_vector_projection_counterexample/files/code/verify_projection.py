#!/usr/bin/env python3
"""Exact and numerical checks for the Haagerup-vector counterexample.

The exact SymPy checks mirror the algebraic identities used in the proof.
The SciPy phase optimization is only a numerical sanity check; it is not used
to prove that the Haagerup vector is suboptimal.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
from scipy.optimize import minimize


def exact_checks() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    root2 = sp.sqrt(2)
    A = sp.Matrix(
        [
            [1, 0],
            [0, 1],
            [1 / root2, 1 / root2],
            [1 / root2, sp.I / root2],
        ]
    )
    Q = sp.simplify(A * A.conjugate().T)
    P = sp.simplify(A * (A.conjugate().T * A).inv() * A.conjugate().T)
    I4 = sp.eye(4)
    Z4 = sp.zeros(4)

    assert sp.simplify(P.conjugate().T - P) == Z4
    assert sp.simplify(P * P - P) == Z4
    assert P.rank() == 2
    assert Q.rank() == 2
    assert [sp.simplify(Q[j, j]) for j in range(4)] == [1, 1, 1, 1]
    assert sp.simplify(P * Q - Q) == Z4
    assert sp.simplify(sp.trace(P * Q)) == 4
    # Hermitian idempotence already proves that P and I-P are positive
    # projections; avoid relying on SymPy's occasionally inconclusive
    # ``is_positive_semidefinite`` predicate for symbolic complex matrices.
    assert sp.simplify((I4 - P).conjugate().T - (I4 - P)) == Z4
    assert sp.simplify((I4 - P) * (I4 - P) - (I4 - P)) == Z4

    print("EXACT CHECKS: PASS")
    print("rank(P) =", P.rank())
    print("diag(Q) =", [Q[j, j] for j in range(4)])
    print("P*Q == Q and Tr(P*Q) =", sp.simplify(sp.trace(P * Q)))
    print("P =")
    sp.pprint(P)
    return A, P, Q


def numerical_sanity(P_exact: sp.Matrix) -> None:
    P = np.array(P_exact.evalf(), dtype=np.complex128)

    def vector(theta: np.ndarray) -> np.ndarray:
        # Global phase is irrelevant, so fix u_1 = 1.
        return np.exp(1j * np.r_[0.0, theta])

    def negative_value(theta: np.ndarray) -> float:
        u = vector(theta)
        return -float(np.real(np.vdot(u, P @ u)))

    starts = [
        np.zeros(3),
        np.array([-np.pi / 4, -np.pi / 8, np.pi / 8]),
    ]
    rng = np.random.default_rng(231209029)
    starts.extend(rng.uniform(-np.pi, np.pi, size=(32, 3)))
    fits = [minimize(negative_value, start, method="BFGS", tol=1e-13) for start in starts]
    best = min(fits, key=lambda fit: fit.fun)
    u = vector(best.x)
    F2 = -best.fun
    lam = np.conjugate(u) * (P @ u) / F2
    xi = np.sqrt(np.maximum(np.real(lam), 0.0))
    inv_xi = np.diag(1.0 / xi)
    candidate_squared = np.linalg.eigvalsh(inv_xi @ P @ inv_xi)[-1]

    print("NUMERICAL SANITY CHECK (not part of the proof)")
    print("optimizer success =", best.success)
    print("F^2 approximately =", f"{F2:.12f}")
    print("phases approximately =", np.angle(u))
    print("Haagerup lambda approximately =", np.real(lam))
    print("max imaginary residual in lambda =", np.max(np.abs(np.imag(lam))))
    print("Haagerup candidate squared norm approximately =", f"{candidate_squared:.12f}")
    print("exact optimum squared cbF norm = 4")
    assert F2 < 4 - 1e-5
    assert np.max(np.abs(np.real(lam) - 0.25)) > 1e-3
    assert candidate_squared > 4 + 1e-3
    print("NUMERICAL CHECKS: PASS")


if __name__ == "__main__":
    _, projection, _ = exact_checks()
    numerical_sanity(projection)
