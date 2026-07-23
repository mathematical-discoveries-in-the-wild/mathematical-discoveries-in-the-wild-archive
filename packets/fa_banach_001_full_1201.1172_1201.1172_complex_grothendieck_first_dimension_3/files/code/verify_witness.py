#!/usr/bin/env python3
"""Exact checks for the 3x3 complex Grothendieck separation witness.

The symbolic checks mirror the proof.  The final numerical optimization is
only a sanity check and is not used to establish strict separation.
"""

import numpy as np
import sympy as sp
from scipy.optimize import differential_evolution


def exact_checks() -> None:
    i = sp.I
    a_mat = sp.Matrix(
        [
            [1, 1, 1],
            [1, -1, -i],
            [1, i, -1],
        ]
    )
    gram = sp.Matrix(
        [
            [1, (-5 - 7 * i) / 18, (-5 + 7 * i) / 18],
            [(-5 + 7 * i) / 18, 1, (7 - 15 * i) / 18],
            [(-5 - 7 * i) / 18, (7 + 15 * i) / 18, 1],
        ]
    )

    assert gram == sp.conjugate(gram.T)
    assert list(gram.diagonal()) == [1, 1, 1]
    assert sp.factor(gram.det()) == 0
    eigenvalues = set(gram.eigenvals())
    expected = {
        sp.Integer(0),
        sp.Rational(3, 2) - sp.sqrt(179) / 18,
        sp.Rational(3, 2) + sp.sqrt(179) / 18,
    }
    assert eigenvalues == expected

    row_norm_squares = [
        sp.simplify((sp.conjugate(a_mat.row(k)) * gram * a_mat.row(k).T)[0])
        for k in range(3)
    ]
    assert row_norm_squares == [sp.Rational(8, 3), 6, 6]
    vector_value = sp.simplify(sum(sp.sqrt(q) for q in row_norm_squares))
    assert vector_value == 8 * sp.sqrt(6) / 3

    # Equality cases in the scalar quadratic bound.
    u_values = [
        (1 - 2 * i) * (1 - sp.sqrt(19) * i) / 10,
        (1 - 2 * i) * (1 + sp.sqrt(19) * i) / 10,
    ]
    r_squares = []
    for u in u_values:
        coeff = (1 - 2 * i) + (3 + 4 * i) * sp.conjugate(u)
        assert sp.simplify(coeff * sp.conjugate(coeff)) == 25
        v = sp.conjugate(coeff) / 5
        r_sq = sp.simplify(sp.expand_complex((1 + u + v) * sp.conjugate(1 + u + v)))
        r_squares.append(r_sq)
    assert r_squares == [
        (112 - 24 * sp.sqrt(19)) / 25,
        (112 + 24 * sp.sqrt(19)) / 25,
    ]
    assert all(sp.simplify(q - sp.Rational(8, 3)) != 0 for q in r_squares)

    print("Exact Gram, vector-value, and equality-case checks passed.")
    print("vector value =", vector_value)
    print("quadratic-bound equality r^2 values =", r_squares)


def numerical_sanity_check() -> None:
    a_mat = np.array(
        [[1, 1, 1], [1, -1, -1j], [1, 1j, -1]], dtype=complex
    )

    def scalar_value(theta: np.ndarray) -> float:
        phases = np.exp(1j * np.array([0.0, theta[0], theta[1]]))
        return float(np.abs(a_mat @ phases).sum())

    result = differential_evolution(
        lambda theta: -scalar_value(theta),
        bounds=[(-np.pi, np.pi), (-np.pi, np.pi)],
        seed=12011172,
        tol=1e-12,
        polish=True,
    )
    scalar = -float(result.fun)
    vector = float(8 * np.sqrt(6) / 3)
    print("numerical scalar maximum candidate =", scalar)
    print("exact vector witness value =", vector)
    print("observed ratio =", vector / scalar)
    assert scalar < vector - 0.1


if __name__ == "__main__":
    exact_checks()
    numerical_sanity_check()
