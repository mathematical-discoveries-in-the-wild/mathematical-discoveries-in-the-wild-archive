#!/usr/bin/env python3
"""Sanity check for the occupancy lower bound in the c0 counterexample.

This is not part of the proof.  It prints the first- and second-moment
quantities used in the Paley-Zygmund estimate for a few values of N.
"""

from __future__ import annotations

import math


def log_p_event(n: int, r: int) -> float:
    """log P(A_1), where A_1 is exactly r +e_1 hits and no -e_1 hits."""
    return (
        sum(math.log(n - i) for i in range(r))
        - math.lgamma(r + 1)
        - r * math.log(2 * n)
        + (n - r) * math.log1p(-1 / n)
    )


def log_q_pair(n: int, r: int) -> float:
    """log P(A_1 cap A_2)."""
    return (
        sum(math.log(n - i) for i in range(2 * r))
        - 2 * math.lgamma(r + 1)
        - 2 * r * math.log(2 * n)
        + (n - 2 * r) * math.log1p(-2 / n)
    )


def main() -> None:
    for n in [10**6, 10**12, 10**24, 10**48, 10**96]:
        r = max(1, int(math.log(n) / (4 * math.log(math.log(n)))))
        lp = log_p_event(n, r)
        lq = log_q_pair(n, r)
        lez = math.log(n) + lp
        ez_display = math.exp(lez) if lez < 700 else float("inf")
        ratio = math.exp(lq - 2 * lp)
        print(
            f"N=1e{int(math.log10(n)):>3} r={r:>3} "
            f"log(E[Z])={lez:9.3f} E[Z]~={ez_display:10.3g} "
            f"pair_ratio={ratio:8.4f}"
        )


if __name__ == "__main__":
    main()
