"""Numerical probes for the finite-atom p<2 c_n formula.

This script is not proof. It compares a global numerical optimization over
N equally weighted atoms with the candidate lower-bound formula attained by
two opposite spikes and zeros:

    D_p/M_p = 2 - (4 - 2^p)/N.

The promoted packet only uses this construction as a lower bound and as
evidence for a separate finite extremal problem.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import differential_evolution


def ratio(x: np.ndarray, p: float) -> float:
    moment = np.mean(np.abs(x) ** p)
    if moment <= 1e-12:
        return 0.0
    diff = np.mean(np.abs(x[:, None] - x[None, :]) ** p)
    return float(diff / moment)


def candidate(N: int, p: float) -> float:
    return 2.0 - (4.0 - 2.0**p) / N


def main() -> None:
    for p in (1.2, 1.5, 1.8):
        print(f"p={p}")
        for N in (2, 3, 4, 5, 8):
            res = differential_evolution(
                lambda z: -ratio(np.asarray(z), p),
                [(-3, 3)] * N,
                seed=123,
                tol=1e-8,
                maxiter=600,
                polish=True,
            )
            print(
                f"  N={N}: numerical={-res.fun:.10f}, "
                f"candidate={candidate(N, p):.10f}"
            )


if __name__ == "__main__":
    main()
