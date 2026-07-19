"""Numerical sanity check for the block constants in the packet.

This is not part of the proof.  It only prints the lower bounds
beta_m=(2-2/m)/m^(1/m^2), which tend to 2.
"""

from __future__ import annotations

import math


def beta(m: int) -> float:
    p = m * m
    return (2.0 - 2.0 / m) / (m ** (1.0 / p))


def main() -> None:
    for m in [3, 4, 5, 10, 20, 50, 100, 500, 1000]:
        print(f"m={m:4d} p={m*m:7d} beta={beta(m):.10f}")
    print("limit: 2")


if __name__ == "__main__":
    main()
