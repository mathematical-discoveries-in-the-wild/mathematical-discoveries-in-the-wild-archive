#!/usr/bin/env python3
"""Sanity-check the stabilizer/coset proof in finite group fusion bialgebras.

This checks concrete instances in C[S_3] and C[D_4].  It is deliberately not
used as proof of the general theorem.
"""

from itertools import permutations

import numpy as np


TOL = 1e-10


def compose(p, q):
    """Permutation product p*q (apply q first, then p)."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)


def generated_group(generators):
    n = len(generators[0])
    identity = tuple(range(n))
    group = {identity}
    frontier = [identity]
    while frontier:
        a = frontier.pop()
        for g in generators:
            for b in (compose(a, g), compose(g, a)):
                if b not in group:
                    group.add(b)
                    frontier.append(b)
    return sorted(group)


def subgroup(group, generators):
    if generators:
        return generated_group(generators)
    return [tuple(range(len(group[0])))]


def left_regular(group):
    index = {g: i for i, g in enumerate(group)}
    matrices = {}
    for g in group:
        matrix = np.zeros((len(group), len(group)), dtype=complex)
        for h in group:
            matrix[index[compose(g, h)], index[h]] = 1.0
        matrices[g] = matrix
    return matrices


def parity(p):
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1.0 if inversions % 2 else 1.0


def assert_close(left, right, label):
    error = np.linalg.norm(left - right)
    if error > TOL:
        raise AssertionError(f"{label}: error={error}")


def verify_case(name, group, h_group, alpha, coset_rep):
    matrices = left_regular(group)
    d = len(h_group)
    identity_matrix = np.eye(len(group), dtype=complex)

    for h in h_group:
        for k in h_group:
            assert abs(alpha(compose(h, k)) - alpha(h) * alpha(k)) < TOL
        assert abs(abs(alpha(h)) - 1.0) < TOL

    coset = {compose(h, coset_rep) for h in h_group}
    eps = {compose(h, coset_rep): np.conjugate(alpha(h)) for h in h_group}
    assert len(coset) == len(h_group)
    assert len(eps) == len(h_group)

    a = sum((eps[g] * matrices[g] for g in coset), np.zeros_like(identity_matrix))
    v = a / d
    e_proj = v.conjugate().T @ v
    q_proj = v @ v.conjugate().T

    assert_close(e_proj @ e_proj, e_proj, f"{name}: E projection")
    assert_close(q_proj @ q_proj, q_proj, f"{name}: Q projection")
    assert_close(a, d * v, f"{name}: a=DV")
    assert_close(a @ a.conjugate().T, d * d * q_proj, f"{name}: aa*=D^2Q")
    assert abs(np.trace(q_proj).real / len(group) - 1.0 / d) < TOL

    phase_regular = sum(
        (np.conjugate(alpha(h)) * matrices[h] for h in h_group),
        np.zeros_like(identity_matrix),
    )
    assert_close(q_proj, phase_regular / d, f"{name}: phased regular Q")

    for h in h_group:
        assert_close(matrices[h] @ q_proj, alpha(h) * q_proj, f"{name}: left stabilizer")
        assert_close(
            matrices[inverse(h)] @ q_proj,
            np.conjugate(alpha(h)) * q_proj,
            f"{name}: adjoint stabilizer",
        )
        assert {compose(h, g) for g in coset} == coset

    # Coefficient form of 1_H * 1_J = |H| 1_J.
    counts = {g: 0 for g in group}
    for h in h_group:
        for g in coset:
            counts[compose(h, g)] += 1
    for g in group:
        expected = d if g in coset else 0
        if counts[g] != expected:
            raise AssertionError(f"{name}: right-shift coefficient at {g}")

    return 1


def main():
    s3 = list(permutations(range(3)))
    e3 = tuple(range(3))
    transposition = (1, 0, 2)
    cycle3 = (1, 2, 0)
    s3_subgroups = [
        ("S3-trivial", subgroup(s3, [])),
        ("S3-C2", subgroup(s3, [transposition])),
        ("S3-C3", subgroup(s3, [cycle3])),
        ("S3-full", s3),
    ]

    rotation = (1, 2, 3, 0)
    reflection = (0, 3, 2, 1)
    d4 = generated_group([rotation, reflection])
    e4 = tuple(range(4))
    d4_subgroups = [
        ("D4-trivial", subgroup(d4, [])),
        ("D4-C2-reflection", subgroup(d4, [reflection])),
        ("D4-C4-rotation", subgroup(d4, [rotation])),
        ("D4-full", d4),
    ]

    cases = 0
    for base_name, h_group in s3_subgroups:
        characters = [("triv", lambda _g: 1.0)]
        characters.append(("sign", parity))
        for char_name, alpha in characters:
            for rep in (e3, transposition, cycle3):
                cases += verify_case(f"{base_name}-{char_name}", s3, h_group, alpha, rep)

    # Express D4 elements uniquely as r^k s^b and build all four real
    # characters of the full group. Their restrictions cover the subgroups.
    d4_words = {}
    for k in range(4):
        r_k = e4
        for _ in range(k):
            r_k = compose(r_k, rotation)
        d4_words[r_k] = (k, 0)
        d4_words[compose(r_k, reflection)] = (k, 1)

    for base_name, h_group in d4_subgroups:
        for r_sign in (1.0, -1.0):
            for s_sign in (1.0, -1.0):
                def alpha(g, rs=r_sign, ss=s_sign):
                    k, b = d4_words[g]
                    return (rs ** k) * (ss ** b)

                for rep in (e4, rotation, reflection):
                    cases += verify_case(base_name, d4, h_group, alpha, rep)

    print(f"verified {cases} finite-group stabilizer/coset cases")


if __name__ == "__main__":
    main()

