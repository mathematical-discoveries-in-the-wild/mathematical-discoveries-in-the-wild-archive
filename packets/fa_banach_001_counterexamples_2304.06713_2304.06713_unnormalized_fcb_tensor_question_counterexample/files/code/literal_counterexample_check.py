"""Tiny arithmetic check for the constant-shift obstruction."""

from __future__ import annotations


def violates_bound(denominator: float, constant_term: float) -> bool:
    """Return True when |constant_term / denominator| exceeds 1."""
    if denominator == 0:
        raise ValueError("The displayed ratio is undefined for denominator 0.")
    return abs(constant_term / denominator) > 1


if __name__ == "__main__":
    d = 4
    epsilon = 0.1
    maxinf = epsilon**2
    proposed_denominator = 10.0
    constant_term = 11.0
    print({"d": d, "maxinf": maxinf, "violates": violates_bound(proposed_denominator, constant_term)})
