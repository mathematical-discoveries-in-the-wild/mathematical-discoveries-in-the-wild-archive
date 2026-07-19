"""Arithmetic checks for the BD/convex-DLD2P counterexample.

This script is not a proof.  It verifies the displayed finite witnesses for
the hyperplane X = {x in c : 2 lim x = x_1 + x_2}.
"""

from fractions import Fraction


def in_hyperplane(limit, x1, x2):
    return 2 * limit == x1 + x2


def main():
    z = {
        "limit": Fraction(0),
        "x1": Fraction(1),
        "x2": Fraction(-1),
    }
    print("z in X:", in_hyperplane(z["limit"], z["x1"], z["x2"]))
    print("z has x1=x2=limit:", z["x1"] == z["x2"] == z["limit"])

    u = {
        "limit": Fraction(1),
        "x1": Fraction(1),
        "x2": Fraction(1),
    }
    print("u in X:", in_hyperplane(u["limit"], u["x1"], u["x2"]))
    print("tail values e_n(u)=1-1/n for n=3..12:")
    for n in range(3, 13):
        value = Fraction(1) - Fraction(1, n)
        print(n, value, "attains 1:", value == 1)

    print("BD witness tail tends to 1 from below; checked first ten terms.")


if __name__ == "__main__":
    main()
