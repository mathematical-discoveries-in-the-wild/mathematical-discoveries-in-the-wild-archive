"""Finite Gram-matrix sanity check for the lacunary Poisson kernels.

The proof packet uses the analytic Gershgorin bound, not this computation.
This script only verifies that the finite matrices behave as expected.
"""

from __future__ import annotations

import numpy as np


def gram(alpha: np.ndarray) -> np.ndarray:
    a = alpha[:, None]
    b = alpha[None, :]
    return 4 * a * b / (a + b) ** 2


def main() -> None:
    for rho in (10.0, 12.0, 16.0):
        alpha = rho ** np.arange(20)
        eigs = np.linalg.eigvalsh(gram(alpha))
        eta = 8 / (rho - 1)
        print(
            f"rho={rho:4.1f}  min_eig={eigs[0]:.6f}  "
            f"max_eig={eigs[-1]:.6f}  gershgorin=[{1-eta:.6f}, {1+eta:.6f}]"
        )


if __name__ == "__main__":
    main()
