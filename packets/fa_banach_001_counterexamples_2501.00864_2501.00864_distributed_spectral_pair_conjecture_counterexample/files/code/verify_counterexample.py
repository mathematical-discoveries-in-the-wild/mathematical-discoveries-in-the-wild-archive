#!/usr/bin/env python3
"""Exact check for the counterexample to Conjecture 5.1 in arXiv:2501.00864.

The check uses only integer arithmetic.  For
P_A(x)=sum_{a in A} x^a=(1+x^3)(1+x^18), the cyclotomic zero orders are
{2, 4, 6, 12, 36}.  Hence P_A(exp(2*pi*i*t/N))=0 exactly when the order
of exp(2*pi*i*t/N), namely N/gcd(N,t), lies in this set.
"""

from math import gcd


M = 24
A = {0, 3, 18, 21}
B = {0, 4, 16, 20}
ZERO_ORDERS = {2, 4, 6, 12, 36}


def order_mod(n: int, t: int) -> int:
    return n // gcd(n, t)


def p_a_zero(n: int, t: int) -> bool:
    return order_mod(n, t) in ZERO_ORDERS


def differences(s):
    return {x - y for x in s for y in s}


def is_distributed() -> bool:
    dset = differences(B)
    for d in dset:
        if d == 0:
            continue
        first = p_a_zero(M, d)
        second = all(p_a_zero(M * M, d + M * e) for e in dset)
        if not (first or second):
            print("failed distributed condition at d=", d)
            return False
    return True


def is_spectral(n: int) -> bool:
    return all(d == 0 or p_a_zero(n, d) for d in differences(B))


def main() -> None:
    print("M =", M)
    print("A =", sorted(A))
    print("B =", sorted(B))
    print("B-B =", sorted(differences(B)))
    print("distributed =", is_distributed())
    print("spectral in Z_M =", is_spectral(M))
    print("spectral in Z_M^2 =", is_spectral(M * M))
    assert is_distributed()
    assert not is_spectral(M)
    assert not is_spectral(M * M)


if __name__ == "__main__":
    main()
