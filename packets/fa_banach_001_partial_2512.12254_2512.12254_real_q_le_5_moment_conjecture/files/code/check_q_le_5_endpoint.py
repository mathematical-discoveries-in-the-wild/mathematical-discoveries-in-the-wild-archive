"""Numerical checks for the q <= 5 partial Hunter moment packet.

This script is not part of the proof. It verifies the scalar endpoint facts
used in the packet on finite grids and prints the post-q=5 interpolation
obstruction that explains why the same one-line argument does not continue.
"""

from __future__ import annotations

import math

from scipy.special import gammaln


def rho_ratio(m: int, q: float) -> float:
    """rho(m,q) / Gamma(q+1)."""
    return math.exp(
        gammaln(m + q)
        - gammaln(m)
        - gammaln(q + 1)
        - 0.5 * q * math.log(m)
    )


def min_ratio(n: int, q: float) -> tuple[float, int]:
    vals = [(rho_ratio(m, q), m) for m in range(1, n + 1)]
    return min(vals)


def main() -> None:
    print("Endpoint q=5 ratios rho(m,5)/Gamma(6):")
    for m in range(1, 16):
        print(f"  m={m:2d} ratio={rho_ratio(m, 5.0):.12f}")

    worst = (float("inf"), None, None)
    for n in [2, 3, 5, 10, 50]:
        for j in range(501):
            q = 5.0 * j / 500.0
            value, m = min_ratio(n, q)
            if value < worst[0]:
                worst = (value, q, m)
    print("\nWorst grid value for 0 <= q <= 5 and n <= 50:")
    print(f"  ratio={worst[0]:.12f} at q={worst[1]:.4f}, m={worst[2]}")

    q = 5.35
    a_q, m_q = min_ratio(50, q)
    a_5, _ = min_ratio(50, 5.0)
    a_6, _ = min_ratio(50, 6.0)
    theta = q - 5.0
    chord = a_5 ** (1.0 - theta) * a_6**theta
    print("\nNaive log-concavity interpolation beyond q=5:")
    print(f"  q={q:.2f}, min rho/Gamma={a_q:.12f} at m={m_q}")
    print(f"  chord from q=5 to q=6 gives {chord:.12f}")
    print(f"  chord/min ratio={chord / a_q:.12f}")


if __name__ == "__main__":
    main()
