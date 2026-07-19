# Partial Result: one-dimensional concave-modulus MAP subcase

Status: `partial_result_likely_valid`.

Source paper: Alexander Brudnyi, "On Properties of Geometric Preduals of
`C^{k,omega}` Spaces", arXiv:1607.04824.

## Target

The source proves that `G_b^{k,omega}(R^n)` has the metric approximation
property when `lim_{t->infty} omega(t)=infty`, and then says that for bounded
moduli it is not clear whether `G_b^{k,omega}(R^n)` itself has the metric
approximation property. See page 5 of `source_paper.pdf` and
`figures/open_problem_crop.png`.

## Result

For `k=0`, `n=1`, and every nondecreasing concave modulus `omega` with
`omega(0)=0`, the geometric predual `G_b^{0,omega}(R)` has the metric
approximation property.

This includes standard bounded concave moduli, so it sharpens the source
paper's bounded approximation result in a genuine one-dimensional subcase.

## Idea

For `k=0`, the unit ball of `C_b^{0,omega}(R)` consists of bounded functions
with `omega`-Lipschitz seminorm at most one. Average over randomly shifted
grid roundings. Concavity of `omega` says that the expected rounded distance
does not exceed the original distance. After clipping to a large interval, the
averaging operator has finite rank and norm at most one on the dual function
space, hence gives a finite-rank contraction on the geometric predual. As the
mesh tends to zero and the interval expands, these contractions converge
strongly to the identity on the closed span of point evaluations.

## Limitations

This packet does not settle the full question in arXiv:1607.04824. The proof is
one-dimensional and uses concavity of the modulus in the shifted-grid
rounding inequality. It does not cover higher-dimensional `R^n`, `k>=1`, or
nonconcave moduli satisfying only the source paper's stated monotonicity
conditions.

## Novelty Check

Cheap run indexes had no exact `1607.04824` hit. Web searches for
`"1607.04824" "geometric preduals"`, `"G_b^{k,omega}" approximation property`,
`"C_b^{k,omega}" "approximation property"`, and snowflake/Lipschitz-free MAP
phrases found the source paper but no direct later answer. The local registry
does contain a separate packet for arXiv:1501.07036 noting that the MAP problem
for arbitrary Lipschitz-free spaces over subsets of `R^N` remains open beyond
known subcases. This packet is therefore recorded as a new partial theorem
for the 1607.04824 target, not as a literature-status identification.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1607.04824.
- `figures/open_problem_crop.png`: crop of the source-page MAP uncertainty.
- `code/random_rounding_sanity.py`: optional numerical sanity check for the
  shifted-grid inequality in standard concave examples.

