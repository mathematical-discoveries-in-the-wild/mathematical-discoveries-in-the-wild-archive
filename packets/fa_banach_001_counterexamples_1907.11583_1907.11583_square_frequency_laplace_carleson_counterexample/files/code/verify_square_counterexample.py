"""Finite sanity checks for the square-frequency counterexample.

The proof in ``main.tex`` is analytic and does not depend on this script.  The
script checks finite square counts, the exact integer-frequency sampling
matrix, and the proved norm-ratio lower bound.
"""

from __future__ import annotations

import math


def max_square_count(length: int, right_endpoint: int) -> int:
    squares = [n * n for n in range(1, math.isqrt(right_endpoint) + 1)]
    best = 0
    for left in range(-length, right_endpoint + 1):
        right = left + length
        count = sum(left <= square <= right for square in squares)
        best = max(best, count)
    return best


def sampling_value(n: int, cutoff: int) -> int:
    # Integral_0^1 exp(2*pi*i*(n^2-k^2)t) dt is 1 when n=k and 0 otherwise.
    return sum(int(n * n == k * k) for k in range(1, cutoff + 1))


def main() -> None:
    print("box-count checks for mu = sum delta_(n^2+i)")
    for length in (1, 2, 4, 9, 16, 25, 64, 100):
        count = max_square_count(length, 400)
        bound = 2.0 * math.sqrt(length)
        assert count <= bound
        print(f"length={length:3d} max_count={count:2d} bound={bound:6.3f}")

    print("\nexact samples and norm-ratio lower bounds")
    for cutoff in (4, 16, 64, 256, 1024, 4096):
        samples = [sampling_value(n, cutoff) for n in range(1, cutoff + 3)]
        assert samples[:cutoff] == [1] * cutoff
        assert samples[cutoff:] == [0, 0]
        output_norm = cutoff ** (2.0 / 3.0)
        input_upper = math.exp(2.0 * math.pi) * math.sqrt(cutoff)
        ratio_lower = output_norm / input_upper
        scaled_ratio = ratio_lower / (cutoff ** (1.0 / 6.0))
        assert math.isclose(scaled_ratio, math.exp(-2.0 * math.pi))
        print(
            f"N={cutoff:4d} output={output_norm:10.5f} "
            f"input_upper={input_upper:12.5f} ratio_lower={ratio_lower:.8f}"
        )


if __name__ == "__main__":
    main()
