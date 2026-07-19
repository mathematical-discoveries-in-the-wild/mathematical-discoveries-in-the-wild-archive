#!/usr/bin/env python3
"""Numerical smoke check for the scalar polynomial-center counterexample.

The proof is exact. This script samples the unit ball to illustrate that
Q(z)=z^2 satisfies ||Q+a z|| = 1+|a| for linear perturbations and fails
for the polynomial perturbation P=-Q.
"""

from __future__ import annotations

import cmath
import math


def max_on_circle(a: complex, samples: int = 20000) -> float:
    return max(
        abs(z * z + a * z)
        for z in (cmath.exp(2j * math.pi * k / samples) for k in range(samples))
    )


def main() -> None:
    for a in [0, 0.25, -0.7, 1.5, 1 + 2j, -0.3 + 0.9j]:
        lhs = max_on_circle(complex(a))
        rhs = 1 + abs(a)
        print(f"a={a!r}: sampled ||Q+a id||={lhs:.8f}, 1+|a|={rhs:.8f}")
        assert abs(lhs - rhs) < 1e-3
    print("polynomial perturbation P=-Q gives ||Q+P||=0 < 2=||Q||+||P||")


if __name__ == "__main__":
    main()
