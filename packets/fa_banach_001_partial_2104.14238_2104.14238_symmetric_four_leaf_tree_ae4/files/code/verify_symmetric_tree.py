import math

import numpy as np


def projection_matrix(r):
    D = r * r + 3 * r + 4
    q = (r + 3) / (2 * D)
    # Coordinates are (a,b,z,c,d).  Put
    # s=a+b+c+d and h=z-r(a+b-c-d)/2.
    M = np.zeros((5, 5), dtype=float)
    for j, x in enumerate(np.eye(5)):
        a, b, z, c, d = x
        s = a + b + c + d
        h = z - 0.5 * r * (a + b - c - d)
        y = np.array(
            [
                a - s / 4 + q * h,
                b - s / 4 + q * h,
                z + (2 * r * q - 1) * h,
                c - s / 4 - q * h,
                d - s / 4 - q * h,
            ]
        )
        M[:, j] = y
    return M


def witness_matrix(r):
    D = r * r + 3 * r + 4
    weights = np.array(
        [
            (r + 2) / (2 * D),
            (r + 2) / (2 * D),
            r * (r + 1) / D,
            (r + 2) / (2 * D),
            (r + 2) / (2 * D),
        ]
    )
    S = np.array(
        [
            [1, -1, 1, -1, -1],
            [-1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, -1],
            [-1, -1, -1, -1, 1],
        ],
        dtype=float,
    )
    return weights[:, None] * S


def formula(r):
    return ((r + 2) * (r + 3)) / (r * r + 3 * r + 4)


def main():
    for r in [0.0, 0.2, math.sqrt(2) - 1, 1.0, 2.0]:
        Q = projection_matrix(r)
        col_norm = np.max(np.sum(np.abs(Q), axis=0))
        A = witness_matrix(r)
        nuclear = np.sum(np.max(np.abs(A), axis=1))
        print(f"r={r:.12g} formula={formula(r):.12g} projection_norm={col_norm:.12g} witness_nu1={nuclear:.12g}")


if __name__ == "__main__":
    main()
