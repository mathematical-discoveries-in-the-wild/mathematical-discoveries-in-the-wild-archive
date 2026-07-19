#!/usr/bin/env python3
"""Sanity check for the compensated-Poisson lower bound."""

from __future__ import annotations

import math


def lower_bound(p: float, r: float) -> float:
    return (r / 2.0) ** p * math.exp(-1.0 / 4.0) * r ** -2


def main() -> None:
    p = 4.0
    for r in [2, 4, 8, 16, 32, 64]:
        print(f"p={p:g} R={r:>2} lower_bound={lower_bound(p, r):.6g}")


if __name__ == "__main__":
    main()
