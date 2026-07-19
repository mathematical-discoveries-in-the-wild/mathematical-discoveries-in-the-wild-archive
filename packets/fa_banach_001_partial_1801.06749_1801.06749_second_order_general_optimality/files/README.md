# Spectral-rich sharpness for the second-order semigroup estimate

Status: `partial_result_likely_valid`

Source target: A. Gomilko, S. Kosowicz, and Yu. Tomilov, *A general approach to approximation theory of operator semigroups*, arXiv:1801.06749, published in Journal de Mathematiques Pures et Appliquees 127 (2019), DOI `10.1016/j.matpur.2018.08.008`.

## Result

The source paper proves the second-order bound
`O(t^3 n^{-3/2})` for bounded `C_0`-semigroups in Corollary 4.10 and proves sharpness only for a shift semigroup and Euler's formula. It then says that the optimality of this estimate should hold in a more general context.

This packet proves that general-context sharpness for the natural spectral-rich class used earlier in the same paper:

> If `-A` generates a bounded `C_0`-semigroup, `overline{ran}(A)=X`, and the spectrum of `A` meets the imaginary axis at all absolute frequencies, then for every fixed `g in B_4`, `g != exp(-z)`, the regularized second-order remainder has `liminf` size at least `c_g t^3 n^{-3/2}`.

Thus the `n^{-3/2}` exponent in Corollary 4.10 cannot be uniformly improved in this spectral class.

## Scope

This is a partial result rather than a full settlement of every possible "more general context". It covers constant families `g_t=g` and semigroups with the same imaginary-axis spectral richness assumed in Proposition 4.11 of the source paper. It does not prove sharpness for arbitrary bounded semigroups, arbitrary varying families `(g_t)`, or the separate holomorphic `n^{-2}` regime.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source passage where the authors defer the more general optimality argument.
- `figures/corollary_4_10_crop.png`: source passage containing Corollary 4.10 and the bound being sharpened.
- `code/scalar_asymptotic_check.py`: numeric sanity check for the scalar asymptotic in the Euler case.

## Novelty check

Run indexes were searched for `1801.06749`, `RowA0++`, `operator semigroups`, `second order`, `n^-3/2`, and optimality phrases. Web searches on 2026-07-18 for the exact title, `RowA0++`, `optimality of (4.29)`, `postpone a general argument`, and close `g^n(tA/n) n^{-3/2}` phrases found the source paper or mirrors but no later paper giving this spectral-rich second-order argument. The packet should still be human-reviewed as a likely original partial result.
