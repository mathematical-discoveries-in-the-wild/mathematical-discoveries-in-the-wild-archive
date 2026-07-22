"""Sanity checks for the finite identities in the J3 separation proof."""

from __future__ import annotations

import numpy as np


def q(matrix: np.ndarray) -> np.ndarray:
    return matrix @ matrix.conj().T + matrix.conj().T @ matrix


def main() -> None:
    b0 = np.array(
        [
            [0.0, 0.0, 1 / np.sqrt(3)],
            [np.sqrt(2 / 3), 0.0, 0.0],
            [0.0, 1 / np.sqrt(3), 0.0],
        ],
        dtype=complex,
    )
    expected_q = np.diag([1.0, 1.0, 2 / 3])
    residual = np.linalg.norm(q(b0) - expected_q)
    assert residual < 1e-12

    samples = [
        (1.0, 0.0),
        (0.0, 1.0),
        (1 / np.sqrt(2), 1j / np.sqrt(2)),
        ((1 + 2j) / np.sqrt(15), (3 - 1j) / np.sqrt(15)),
    ]
    generator_residuals = []
    for alpha, beta in samples:
        generator = np.array([[0.0, alpha], [beta, 0.0]], dtype=complex)
        generator_residuals.append(np.linalg.norm(q(generator) - np.eye(2)))
    assert max(generator_residuals) < 1e-12

    e3 = np.array([0.0, 0.0, 1.0], dtype=complex)
    assert np.linalg.norm(b0 @ e3 - np.array([1 / np.sqrt(3), 0, 0])) < 1e-12
    assert np.linalg.norm(b0.conj().T @ e3 - np.array([0, 1 / np.sqrt(3), 0])) < 1e-12

    print(f"B0 Q-residual: {residual:.3e}")
    print(f"maximum generator Q-residual: {max(generator_residuals):.3e}")
    print("finite identity checks passed")


if __name__ == "__main__":
    main()
