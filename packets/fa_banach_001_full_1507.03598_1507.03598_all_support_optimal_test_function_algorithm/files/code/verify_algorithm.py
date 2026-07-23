#!/usr/bin/env python3
"""Numerically verify the all-support cell-orbit construction.

The normalized equation on [0,L] is

    q(t) + beta * integral_[0,L] 1_{|t-s|<=1} q(s) ds = 1,

with beta=1/2 for SO(even) and beta=-1/2 for Sp.  Breakpoints from
(Z union (L+Z)) intersect [0,L] make translation by one preserve cells.
On each translation orbit the differentiated equation is y'=Ay.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm


TOL = 1e-10


def merged(values: list[float], tolerance: float = TOL) -> list[float]:
    out: list[float] = []
    for value in sorted(values):
        if not out or abs(value - out[-1]) > tolerance:
            out.append(value)
    return out


def make_breakpoints(length: float) -> list[float]:
    if length <= 0:
        raise ValueError("length must be positive")
    values = [0.0, length]
    for integer in range(int(np.floor(length)) + 1):
        if TOL < integer < length - TOL:
            values.append(float(integer))
        reflected = length - integer
        if TOL < reflected < length - TOL:
            values.append(float(reflected))
    return merged(values)


def integral_expm(matrix: np.ndarray, time: float) -> np.ndarray:
    """Return integral_0^time exp(s*matrix) ds, including singular matrix."""
    size = matrix.shape[0]
    block = np.zeros((2 * size, 2 * size), dtype=float)
    block[:size, :size] = matrix
    block[:size, size:] = np.eye(size)
    return expm(time * block)[:size, size:]


@dataclass
class Orbit:
    cells: list[int]
    positions: dict[int, int]
    length: float
    matrix: np.ndarray
    endpoint: np.ndarray
    integral: np.ndarray


class CellOrbitSolution:
    def __init__(self, length: float, beta: float):
        self.length = float(length)
        self.beta = float(beta)
        self.breakpoints = make_breakpoints(self.length)
        self.cells = list(zip(self.breakpoints[:-1], self.breakpoints[1:]))
        self.cell_count = len(self.cells)
        self.plus = [self._translated_cell(i, 1.0) for i in range(self.cell_count)]
        self.minus = [self._translated_cell(i, -1.0) for i in range(self.cell_count)]
        self.orbits = self._make_orbits()
        self.orbit_of: dict[int, Orbit] = {
            cell: orbit for orbit in self.orbits for cell in orbit.cells
        }
        self.endpoint_map = np.zeros((self.cell_count, self.cell_count))
        self.integral_map = np.zeros((self.cell_count, self.cell_count))
        for orbit in self.orbits:
            for row_cell in orbit.cells:
                row = orbit.positions[row_cell]
                for col_cell in orbit.cells:
                    col = orbit.positions[col_cell]
                    self.endpoint_map[row_cell, col_cell] = orbit.endpoint[row, col]
                    self.integral_map[row_cell, col_cell] = orbit.integral[row, col]
        self.system_matrix, self.rhs = self._make_linear_system()
        self.initial_values = np.linalg.solve(self.system_matrix, self.rhs)

    def _translated_cell(self, index: int, shift: float) -> int | None:
        left, right = self.cells[index]
        target_left = left + shift
        target_right = right + shift
        if target_left < -TOL or target_right > self.length + TOL:
            return None
        for candidate, (cand_left, cand_right) in enumerate(self.cells):
            if (
                abs(cand_left - target_left) <= TOL
                and abs(cand_right - target_right) <= TOL
            ):
                return candidate
        raise RuntimeError(f"translation did not preserve cell {index} by {shift}")

    def _make_orbits(self) -> list[Orbit]:
        remaining = set(range(self.cell_count))
        orbits: list[Orbit] = []
        while remaining:
            seed = min(remaining)
            stack = [seed]
            component: set[int] = set()
            while stack:
                cell = stack.pop()
                if cell in component:
                    continue
                component.add(cell)
                for neighbor in (self.plus[cell], self.minus[cell]):
                    if neighbor is not None:
                        stack.append(neighbor)
            remaining -= component
            cells = sorted(component)
            positions = {cell: position for position, cell in enumerate(cells)}
            lengths = [self.cells[cell][1] - self.cells[cell][0] for cell in cells]
            if max(lengths) - min(lengths) > TOL:
                raise RuntimeError("translation orbit has unequal cell lengths")
            matrix = np.zeros((len(cells), len(cells)), dtype=float)
            for cell in cells:
                row = positions[cell]
                if self.plus[cell] is not None:
                    matrix[row, positions[self.plus[cell]]] -= self.beta
                if self.minus[cell] is not None:
                    matrix[row, positions[self.minus[cell]]] += self.beta
            if np.linalg.norm(matrix + matrix.T, ord=np.inf) > TOL:
                raise RuntimeError("orbit matrix should be skew-symmetric")
            cell_length = lengths[0]
            orbits.append(
                Orbit(
                    cells=cells,
                    positions=positions,
                    length=cell_length,
                    matrix=matrix,
                    endpoint=expm(cell_length * matrix),
                    integral=integral_expm(matrix, cell_length),
                )
            )
        return orbits

    def _make_linear_system(self) -> tuple[np.ndarray, np.ndarray]:
        matrix = np.zeros((self.cell_count, self.cell_count), dtype=float)
        rhs = np.zeros(self.cell_count, dtype=float)
        for row in range(self.cell_count - 1):
            matrix[row, :] = self.endpoint_map[row, :]
            matrix[row, row + 1] -= 1.0

        matrix[-1, 0] = 1.0
        cutoff = min(1.0, self.length)
        for cell, (_, right) in enumerate(self.cells):
            if right <= cutoff + TOL:
                matrix[-1, :] += self.beta * self.integral_map[cell, :]
        rhs[-1] = 1.0
        return matrix, rhs

    def _cell_index(self, point: float) -> int:
        if point < -TOL or point > self.length + TOL:
            raise ValueError("point outside interval")
        if point >= self.length - TOL:
            return self.cell_count - 1
        return int(np.searchsorted(self.breakpoints, point, side="right") - 1)

    def value(self, point: float) -> float:
        cell = self._cell_index(point)
        left, _ = self.cells[cell]
        orbit = self.orbit_of[cell]
        local = max(0.0, min(point - left, orbit.length))
        vector = expm(local * orbit.matrix) @ self.initial_values[orbit.cells]
        return float(vector[orbit.positions[cell]])

    def integral(self, left: float = 0.0, right: float | None = None) -> float:
        if right is None:
            right = self.length
        left = max(0.0, left)
        right = min(self.length, right)
        total = 0.0
        for cell, (cell_left, cell_right) in enumerate(self.cells):
            lo = max(left, cell_left)
            hi = min(right, cell_right)
            if hi <= lo + TOL:
                continue
            orbit = self.orbit_of[cell]
            start = lo - cell_left
            stop = hi - cell_left
            propagator = integral_expm(orbit.matrix, stop) - integral_expm(
                orbit.matrix, start
            )
            vector = propagator @ self.initial_values[orbit.cells]
            total += float(vector[orbit.positions[cell]])
        return total

    def residual(self, point: float) -> float:
        window = self.integral(max(0.0, point - 1.0), min(self.length, point + 1.0))
        return self.value(point) + self.beta * window - 1.0

    def diagnostic(self) -> dict[str, float | int]:
        grid = np.linspace(0.0, self.length, 401)
        residual = max(abs(self.residual(float(point))) for point in grid)
        continuity = max(
            [
                abs(
                    float(self.endpoint_map[cell, :] @ self.initial_values)
                    - self.initial_values[cell + 1]
                )
                for cell in range(self.cell_count - 1)
            ]
            or [0.0]
        )
        values = np.array([self.value(float(point)) for point in grid])
        return {
            "cells": self.cell_count,
            "orbits": len(self.orbits),
            "condition_number": float(np.linalg.cond(self.system_matrix)),
            "max_residual": float(residual),
            "continuity_error": float(continuity),
            "integral": float(self.integral()),
            "minimum": float(values.min()),
            "maximum": float(values.max()),
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lengths",
        nargs="+",
        type=float,
        default=[0.4, 1.0, 1.4, 2.0, 2.4, 3.0, 3.7, 5.25, 8.1],
    )
    args = parser.parse_args()
    for length in args.lengths:
        for group, beta in (("SO(even)", 0.5), ("Sp", -0.5)):
            solution = CellOrbitSolution(length, beta)
            info = solution.diagnostic()
            if info["max_residual"] > 2e-8:
                raise AssertionError((length, group, info))
            print(f"L={length:g} group={group} {info}")

        sp = CellOrbitSolution(length, -0.5)
        scaling = 1.0 / (1.0 + sp.integral())
        grid = np.linspace(0.0, length, 401)
        so_odd_residual = max(
            abs(
                scaling * sp.value(float(point))
                + scaling * sp.integral()
                - 0.5
                * scaling
                * sp.integral(
                    max(0.0, float(point) - 1.0),
                    min(length, float(point) + 1.0),
                )
                - 1.0
            )
            for point in grid
        )
        if so_odd_residual > 2e-8:
            raise AssertionError((length, "SO(odd)", so_odd_residual))
        print(
            f"L={length:g} group=SO(odd) scaling={scaling:.12g} "
            f"max_residual={so_odd_residual:.3g}"
        )


if __name__ == "__main__":
    main()
