"""Sanity check for the ODE obstruction in the alpha=1 packet.

This is not a proof.  It records the elementary phase-line calculation for
F_a(y) = a*sqrt(1+y^2) - 1 - y^2.
"""

from __future__ import annotations

import math


def equilibria(a: float) -> list[float]:
    """Return real equilibria of y' = F_a(y)."""
    if a < 1:
        return []
    if abs(a - 1) < 1e-12:
        return [0.0]
    root = math.sqrt(a * a - 1)
    return [-root, root]


def compatible_with_periodic_support(a: float) -> bool:
    """A constant y=h'/h gives periodic h only when y=0."""
    return any(abs(y) < 1e-12 for y in equilibria(a))


for a in [0.5, 1.0, 2.0, 3.0]:
    print(f"a={a}: equilibria={equilibria(a)}, periodic_support={compatible_with_periodic_support(a)}")

assert compatible_with_periodic_support(1.0)
assert not compatible_with_periodic_support(2.0)
