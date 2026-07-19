"""Sanity checks for finite truncations of the compact non-L-ordered example.

The proof packet is symbolic; this script only verifies the arithmetic pattern
used in the finite chains for a bounded range of n.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


getcontext().prec = 50
SQRT2 = Decimal(2).sqrt()
TOL = Decimal("1e-45")


def epsilon(n: int) -> Decimal:
    return SQRT2 / (Decimal(n) ** 3)


def main() -> None:
    for n in range(2, 101):
        eps = epsilon(n)
        assert Decimal(0) < eps < Decimal(1) / Decimal(n)
        total_bridge = Decimal(n) * eps
        assert abs(total_bridge - SQRT2 / (Decimal(n) ** 2)) < TOL
        assert total_bridge < Decimal("0.36")
        for i in range(n):
            a_i = Decimal(i) / Decimal(n)
            b_i = Decimal(i + 1) / Decimal(n) - eps
            a_next = Decimal(i + 1) / Decimal(n)
            assert Decimal(0) <= a_i <= Decimal(1)
            assert Decimal(0) <= b_i <= Decimal(1)
            assert a_i < b_i < a_next
            assert abs((a_next - b_i) - eps) < TOL
    print("finite-chain arithmetic checks passed for 2 <= n <= 100")


if __name__ == "__main__":
    main()
