#!/usr/bin/env python3
"""Exact rational checks for the 2x2 stability-radius counterexample."""

from fractions import Fraction


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


T = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
I = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]

# det(T - lambda I) = lambda(lambda - 1).
for lam in [Fraction(1, 2), Fraction(1), Fraction(2)]:
    pencil = [[T[i][j] - lam * I[i][j] for j in range(2)] for i in range(2)]
    assert determinant(pencil) == lam * (lam - 1)

for epsilon in [Fraction(1, 2), Fraction(1, 10), Fraction(1, 1000)]:
    L = [
        [Fraction(1), Fraction(1)],
        [-Fraction(1) + epsilon, -Fraction(1) + epsilon],
    ]
    assert matmul(matmul(T, L), T) == T
    assert matmul(matmul(L, T), L) == L
    assert determinant(L) == 0
    assert L[0][0] + L[1][1] == epsilon
    # The characteristic polynomial is z(z-epsilon), so r(L)=epsilon.
    assert matmul(L, L) == [[epsilon * entry for entry in row] for row in L]

print("all exact checks passed")
print("det(T-lambda I)=lambda(lambda-1), so d(T;I)=1")
print("L_epsilon is a generalized inverse and r(L_epsilon)=epsilon -> 0")


if __name__ == "__main__":
    pass
