# Property-(u) ell_1-preduals contain c0

Status: `partial_result_likely_valid`

Run: `fa_banach_001`  
Source: arXiv:1504.08223, Spiros A. Argyros, Ioannis Gasparis, and
Pavlos Motakis, "On the structure of separable L_infty-spaces"  
Processed: 2026-07-03 by `agent_lane_04` in lane 1

## Claim

Let `X` be an infinite-dimensional Banach space with `X*` isomorphic to
`ell_1`.  If `X` has Pelczynski's property-(u), then `X` contains an
isomorphic copy of `c0`.

Equivalently, any counterexample to Godefroy--Li Question IV.2 must already
contain `c0`; the remaining hard step is to prove that such a space is actually
isomorphic to `c0`.

The packet also records the resulting self-reduction: such an `X` splits as
`c0 \oplus Y`, where either `Y` is finite-dimensional and `X` is isomorphic to
`c0`, or `Y` is again an infinite-dimensional isomorphic `ell_1`-predual with
property-(u).

## Source Question

On page 2, the source paper says that its asymptotic `c0` isomorphic
`ell_1`-predual without `c0` is a step toward Godefroy--Li Question IV.2:
whether every isomorphic `ell_1`-predual satisfying Pelczynski's property-(u)
is isomorphic to `c0`.

## Proof Summary

Property-(u) represents weakly Cauchy sequences, modulo weakly null errors, as
partial sums of weakly unconditionally Cauchy series.  If a space contains no
copy of `c0`, the Bessaga--Pelczynski theorem makes every such series
unconditionally norm convergent.  Hence property-(u) plus no `c0` implies weak
sequential completeness.

If `X*` is separable, then `X` contains no `ell_1`.  Rosenthal's `ell_1`
theorem and Eberlein--Smulian then imply that a weakly sequentially complete
such `X` is reflexive.  But an infinite-dimensional space with dual isomorphic
to `ell_1` cannot be reflexive.  Therefore `X` must contain `c0`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: page-2 crop of the GL Question IV.2
  passage.

## Human Review Focus

1. Check the exact convention for property-(u); the packet uses the standard
   weakly Cauchy / WUC partial-sum formulation.
2. Verify the use of Bessaga--Pelczynski: no `c0` iff every WUC series is
   unconditionally convergent.
3. Check the self-reduction: Sobczyk complements the first `c0`; property-(u)
   passes to complemented subspaces; complemented infinite-dimensional
   subspaces of `ell_1` are isomorphic to `ell_1`.
4. Keep the status partial: the proof gives containment and recursive
   splitting of `c0`, not isomorphism to `c0`.
