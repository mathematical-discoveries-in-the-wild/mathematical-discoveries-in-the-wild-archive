#!/usr/bin/env python3
"""Arithmetic checks for the non-attained-cotype endpoint counterexample."""

from fractions import Fraction


def r(n: int) -> Fraction:
    return Fraction(2 * n + 1, n)


def log_n_N(n: int) -> int:
    return 4 * n + 2


for n in range(1, 8):
    rn = r(n)
    cotype2_exponent = Fraction(1, 2) - Fraction(1, rn)
    endpoint_exponent = 1 - 4 * (Fraction(1, rn) - Fraction(1, 4))

    # N_n = n^(4n+2).  These are logarithms base n of the relevant powers.
    cotype2_log = log_n_N(n) * cotype2_exponent
    endpoint_log = log_n_N(n) * endpoint_exponent

    print(
        f"n={n}: r_n={rn}, "
        f"N_n^(1/2-1/r_n)=n^{cotype2_log}, "
        f"N_n^(1-4(1/r_n-1/4))=n^{endpoint_log}"
    )

    assert cotype2_log == 1
    assert endpoint_log == 4

print("Thus cotype-2 block constants grow like n.")
print("The endpoint ell_4 block contribution is n^-4 * n^4 = 1 for every n.")
