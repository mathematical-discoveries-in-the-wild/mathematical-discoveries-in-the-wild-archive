#!/usr/bin/env python3
"""Exact certificate for the rational-octagon weak L-P counterexample.

Only Python's standard library is used.  Every calculation is over Q.
The four-dimensional operator ball is cut out by 32 inequalities.  Every
polytope vertex is the unique solution of some four independent active
inequalities, so enumerating all 4-subsets is exhaustive.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
import json


V_PLUS = (
    (F(1), F(0)),
    (F(2, 3), F(2, 3)),
    (F(0), F(1)),
    (F(-2, 3), F(2, 3)),
)
VERTICES = V_PLUS + tuple((-x, -y) for x, y in V_PLUS)
FACETS = (
    (F(1), F(1, 2)),
    (F(1, 2), F(1)),
    (F(-1, 2), F(1)),
    (F(-1), F(1, 2)),
    (F(-1), F(-1, 2)),
    (F(-1, 2), F(-1)),
    (F(1, 2), F(-1)),
    (F(1), F(-1, 2)),
)


def operator_constraints() -> tuple[tuple[F, ...], ...]:
    return tuple(
        (
            functional[0] * vertex[0],
            functional[0] * vertex[1],
            functional[1] * vertex[0],
            functional[1] * vertex[1],
        )
        for vertex in V_PLUS
        for functional in FACETS
    )


CONSTRAINTS = operator_constraints()


def solve_active_rows(indices: tuple[int, ...]) -> tuple[F, ...] | None:
    """Solve C_I z=1 by exact Gauss-Jordan elimination."""
    augmented = [list(CONSTRAINTS[index]) + [F(1)] for index in indices]
    for column in range(4):
        pivot = next(
            (row for row in range(column, 4) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            return None
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(4):
            if row == column or augmented[row][column] == 0:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                augmented[row][j] - scale * augmented[column][j]
                for j in range(5)
            ]
    return tuple(augmented[row][4] for row in range(4))


def feasible(operator: tuple[F, ...]) -> bool:
    return all(
        sum(row[j] * operator[j] for j in range(4)) <= 1
        for row in CONSTRAINTS
    )


def enumerate_operator_vertices() -> set[tuple[F, ...]]:
    vertices: set[tuple[F, ...]] = set()
    for indices in combinations(range(len(CONSTRAINTS)), 4):
        operator = solve_active_rows(indices)
        if operator is not None and feasible(operator):
            vertices.add(operator)
    return vertices


def matmul(
    left: tuple[tuple[F, F], tuple[F, F]],
    right: tuple[tuple[F, F], tuple[F, F]],
) -> tuple[tuple[F, F], tuple[F, F]]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def as_matrix(operator: tuple[F, ...]) -> tuple[tuple[F, F], tuple[F, F]]:
    return ((operator[0], operator[1]), (operator[2], operator[3]))


def as_tuple(matrix: tuple[tuple[F, F], tuple[F, F]]) -> tuple[F, ...]:
    return (matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1])


def signed_permutation_group() -> tuple[tuple[tuple[F, F], tuple[F, F]], ...]:
    group = []
    for swap in (False, True):
        for first_sign in (F(-1), F(1)):
            for second_sign in (F(-1), F(1)):
                if swap:
                    group.append(((F(0), first_sign), (second_sign, F(0))))
                else:
                    group.append(((first_sign, F(0)), (F(0), second_sign)))
    return tuple(group)


ISOMETRIES = signed_permutation_group()


def maps_a_vertex_to_a_vertex(operator: tuple[F, ...]) -> bool:
    matrix = as_matrix(operator)
    for x in VERTICES:
        image = (
            matrix[0][0] * x[0] + matrix[0][1] * x[1],
            matrix[1][0] * x[0] + matrix[1][1] * x[1],
        )
        if image in VERTICES:
            return True
    return False


def symmetry_orbits(
    operator_vertices: set[tuple[F, ...]],
) -> list[set[tuple[F, ...]]]:
    unseen = set(operator_vertices)
    orbits = []
    while unseen:
        representative = min(unseen)
        matrix = as_matrix(representative)
        orbit = {
            as_tuple(matmul(left, matmul(matrix, right)))
            for left in ISOMETRIES
            for right in ISOMETRIES
        }
        assert orbit <= operator_vertices
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def fraction_string(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    operator_vertices = enumerate_operator_vertices()
    assert len(CONSTRAINTS) == 32
    assert len(operator_vertices) == 96
    assert all(maps_a_vertex_to_a_vertex(operator) for operator in operator_vertices)

    orbits = symmetry_orbits(operator_vertices)
    orbit_data = sorted(
        (
            len(orbit),
            [fraction_string(entry) for entry in min(orbit)],
        )
        for orbit in orbits
    )
    assert [size for size, _ in orbit_data] == [8, 8, 16, 16, 16, 32]
    print(
        json.dumps(
            {
                "arithmetic": "exact rational",
                "constraints": len(CONSTRAINTS),
                "four_subsets_checked": 35960,
                "operator_vertices": len(operator_vertices),
                "bad_operator_vertices": 0,
                "symmetry_orbits": orbit_data,
                "verdict": "(X,X) has weak L-P property and |Ext(B_X)|=8",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
