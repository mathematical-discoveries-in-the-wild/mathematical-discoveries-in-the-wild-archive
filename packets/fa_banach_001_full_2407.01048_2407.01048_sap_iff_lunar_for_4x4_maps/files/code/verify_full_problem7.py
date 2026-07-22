#!/usr/bin/env python3
"""Independent exact verifier for the full answer to arXiv:2407.01048 Problem 7.

The C++ enumerator checks all 17,427,192 canonical proper colorings, records
15,667,716 non-lunar ones, and quotients complete directed failure normal
forms into 14,828 symmetry orbits.  For each orbit this
script checks a stored scalar or 2x2 integer coefficient certificate.  Exact
characteristic polynomials and Sturm root counts, not floating-point norms,
are the acceptance gate.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
from pathlib import Path
import re
import subprocess
import tempfile

import numpy as np
import sympy as sp


N = 4
EXPECTED_NORMALIZED_COUNTS = {
    5: 625,
    6: 14750,
    7: 73322,
    8: 123684,
    9: 88498,
    10: 29963,
    11: 4970,
    12: 385,
    13: 11,
}
EXPECTED_ORBIT_COUNTS = {
    5: 16,
    6: 233,
    7: 1564,
    8: 4238,
    9: 5087,
    10: 2862,
    11: 736,
    12: 87,
    13: 5,
}
EXPECTED_TYPE_COUNTS = {
    (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 37180,
    (1, 0): 0, (1, 1): 35439, (1, 2): 39043, (1, 3): 34477,
    (2, 0): 0, (2, 1): 39043, (2, 2): 35439, (2, 3): 34477,
    (3, 0): 37180, (3, 1): 34477, (3, 2): 34477, (3, 3): 42329,
}
EXPECTED_CANONICAL_COUNTS = {
    4: (24, 0),
    5: (4896, 4752),
    6: (185532, 183168),
    7: (1569864, 1563168),
    8: (4552617, 4495344),
    9: (5787840, 5504064),
    10: (3717416, 3071652),
    11: (1310592, 764760),
    12: (265110, 78072),
    13: (31152, 2736),
    14: (2076, 0),
    15: (72, 0),
    16: (1, 0),
}


def load_representatives(classifier_source: Path) -> list[np.ndarray]:
    with tempfile.TemporaryDirectory(prefix="problem7_classifier_") as directory:
        executable = Path(directory) / "classify_fixed_failure_orbits"
        subprocess.run(
            ["c++", "-O3", "-std=c++17", str(classifier_source), "-o", str(executable)],
            check=True,
        )
        completed = subprocess.run(
            [str(executable)], check=True, capture_output=True, text=True
        )
    lines = completed.stdout.splitlines()
    assert "canonical proper colorings 17427192" in lines
    assert "canonical nonlunar colorings 15667716" in lines
    assert "normalized-failure union colorings 336208" in lines
    assert "all nonlunar symmetry orbits 14828" in lines
    for colors, (canonical, nonlunar) in EXPECTED_CANONICAL_COUNTS.items():
        assert f"{colors} colors canonical {canonical} nonlunar {nonlunar}" in lines
    for (row_type, column_type), count in EXPECTED_TYPE_COUNTS.items():
        assert f"type {row_type} {column_type} colorings {count}" in lines
    for colors, count in EXPECTED_NORMALIZED_COUNTS.items():
        assert f"{colors} colors {count}" in lines
    for colors, count in EXPECTED_ORBIT_COUNTS.items():
        assert f"{colors} colors orbits {count}" in lines

    representatives = []
    for index, line in enumerate(lines):
        match = re.fullmatch(r"representative (\d+) colors (\d+)", line)
        if match is None:
            continue
        rows = [
            [int(value) for value in lines[index + offset].split()]
            for offset in range(1, 5)
        ]
        grid = np.array(rows, dtype=int)
        assert int(grid.max()) + 1 == int(match.group(2))
        representatives.append(grid)
    assert len(representatives) == 14828
    assert all(
        tuple(representatives[index].ravel())
        < tuple(representatives[index + 1].ravel())
        for index in range(len(representatives) - 1)
    )
    return representatives


def coordinatewise_injective(grid: np.ndarray) -> bool:
    return all(len(set(grid[row, :])) == N for row in range(N)) and all(
        len(set(grid[:, column])) == N for column in range(N)
    )


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


def tensor_pattern(grid: np.ndarray) -> np.ndarray:
    pattern = np.full((N * N, N * N), -1, dtype=int)
    for r1, r2, c1, c2 in itertools.product(range(N), repeat=4):
        if grid[r1, c1] == grid[r2, c2]:
            pattern[N * r1 + r2, N * c1 + c2] = int(grid[r1, c1])
    return pattern


def support_components(pattern: np.ndarray) -> list[tuple[list[int], list[int]]]:
    row_neighbors = [set(np.flatnonzero(pattern[row] >= 0)) for row in range(16)]
    column_neighbors = [
        set(np.flatnonzero(pattern[:, column] >= 0)) for column in range(16)
    ]
    unseen_rows = {row for row in range(16) if row_neighbors[row]}
    components = []
    while unseen_rows:
        seed = min(unseen_rows)
        rows = {seed}
        columns: set[int] = set()
        row_frontier = {seed}
        while row_frontier:
            next_columns = (
                set().union(*(row_neighbors[row] for row in row_frontier)) - columns
            )
            columns |= next_columns
            next_rows = (
                set().union(*(column_neighbors[column] for column in next_columns))
                - rows
            )
            rows |= next_rows
            row_frontier = next_rows
        unseen_rows -= rows
        components.append((sorted(rows), sorted(columns)))
    return components


def block_operator(pattern: np.ndarray, coefficients: np.ndarray) -> sp.Matrix:
    rows, columns = pattern.shape
    if coefficients.ndim == 1:
        dimension = 1
        integer = np.zeros((rows, columns), dtype=int)
        support = pattern >= 0
        integer[support] = coefficients[pattern[support]]
        return sp.Matrix(integer.tolist())
    dimension = int(coefficients.shape[1])
    integer = np.zeros((rows * dimension, columns * dimension), dtype=int)
    for row in range(rows):
        for column in range(columns):
            color = int(pattern[row, column])
            if color >= 0:
                integer[
                    row * dimension : (row + 1) * dimension,
                    column * dimension : (column + 1) * dimension,
                ] = coefficients[color]
    return sp.Matrix(integer.tolist())


def verify_exact_gap(source: sp.Matrix, target: sp.Matrix, record: dict) -> None:
    threshold = sp.Rational(
        int(record["threshold_numerator"]), int(record["threshold_denominator"])
    )
    source_polynomial = (source.T * source).charpoly().as_poly()
    target_polynomial = (target.T * target).charpoly().as_poly()
    assert source_polynomial.eval(threshold) != 0
    assert target_polynomial.eval(threshold) != 0
    source_above = int(source_polynomial.count_roots(threshold, sp.oo))
    target_above = int(target_polynomial.count_roots(threshold, sp.oo))
    assert source_above == int(record["source_roots_above"]) == 0
    assert target_above == int(record["target_roots_above"])
    assert target_above > 0


def verify_record(task: tuple[np.ndarray, str, dict]) -> str:
    grid, kind, record = task
    coefficients = np.array(record["coefficients"], dtype=int)
    colors = int(grid.max()) + 1
    if kind == "scalar":
        assert coefficients.shape == (colors,)
    else:
        assert coefficients.shape == (colors, 2, 2)
    source = block_operator(grid, coefficients)
    full_target_pattern = tensor_pattern(grid)
    if kind == "scalar":
        target_pattern = full_target_pattern
    else:
        components = support_components(full_target_pattern)
        rows, columns = components[int(record["component"])]
        target_pattern = full_target_pattern[np.ix_(rows, columns)]
    target = block_operator(target_pattern, coefficients)
    verify_exact_gap(source, target, record)
    return kind


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--classifier-source", default="classify_all_failure_orbits.cpp")
    parser.add_argument("--scalar-data", default="directed_failure_scalar_certificates.json")
    parser.add_argument("--matrix-data", default="directed_failure_matrix_certificates.json")
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    representatives = load_representatives(Path(args.classifier_source))
    assert all(coordinatewise_injective(grid) for grid in representatives)
    assert all(not is_lunar(grid) for grid in representatives)
    print(
        "classification: 17,427,192 proper canonical colorings; "
        "15,667,716 non-lunar; 14,828 symmetry orbits"
    )

    scalar = json.loads(Path(args.scalar_data).read_text())
    matrix = json.loads(Path(args.matrix_data).read_text())
    assert scalar["missing"] == [] or len(scalar["missing"]) == len(matrix["records"])
    assert matrix["missing"] == []
    scalar_records = {int(record["index"]): record for record in scalar["records"]}
    matrix_records = {int(record["index"]): record for record in matrix["records"]}
    assert len(scalar_records) == 7331
    assert len(matrix_records) == 7497
    assert not (set(scalar_records) & set(matrix_records))
    assert set(scalar_records) | set(matrix_records) == set(range(14828))

    tasks = []
    for index, grid in enumerate(representatives):
        if index in scalar_records:
            tasks.append((grid, "scalar", scalar_records[index]))
        else:
            tasks.append((grid, "matrix", matrix_records[index]))

    counts = {"scalar": 0, "matrix": 0}
    if args.workers == 1:
        results = map(verify_record, tasks)
    else:
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=args.workers)
        results = executor.map(verify_record, tasks, chunksize=20)
    try:
        for completed, kind in enumerate(results, start=1):
            counts[kind] += 1
            if completed % 500 == 0:
                print(f"exact certificates checked: {completed}/14828", flush=True)
    finally:
        if args.workers != 1:
            executor.shutdown()

    assert counts == {"scalar": 7331, "matrix": 7497}
    print("exact certificates: 7,331 scalar; 7,497 at matrix level 2")
    print("PASS: every non-lunar coordinatewise-injective 4x4 map fails SAP")


if __name__ == "__main__":
    main()
