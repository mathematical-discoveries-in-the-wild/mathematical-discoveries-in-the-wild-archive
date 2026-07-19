"""Sanity check for the finite-set exponent in the packet proof.

For a finite set A={a_1,...,a_m}, the proof bounds

    ||(x_1,...,x_n)||_n^(p,q) <= M n^max(0, 1/q - 1/p),

where M=sum ||a_i||.  After normalization by n^(1/q), the exponent is
negative: -1/q if q >= p and -1/p if q < p.
"""

from fractions import Fraction


def normalized_exponent(p: int, q: int) -> Fraction:
    raw = max(Fraction(0), Fraction(1, q) - Fraction(1, p))
    return raw - Fraction(1, q)


if __name__ == "__main__":
    for p in range(1, 8):
        for q in range(1, 8):
            exponent = normalized_exponent(p, q)
            assert exponent < 0, (p, q, exponent)
    print("all checked exponents are negative")

