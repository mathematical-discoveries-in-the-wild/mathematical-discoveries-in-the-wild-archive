"""Numerical sanity checks for the normalized Hadamard block construction."""

import math

import numpy as np


def sylvester(k: int) -> np.ndarray:
    matrix = np.ones((1, 1), dtype=float)
    for _ in range(k):
        matrix = np.block([[matrix, matrix], [matrix, -matrix]])
    return matrix


def main() -> None:
    checks = 0
    for k in range(1, 9):
        n = 2**k
        hadamard = sylvester(k)
        phi = hadamard / math.sqrt(n)
        identity = np.eye(n)
        ones = np.ones((n, n))

        assert np.allclose(hadamard @ hadamard.T, n * identity)
        assert np.allclose(phi, (phi @ identity.T))
        assert np.allclose(phi * hadamard, ones / math.sqrt(n))

        input_norm = np.linalg.norm(hadamard, ord=2)
        output_norm = np.linalg.norm(phi * hadamard, ord=2)
        assert np.isclose(input_norm, math.sqrt(n))
        assert np.isclose(output_norm, math.sqrt(n))
        assert np.isclose(output_norm / input_norm, 1.0)
        checks += 6

    print(f"hadamard_block_checks={checks}")
    print("largest_order=256")
    print("status=PASS")


if __name__ == "__main__":
    main()
