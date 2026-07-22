#!/usr/bin/env python3
"""Finite sanity checks for the rank-two/random-sign proof.

The script is not part of the proof. It checks small real and complex arrays,
including an exact enumeration of every sign form when the ambient array has
at most nine coefficients.
"""

from __future__ import annotations

import itertools

import numpy as np


SEED = 180502115
TOL = 2.0e-10


def pure_tensor(vectors: list[np.ndarray]) -> np.ndarray:
    out = vectors[0]
    for vector in vectors[1:]:
        out = np.multiply.outer(out, vector)
    return out


def decomposable_difference(
    rng: np.random.Generator, arity: int, dimension: int, complex_: bool
) -> np.ndarray:
    def vector() -> np.ndarray:
        value = rng.normal(size=dimension)
        if complex_:
            value = value + 1j * rng.normal(size=dimension)
        return value

    return pure_tensor([vector() for _ in range(arity)]) - pure_tensor(
        [vector() for _ in range(arity)]
    )


def diagonal(array: np.ndarray) -> np.ndarray:
    dimension = array.shape[0]
    return np.asarray([array[(j,) * array.ndim] for j in range(dimension)])


def all_signs(coefficient_count: int) -> np.ndarray:
    return np.asarray(list(itertools.product((-1.0, 1.0), repeat=coefficient_count)))


def exact_family_ratio(arrays: list[np.ndarray], p: float) -> float:
    flat = np.stack([array.reshape(-1) for array in arrays])
    signs = all_signs(flat.shape[1])
    evaluations = signs @ flat.T
    denominator = np.max(np.sum(np.abs(evaluations) ** p, axis=1) ** (1.0 / p))
    numerator = sum(np.linalg.norm(diagonal(array), ord=1) ** p for array in arrays)
    numerator = numerator ** (1.0 / p)
    return float(numerator / denominator)


def main() -> None:
    rng = np.random.default_rng(SEED)
    deterministic_cases = 0
    family_cases = 0
    max_p2_ratio = 0.0

    for complex_ in (False, True):
        for arity, dimension in ((2, 2), (2, 3), (3, 2), (3, 3)):
            arrays: list[np.ndarray] = []
            for _ in range(120):
                array = decomposable_difference(rng, arity, dimension, complex_)
                flattening = array.reshape(dimension, -1)
                rank = np.linalg.matrix_rank(flattening, tol=1.0e-10)
                diagonal_norm = np.linalg.norm(diagonal(array), ord=1)
                hs_norm = np.linalg.norm(array.reshape(-1), ord=2)
                assert rank <= 2
                assert diagonal_norm <= np.sqrt(2.0) * hs_norm + TOL
                deterministic_cases += 1
                arrays.append(array)

            # Exact sign enumeration is kept small: 2^9 is the largest set.
            if dimension**arity <= 9:
                for offset in range(0, 15, 3):
                    family = arrays[offset : offset + 3]
                    for p in (1.0, 1.5, 2.0, 4.0):
                        ratio = exact_family_ratio(family, p)
                        assert np.isfinite(ratio)
                        if p == 2.0:
                            # Exact sign orthogonality plus the deterministic
                            # estimate proves this finite p=2 bound.
                            assert ratio <= np.sqrt(2.0) + TOL
                            max_p2_ratio = max(max_p2_ratio, ratio)
                        family_cases += 1

    print(f"seed={SEED}")
    print(f"deterministic rank/diagonal cases={deterministic_cases}")
    print(f"exact finite sign-family cases={family_cases}")
    print(f"largest observed p=2 ratio={max_p2_ratio:.10f}")
    print("all checks passed")


if __name__ == "__main__":
    main()

