"""Sanity checks for the abstract module lemma in the packet.

This is not a proof assistant formalization. It records the algebraic identities
used in Lemma 1 in a small finite-dimensional model: a unital algebra A acting on
itself, a quotient q, and a module morphism phi. The lift is determined by a lift
of phi(e).
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    # A = C^2 with coordinatewise multiplication and right identity e=(1,1).
    e = np.array([1.0, 1.0])

    # Y = C^3 as an A-left module through the first two coordinates.
    # q drops the last coordinate, so Z = C^2.
    def act(a: np.ndarray, y: np.ndarray) -> np.ndarray:
        return np.array([a[0] * y[0], a[1] * y[1], a[0] * y[2]])

    def q(y: np.ndarray) -> np.ndarray:
        return y[:2]

    # A module morphism phi: A -> Z, phi(a)=a*phi(e).
    phi_e = np.array([2.0, -3.0])

    def phi(a: np.ndarray) -> np.ndarray:
        return a * phi_e

    # Choose a lift y of phi(e).
    y = np.array([2.0, -3.0, 7.0])

    def lifted_phi(a: np.ndarray) -> np.ndarray:
        return act(a, y)

    tests = [
        np.array([0.0, 0.0]),
        np.array([1.0, 0.0]),
        np.array([0.0, 1.0]),
        np.array([4.0, -5.0]),
    ]

    assert np.allclose(phi(e), phi_e)
    for a in tests:
        assert np.allclose(q(lifted_phi(a)), phi(a))

    print("module lifting identity verified in the finite-dimensional model")


if __name__ == "__main__":
    main()
