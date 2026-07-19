#!/usr/bin/env python3
"""Finite sanity checks for the torsion Cotlar collapse packet.

The proof in the packet is symbolic. This script only enumerates equality
patterns with three colors on a few small finite groups to catch obvious
mistakes in the algebraic identity.
"""

from __future__ import annotations

from itertools import permutations, product


def cyclic(n: int):
    elems = list(range(n))
    identity = 0
    inv = {a: (-a) % n for a in elems}

    def mul(a, b):
        return (a + b) % n

    return elems, identity, inv, mul


def elementary_two_group(rank: int):
    elems = list(product([0, 1], repeat=rank))
    identity = tuple([0] * rank)
    inv = {a: a for a in elems}

    def mul(a, b):
        return tuple((x + y) % 2 for x, y in zip(a, b))

    return elems, identity, inv, mul


def dihedral(n: int):
    elems = [(i, j) for i in range(n) for j in range(2)]
    identity = (0, 0)

    def mul(a, b):
        i, j = a
        k, ell = b
        return ((i + ((-1) ** j) * k) % n, (j + ell) % 2)

    inv = {
        a: next(b for b in elems if mul(a, b) == identity and mul(b, a) == identity)
        for a in elems
    }
    return elems, identity, inv, mul


def symmetric_three():
    elems = list(permutations(range(3)))
    identity = (0, 1, 2)

    def mul(p, q):
        return tuple(p[i] for i in q)

    inv = {
        p: next(q for q in elems if mul(p, q) == identity and mul(q, p) == identity)
        for p in elems
    }
    return elems, identity, inv, mul


def cotlar_valid(elems, identity, inv, mul, color):
    for g in elems:
        if g == identity:
            continue
        for h in elems:
            if color[inv[g]] != color[h] and color[mul(g, h)] != color[g]:
                return False
    return True


def count_valid(builder, colors: int = 3):
    elems, identity, inv, mul = builder()
    others = [x for x in elems if x != identity]
    valid = 0
    nonconstant_off_identity = 0
    for assignment in product(range(colors), repeat=len(others)):
        color = {identity: 0}
        color.update(dict(zip(others, assignment)))
        if cotlar_valid(elems, identity, inv, mul, color):
            valid += 1
            if len({color[x] for x in others}) > 1:
                nonconstant_off_identity += 1
    return valid, nonconstant_off_identity


def main() -> None:
    cases = [
        ("C2", lambda: cyclic(2)),
        ("C3", lambda: cyclic(3)),
        ("C4", lambda: cyclic(4)),
        ("C5", lambda: cyclic(5)),
        ("C2^2", lambda: elementary_two_group(2)),
        ("C2^3", lambda: elementary_two_group(3)),
        ("D3", lambda: dihedral(3)),
        ("D4", lambda: dihedral(4)),
        ("S3", symmetric_three),
    ]
    for name, builder in cases:
        valid, nonconstant = count_valid(builder)
        print(f"{name}: valid={valid} nonconstant_off_identity={nonconstant}")
        assert nonconstant == 0


if __name__ == "__main__":
    main()
