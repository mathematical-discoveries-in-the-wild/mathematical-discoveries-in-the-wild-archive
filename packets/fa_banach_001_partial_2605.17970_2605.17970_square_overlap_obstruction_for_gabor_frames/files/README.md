# Square-Overlap Obstruction for Gabor Frames

Status: `partial_result_likely_valid`.

## Source Target

- Source: Nir Lev and Anton Tselishchev, "Gabor unconditional bases and frames in `L^p(R)`", arXiv:2605.17970.
- Targeted source problem: the paper proves nonexistence of unconditional Gabor bases and unconditional Schauder frames in `L^p(R)`, `1<p<2`, when the time projection has bounded density, and leaves open the same nonexistence question for arbitrary countable `Lambda subset R x R` and arbitrary `g in L^p(R)`.

## Result

Let `1<p<2`, let `g in L^p(R)` be nonzero, and let
`Lambda subset R x R` be countable with time projection
`T={t : (t,s) in Lambda for some s}`. If

```text
sum_{t in T} |g(x-t)|^2 < infinity
```

on a measurable set of positive Lebesgue measure, then no coefficient
functionals can make the Gabor system
`{e_s tau_t g : (t,s) in Lambda}` an unconditional Schauder frame for
`L^p(R)`. In particular, no unconditional basis of this Gabor form exists under
the same square-overlap hypothesis.

Equivalently, any hypothetical counterexample to the full open problem must
satisfy the necessary condition

```text
sum_{t in T} |g(x-t)|^2 = infinity
```

almost everywhere on every positive-measure region.

## Why This Matters

The source proof uses bounded density of `T` only to guarantee a finite local
translated-window envelope. This packet isolates the actual envelope condition
and improves the pointwise exponent from `p` to `2`. It therefore recovers the
bounded-density theorem and also rules out arbitrary countable time sets whose
translates of the chosen window have locally square-summable overlap on any
positive-measure set.

The remaining open case is now sharply localized: if an unconditional Gabor
frame for `1<p<2` exists, its time projection must force locally infinite
square overlap of the window almost everywhere.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2605.17970.
- `figures/open_problem_crop.png`: crop from page 5 showing the source's open problem.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Review as a genuine partial obstruction/reduction, not as a full solution. The
main checks are:

1. the coefficient block estimate remains valid when the frequency set depends
   on the time coordinate;
2. the local `L^2` estimate for the functions `u_t f` follows from the
   nonuniform exponential Bessel estimate used in the source;
3. the square-envelope pointwise inequality is legitimate after passing to
   pointwise convergent subsequences of unconditional partial sums;
4. the final contradiction with bounded inclusion `L^p(E) -> L^2(E)` is correct
   for every positive-measure Lebesgue set when `1<p<2`.
