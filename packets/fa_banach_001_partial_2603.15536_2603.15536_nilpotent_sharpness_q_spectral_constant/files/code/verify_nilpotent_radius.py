#!/usr/bin/env python3
"""Sanity checks for the nilpotent sharpness packet.

The proof is analytic.  This script records the elementary scalar identities
used in the packet and prints representative values of the disk radius
D(q)=(1+sqrt(1-|q|^2))/(2|q|) and the conjectured constant.
"""

from __future__ import annotations

import math


def radius(r: float) -> float:
    return (1.0 + math.sqrt(1.0 - r * r)) / (2.0 * r)


def conjectured_constant(r: float) -> float:
    return max(1.0, 2.0 * r / (1.0 + math.sqrt(1.0 - r * r)))


def main() -> None:
    print("r        D(r)          C(r)          C(r)*D(r)")
    for r in [0.2, 0.5, 0.75, 0.8, 0.9, 0.99, 1.0]:
        d = radius(r)
        c = conjectured_constant(r)
        print(f"{r:0.2f}   {d:0.10f}   {c:0.10f}   {c*d:0.10f}")

    for k in range(1, 1000):
        r = k / 1000.0
        d = radius(r)
        c = conjectured_constant(r)
        assert c * d >= 1.0 - 1e-12
        if r >= 0.8:
            assert abs(c * d - 1.0) < 1e-12

    threshold = 4.0 / 5.0
    assert abs(radius(threshold) - 1.0) < 1e-12
    assert abs(conjectured_constant(threshold) - 1.0) < 1e-12
    print("checks passed")


if __name__ == "__main__":
    main()
