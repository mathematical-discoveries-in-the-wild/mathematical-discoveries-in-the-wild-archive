"""Finite-tree sanity check for the sweep product identity.

The script builds random matrix-valued Haar coefficients on d-adic trees,
forms the paraproduct, its positive square, the sweep paraproduct, and the
remaining Haar-block diagonal.  It checks the identities for d=2 and d=3.
"""

from __future__ import annotations

import itertools
import numpy as np


def child_vectors(d: int) -> np.ndarray:
    """Rows form a real mean-zero basis orthonormal for child average."""
    vectors = []
    for j in range(d - 1):
        vector = np.zeros(d)
        vector[: j + 1] = 1.0
        vector[j + 1] = -(j + 1)
        vectors.append(vector)
    matrix = np.asarray(vectors)
    matrix /= np.sqrt(np.mean(matrix * matrix, axis=1))[:, None]
    return matrix


def run_case(d: int, depth: int = 4, matrix_size: int = 2) -> dict[str, float]:
    rng = np.random.default_rng(20260719 + d)
    leaves = list(itertools.product(range(d), repeat=depth))
    leaf_count = len(leaves)
    modes = child_vectors(d)

    intervals: list[tuple[int, ...]] = []
    haar: dict[tuple[tuple[int, ...], int], np.ndarray] = {}
    masks: dict[tuple[int, ...], np.ndarray] = {}
    for level in range(depth):
        for node in itertools.product(range(d), repeat=level):
            intervals.append(node)
            mask = np.array([leaf[:level] == node for leaf in leaves], dtype=float)
            masks[node] = mask
            relative_measure = mask.mean()
            for mode in range(d - 1):
                values = np.zeros(leaf_count)
                for index, leaf in enumerate(leaves):
                    if leaf[:level] == node:
                        values[index] = modes[mode, leaf[level]] / np.sqrt(relative_measure)
                haar[node, mode] = values

    coefficients: dict[tuple[tuple[int, ...], int], np.ndarray] = {}
    for node in intervals:
        for mode in range(d - 1):
            real = rng.normal(size=(matrix_size, matrix_size))
            imag = rng.normal(size=(matrix_size, matrix_size))
            coefficients[node, mode] = (real + 1j * imag) / np.sqrt(20 * leaf_count)

    dimension = leaf_count * matrix_size
    paraproduct = np.zeros((dimension, dimension), dtype=complex)
    square_coefficients: dict[tuple[int, ...], np.ndarray] = {}
    for node in intervals:
        mask = masks[node]
        averaging = mask / mask.sum()
        square = np.zeros((matrix_size, matrix_size), dtype=complex)
        for mode in range(d - 1):
            coefficient = coefficients[node, mode]
            square += coefficient.conj().T @ coefficient
            scalar_operator = np.outer(haar[node, mode], averaging)
            paraproduct += np.kron(scalar_operator, coefficient)
        square_coefficients[node] = square

    sweep = np.zeros((leaf_count, matrix_size, matrix_size), dtype=complex)
    for node in intervals:
        relative_measure = masks[node].mean()
        sweep += (
            masks[node][:, None, None]
            * square_coefficients[node][None, :, :]
            / relative_measure
        )

    sweep_paraproduct = np.zeros_like(paraproduct)
    for node in intervals:
        averaging = masks[node] / masks[node].sum()
        for mode in range(d - 1):
            coefficient = np.tensordot(
                haar[node, mode] / leaf_count,
                sweep,
                axes=(0, 0),
            )
            sweep_paraproduct += np.kron(
                np.outer(haar[node, mode], averaging), coefficient
            )

    positive_square = paraproduct.conj().T @ paraproduct
    symmetric_sweep = sweep_paraproduct + sweep_paraproduct.conj().T
    diagonal = positive_square - symmetric_sweep

    scalar_basis = [np.ones(leaf_count)]
    block_sizes = [1]
    for node in intervals:
        scalar_basis.extend(haar[node, mode] for mode in range(d - 1))
        block_sizes.append(d - 1)
    unitary_scalar = np.column_stack(scalar_basis) / np.sqrt(leaf_count)
    unitary = np.kron(unitary_scalar, np.eye(matrix_size))
    diagonal_in_haar_basis = unitary.conj().T @ diagonal @ unitary

    allowed = np.zeros((dimension, dimension), dtype=bool)
    offset = 0
    for size in block_sizes:
        width = size * matrix_size
        allowed[offset : offset + width, offset : offset + width] = True
        offset += width
    off_block_error = np.linalg.norm(diagonal_in_haar_basis[~allowed])

    bmo_squared = 0.0
    for node in intervals:
        descendant_sum = np.zeros((matrix_size, matrix_size), dtype=complex)
        for child_node in intervals:
            if len(child_node) >= len(node) and child_node[: len(node)] == node:
                descendant_sum += square_coefficients[child_node]
        relative_measure = masks[node].mean()
        bmo_squared = max(
            bmo_squared,
            float(np.linalg.eigvalsh(descendant_sum / relative_measure).max()),
        )

    minimum_diagonal_eigenvalue = float(np.linalg.eigvalsh(diagonal).min())
    diagonal_norm = float(np.linalg.norm(diagonal, 2))
    identity_error = float(
        np.linalg.norm(positive_square - symmetric_sweep - diagonal)
    )
    return {
        "d": float(d),
        "identity_error": identity_error,
        "off_block_error": float(off_block_error),
        "minimum_diagonal_eigenvalue": minimum_diagonal_eigenvalue,
        "diagonal_norm": diagonal_norm,
        "bmo_squared": bmo_squared,
        "diagonal_bound_slack": bmo_squared - diagonal_norm,
    }


if __name__ == "__main__":
    for branching in (2, 3):
        print(run_case(branching))
