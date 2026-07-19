"""Verify the polyhedral counterexample to the corrected projection problem."""

import math
from fractions import Fraction


def norm_x(x1: float, x2: float) -> float:
    a = math.sqrt(3 / 5)
    b = math.sqrt(2 / 5)
    return max(abs(x1), abs(x2), abs(a * x1 + b * x2))


def main() -> None:
    a = math.sqrt(3 / 5)
    b = math.sqrt(2 / 5)
    target_q = Fraction(1, 2)
    epsilon_q = Fraction(1, 5)
    lower_q = (1 - epsilon_q) * target_q
    upper_q = (1 + epsilon_q) * target_q
    target = float(target_q)
    lower = float(lower_q)
    upper = float(upper_q)

    print(f"a^2 = {a*a:.12f}, b^2 = {b*b:.12f}")
    print(f"target n/d = {target_q}")
    print(f"epsilon interval = [{lower_q}, {upper_q}]")
    for k, exact, value in [(1, Fraction(3, 5), a * a), (2, Fraction(2, 5), b * b)]:
        print(
            f"k={k}: common hypothesis value={exact} "
            f"({value:.12f}); in interval={lower_q <= exact <= upper_q}"
        )

    max_flat_norm = 0.0
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            value = norm_x(s1 / math.sqrt(2), s2 / math.sqrt(2))
            max_flat_norm = max(max_flat_norm, value)
            print(f"norm(({s1})/sqrt(2), ({s2})/sqrt(2)) = {value:.12f}")

    print(f"max norm of flat coordinate-modulus vectors = {max_flat_norm:.12f}")
    print(f"(a+b)/sqrt(2) = {(a+b)/math.sqrt(2):.12f}")
    print("All are strictly below 1, so no corrected flat projection Q can exist.")


if __name__ == "__main__":
    main()
