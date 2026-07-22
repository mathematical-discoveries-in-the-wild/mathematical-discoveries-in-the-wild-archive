#!/usr/bin/env python3
"""Finite-dimensional smoke tests for the two exact optimizer formulas.

This checks the polar-unitary optimizer for Re tr(CV) and the eigenvector-
alignment optimizer for tr(A V B V*) on random matrices.  It is not a proof
of the large-N statements.
"""

from __future__ import annotations

import numpy as np


def normalized_trace(a: np.ndarray) -> complex:
    return np.trace(a) / a.shape[0]


def main() -> None:
    rng = np.random.default_rng(260602985)
    tests = 0

    for n in range(2, 11):
        for _ in range(20):
            c = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            left, singular, right_star = np.linalg.svd(c)
            polar_optimizer = right_star.conj().T @ left.conj().T
            polar_value = normalized_trace(c @ polar_optimizer).real
            predicted_polar = singular.sum() / n
            assert np.allclose(
                polar_optimizer.conj().T @ polar_optimizer,
                np.eye(n),
                atol=1e-10,
            )
            assert abs(polar_value - predicted_polar) < 1e-10

            x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            a = (x + x.conj().T) / 2
            b = (y + y.conj().T) / 2
            eig_a, vec_a = np.linalg.eigh(a)
            eig_b, vec_b = np.linalg.eigh(b)
            order_a = np.argsort(eig_a)[::-1]
            order_b = np.argsort(eig_b)[::-1]
            eig_a = eig_a[order_a]
            eig_b = eig_b[order_b]
            vec_a = vec_a[:, order_a]
            vec_b = vec_b[:, order_b]
            rearrangement_optimizer = vec_a @ vec_b.conj().T
            rearrangement_value = normalized_trace(
                a @ rearrangement_optimizer @ b @ rearrangement_optimizer.conj().T
            ).real
            predicted_rearrangement = np.dot(eig_a, eig_b) / n
            assert np.allclose(
                rearrangement_optimizer.conj().T @ rearrangement_optimizer,
                np.eye(n),
                atol=1e-10,
            )
            assert abs(rearrangement_value - predicted_rearrangement) < 1e-10
            tests += 1

    print(f"PASS: {tests} random matrix pairs; orders 2 through 10")


if __name__ == "__main__":
    main()
