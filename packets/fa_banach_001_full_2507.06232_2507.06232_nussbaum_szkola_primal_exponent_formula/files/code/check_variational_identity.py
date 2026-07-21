#!/usr/bin/env python3
"""Numerically check the two algebraic identities used in the proof packet.

This is only a sanity check.  The packet's proof is analytic.
"""

from __future__ import annotations

import math
import numpy as np


def random_state(rng: np.random.Generator, dimension: int) -> np.ndarray:
    matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    state = matrix @ matrix.conj().T
    return state / np.trace(state)


def psd_power(matrix: np.ndarray, exponent: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    powered = np.maximum(values, 0.0) ** exponent
    return (vectors * powered) @ vectors.conj().T


def relative_entropy(distribution: np.ndarray, reference: np.ndarray) -> float:
    mask = distribution > 0
    if np.any(reference[mask] <= 0):
        return math.inf
    return float(
        np.sum(distribution[mask] * np.log2(distribution[mask] / reference[mask]))
    )


def nussbaum_szkola_pair(
    rho: np.ndarray, sigma: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    rho_values, rho_vectors = np.linalg.eigh(rho)
    sigma_values, sigma_vectors = np.linalg.eigh(sigma)
    overlaps = np.abs(rho_vectors.conj().T @ sigma_vectors) ** 2
    p_dist = rho_values[:, None] * overlaps
    q_dist = sigma_values[None, :] * overlaps
    return p_dist, q_dist


def check_petz_gibbs_identity(rng: np.random.Generator) -> float:
    largest_error = 0.0
    for _ in range(80):
        dimension = int(rng.integers(2, 6))
        rho = random_state(rng, dimension)
        sigma = random_state(rng, dimension)
        p_dist, q_dist = nussbaum_szkola_pair(rho, sigma)

        for s_value in (0.05, 0.2, 0.5, 0.8, 1.0):
            alpha = 1.0 / (1.0 + s_value)
            petz_overlap = float(
                np.trace(psd_power(rho, alpha) @ psd_power(sigma, 1.0 - alpha)).real
            )
            petz_divergence = math.log2(petz_overlap) / (alpha - 1.0)

            unnormalized = p_dist**alpha * q_dist ** (1.0 - alpha)
            tilted = unnormalized / np.sum(unnormalized)
            variational_value = relative_entropy(
                tilted.ravel(), p_dist.ravel()
            ) + s_value * relative_entropy(tilted.ravel(), q_dist.ravel())
            largest_error = max(
                largest_error, abs(s_value * petz_divergence - variational_value)
            )
    return largest_error


def check_classical_chain_rule(rng: np.random.Generator) -> float:
    largest_error = 0.0
    for _ in range(100):
        p_input = rng.dirichlet(np.ones(3))
        tilted_channel = np.vstack([rng.dirichlet(np.ones(5)) for _ in range(3)])
        q_output = rng.dirichlet(np.ones(5))
        output = p_input @ tilted_channel

        left = sum(
            p_input[x] * relative_entropy(tilted_channel[x], q_output)
            for x in range(3)
        )
        mutual_information = sum(
            p_input[x] * relative_entropy(tilted_channel[x], output)
            for x in range(3)
        )
        right = mutual_information + relative_entropy(output, q_output)
        largest_error = max(largest_error, abs(left - right))
    return largest_error


def main() -> None:
    rng = np.random.default_rng(250706232)
    petz_error = check_petz_gibbs_identity(rng)
    chain_error = check_classical_chain_rule(rng)
    print(f"max Petz/Gibbs identity error: {petz_error:.3e}")
    print(f"max classical chain-rule error: {chain_error:.3e}")
    if petz_error > 2e-10 or chain_error > 2e-10:
        raise SystemExit("numerical identity check failed")


if __name__ == "__main__":
    main()
