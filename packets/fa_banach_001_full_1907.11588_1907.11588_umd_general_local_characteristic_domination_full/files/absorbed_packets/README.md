# Absorbed proof-history packets

These packets were created during the push toward the full UMD result for
Yaroslavtsev arXiv:1907.11588, Remark 12.10.  They are kept here as proof
history and supporting intuition, but they should no longer be counted as
separate active partial results: the finite-cotype de-Poissonization proof in
the parent packet supersedes their positive conclusions.

The `c0` counterexample is intentionally not moved here.  It remains under
`solutions/counterexamples/` because it is not superseded by the UMD theorem:
it records the sharp boundary that the broad Banach-space aggregate-domination
statement is false outside finite cotype/UMD geometry.

## Route Summary

1. Hilbert case.
   The first stable route used Hilbert square identities and Rosenthal-type
   estimates.  The packets show how characteristic domination controls the
   Hilbert quadratic and jump quantities, first at `p=2`, then for `p>=2`, and
   finally for all finite `p`.

2. Non-Hilbert model spaces.
   The next packets pushed through `ell_q` and `L^q(S)` subcases.  They used
   scalarization, Banach-function-space BDG estimates, and
   Dirksen-Yaroslavtsev `L^q` Burkholder-Rosenthal formulas to learn what the
   discrete aggregate comparison should look like beyond Hilbert space.

3. Endpoint and Poissonization attempts.
   The `p=1` endpoint packets isolated square-function and positive
   Poissonization mechanisms.  These made the later compound-Poisson viewpoint
   natural: compare the Bernoulli family with the Poisson aggregate and use
   measure domination after Poisson superposition.

4. General UMD conditional reduction.
   The conditional de-Poissonization packet identified the exact missing
   property: for symmetric finite independent families, control the
   compound-Poisson sum with the same aggregate nonzero law by the original
   Bernoulli sum.

5. Final full result.
   The parent packet proves this missing de-Poissonization estimate in every
   finite-cotype Banach space by the Maurey-Pisier contraction principle.
   Since UMD spaces have finite cotype, Yaroslavtsev's accessible-jump
   reduction gives the general local martingale theorem.

## Absorbed Conditional Packets

- `conditional/1907.11588_Lq_p1_endpoint_square_function_reduction/`
- `conditional/1907.11588_UMD_depoissonization_reduction/`

## Absorbed Partial Packets

- `partial/1907.11588_hilbert_l2_general_characteristic_domination/`
- `partial/1907.11588_hilbert_pge2_general_characteristic_domination/`
- `partial/1907.11588_hilbert_all_p_general_characteristic_domination/`
- `partial/1907.11588_ellq_natural_exponent_characteristic_domination/`
- `partial/1907.11588_Lq_discrete_aggregate_domination_all_p/`
- `partial/1907.11588_Lq_general_local_characteristic_domination/`
- `partial/1907.11588_Lq_p1_endpoint_qle2_square_function/`
- `partial/1907.11588_Lq_p1_qgt2_deterministic_dominator_square/`
- `partial/1907.11588_Lq_p1_endpoint_all_q_poissonization/`
