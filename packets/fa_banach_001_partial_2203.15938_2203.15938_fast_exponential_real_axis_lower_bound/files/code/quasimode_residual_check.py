#!/usr/bin/env python3
"""Numerical sanity check for the fast-exponential quasimode scaling.

This script is not used in the proof.  It discretizes the first-order model
for a smooth compactly supported input and reports the size of the normalized
second-derivative correction t^{-2} exp(-t^2)||v''||/||v||.
"""

from __future__ import annotations

import math
import numpy as np


def smooth_bump(y: np.ndarray, left: float = -0.9, right: float = 0.9) -> np.ndarray:
    out = np.zeros_like(y)
    inside = (y > left) & (y < right)
    z = (2 * (y[inside] - left) / (right - left)) - 1
    out[inside] = np.exp(-1.0 / (1.0 - z * z))
    return out


def input_f(y: np.ndarray) -> np.ndarray:
    return np.sin(math.pi * (y + 1.0) / 4.0) * smooth_bump(y)


def model_solution(t: float, n: int = 6000) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    y = np.linspace(-1.35, 1.05, n)
    h = y[1] - y[0]
    w = np.exp(np.clip(t * t * (y * y - 1.0), -700, 60))
    f = input_f(y)
    v = np.zeros_like(y)
    # Stable backward implicit Euler solve for v' = Wv - f, v(right)=0.
    # The large positive W on the far-left tail is damping in this direction.
    for i in range(n - 2, -1, -1):
        v[i] = (v[i + 1] + h * f[i]) / (1.0 + h * w[i])
    return y, f, v


def l2_norm(values: np.ndarray, h: float) -> float:
    return float(np.sqrt(np.trapz(values * values, dx=h)))


def main() -> None:
    print("t  ||f||/||v||  normalized_second_derivative")
    for t in (4.0, 5.0, 6.0, 7.0):
        y, f, v = model_solution(t)
        h = y[1] - y[0]
        vpp = np.gradient(np.gradient(v, h), h)
        ratio = l2_norm(f, h) / l2_norm(v, h)
        correction = math.exp(-t * t) * t ** -2 * l2_norm(vpp, h) / l2_norm(v, h)
        print(f"{t:3.1f}  {ratio:10.6f}  {correction:12.4e}")


if __name__ == "__main__":
    main()
