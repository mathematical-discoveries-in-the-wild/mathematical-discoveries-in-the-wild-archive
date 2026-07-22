#!/usr/bin/env python3
"""Finite-range sanity checks for the arXiv:2501.14581 counterexample.

The uniform argument is in main.tex.  These floating-point checks are not a
proof and are included only to catch transcription or sign errors.
"""

import math


B = math.exp(4.0)


def h(n: int) -> float:
    return math.sin(math.log(math.log(n + B)))


def c(n: int) -> float:
    return 0.0 if n == 0 else 15.0 * n / math.log(n + B)


def defect(m: int, n: int) -> float:
    return abs((m + n) * h(m + n) - m * h(m) - n * h(n))


def main() -> None:
    max_ratio = (0.0, (0, 0))
    exhaustive_limit = 800
    for n in range(1, exhaustive_limit + 1):
        assert c(n) >= c(n - 1)
        for m in range(1, n + 1):
            d = defect(m, n)
            bound = c(m) + c(n)
            assert d <= bound + 1e-11 * max(1.0, bound)
            ratio = d / bound
            if ratio > max_ratio[0]:
                max_ratio = (ratio, (m, n))

    subadditive_limit = 400
    for n in range(1, subadditive_limit + 1):
        for m in range(1, subadditive_limit + 1):
            assert c(m + n) <= c(m) + c(n) + 1e-12 * (c(m) + c(n))

    large_ns = [10**k for k in range(3, 13)]
    for n in large_ns:
        probes = {
            1,
            max(1, int(math.sqrt(n))),
            max(1, n // int(max(1.0, math.log(n)))),
            n // 2,
            n,
        }
        for m in probes:
            assert defect(m, n) <= c(m) + c(n)

    print(f"exhaustive defect checks: 1 <= m <= n <= {exhaustive_limit}: PASS")
    print(f"finite subadditivity checks: 1 <= m,n <= {subadditive_limit}: PASS")
    print(f"large-scale probes through n={large_ns[-1]}: PASS")
    print(f"largest exhaustive defect/bound ratio: {max_ratio[0]:.12f} at {max_ratio[1]}")


if __name__ == "__main__":
    main()
