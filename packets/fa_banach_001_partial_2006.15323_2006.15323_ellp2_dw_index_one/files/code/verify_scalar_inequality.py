#!/usr/bin/env python3
"""Numerical sanity check for the scalar inequality in the packet."""

from __future__ import annotations

import math


def value(p: float, t: float) -> float:
    # t = |a|^p in the proof's first parametrization.
    return t ** (2.0 / p) * (1.0 - t) ** (2.0 - 2.0 / p) + t ** (4.0 / p)


def main() -> None:
    worst = (0.0, None, None)
    for i in range(601):
        p = 2.0 + 6.0 * i / 600.0
        for j in range(20001):
            t = j / 20000.0
            v = value(p, t)
            if v > worst[0]:
                worst = (v, p, t)
    print(f"max grid value={worst[0]:.12f} at p={worst[1]:.6f}, t={worst[2]:.6f}")
    if worst[0] > 1.0 + 1e-10:
        raise SystemExit("scalar inequality failed on grid")


if __name__ == "__main__":
    main()
