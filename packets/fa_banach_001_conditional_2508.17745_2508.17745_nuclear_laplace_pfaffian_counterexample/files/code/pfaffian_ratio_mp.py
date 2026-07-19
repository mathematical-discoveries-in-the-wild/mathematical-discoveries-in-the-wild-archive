#!/usr/bin/env python3
"""High-precision continuation of the normalized Pfaffian experiment."""

import argparse
import math
import mpmath as mp


def qentry(i: int, j: int) -> mp.mpf:
    if i == j:
        return mp.mpf("0")
    if i > j:
        return -qentry(j, i)
    # 2 I_{1/2}(2i+1,2j+1)-1.
    return 2 * mp.betainc(2 * i + 1, 2 * j + 1, 0, mp.mpf("0.5"), regularized=True) - 1


def pfaffian(matrix: list[list[mp.mpf]]) -> mp.mpf:
    a = [row[:] for row in matrix]
    size = len(a)
    value = mp.mpf("1")
    for k in range(0, size, 2):
        pivot = max(range(k + 1, size), key=lambda j: abs(a[k][j]))
        if pivot != k + 1:
            for row in range(size):
                a[row][k + 1], a[row][pivot] = a[row][pivot], a[row][k + 1]
            a[k + 1], a[pivot] = a[pivot], a[k + 1]
            value = -value
        p = a[k][k + 1]
        value *= p
        for i in range(k + 2, size):
            for j in range(i + 1, size):
                updated = a[i][j] - (
                    a[k][i] * a[k + 1][j] - a[k][j] * a[k + 1][i]
                ) / p
                a[i][j] = updated
                a[j][i] = -updated
    return value


def integral(indices: list[int]) -> mp.mpf:
    n = len(indices)
    size = n if n % 2 == 0 else n + 1
    matrix = [[mp.mpf("0") for _ in range(size)] for _ in range(size)]
    for row, i in enumerate(indices):
        for col in range(row + 1, n):
            entry = qentry(i, indices[col])
            matrix[row][col] = entry
            matrix[col][row] = -entry
        if n % 2:
            matrix[row][n] = 1
            matrix[n][row] = -1
    return pfaffian(matrix)


def ratio(n: int) -> mp.mpf:
    return integral(list(range(1, n))) / integral(list(range(n)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=120)
    parser.add_argument("--step", type=int, default=10)
    parser.add_argument("--dps", type=int, default=300)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    previous = None
    print("n\tratio\tratio/log(n)\tn*(increment)")
    for n in range(args.step, args.max_n + 1, args.step):
        value = ratio(n)
        increment = mp.nan
        if previous is not None:
            increment = n * (value - previous) / args.step
        previous = value
        print(
            f"{n}\t{mp.nstr(value, 18)}\t"
            f"{mp.nstr(value / mp.log(n), 18)}\t{mp.nstr(increment, 18)}"
        )


if __name__ == "__main__":
    main()
