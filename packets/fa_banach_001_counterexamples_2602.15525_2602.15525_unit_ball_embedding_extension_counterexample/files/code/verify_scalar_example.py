"""Finite-grid sanity check for the scalar counterexample.

This is not a proof.  It only checks the concrete map
    t -> (t, abs(t))
from [-1, 1] to l_infinity^2 on a rational grid.
"""

from fractions import Fraction


def linf_distance(p, q):
    return max(abs(p[0] - q[0]), abs(p[1] - q[1]))


grid = [Fraction(k, 20) for k in range(-20, 21)]

for s in grid:
    for t in grid:
        lhs = linf_distance((s, abs(s)), (t, abs(t)))
        rhs = abs(s - t)
        if lhs != rhs:
            raise AssertionError((s, t, lhs, rhs))

print(f"checked {len(grid) ** 2} grid pairs; all distances agree")
