"""Sanity check for the diagonal dimension-spectrum counterexample."""

from __future__ import annotations


def d_only_poles(max_k: int = 5) -> list[complex]:
    return [complex(1 - k, 0) for k in range(max_k + 1)]


def algebra_visible_poles(max_k: int = 3, max_m: int = 3) -> list[complex]:
    return [
        complex(1 - k, m)
        for k in range(max_k + 1)
        for m in range(-max_m, max_m + 1)
    ]


target = complex(1, 1)
print("D-only poles:", d_only_poles())
print("Sample algebra-visible poles:", algebra_visible_poles())
print("target pole from Tr(U |D|^{-s}) = zeta(s-i):", target)
print("target in D-only probes?", target in d_only_poles())

assert target not in d_only_poles()
assert target in algebra_visible_poles()
