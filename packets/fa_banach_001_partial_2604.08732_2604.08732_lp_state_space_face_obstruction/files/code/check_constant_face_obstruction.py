"""Finite checks for the constant-face inclusion in the packet.

The infinite-dimensional non-compactness argument is mathematical, not
numerical. This script only verifies the defining equalities in finite
truncations of ell_1 / ell_infinity.
"""

from __future__ import annotations

import math


def linfty_norm(vec: list[float]) -> float:
    return max(abs(x) for x in vec)


def constant_lq_norm(vec: list[float], measure: float = 1.0) -> float:
    # A constant function with value vec has L^q norm measure^(1/q)*||vec||.
    q = 2.0
    return (measure * linfty_norm(vec) ** q) ** (1.0 / q)


def pairing_with_constant_e1(vec: list[float], measure: float = 1.0) -> float:
    return measure * vec[0]


def main() -> None:
    samples = [
        [1.0, 0.0, 0.0, 0.0],
        [1.0, -1.0, 0.5, 0.25],
        [1.0, 0.7, -0.9, 1.0],
    ]
    for sample in samples:
        norm = constant_lq_norm(sample)
        pairing = pairing_with_constant_e1(sample)
        print(f"sample={sample} Lq_norm={norm:.6f} pairing={pairing:.6f}")
        assert math.isclose(norm, 1.0)
        assert math.isclose(pairing, 1.0)


if __name__ == "__main__":
    main()
