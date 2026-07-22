#!/usr/bin/env python3
"""Exact checks for the unit-cube discrete-covariogram counterexample."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
import math


def discrete_covariogram_on_e1(n: int, r: Fraction) -> int:
    """Count vertices z of [0,1]^n for which z-r*e_1 remains in the cube."""
    count = 0
    for vertex in product((0, 1), repeat=n):
        shifted_first = Fraction(vertex[0]) - r
        if 0 <= shifted_first <= 1:
            count += 1
    return count


def main() -> None:
    rows = []
    for n in range(1, 21):
        total = 2**n
        assert discrete_covariogram_on_e1(n, Fraction(0)) == total
        assert discrete_covariogram_on_e1(n, Fraction(1, 2)) == total // 2
        assert discrete_covariogram_on_e1(n, Fraction(1)) == total // 2
        assert discrete_covariogram_on_e1(n, Fraction(3, 2)) == 0

        rho_p_to_p = Fraction(1, 2)
        right_radius = Fraction(n + 1, 2)  # p=1
        left_radius_squared = Fraction(math.comb(n + 2, n), 2)  # q=2
        right_radius_squared = right_radius**2
        squared_margin = left_radius_squared - right_radius_squared
        assert squared_margin == Fraction(n + 1, 4) > 0

        rows.append(
            {
                "dimension": n,
                "rho_p_to_p": str(rho_p_to_p),
                "right_radius_p1": str(right_radius),
                "left_radius_q2_squared": str(left_radius_squared),
                "right_radius_p1_squared": str(right_radius_squared),
                "positive_squared_margin": str(squared_margin),
            }
        )

    print(json.dumps({"dimensions_checked": 20, "rows": rows}, indent=2))


if __name__ == "__main__":
    main()

