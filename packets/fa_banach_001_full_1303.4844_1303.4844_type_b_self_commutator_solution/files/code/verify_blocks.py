#!/usr/bin/env python3
"""Verify the explicit so(3) and so(4) self-commutator blocks.

The symbolic checks certify the displayed matrix identities after ordinary
algebraic simplification.  Random tests exercise orthogonal conjugacy and the
operator-norm estimate; they are sanity checks, not a proof of the infinite
direct-sum theorem.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
import sympy as sp


def matrix_unit_skew(dim: int, j: int, k: int, dtype=object):
    matrix = np.zeros((dim, dim), dtype=dtype)
    matrix[j - 1, k - 1] = 1
    matrix[k - 1, j - 1] = -1
    return matrix


def sympy_skew(dim: int, j: int, k: int) -> sp.Matrix:
    matrix = sp.zeros(dim)
    matrix[j - 1, k - 1] = 1
    matrix[k - 1, j - 1] = -1
    return matrix


def symbolic_checks() -> None:
    lam = sp.symbols("lambda", nonnegative=True, real=True)
    l12 = sympy_skew(3, 1, 2)
    l13 = sympy_skew(3, 1, 3)
    l23 = sympy_skew(3, 2, 3)
    y3 = sp.sqrt(lam / 2) * (l13 + sp.I * l23)
    residual3 = sp.simplify(y3.conjugate().T * y3 - y3 * y3.conjugate().T - sp.I * lam * l12)
    assert residual3 == sp.zeros(3)
    assert sp.simplify(y3.T + y3) == sp.zeros(3)

    p, q = sp.symbols("p q", nonnegative=True, real=True)
    l12 = sympy_skew(4, 1, 2)
    l13 = sympy_skew(4, 1, 3)
    l14 = sympy_skew(4, 1, 4)
    l23 = sympy_skew(4, 2, 3)
    l24 = sympy_skew(4, 2, 4)
    l34 = sympy_skew(4, 3, 4)
    a1 = (l12 + l34) / 2
    a2 = (l13 - l24) / 2
    a3 = (l14 + l23) / 2
    b1 = (l12 - l34) / 2
    b2 = (l13 + l24) / 2
    b3 = (l14 - l23) / 2
    assert sp.simplify(a2 * a3 - a3 * a2 + a1) == sp.zeros(4)
    assert sp.simplify(b2 * b3 - b3 * b2 - b1) == sp.zeros(4)
    for a in (a1, a2, a3):
        for b in (b1, b2, b3):
            assert sp.simplify(a * b - b * a) == sp.zeros(4)
    y4 = sp.sqrt(p / 2) * (a2 + sp.I * a3) + sp.sqrt(q / 2) * (b2 - sp.I * b3)
    target4 = sp.I * p * a1 + sp.I * q * b1
    residual4 = sp.simplify(y4.conjugate().T * y4 - y4 * y4.conjugate().T - target4)
    assert residual4 == sp.zeros(4)
    assert sp.simplify(y4.T + y4) == sp.zeros(4)


def real_orthogonal(dim: int, rng: np.random.Generator) -> np.ndarray:
    q, r = np.linalg.qr(rng.normal(size=(dim, dim)))
    signs = np.sign(np.diag(r))
    signs[signs == 0] = 1
    return q @ np.diag(signs)


def canonical_three(lam: float) -> tuple[np.ndarray, np.ndarray]:
    l12 = matrix_unit_skew(3, 1, 2, complex)
    l13 = matrix_unit_skew(3, 1, 3, complex)
    l23 = matrix_unit_skew(3, 2, 3, complex)
    target = 1j * lam * l12
    y = math.sqrt(lam / 2) * (l13 + 1j * l23)
    return target, y


def canonical_four(lam: float, mu: float) -> tuple[np.ndarray, np.ndarray]:
    l12 = matrix_unit_skew(4, 1, 2, complex)
    l13 = matrix_unit_skew(4, 1, 3, complex)
    l14 = matrix_unit_skew(4, 1, 4, complex)
    l23 = matrix_unit_skew(4, 2, 3, complex)
    l24 = matrix_unit_skew(4, 2, 4, complex)
    l34 = matrix_unit_skew(4, 3, 4, complex)
    a2 = (l13 - l24) / 2
    a3 = (l14 + l23) / 2
    b2 = (l13 + l24) / 2
    b3 = (l14 - l23) / 2
    target = 1j * (lam * l12 + mu * l34)
    y = math.sqrt((lam + mu) / 2) * (a2 + 1j * a3)
    y += math.sqrt((lam - mu) / 2) * (b2 - 1j * b3)
    return target, y


def random_checks(cases: int, seed: int) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    max_residual = 0.0
    max_bound_ratio = 0.0
    for index in range(cases):
        if index % 2 == 0:
            lam = float(10 ** rng.uniform(-8, 4))
            target, y = canonical_three(lam)
            dim = 3
        else:
            lam = float(10 ** rng.uniform(-8, 4))
            mu = float(rng.uniform(0, lam))
            target, y = canonical_four(lam, mu)
            dim = 4
        q = real_orthogonal(dim, rng)
        target = q @ target @ q.T
        y = q @ y @ q.T
        commutator = y.conj().T @ y - y @ y.conj().T
        scale = max(1.0, np.linalg.norm(target, 2))
        residual = np.linalg.norm(commutator - target, 2) / scale
        max_residual = max(max_residual, float(residual))
        assert np.linalg.norm(y.T + y, 2) <= 1e-10 * max(1.0, np.linalg.norm(y, 2))
        assert np.linalg.norm(target.conj().T - target, 2) <= 1e-10 * scale
        ratio = np.linalg.norm(y, 2) / math.sqrt(np.linalg.norm(target, 2))
        max_bound_ratio = max(max_bound_ratio, float(ratio))
        assert ratio <= math.sqrt(2) + 1e-10
    assert max_residual <= 2e-10
    return max_residual, max_bound_ratio


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=13034844)
    args = parser.parse_args()
    symbolic_checks()
    residual, ratio = random_checks(args.cases, args.seed)
    print("symbolic checks: PASS")
    print(f"random cases: {args.cases} (seed={args.seed})")
    print(f"maximum relative commutator residual: {residual:.3e}")
    print(f"maximum ||Y||/sqrt(||T||): {ratio:.12f}")
    print(f"claimed upper bound: sqrt(2)={math.sqrt(2):.12f}")
    print("random checks: PASS")


if __name__ == "__main__":
    main()
