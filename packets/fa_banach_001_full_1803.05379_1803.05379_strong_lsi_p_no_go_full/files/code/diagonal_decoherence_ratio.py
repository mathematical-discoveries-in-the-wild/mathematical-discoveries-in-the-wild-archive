"""Numerical stress check for the p>1 decoherence obstruction.

This computes the second-variation quotient in the two-dimensional model
N = diagonal matrices, L = E_N - id, sigma_tr = I/2.
The entropy coefficient is the relative-entropy divided difference g(x,y).
The p-energy coefficient is proportional to the product of divided differences
for t^(1/p) and t^(1/q).
"""

from __future__ import annotations

import math


def divided_power(x: float, y: float, a: float) -> float:
    if x == y:
        return a * x ** (a - 1.0)
    return (x**a - y**a) / (x - y)


def entropy_dd(x: float, y: float) -> float:
    if x == y:
        return 1.0 / x
    return (math.log(x) - math.log(y)) / (x - y)


def quotient(k: int, p: float) -> float:
    x = 1.0 / k
    y = 1.0 - 1.0 / k
    q = p / (p - 1.0)
    a = divided_power(x, y, 1.0 / p)
    b = divided_power(x, y, 1.0 / q)
    energy_coeff = p / (p - 1.0) * a * b
    entropy_coeff = (1.0 / p) * entropy_dd(x, y)
    return energy_coeff / entropy_coeff


def main() -> None:
    for p in (1.1, 1.25, 1.5, 2.0, 3.0, 8.0):
        vals = [quotient(k, p) for k in (10, 100, 1000, 10000, 100000)]
        print(f"p={p:4.2f}", " ".join(f"{v:.6g}" for v in vals))


if __name__ == "__main__":
    main()
