#!/usr/bin/env python3
"""Exact verifier for the five-color boundary theorem.

The only floating-point operation is a fast proposal filter.  Every accepted
norm inequality is certified afterward by exact Sturm root counts for the
integer characteristic polynomials of A^T A and B^T B.
"""

from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp


N = 4
PERMUTATIONS = list(itertools.permutations(range(N)))


def canonicalize(grid: np.ndarray) -> np.ndarray:
    relabel: dict[int, int] = {}
    flat: list[int] = []
    for old_value in np.asarray(grid).ravel(order="C"):
        old = int(old_value)
        if old not in relabel:
            relabel[old] = len(relabel)
        flat.append(relabel[old])
    return np.array(flat, dtype=int).reshape(N, N)


def coordinatewise_injective(grid: np.ndarray) -> bool:
    return all(len(set(grid[row, :])) == N for row in range(N)) and all(
        len(set(grid[:, column])) == N for column in range(N)
    )


def enumerate_colorings(exact_colors: int):
    """Canonical restricted-growth enumeration of proper K_4,4 edge colorings."""
    grid = np.full((N, N), -1, dtype=np.int8)
    row_masks = [0] * 16
    column_masks = [0] * 16

    def visit(position: int, colors: int):
        if colors > exact_colors:
            return
        if colors + (N * N - position) < exact_colors:
            return
        if position == N * N:
            if colors == exact_colors:
                assert coordinatewise_injective(grid)
                yield grid.copy()
            return
        row, column = divmod(position, N)
        for color in range(min(colors + 1, exact_colors)):
            if row_masks[color] & (1 << row):
                continue
            if column_masks[color] & (1 << column):
                continue
            is_new = color == colors
            grid[row, column] = color
            row_masks[color] |= 1 << row
            column_masks[color] |= 1 << column
            yield from visit(position + 1, colors + int(is_new))
            row_masks[color] &= ~(1 << row)
            column_masks[color] &= ~(1 << column)

    yield from visit(0, 0)


def solution_set(grid: np.ndarray, a: int, b: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        (x, y)
        for x in range(N)
        for y in range(N)
        if grid[a, x] == grid[b, y]
    )


def is_lunar(grid: np.ndarray) -> bool:
    solutions = [
        solution_set(grid, a, b) for a in range(N) for b in range(N)
    ]
    return all(
        first == second or not (first & second)
        for index, first in enumerate(solutions)
        for second in solutions[index + 1 :]
    )


def orbit_key(grid: np.ndarray) -> tuple[int, ...]:
    """Quotient by row/column permutations, color relabeling, and transpose."""
    best = None
    for rows in PERMUTATIONS:
        row_grid = grid[list(rows), :]
        for columns in PERMUTATIONS:
            transformed = row_grid[:, list(columns)]
            for candidate in (transformed, transformed.T):
                candidate_key = tuple(int(x) for x in canonicalize(candidate).ravel())
                if best is None or candidate_key < best:
                    best = candidate_key
    assert best is not None
    return best


def tensor_pattern(grid: np.ndarray) -> np.ndarray:
    pattern = np.full((N * N, N * N), -1, dtype=int)
    for a, b, x, y in itertools.product(range(N), repeat=4):
        if grid[a, x] == grid[b, y]:
            pattern[N * a + b, N * x + y] = int(grid[a, x])
    return pattern


def tensor_matrix(pattern: np.ndarray, coefficients: np.ndarray) -> np.ndarray:
    matrix = np.zeros_like(pattern, dtype=int)
    support = pattern >= 0
    matrix[support] = coefficients[pattern[support]]
    return matrix


def primitive_candidates(bound: int = 3):
    for values in itertools.product(range(-bound, bound + 1), repeat=5):
        if not any(values):
            continue
        if next(value for value in values if value) < 0:
            continue
        divisor = 0
        for value in values:
            divisor = math.gcd(divisor, abs(value))
        if divisor == 1:
            yield np.array(values, dtype=int)


def exact_separation(
    grid: np.ndarray,
    coefficients: np.ndarray,
    source_norm: float,
    target_norm: float,
):
    """Return an exact rational separator, or None if this proposal fails."""
    source_np = coefficients[grid]
    target_np = tensor_matrix(tensor_pattern(grid), coefficients)
    source = sp.Matrix(source_np.tolist())
    target = sp.Matrix(target_np.tolist())

    midpoint = (source_norm * source_norm + target_norm * target_norm) / 2
    threshold = sp.Rational(round(midpoint * 10**8), 10**8)
    source_polynomial = (source.T * source).charpoly().as_poly()
    target_polynomial = (target.T * target).charpoly().as_poly()
    if source_polynomial.eval(threshold) == 0:
        return None
    if target_polynomial.eval(threshold) == 0:
        return None
    source_above = int(source_polynomial.count_roots(threshold, sp.oo))
    target_above = int(target_polynomial.count_roots(threshold, sp.oo))
    if source_above == 0 and target_above > 0:
        return threshold, source_above, target_above
    return None


def find_certificate(grid: np.ndarray, candidates: list[np.ndarray]):
    pattern = tensor_pattern(grid)
    for coefficients in candidates:
        source = coefficients[grid]
        target = tensor_matrix(pattern, coefficients)
        source_norm = float(np.linalg.norm(source, 2))
        target_norm = float(np.linalg.norm(target, 2))
        if target_norm <= (1 + 10**-7) * source_norm:
            continue
        exact = exact_separation(
            grid, coefficients, source_norm, target_norm
        )
        if exact is not None:
            return coefficients, source_norm, target_norm, exact
    return None


def main() -> None:
    four_colorings = list(enumerate_colorings(4))
    assert len(four_colorings) == 24
    assert all(is_lunar(grid) for grid in four_colorings)
    print("four colors: 24 canonical colorings, all lunar")

    five_colorings = list(enumerate_colorings(5))
    assert len(five_colorings) == 4896
    lunar_count = sum(is_lunar(grid) for grid in five_colorings)
    assert lunar_count == 144
    print("five colors: 4896 canonical colorings; 144 lunar; 4752 non-lunar")

    orbit_keys = {orbit_key(grid) for grid in five_colorings}
    representatives = [
        np.array(key, dtype=int).reshape(N, N) for key in sorted(orbit_keys)
    ]
    lunar_representatives = [grid for grid in representatives if is_lunar(grid)]
    nonlunar_representatives = [
        grid for grid in representatives if not is_lunar(grid)
    ]
    assert len(representatives) == 17
    assert len(lunar_representatives) == 1
    assert len(nonlunar_representatives) == 16
    print("isomorphism classes: 17 total; 1 lunar; 16 non-lunar")

    candidates = list(primitive_candidates(3))
    assert len(candidates) == 8161
    for index, grid in enumerate(nonlunar_representatives):
        certificate = find_certificate(grid, candidates)
        assert certificate is not None
        coefficients, source_norm, target_norm, exact = certificate
        threshold, source_above, target_above = exact
        print(
            f"class {index:02d}: c={coefficients.tolist()} "
            f"numeric=({source_norm:.12f},{target_norm:.12f}) "
            f"threshold={threshold} roots_above=({source_above},{target_above})"
        )

    print("PASS: every non-lunar five-color class fails scalar SAP exactly")


if __name__ == "__main__":
    main()
