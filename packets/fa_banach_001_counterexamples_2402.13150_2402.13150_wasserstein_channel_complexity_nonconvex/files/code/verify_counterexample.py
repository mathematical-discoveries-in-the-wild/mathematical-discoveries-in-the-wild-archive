#!/usr/bin/env python3
"""Exact symbolic checks for the one-qubit nonconvexity counterexample."""

import sympy as sp


def main() -> None:
    i = sp.I
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -i], [i, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    paulis = (sx, sy, sz)
    identity2 = sp.eye(2)
    identity4 = sp.eye(4)

    cost = sp.zeros(4)
    for sigma in paulis:
        difference = sp.kronecker_product(sigma, identity2) - sp.kronecker_product(
            identity2, sigma.T
        )
        cost += difference**2

    omega_vector = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    expected_cost = 8 * (identity4 - omega_vector * omega_vector.T.conjugate())
    assert sp.simplify(cost - expected_cost) == sp.zeros(4)
    assert cost.eigenvals() == {sp.Integer(0): 1, sp.Integer(8): 3}

    t = sp.symbols("t", positive=True, real=True)
    rho = sp.diag(1, 0)
    omega_sqrt = sp.diag(sp.sqrt(1 - t), sp.sqrt(t))
    omega = sp.diag(1 - t, t)

    contributions = []
    for sigma in paulis:
        term = (
            sp.trace(rho * sigma * rho * sigma)
            + sp.trace(omega_sqrt * sigma * omega_sqrt * sigma)
            - 2 * sp.trace(rho * sigma) * sp.trace(omega * sigma)
        )
        contributions.append(sp.simplify(term))

    assert contributions == [
        2 * sp.sqrt(t) * sp.sqrt(1 - t),
        2 * sp.sqrt(t) * sp.sqrt(1 - t),
        4 * t,
    ]
    exact_curve = sp.simplify(sum(contributions))
    assert exact_curve == 4 * t + 4 * sp.sqrt(t) * sp.sqrt(1 - t)

    at_quarter = sp.simplify(exact_curve.subs(t, sp.Rational(1, 4)))
    assert at_quarter == 1 + sp.sqrt(3)
    lower_bound = sp.sqrt(at_quarter)
    convexity_upper_bound = sp.sqrt(2) / 2
    assert sp.simplify(lower_bound**2 - convexity_upper_bound**2) > 0

    print("cost_identity: exact")
    print("cost_spectrum:", sorted(cost.eigenvals().keys()))
    print("pure_input_contributions:", contributions)
    print("d_squared_curve:", exact_curve)
    print("t=1/4 lower_bound:", lower_bound)
    print("convexity_upper_bound:", convexity_upper_bound)
    print("squared_gap:", sp.simplify(lower_bound**2 - convexity_upper_bound**2))
    print("VERDICT: all exact symbolic checks passed")


if __name__ == "__main__":
    main()
