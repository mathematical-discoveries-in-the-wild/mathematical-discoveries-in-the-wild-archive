#!/usr/bin/env python3
"""Finite-dimensional sanity check for the square-zero unitization packet."""

from __future__ import annotations

from dataclasses import dataclass


Vector = tuple[float, float]


def vadd(x: Vector, y: Vector) -> Vector:
    return (x[0] + y[0], x[1] + y[1])


def smul(a: float, x: Vector) -> Vector:
    return (a * x[0], a * x[1])


@dataclass(frozen=True)
class AElement:
    scalar: float
    vector: Vector

    def __mul__(self, other: "AElement") -> "AElement":
        return AElement(
            self.scalar * other.scalar,
            vadd(smul(self.scalar, other.vector), smul(other.scalar, self.vector)),
        )

    def scale(self, c: float) -> "AElement":
        return AElement(c * self.scalar, smul(c, self.vector))


def tensor_scale_left(a: AElement, p: AElement, q: AElement) -> tuple[AElement, AElement]:
    return (a * p, q)


def tensor_scale_right(p: AElement, q: AElement, a: AElement) -> tuple[AElement, AElement]:
    return (p, q * a)


def main() -> None:
    p = AElement(0.0, (1.0, 0.0))
    q = AElement(0.0, (0.0, 1.0))

    for a in [
        AElement(2.0, (3.0, -4.0)),
        AElement(-1.5, (0.25, 7.0)),
        AElement(0.0, (9.0, 8.0)),
    ]:
        left = tensor_scale_left(a, p, q)
        right = tensor_scale_right(p, q, a)
        expected = (p.scale(a.scalar), q)
        assert left == expected
        assert right == (p, q.scale(a.scalar))
        assert left[0] == p.scale(a.scalar)
        assert right[1] == q.scale(a.scalar)

    assert p.vector != (0.0, 0.0)
    assert q.vector != (0.0, 0.0)
    print("ok: square-zero unitization gives aM = lambda M = Ma for tested elements")


if __name__ == "__main__":
    main()
