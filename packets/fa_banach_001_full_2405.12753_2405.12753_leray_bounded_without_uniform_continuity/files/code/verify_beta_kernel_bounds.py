#!/usr/bin/env python3
"""Finite sanity checks for the beta-kernel estimates in the packet.

This script is not part of the proof.  It evaluates all quantities through
log-gamma formulas to avoid overflow.
"""

from __future__ import annotations

import math


def log_b0(m: int, n: int) -> float:
    """log of max_s s^(2m)(1-s)^(2n), with 0 log 0 := 0."""
    total = m + n
    if total == 0:
        return 0.0
    value = 0.0
    if m:
        value += 2.0 * m * math.log(m / total)
    if n:
        value += 2.0 * n * math.log(n / total)
    return value


def log_j(c: float, m: int, n: int) -> float:
    total = m + n
    if total == 0:
        return 0.0
    log_beta = (
        math.lgamma(2.0 * c * m + 1.0)
        + math.lgamma(2.0 * c * n + 1.0)
        - math.lgamma(2.0 * c * total + 2.0)
    )
    return log_beta - c * log_b0(m, n)


def log_gamma_factor(m: int, n: int) -> float:
    total = m + n
    return (
        2.0
        * (
            math.lgamma(total + 2.0)
            - math.lgamma(m + 1.0)
            - math.lgamma(n + 1.0)
        )
        + log_b0(m, n)
    )


def main() -> None:
    grid_max = 300
    c_values = (0.05, 0.1, 0.25, 0.5, 0.9)

    for c in c_values:
        max_scaled = 0.0
        argmax = (0, 0)
        for m in range(grid_max + 1):
            for n in range(grid_max + 1):
                if m + n == 0:
                    continue
                scale_log = (
                    log_j(c, m, n)
                    + 1.5 * math.log(m + n + 1.0)
                    - 0.5 * math.log((m + 1.0) * (n + 1.0))
                )
                scaled = math.exp(scale_log)
                if scaled > max_scaled:
                    max_scaled = scaled
                    argmax = (m, n)
        print(
            f"c={c:0.2f}: max J_c*(M+1)^(3/2)/sqrt((m+1)(n+1)) "
            f"= {max_scaled:.12g} at {argmax}"
        )

    max_binomial = 0.0
    binomial_argmax = (0, 0)
    for m in range(grid_max + 1):
        for n in range(grid_max + 1):
            if m + n == 0:
                continue
            total = m + n
            scale_log = (
                log_gamma_factor(m, n)
                + math.log((m + 1.0) * (n + 1.0))
                - 3.0 * math.log(total + 1.0)
            )
            scaled = math.exp(scale_log)
            if scaled > max_binomial:
                max_binomial = scaled
                binomial_argmax = (m, n)
    print(
        "max gamma^2*B0*(m+1)(n+1)/(M+1)^3 "
        f"= {max_binomial:.12g} at {binomial_argmax}"
    )

    assert math.isfinite(max_binomial)
    assert all(math.isfinite(log_j(c, grid_max, grid_max)) for c in c_values)
    print(
        f"PASS: checked {len(c_values)} beta exponents and all "
        f"(m,n) in [0,{grid_max}]^2."
    )


if __name__ == "__main__":
    main()

