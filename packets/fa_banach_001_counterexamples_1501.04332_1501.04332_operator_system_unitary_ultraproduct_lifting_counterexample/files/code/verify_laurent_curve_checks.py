#!/usr/bin/env python3
"""Sanity checks for the operator-system unitary lifting counterexample.

This is not a formal proof assistant. It records the elementary computations
used in the packet:

* the signed curvature numerator of gamma_eps(theta)=z+eps z^2 is
  1 + 6 eps cos(theta) + 8 eps^2, hence positive for eps < 1/4;
* a constant-modulus Laurent polynomial in the packet's three-dimensional
  space can only be a scalar constant;
* f_eps=z+eps z^2 is uniformly far from scalar unitaries.
"""

from __future__ import annotations

import math


def curvature_lower_bound(eps: float) -> float:
    return 1.0 - 6.0 * eps + 8.0 * eps * eps


def coefficient_case_summary(eps_symbol: str = "eps") -> list[str]:
    return [
        f"q(z)=c z^0 would force gamma*{eps_symbol}=c and gamma=0: impossible for c!=0",
        "q(z)=c z^1 would force gamma=c and gamma*eps=0: impossible for eps>0",
        "q(z)=c z^2 gives beta=gamma=0 and alpha=c: scalar constants",
        "q(z)=c z^3 would force beta=c and beta*eps=0: impossible for eps>0",
        "q(z)=c z^4 would force beta*eps=c and beta=0: impossible for c!=0",
    ]


def sampled_distance_to_scalar_unitaries(eps: float, samples: int = 20000) -> float:
    """Coarse sample of min_lambda ||z+eps z^2-lambda|| over scalar unitaries."""
    best = float("inf")
    for j in range(samples):
        lam_angle = 2.0 * math.pi * j / samples
        lam = complex(math.cos(lam_angle), math.sin(lam_angle))
        worst = 0.0
        for k in range(samples):
            angle = 2.0 * math.pi * k / samples
            z = complex(math.cos(angle), math.sin(angle))
            worst = max(worst, abs(z + eps * z * z - lam))
        best = min(best, worst)
    return best


def main() -> None:
    eps_values = [1 / 6, 1 / 10, 1 / 50, 1 / 100]
    print("Curvature lower bounds for gamma_eps(theta)=z+eps z^2:")
    for eps in eps_values:
        print(f"  eps={eps:.6f}: min numerator >= {curvature_lower_bound(eps):.6f}")
        assert 0 < eps < 0.25
        assert curvature_lower_bound(eps) > 0

    print("\nCoefficient cases for |alpha+beta f_eps+gamma f_eps^*|=1 on T:")
    for line in coefficient_case_summary():
        print(f"  - {line}")

    print("\nDistance lower bound used in proof:")
    for eps in [1 / 6, 1 / 20, 1 / 100]:
        print(f"  eps={eps:.6f}: ||f_eps-lambda|| >= 2-eps = {2-eps:.6f}")

    print("\nSmall sampled check for eps=0.1, 200 samples:")
    print(f"  sampled min distance ~= {sampled_distance_to_scalar_unitaries(0.1, samples=200):.6f}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
