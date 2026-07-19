"""Sanity check for the finite lower bound in the Q_A^(t) packet.

This is not a proof.  It evaluates the lower bound obtained from the odd
Riesz-product test polynomial for the sample vector y_n = n^(-1/2).
"""

from __future__ import annotations

import math


def lower_bound(n: int, t: float = 4.0) -> float:
    y = [1.0 / math.sqrt(k) for k in range(1, n + 1)]
    r = sum(v**t for v in y) ** (1.0 / t)
    a_log = 0.0
    ratio_log = 0.0
    for v in y:
        b2 = (v / r) ** 2
        a_log += math.log1p(b2)
        if b2 >= 1.0:
            ratio_log = float("-inf")
        elif ratio_log != float("-inf"):
            ratio_log += math.log1p(-b2) - math.log1p(b2)
    ratio = 0.0 if ratio_log == float("-inf") else math.exp(ratio_log)
    return 0.5 * r * math.exp(0.5 * a_log) * (1.0 - ratio)


def main() -> None:
    for n in [4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        print(f"N={n:4d} lower_bound={lower_bound(n):.6f}")


if __name__ == "__main__":
    main()
