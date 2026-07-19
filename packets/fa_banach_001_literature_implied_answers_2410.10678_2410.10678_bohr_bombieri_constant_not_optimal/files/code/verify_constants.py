"""Verify the constants used in the Bohr-Bombieri packet.

This script is not a proof of the Bohr-Bombieri theorem.  It only checks the
algebraic simplification of the supporting theorem at r=1/2 and the strict
improvement over the constant used in arXiv:2410.10678, Example 6.3.
"""

from decimal import Decimal, getcontext


def main() -> None:
    getcontext().prec = 50
    sqrt6 = Decimal(6).sqrt()
    sqrt3 = Decimal(3).sqrt()
    improved = Decimal(6) - Decimal(2) * sqrt6
    source = Decimal(2) * sqrt3 / Decimal(3)
    print(f"6 - 2*sqrt(6) = {improved}")
    print(f"2*sqrt(3)/3    = {source}")
    print(f"strict improvement: {improved < source}")
    assert improved > 1
    assert improved < source


if __name__ == "__main__":
    main()
