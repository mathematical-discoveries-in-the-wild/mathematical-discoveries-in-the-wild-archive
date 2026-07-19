"""Numerical sanity checks for the 2407.14156 counterexample packet.

The proof in the packet is analytic.  This script only verifies the advertised
matrix identities for the two-dimensional rotation example.
"""

import math
import numpy as np


def main() -> None:
    identity = np.eye(2)
    rotation = np.array([[0.0, -1.0], [1.0, 0.0]])
    t = 0.5 * (identity + rotation)

    # Linear firm nonexpansiveness: T^T T <= (T + T^T)/2.
    firm_gap = 0.5 * (t + t.T) - t.T @ t
    print("T =")
    print(t)
    print("firm gap eigenvalues:", np.linalg.eigvalsh(firm_gap))

    # Nonexpansive variable in the source paper's (CP) formulation.
    n = 2.0 * t - identity
    print("N = 2T - I =")
    print(n)
    print("operator norm of N:", np.linalg.norm(n, 2))

    # Circulation around the unit circle is pi, so T is not conservative.
    grid = np.linspace(0.0, 2.0 * math.pi, 200_001)
    gamma = np.stack([np.cos(grid), np.sin(grid)], axis=1)
    gamma_prime = np.stack([-np.sin(grid), np.cos(grid)], axis=1)
    integrand = np.einsum("ij,ij->i", gamma @ t.T, gamma_prime)
    circulation = np.trapz(integrand, grid)
    print("unit-circle circulation:", circulation)
    print("expected circulation:", math.pi)

    assert np.all(np.linalg.eigvalsh(firm_gap) >= -1e-12)
    assert abs(np.linalg.norm(n, 2) - 1.0) < 1e-12
    assert abs(circulation - math.pi) < 1e-8


if __name__ == "__main__":
    main()
