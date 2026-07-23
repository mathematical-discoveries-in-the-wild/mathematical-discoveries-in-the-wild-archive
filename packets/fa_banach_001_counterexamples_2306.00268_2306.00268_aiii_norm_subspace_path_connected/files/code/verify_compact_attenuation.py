#!/usr/bin/env python3
"""Finite-window checks for compact attenuation of cyclic shifts.

The infinite-dimensional proof is analytic.  These matrices only verify its
explicit identities and the rapid norm decay after attenuation.
"""

from __future__ import annotations

import numpy as np


def cyclic_approximant(radius: int, window: int) -> np.ndarray:
    labels = np.arange(-window, window + 1)
    position = {int(n): j for j, n in enumerate(labels)}
    unitary = np.eye(labels.size)

    for n in range(-radius, radius):
        unitary[:, position[n]] = 0.0
        unitary[position[n + 1], position[n]] = 1.0

    unitary[:, position[radius]] = 0.0
    unitary[position[-radius], position[radius]] = 1.0
    return unitary


def truncated_right_shift(window: int) -> np.ndarray:
    labels = np.arange(-window, window + 1)
    position = {int(n): j for j, n in enumerate(labels)}
    shift = np.zeros((labels.size, labels.size))
    for n in range(-window, window):
        shift[position[n + 1], position[n]] = 1.0
    return shift


def attenuation(window: int) -> np.ndarray:
    labels = np.arange(-window, window + 1)
    return np.diag(2.0 ** (-np.abs(labels)))


def verify() -> None:
    print(" N   ||(C_N-R)D||    bound 2^(1-N)   polar error")
    previous = float("inf")

    for radius in (2, 3, 4, 6, 8, 10):
        window = 4 * radius + 4
        cyclic = cyclic_approximant(radius, window)
        shift = truncated_right_shift(window)
        diagonal = attenuation(window)

        identity = np.eye(cyclic.shape[0])
        assert np.allclose(cyclic.conj().T @ cyclic, identity)
        assert np.allclose(cyclic @ cyclic.conj().T, identity)

        attenuated = cyclic @ diagonal
        # In finite dimensions D is invertible, so the polar unitary is exactly
        # C_N.  Recover it from A(A*A)^(-1/2) using the diagonal formula.
        recovered_polar = attenuated @ np.diag(1.0 / np.diag(diagonal))
        polar_error = np.linalg.norm(recovered_polar - cyclic, 2)

        norm_difference = np.linalg.norm((cyclic - shift) @ diagonal, 2)
        analytic_bound = 2.0 ** (1 - radius)
        # The truncated shift has one extra outer-boundary defect of size
        # 2^(-window), far below the displayed bound.
        assert norm_difference <= analytic_bound + 2.0 ** (-window) + 1.0e-12
        assert norm_difference < previous
        assert polar_error < 1.0e-12
        previous = norm_difference

        labels = np.arange(-window, window + 1)
        interior = np.where((labels >= -radius) & (labels < radius))[0]
        assert np.allclose(cyclic[:, interior], shift[:, interior])

        print(
            f"{radius:2d}   {norm_difference:14.8e}   "
            f"{analytic_bound:14.8e}   {polar_error:10.2e}"
        )

    print("all compact-attenuation checks passed")


if __name__ == "__main__":
    verify()
