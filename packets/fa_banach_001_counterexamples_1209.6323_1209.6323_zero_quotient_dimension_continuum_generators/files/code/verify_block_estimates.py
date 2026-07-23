#!/usr/bin/env python3
"""Finite consistency checks for the block-separation estimates.

This script is not part of the proof.  It evaluates the logarithmic upper
bounds used twice in the argument, avoiding floating-point underflow.
"""

from math import log


def level(k: int) -> int:
    return 1 if k == 0 else 2 ** (2**k)


def main() -> None:
    constant = 7.0
    terms = 4
    minimum_power = 1.0 / 16.0
    maximum_ampliation = 12

    print("k  log(RHS/xi_A) upper bound  log(RHS/zeta) upper bound")
    for k in range(2, 8):
        current = level(k)
        previous = level(k - 1)
        block_start = level(k)

        incomparable_bound = (
            log(constant * terms) - minimum_power * current + previous
        )
        slow_sequence_bound = (
            log(constant * terms)
            + log(log(maximum_ampliation * block_start + 1))
            - minimum_power * current
        )
        print(
            f"{k:1d}  {incomparable_bound:25.6g}"
            f"  {slow_sequence_bound:25.6g}"
        )

    for r in range(6):
        exponent = 2.0 ** (-r)
        root_exponent = 2.0 ** (-(r + 1))
        assert 2.0 * root_exponent == exponent

    print("successive-root square identities checked for r=0,...,5")


if __name__ == "__main__":
    main()
