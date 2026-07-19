# Conditional Packet: Two-level reduction for the real-exponent Hunter moment conjecture

status: conditional_reduction_likely_valid

run: fa_banach_001

target arXiv id: 2512.12254

source paper: Silouanos Brazitikos and Christos Pandis, "Sharp inequalities for symmetric polynomials, Hunter's conjecture, and moments of exponential random variables", arXiv:2512.12254.

## Claim

For every real exponent `q > 2`, any relative-interior local extremum of

```text
E(a_1 X_1 + ... + a_n X_n)^q
```

on a fixed positive coordinate support under `sum a_i^2 = 1` has at most two distinct positive coefficient values.

Consequently, Conjecture 4.8 of the source paper for `q > 5` is reduced to the following two-level Gamma inequality: for all integers `r,s >= 1`, all `x >= 0`, and independent `G_r ~ Gamma(r)`, `G_s ~ Gamma(s)`,

```text
E(x G_r + G_s)^q / (r x^2 + s)^(q/2)
  >= min_{1 <= m <= r+s} rho(m,q).
```

The previous lane-5 packet already proves Conjecture 4.8 for `0 < q <= 5`, so a proof of this two-level dependency for all `q > 5` would complete the real-exponent conjecture.

## Conditional Dependency

This is not a full solution of Conjecture 4.8. The remaining unproved dependency is exactly the two-level Gamma inequality above.

The packet proves the extremizer reduction rigorously, but it does not prove the two-level inequality. Numerical checks included here found no violation of the dependency.

## Files

- `main.tex` - conditional solution packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2512.12254.
- `figures/open_problem_crop.png` - crop of Conjecture 4.8 from the source packet.
- `code/pair_splitting_scan.py` - deterministic grouped slice checks.
- `code/exact_vector_search.py` - exact divided-difference arbitrary-vector search.

## Human Review Recommendation

Review as a likely valid conditional reduction. The key mathematical check is the divided-difference extremizer lemma, especially the repeated-node identities and the strict monotonicity of divided differences of `x^(q+n-1)` when `q > 2`. The main open task is to prove or disprove the two-level Gamma inequality.
