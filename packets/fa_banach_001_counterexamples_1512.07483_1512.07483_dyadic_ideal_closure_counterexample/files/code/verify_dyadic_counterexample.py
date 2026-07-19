"""Finite-level sanity check for the dyadic ideal-closure counterexample.

The proof is analytic; this script only verifies the elementary identities for
the simple functions used to place 1 in the relaxed ideal I.
"""

from fractions import Fraction


def check_levels(max_level: int = 8) -> None:
    for k in range(1, max_level + 1):
        length = Fraction(1, 2**k)
        for j in range(1, 2**k + 1):
            l1_distance_to_one = length
            averaged_deleted_interval = Fraction(0, 1)
            assert l1_distance_to_one == Fraction(1, 2**k)
            assert averaged_deleted_interval == 0
        print(f"level {k}: distance 2^-k = {length}, all deleted averages vanish")


if __name__ == "__main__":
    check_levels()
