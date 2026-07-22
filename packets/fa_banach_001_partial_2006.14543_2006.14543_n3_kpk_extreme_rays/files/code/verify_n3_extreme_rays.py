"""Exact extreme-ray probe for C_3={P>=0: K_3 P K_3>=0}."""

from __future__ import annotations

import itertools
import math

import sympy as sp


def primitive_integer(values: list[sp.Rational]) -> tuple[int, ...]:
    den = math.lcm(*(int(v.q) for v in values))
    nums = [int(v * den) for v in values]
    common = math.gcd(*[abs(v) for v in nums if v])
    nums = [v // common for v in nums]
    first = next(v for v in nums if v)
    if first < 0:
        nums = [-v for v in nums]
    return tuple(nums)


def enumerate_rays() -> tuple[set[tuple[int, ...]], sp.Matrix]:
    n = 3
    identity = sp.eye(n)
    ones = sp.ones(n)
    k = sp.Rational(2, n) * ones - identity
    transform = sp.kronecker_product(k, k)
    inequalities = sp.eye(n * n).col_join(transform)
    rays: set[tuple[int, ...]] = set()

    for active in itertools.combinations(range(2 * n * n), n * n - 1):
        exact_sub = inequalities[list(active), :]
        null = exact_sub.nullspace()
        if len(null) != 1:
            continue
        ray = primitive_integer(list(null[0]))
        ray_vec = sp.Matrix(ray)
        if any(value < 0 for value in inequalities * ray_vec):
            ray = tuple(-value for value in ray)
            ray_vec = -ray_vec
        if all(value >= 0 for value in inequalities * ray_vec):
            rays.add(ray)

    return rays, transform


def matrix_tuple(matrix: sp.Matrix) -> tuple[int, ...]:
    return primitive_integer(list(matrix))


def orbit(ray: tuple[int, ...], transform: sp.Matrix) -> set[tuple[int, ...]]:
    n = 3
    p = sp.Matrix(n, n, ray)
    permutations = list(itertools.permutations(range(n)))
    result: set[tuple[int, ...]] = set()
    for rows in permutations:
        for cols in permutations:
            m = p.extract(rows, cols)
            for candidate in (m, m.T):
                result.add(matrix_tuple(candidate))
                qvec = transform * sp.Matrix(list(candidate))
                result.add(primitive_integer(list(qvec)))
    return result


def main() -> None:
    rays, transform = enumerate_rays()
    n = 3
    k = sp.Rational(2, n) * sp.ones(n) - sp.eye(n)
    inequalities = sp.eye(n * n).col_join(sp.kronecker_product(k, k))
    print(f"active_bases_tested={math.comb(18, 8)}")
    print(f"extreme_rays={len(rays)}")
    unseen = set(rays)
    classes = []
    while unseen:
        representative = min(unseen)
        current = orbit(representative, transform) & rays
        classes.append((representative, current))
        unseen -= current
    assert len(rays) == 78
    assert sorted(len(current) for _, current in classes) == [6, 36, 36]
    print(f"symmetry_orbits={len(classes)}")
    for index, (representative, current) in enumerate(classes, 1):
        p = sp.Matrix(3, 3, representative)
        q = sp.Matrix(3, 3, transform * sp.Matrix(representative))
        q = q.applyfunc(sp.simplify)
        values = inequalities * sp.Matrix(representative)
        active = [row for row, value in enumerate(values) if value == 0]
        active_rank = inequalities[active, :].rank()
        print(f"\nORBIT {index}: size={len(current)}")
        print("P=")
        print(p)
        print("KPK=")
        print(q)
        print(f"support_sizes=({sum(v != 0 for v in p)},{sum(v != 0 for v in q)})")
        print(f"active_constraints={len(active)}, active_rank={active_rank}")
        assert active_rank == 8


if __name__ == "__main__":
    main()
