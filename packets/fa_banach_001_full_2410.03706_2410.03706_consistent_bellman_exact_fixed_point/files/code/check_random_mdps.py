#!/usr/bin/env python3
"""Numerical stress test for the exact consistent-Bellman fixed-point formula."""

from __future__ import annotations

import json
import numpy as np


def iterate(operator, shape, tol=2e-13, max_steps=200_000):
    q = np.zeros(shape, dtype=float)
    for step in range(1, max_steps + 1):
        q_next = operator(q)
        if np.max(np.abs(q_next - q)) <= tol:
            return q_next, step
        q = q_next
    raise RuntimeError("value iteration did not converge")


def run(seed=20260722, trials=400):
    rng = np.random.default_rng(seed)
    worst_formula = 0.0
    worst_consistent_residual = 0.0
    worst_value_match = 0.0
    worst_gap_identity = 0.0
    max_classical_steps = 0
    max_consistent_steps = 0

    for _ in range(trials):
        n_states = int(rng.integers(2, 8))
        n_actions = int(rng.integers(2, 6))
        gamma = float(rng.uniform(0.0, 0.98))
        reward = rng.normal(size=(n_states, n_actions))

        transition = rng.dirichlet(np.ones(n_states), size=(n_states, n_actions))
        # Mix in state-dependent self-loops, including nearly absorbing pairs.
        loop_weight = rng.uniform(0.0, 0.995, size=(n_states, n_actions, 1))
        identity = np.zeros_like(transition)
        for state in range(n_states):
            identity[state, :, state] = 1.0
        transition = (1.0 - loop_weight) * transition + loop_weight * identity

        def classical(q):
            value = np.max(q, axis=1)
            return reward + gamma * np.einsum("sak,k->sa", transition, value)

        def consistent(q):
            value = np.max(q, axis=1)
            continuation = np.einsum("sak,k->sa", transition, value)
            diagonal = transition[np.arange(n_states), :, np.arange(n_states)]
            continuation += diagonal * (q - value[:, None])
            return reward + gamma * continuation

        q_star, classical_steps = iterate(classical, reward.shape)
        q_consistent, consistent_steps = iterate(consistent, reward.shape)
        max_classical_steps = max(max_classical_steps, classical_steps)
        max_consistent_steps = max(max_consistent_steps, consistent_steps)

        value_star = np.max(q_star, axis=1)
        diagonal = transition[np.arange(n_states), :, np.arange(n_states)]
        denominator = 1.0 - gamma * diagonal
        formula = value_star[:, None] - (
            (value_star[:, None] - q_star) / denominator
        )

        formula_error = float(np.max(np.abs(q_consistent - formula)))
        residual = float(np.max(np.abs(consistent(formula) - formula)))
        value_match = float(np.max(np.abs(np.max(formula, axis=1) - value_star)))
        gap_identity = float(
            np.max(
                np.abs(
                    (value_star[:, None] - formula)
                    - (value_star[:, None] - q_star) / denominator
                )
            )
        )

        worst_formula = max(worst_formula, formula_error)
        worst_consistent_residual = max(worst_consistent_residual, residual)
        worst_value_match = max(worst_value_match, value_match)
        worst_gap_identity = max(worst_gap_identity, gap_identity)

    report = {
        "seed": seed,
        "trials": trials,
        "worst_formula_error": worst_formula,
        "worst_consistent_residual": worst_consistent_residual,
        "worst_value_match_error": worst_value_match,
        "worst_gap_identity_error": worst_gap_identity,
        "max_classical_iterations": max_classical_steps,
        "max_consistent_iterations": max_consistent_steps,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    assert worst_formula < 2e-10
    assert worst_consistent_residual < 2e-10
    assert worst_value_match < 2e-10
    assert worst_gap_identity < 2e-10


if __name__ == "__main__":
    run()

