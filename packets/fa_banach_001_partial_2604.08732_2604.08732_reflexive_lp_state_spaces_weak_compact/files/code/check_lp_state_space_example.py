"""Finite-partition check for the ell_1^2 example in the packet.

The mathematical example is continuous-measure: X=ell_1^2, X*=ell_infty^2,
f(t)=e_1, and g_h(t)=(1,h(t)) with |h(t)|<=1.  On a finite probability
partition this script verifies the same norm-attainment equalities.
"""

from __future__ import annotations

import math


def lq_state_norm(h_values: list[float], q: float) -> float:
    weights = [1.0 / len(h_values)] * len(h_values)
    return sum(w * max(1.0, abs(h)) ** q for w, h in zip(weights, h_values)) ** (1.0 / q)


def pairing_with_constant_e1(h_values: list[float]) -> float:
    weights = [1.0 / len(h_values)] * len(h_values)
    return sum(weights)


def main() -> None:
    q = 2.0
    examples = {
        "zero": [0.0, 0.0, 0.0, 0.0],
        "constant_one": [1.0, 1.0, 1.0, 1.0],
        "oscillating": [-1.0, 0.5, 1.0, -0.25],
    }

    for name, h_values in examples.items():
        norm = lq_state_norm(h_values, q)
        pairing = pairing_with_constant_e1(h_values)
        print(f"{name}: L^q norm={norm:.12f}, pairing={pairing:.12f}")
        assert math.isclose(norm, 1.0)
        assert math.isclose(pairing, 1.0)

    print("All listed g_h lie in the state space; zero and constant_one are distinct.")


if __name__ == "__main__":
    main()
