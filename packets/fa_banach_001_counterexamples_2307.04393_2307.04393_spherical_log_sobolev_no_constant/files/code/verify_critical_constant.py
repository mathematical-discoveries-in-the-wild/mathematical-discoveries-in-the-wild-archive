"""Numerical sanity check for the critical von Mises-Fisher asymptotic.

The proof packet shows symbolically that the constant D_n below is positive.
This script prints representative values.
"""

import mpmath as mp


def critical_gap(n: int) -> mp.mpf:
    x = mp.mpf(n) / 2
    return (
        mp.log(2)
        + mp.log(mp.pi) / 2
        - x
        - mp.log(mp.gamma(x + mp.mpf("0.5")))
        + 2 * x * mp.log(x)
        - x * mp.digamma(x)
    )


def main() -> None:
    for n in range(1, 21):
        print(f"n={n:2d} D_n={float(critical_gap(n)):.12f}")


if __name__ == "__main__":
    main()
