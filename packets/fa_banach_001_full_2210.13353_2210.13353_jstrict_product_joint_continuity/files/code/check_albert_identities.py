#!/usr/bin/env python3
"""Exact stress test of the quadratic identities in the real Albert algebra."""

from __future__ import annotations

import random
from fractions import Fraction as F


Oct = tuple[F, F, F, F, F, F, F, F]
Mat = tuple[tuple[Oct, Oct, Oct], tuple[Oct, Oct, Oct], tuple[Oct, Oct, Oct]]


def oadd(x: Oct, y: Oct) -> Oct:
    return tuple(a + b for a, b in zip(x, y, strict=True))  # type: ignore[return-value]


def oscale(t: F, x: Oct) -> Oct:
    return tuple(t * a for a in x)  # type: ignore[return-value]


def oconj(x: Oct) -> Oct:
    return (x[0],) + tuple(-a for a in x[1:])  # type: ignore[return-value]


# Oriented Fano-plane triples: e_i e_j = e_k for each cyclic orientation.
FANO = ((1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5))
OMUL: dict[tuple[int, int], tuple[int, int]] = {}
for i in range(1, 8):
    OMUL[(0, i)] = (1, i)
    OMUL[(i, 0)] = (1, i)
    OMUL[(i, i)] = (-1, 0)
OMUL[(0, 0)] = (1, 0)
for i, j, k in FANO:
    for a, b, c in ((i, j, k), (j, k, i), (k, i, j)):
        OMUL[(a, b)] = (1, c)
        OMUL[(b, a)] = (-1, c)


def omul(x: Oct, y: Oct) -> Oct:
    out = [F(0) for _ in range(8)]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            sign, k = OMUL[(i, j)]
            out[k] += sign * a * b
    return tuple(out)  # type: ignore[return-value]


ZERO_O: Oct = (F(0),) * 8  # type: ignore[assignment]


def madd(x: Mat, y: Mat) -> Mat:
    return tuple(
        tuple(oadd(x[i][j], y[i][j]) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mscale(t: F, x: Mat) -> Mat:
    return tuple(
        tuple(oscale(t, x[i][j]) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mmul(x: Mat, y: Mat) -> Mat:
    return tuple(
        tuple(
            sum_oct(omul(x[i][k], y[k][j]) for k in range(3))
            for j in range(3)
        )
        for i in range(3)
    )  # type: ignore[return-value]


def sum_oct(items) -> Oct:
    out = ZERO_O
    for item in items:
        out = oadd(out, item)
    return out


def circ(x: Mat, y: Mat) -> Mat:
    return mscale(F(1, 2), madd(mmul(x, y), mmul(y, x)))


def usq(a: Mat, x: Mat) -> Mat:
    return madd(mscale(F(2), circ(a, circ(a, x))), mscale(F(-1), circ(circ(a, a), x)))


def ubilin(x: Mat, y: Mat, z: Mat) -> Mat:
    return madd(
        madd(circ(circ(x, z), y), circ(circ(y, z), x)),
        mscale(F(-1), circ(circ(x, y), z)),
    )


def rand_oct(rng: random.Random) -> Oct:
    return tuple(F(rng.randint(-2, 2)) for _ in range(8))  # type: ignore[return-value]


def rand_albert(rng: random.Random) -> Mat:
    out = [[ZERO_O for _ in range(3)] for _ in range(3)]
    for i in range(3):
        diag = [F(0) for _ in range(8)]
        diag[0] = F(rng.randint(-2, 2))
        out[i][i] = tuple(diag)  # type: ignore[assignment]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        q = rand_oct(rng)
        out[i][j] = q
        out[j][i] = oconj(q)
    return tuple(tuple(row) for row in out)  # type: ignore[return-value]


def main() -> None:
    rng = random.Random(221013353)
    for trial in range(40):
        c, x, y, z = (rand_albert(rng) for _ in range(4))

        # Fundamental identity.
        left = usq(usq(c, x), z)
        right = usq(c, usq(x, usq(c, z)))
        assert left == right, ("fundamental identity", trial)

        # Quadratic-tail product identity.
        left = circ(usq(c, x), usq(c, y))
        right = usq(c, ubilin(x, y, circ(c, c)))
        assert left == right, ("tail product identity", trial)

    print("40 exact random Albert-algebra trials passed")
    print("checked: U_{U_c x}=U_c U_x U_c")
    print("checked: U_c x circ U_c y = U_c(U_{x,y}(c^2))")


if __name__ == "__main__":
    main()
