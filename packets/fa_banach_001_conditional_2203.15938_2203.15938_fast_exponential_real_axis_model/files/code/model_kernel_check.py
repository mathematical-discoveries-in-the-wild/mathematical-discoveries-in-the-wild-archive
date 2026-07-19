"""Numerical check for the fast-exponential real-axis model kernel.

This script discretizes the inverse kernel of

    B_t = -d/dx + exp(t^2 (x^2 - 1))

and compares its largest singular value with 4/pi, the norm of the Volterra
limit on (-1, 1).  The computation is only a sanity check for the packet; the
packet proof uses Hilbert-Schmidt kernel convergence.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.sparse.linalg import svds


def model_norm(t: float, n: int = 3500) -> float:
    # The barrier transition is sharp for large t.  A shrinking window keeps
    # the matrix modest while still including the relevant boundary layers.
    length = 1.0 + 6.0 / t
    x = np.linspace(-length, length, n)
    h = x[1] - x[0]
    exponent = np.minimum(t * t * (x * x - 1.0), 700.0)
    w = np.exp(exponent)
    primitive = np.zeros(n)
    primitive[1:] = np.cumsum(0.5 * (w[:-1] + w[1:]) * h)

    kernel = np.zeros((n, n), dtype=float)
    for i in range(n):
        kernel[i, i:] = np.exp(-(primitive[i:] - primitive[i])) * h

    return float(svds(kernel, k=1, return_singular_vectors=False, tol=1e-7)[0])


def main() -> None:
    target = 4.0 / math.pi
    print(f"target 4/pi = {target:.10f}")
    for t in (24.0, 36.0, 48.0, 64.0, 80.0):
        value = model_norm(t)
        print(f"t={t:5.1f}  norm={value:.10f}  ratio={value / target:.6f}")


if __name__ == "__main__":
    main()
