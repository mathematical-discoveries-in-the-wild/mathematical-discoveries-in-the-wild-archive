#!/usr/bin/env python3
"""Numerically verify the finite-dimensional identities in the counterexample.

This script is a deterministic sanity check, not a substitute for the exact
linear-algebra proof in main.tex.
"""

from __future__ import annotations

import itertools

import numpy as np


TOL = 1.0e-10


def close_to_one_of(matrix: np.ndarray, candidates: list[np.ndarray]) -> bool:
    return any(np.linalg.norm(matrix - candidate) < TOL for candidate in candidates)


def main() -> None:
    i = 1j
    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -i], [i, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)

    quaternion_group = [
        sign * matrix
        for sign, matrix in itertools.product(
            (1, -1), (identity, i * x, i * y, i * z)
        )
    ]
    assert len(quaternion_group) == 8
    assert all(
        np.linalg.norm(q.conj().T @ q - identity) < TOL for q in quaternion_group
    )
    assert all(
        close_to_one_of(q1 @ q2, quaternion_group)
        for q1, q2 in itertools.product(quaternion_group, repeat=2)
    )

    r = 1 / np.sqrt(3)
    a = np.sqrt((1 + r) / 2)
    b = np.exp(i * np.pi / 4) * np.sqrt((1 - r) / 2)
    xi = np.array([a, b], dtype=complex)
    assert abs(np.vdot(xi, xi) - 1) < TOL

    bloch = np.array(
        [np.vdot(xi, matrix @ xi).real for matrix in (x, y, z)]
    )
    assert np.linalg.norm(bloch - np.array([r, r, r])) < TOL

    q = [identity, i * x, i * y, i * z]
    orbit = [matrix @ xi for matrix in q]
    projectors = [np.outer(vector, vector.conj()) for vector in orbit]
    pauli_coordinates = np.array(
        [
            [np.trace(projector @ matrix).real for matrix in (identity, x, y, z)]
            for projector in projectors
        ]
    )
    expected_coordinates = np.array(
        [
            [1, r, r, r],
            [1, r, -r, -r],
            [1, -r, r, -r],
            [1, -r, -r, r],
        ]
    )
    assert np.linalg.norm(pauli_coordinates - expected_coordinates) < TOL
    determinant = np.linalg.det(pauli_coordinates)
    assert abs(determinant + 16 / (3 * np.sqrt(3))) < TOL
    assert np.linalg.matrix_rank(pauli_coordinates, tol=TOL) == 4

    # np.vdot is conjugate-linear in its first argument, so the transpose below
    # converts to the paper's convention, which is linear in the first argument.
    gram = np.array(
        [[np.vdot(vj, vi) for vj in orbit] for vi in orbit], dtype=complex
    )
    expected_gram = np.array(
        [
            [1, -i * r, -i * r, -i * r],
            [i * r, 1, -i * r, i * r],
            [i * r, i * r, 1, -i * r],
            [i * r, -i * r, i * r, 1],
        ],
        dtype=complex,
    )
    assert np.linalg.norm(gram - expected_gram) < TOL
    eigenvalues = np.linalg.eigvalsh(gram)
    assert np.linalg.norm(eigenvalues - np.array([0, 0, 2, 2])) < TOL
    assert np.linalg.matrix_rank(gram, tol=TOL) == 2

    print("Q8 closure and unitarity: PASS (8 elements, 64 products)")
    print("xi norm:                  PASS")
    print("Bloch vector:             ", bloch)
    print("projector coordinate det: ", determinant)
    print("projector span rank:       ", np.linalg.matrix_rank(pauli_coordinates))
    print("Gram eigenvalues:          ", eigenvalues)
    print("Gram rank:                 ", np.linalg.matrix_rank(gram, tol=TOL))
    print("all checks: PASS")


if __name__ == "__main__":
    main()
