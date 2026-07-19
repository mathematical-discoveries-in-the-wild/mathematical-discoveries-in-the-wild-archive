"""Sanity check for the compact non-Hilbert-Schmidt diagonal model.

For commuting diagonal compact self-adjoint A,B with eigenvalue pairs z_j,
the compact tracial joint spectral measure is the sum of segment measures
((1-t)/t) dt pushed forward by t -> t z_j.  This script illustrates that
annular mass is finite even when the global second moment diverges.
"""

from __future__ import annotations

import math


def pairs(count: int) -> list[tuple[float, float]]:
    # Not Hilbert-Schmidt: sum 1/j diverges, but eigenvalues tend to zero.
    return [((j + 1) ** -0.5, (-1.0) ** j * 0.3 * (j + 1) ** -0.55) for j in range(count)]


def segment_annular_mass(radius: float, delta: float, big_r: float) -> float:
    """Integral of (1-t)/t over t with delta <= t*radius <= big_r, 0<t<=1."""
    if radius < delta:
        return 0.0
    lo = delta / radius
    hi = min(1.0, big_r / radius)
    if lo >= hi:
        return 0.0
    return math.log(hi / lo) - (hi - lo)


def main() -> int:
    z = pairs(200_000)
    partial_second = sum(a * a + b * b for a, b in z)
    print("partial_second_moment_first_200000", partial_second)
    for delta in [0.5, 0.25, 0.1, 0.05]:
        mass = sum(segment_annular_mass(math.hypot(a, b), delta, 2.0) for a, b in z)
        active = sum(1 for a, b in z if math.hypot(a, b) >= delta)
        print(f"annulus_delta={delta:g}", "active_segments", active, "mass", round(mass, 6))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
