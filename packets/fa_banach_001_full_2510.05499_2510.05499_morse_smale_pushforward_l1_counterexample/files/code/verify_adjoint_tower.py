#!/usr/bin/env python3
"""Exact finite audit of the Jacobian-neutral adjoint-tower obstruction."""

from fractions import Fraction


def coefficient(k, n):
    return max(Fraction(0), Fraction(1) - Fraction(abs(k), n))


def main():
    stable = Fraction(1, 2)
    unstable = Fraction(4, 1)
    jacobian = stable * unstable
    adjoint_multiplier = jacobian * stable

    assert jacobian == 2
    assert adjoint_multiplier == 1
    print("PASS: det(diag(1/2,4)) = 2 and the stable adjoint multiplier is 1.")

    for n in (2, 3, 5, 10, 50, 100):
        values = {k: coefficient(k, n) for k in range(-n - 1, n + 2)}
        shift_error = max(
            abs(values[k + 1] - values[k]) for k in range(-n - 1, n + 1)
        )
        assert max(values.values()) == 1
        assert shift_error == Fraction(1, n)
        print(f"PASS: N={n:3d}, ||psi_N||=1, adjoint error={shift_error}.")

    print("PASS: the exact tower error tends to zero while the dual norm stays one.")


if __name__ == "__main__":
    main()

