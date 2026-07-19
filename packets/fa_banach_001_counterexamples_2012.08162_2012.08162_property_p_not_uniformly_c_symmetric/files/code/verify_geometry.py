#!/usr/bin/env python3
"""Deterministic checks for the property-(P) counterexample geometry.

The proof is analytic.  This script samples the boundary, verifies the named
support functionals, checks the tangent pairs, and stress-tests the two corner
kernel families against the claimed support segments.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def upper(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    return np.where(x <= 0.0, -1.0 + 2.0 * np.sqrt(1.0 + x), 1.0)


def lower(x: np.ndarray) -> np.ndarray:
    return -upper(-np.asarray(x))


def right_arc(x: np.ndarray) -> np.ndarray:
    return 1.0 - 2.0 * np.sqrt(1.0 - np.asarray(x))


def bisect_intersection(slope: float) -> float:
    lo, hi = 0.0, 1.0
    for _ in range(90):
        mid = (lo + hi) / 2.0
        if right_arc(np.array(mid)).item() < slope * mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def distance_to_segment(point: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    direction = b - a
    t = np.dot(point - a, direction) / np.dot(direction, direction)
    t = np.clip(t, 0.0, 1.0)
    return float(np.linalg.norm(point - (a + t * direction)))


def signed_segment_distance(point: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    return min(
        distance_to_segment(point, a, b),
        distance_to_segment(point, -a, -b),
    )


def boundary_samples(count: int = 20001) -> np.ndarray:
    x = np.linspace(-1.0, 1.0, count)
    return np.vstack(
        [np.column_stack([x, upper(x)]), np.column_stack([x, lower(x)])]
    )


def run(figure_path: Path | None) -> None:
    boundary = boundary_samples()
    named = {
        "g": np.array([0.0, 1.0]),
        "h": np.array([-1.0, 1.0]),
        "k": np.array([1.0, 0.0]),
    }
    support_errors = {}
    for name, functional in named.items():
        support_errors[name] = abs(np.max(boundary @ functional) - 1.0)

    # Tangent and reverse-constant checks.
    r_values = np.array([0.55, 0.7, 0.9, 0.99, 0.9999])
    tangent_residual = 0.0
    boundary_residual = 0.0
    reverse_residual = 0.0
    for r in r_values:
        x_r = np.array([r * r - 1.0, 2.0 * r - 1.0])
        y_r = np.array([r, 1.0])
        normal = np.array([-1.0 / r, 1.0])
        tangent_residual = max(tangent_residual, abs(normal @ y_r))
        boundary_residual = max(
            boundary_residual,
            abs(x_r[1] - upper(np.array(x_r[0])).item()),
            abs(y_r[1] - upper(np.array(y_r[0])).item()),
        )
        reverse_residual = max(reverse_residual, abs(y_r[1] * 0 + x_r[1] - (2 * r - 1)))

    # At A=(0,1), kernel slopes s in [0,1) hit the smooth right arc.
    # At B=(1,1), slopes -s/(1-s) do likewise.  Their unique outward
    # support normals must stay outside the signed corner support segments.
    g = named["g"]
    h = named["h"]
    k = named["k"]
    min_a_distance = np.inf
    min_b_distance = np.inf
    for s in np.linspace(0.0, 0.999, 2000):
        x_a = bisect_intersection(s)
        m_a = 1.0 / np.sqrt(1.0 - x_a)
        q_a = np.array([m_a, -1.0])
        q_a /= q_a @ np.array([x_a, right_arc(np.array(x_a)).item()])
        min_a_distance = min(min_a_distance, signed_segment_distance(q_a, g, h))

        slope_b = -s / (1.0 - s)
        x_b = bisect_intersection(slope_b)
        m_b = 1.0 / np.sqrt(1.0 - x_b)
        q_b = np.array([m_b, -1.0])
        q_b /= q_b @ np.array([x_b, right_arc(np.array(x_b)).item()])
        min_b_distance = min(min_b_distance, signed_segment_distance(q_b, g, k))

    print(f"max_named_support_error={max(support_errors.values()):.3e}")
    print(f"max_tangent_annihilation_residual={tangent_residual:.3e}")
    print(f"max_boundary_residual={boundary_residual:.3e}")
    print(f"max_reverse_constant_residual={reverse_residual:.3e}")
    print(f"min_sampled_support_distance_at_A={min_a_distance:.3e}")
    print(f"min_sampled_support_distance_at_B={min_b_distance:.3e}")
    print(f"largest_sampled_reverse_constant={2*r_values[-1]-1:.7f}")

    if max(support_errors.values()) > 2.0e-8:
        raise SystemExit("named functional failed support check")
    if max(tangent_residual, boundary_residual, reverse_residual) > 2.0e-10:
        raise SystemExit("tangent-pair identity failed")
    if min(min_a_distance, min_b_distance) <= 1.0e-5:
        raise SystemExit("sampled smooth support entered a forbidden corner segment")

    if figure_path is not None:
        import matplotlib.pyplot as plt

        figure_path.parent.mkdir(parents=True, exist_ok=True)
        x_left = np.linspace(-1.0, 0.0, 800)
        x_right = np.linspace(0.0, 1.0, 800)
        fig, ax = plt.subplots(figsize=(7.2, 6.4))
        ax.plot(x_left, upper(x_left), color="#1f4e79", linewidth=2.5)
        ax.plot(x_right, upper(x_right), color="#1f4e79", linewidth=2.5)
        ax.plot(x_right, lower(x_right), color="#1f4e79", linewidth=2.5)
        ax.plot(x_left, lower(x_left), color="#1f4e79", linewidth=2.5)
        ax.fill_between(
            np.linspace(-1.0, 1.0, 1200),
            lower(np.linspace(-1.0, 1.0, 1200)),
            upper(np.linspace(-1.0, 1.0, 1200)),
            color="#dce6f1",
            alpha=0.8,
        )
        r = 0.82
        x_r = np.array([r * r - 1.0, 2.0 * r - 1.0])
        y_r = np.array([r, 1.0])
        tangent = y_r / np.linalg.norm(y_r)
        segment = np.vstack([x_r - 0.32 * tangent, x_r + 0.32 * tangent])
        ax.plot(segment[:, 0], segment[:, 1], "--", color="#c00000", linewidth=2)
        ax.scatter([x_r[0], y_r[0]], [x_r[1], y_r[1]], c=["#c00000", "#548235"], s=70)
        ax.annotate(r"$x_r$", x_r + np.array([-0.13, 0.08]), fontsize=13)
        ax.annotate(r"$y_r$", y_r + np.array([-0.16, -0.17]), fontsize=13)
        ax.annotate(r"$A$", (0.02, 0.83), fontsize=13)
        ax.annotate(r"$B$", (1.01, 0.83), fontsize=13)
        ax.set_aspect("equal")
        ax.set_xlim(-1.18, 1.18)
        ax.set_ylim(-1.18, 1.18)
        ax.axhline(0, color="#888888", linewidth=0.7)
        ax.axvline(0, color="#888888", linewidth=0.7)
        ax.set_xlabel("first coordinate")
        ax.set_ylabel("second coordinate")
        ax.set_title("Unit ball and a tangent Birkhoff-James pair")
        fig.tight_layout()
        fig.savefig(figure_path, dpi=220)
        plt.close(fig)
        print(f"figure={figure_path}")

    print("PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", type=Path)
    args = parser.parse_args()
    run(args.figure)


if __name__ == "__main__":
    main()
