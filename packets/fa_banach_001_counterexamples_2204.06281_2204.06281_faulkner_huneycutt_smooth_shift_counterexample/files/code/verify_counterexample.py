#!/usr/bin/env python3
"""Exact checks for the 2204.06281 Faulkner-Huneycutt counterexample."""

from fractions import Fraction


def phi(a, b, c):
    return (a + b + c) ** 4 + (a - c) ** 4 + (b - c) ** 4 + (a - b) ** 4


def coeff_a(a, b, c):
    return (a + b + c) ** 3 + (a - c) ** 3 + (a - b) ** 3


def coeff_b(a, b, c):
    return (a + b + c) ** 3 + (b - c) ** 3 - (a - b) ** 3


def coeff_c(a, b, c):
    return (a + b + c) ** 3 - (a - c) ** 3 - (b - c) ** 3


def get(x, index):
    return x.get(index, Fraction(0))


def support_coordinate(x, k):
    """N(x)^3 times the support functional at x evaluated on e_k."""
    return (
        coeff_c(get(x, k - 2), get(x, k - 1), get(x, k))
        + coeff_b(get(x, k - 1), get(x, k), get(x, k + 1))
        + coeff_a(get(x, k), get(x, k + 1), get(x, k + 2))
    )


def norm_fourth_power(x):
    if not x:
        return Fraction(0)
    last = max(x) + 2
    return sum(phi(get(x, n - 2), get(x, n - 1), get(x, n)) for n in range(1, last + 1))


def shift_two(x):
    return {k + 2: v for k, v in x.items() if v}


def main():
    e1 = {1: Fraction(1)}
    e2 = {2: Fraction(1)}
    e1_plus_e2 = {1: Fraction(1), 2: Fraction(1)}

    for k in range(3, 12):
        assert support_coordinate(e1, k) == 0, (e1, k, support_coordinate(e1, k))
        assert support_coordinate(e2, k) == 0, (e2, k, support_coordinate(e2, k))

    obstruction = support_coordinate(e1_plus_e2, 3)
    assert obstruction == 6, obstruction

    samples = [
        {1: Fraction(2), 3: Fraction(-1), 5: Fraction(4)},
        {2: Fraction(3), 4: Fraction(1), 6: Fraction(-2)},
        {1: Fraction(1), 2: Fraction(1), 3: Fraction(1)},
    ]
    for x in samples:
        assert norm_fourth_power(shift_two(x)) == norm_fourth_power(x), x

    print("e1 and e2 annihilate the shifted range: ok")
    print("support coefficient for e1+e2 in direction e3:", obstruction)
    print("two-step shift preserves the fourth power of the norm on samples: ok")


if __name__ == "__main__":
    main()
