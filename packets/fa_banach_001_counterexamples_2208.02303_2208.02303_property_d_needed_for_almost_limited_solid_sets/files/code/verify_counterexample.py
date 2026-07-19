"""Symbolic sanity checks for the C[0,1] counterexample.

The proof is analytic. This script records the elementary numerical identities
for the witness points t_n=1/(2n), s_n=1/(2n+1).
"""

from fractions import Fraction


def witness_values(n: int) -> tuple[Fraction, Fraction, Fraction]:
    t = Fraction(1, 2 * n)
    s = Fraction(1, 2 * n + 1)
    return t, s, t - s


if __name__ == "__main__":
    for n in range(1, 8):
        t, s, gap = witness_values(n)
        print(f"n={n}: t={t}, s={s}, gap={gap}")
    print("For every continuous f, f(t_n)-f(s_n) -> 0 since t_n,s_n -> 0.")
    print("For each fixed n, a continuous f_n with values 1 and -1 at the two points has ||f_n||_inf=1.")
