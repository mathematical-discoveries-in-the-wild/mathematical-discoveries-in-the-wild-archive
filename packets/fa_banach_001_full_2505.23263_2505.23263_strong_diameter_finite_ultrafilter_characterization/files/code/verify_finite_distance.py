#!/usr/bin/env python3
"""Sanity-check the finite-Ult(I) total-variation obstruction on grids."""

from fractions import Fraction
def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first, *tail)


def main() -> None:
    checks = 0
    for m in range(1, 9):
        uniform = Fraction(1, m)
        predicted = 2 * (1 - uniform)
        for denominator in range(1, 15):
            best = Fraction(0)
            for counts in compositions(denominator, m):
                distance = sum(
                    abs(uniform - Fraction(count, denominator))
                    for count in counts
                )
                assert distance <= predicted
                best = max(best, distance)
                checks += 1
            assert best == predicted
    print(f"checked={checks} finite_simplex_bound=passed m=1..8 grids=1..14")


if __name__ == "__main__":
    main()
