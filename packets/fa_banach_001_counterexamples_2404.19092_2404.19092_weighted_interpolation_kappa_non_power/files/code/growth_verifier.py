"""Sanity check for the kappa envelope in the packet.

This is not part of the proof. It works at the level L = log(n) and prints
logarithmic ratios for
A_n = max(1, sup_{k>=2} 2^{-k} n^{(1-1/k)/2}).
"""

from __future__ import annotations

import math


def log_a_from_log_n(log_n: float, k_max: int = 100000) -> tuple[float, int]:
    best = 0.0
    best_k = 2
    for k in range(2, k_max + 1):
        value = -k * math.log(2.0) + (1.0 - 1.0 / k) * log_n / 2.0
        if value > best:
            best = value
            best_k = k
    return best, best_k


def main() -> None:
    print("L=log(n), log(A/sqrt(n)), log(A/n^0.49), log(A/n^0.40), argmax_k")
    for log_n in (25.0, 100.0, 400.0, 1600.0, 6400.0, 25600.0):
        la, best_k = log_a_from_log_n(log_n)
        print(
            f"{log_n:8.1f}, "
            f"{la - 0.5 * log_n:12.6f}, "
            f"{la - 0.49 * log_n:12.6f}, "
            f"{la - 0.40 * log_n:12.6f}, "
            f"{best_k:5d}"
        )


if __name__ == "__main__":
    main()
