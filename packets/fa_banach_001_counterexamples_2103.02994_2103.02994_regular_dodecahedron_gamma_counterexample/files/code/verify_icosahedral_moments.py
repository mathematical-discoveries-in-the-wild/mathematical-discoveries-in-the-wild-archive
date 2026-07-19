#!/usr/bin/env python3
"""Exact moment certificate for the regular-dodecahedron counterexample."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, y, z = sp.symbols("x y z", real=True)
    phi = (1 + sp.sqrt(5)) / 2
    norm_squared = sp.simplify(1 + phi**2)

    raw_normals = []
    for first_sign in (-1, 1):
        for second_sign in (-1, 1):
            raw_normals.extend(
                [
                    (0, first_sign, second_sign * phi),
                    (first_sign, second_sign * phi, 0),
                    (first_sign * phi, 0, second_sign),
                ]
            )

    normal_set = set(raw_normals)
    assert len(normal_set) == 12
    assert all(tuple(-entry for entry in normal) in normal_set for normal in normal_set)

    vector = (x, y, z)
    raw_dots = [sum(vector[i] * normal[i] for i in range(3)) for normal in raw_normals]
    second_moment = sp.expand(sum(dot**2 for dot in raw_dots) / norm_squared)
    fourth_moment = sp.expand(sum(dot**4 for dot in raw_dots) / norm_squared**2)

    radius_squared = x**2 + y**2 + z**2
    assert sp.simplify(second_moment - 4 * radius_squared) == 0
    assert sp.simplify(fourth_moment - sp.Rational(12, 5) * radius_squared**2) == 0

    # If each facet has area a and the inradius is 1, V(K)=12a/3=4a.
    gamma_minus_2_coefficient = sp.Rational(1, 4) * 4
    gamma_minus_4_coefficient = sp.Rational(1, 4) * sp.Rational(12, 5)
    assert gamma_minus_2_coefficient == 1
    assert gamma_minus_4_coefficient == sp.Rational(3, 5)

    print(
        json.dumps(
            {
                "arithmetic": "exact symbolic over Q(sqrt(5))",
                "normal_count": len(raw_normals),
                "second_moment": "sum <x,u>^2 = 4 |x|^2",
                "fourth_moment": "sum <x,u>^4 = (12/5) |x|^4",
                "volume_to_facet_area_ratio": "V(K)/a = 4",
                "Gamma_-2": "B_2^3",
                "Gamma_-4": "(5/3)^(1/4) B_2^3",
                "verdict": "regular dodecahedron satisfies Theorem 4.1(3) but is not an ellipsoid",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
