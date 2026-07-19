# Counterexample: asymmetric half-line norm and the literal strong Suzuki condition

Status: `counterexample_likely_valid_scoped`.

Source/open-problem signal: arXiv:2402.06657, S. Cobzas, *The strong Ekeland
variational principle in quasi-pseudometric spaces*.

## Claim

The literal unqualified extension of the displayed quasi-pseudometric
Suzuki-style strong Ekeland condition to arbitrary asymmetric normed spaces is
false.

Take `X = R` and the standard one-sided asymmetric norm
`q(t) = max(t,0)`.  With the associated quasi-metric
`d(x,y) = q(y-x) = max(y-x,0)`, let `f = 0` be the constant function.
For any `x0 in R` and `lambda > 0`, no point `z` can satisfy the four displayed
conditions (3.16) from the source with `rho=d`.

Indeed, condition (i) forces `z >= x0`.  Conditions (ii) and (iii) then hold
for this constant function exactly as the one-sided order dictates, but
condition (iv) fails: the constant sequence `x_n = z-1` satisfies
`f(x_n) + lambda d(z,x_n) = 0 = f(z)`, while
`d(x_n,z) = 1` for all `n`.

## Scope

This does not disprove every possible asymmetric-normed-space analogue of
Suzuki's theorems.  It refutes the naive formulation obtained by inserting the
quasi-metric of an arbitrary asymmetric normed space into the source's
displayed condition (3.16), where the premise uses the forward distance from
`z` to the minimizing sequence and the conclusion asks for the reverse
convergence toward `z`.

Refined versions may still hold under stronger separation hypotheses
(`T_1`/Hausdorff assumptions), compactness assumptions, bicompleteness, or a
different one-sided strong-minimum convention.  The example is intentionally
minimal: it shows that the familiar one-dimensional asymmetric normed space
already blocks the unqualified extension.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2402.06657.
- `figures/open_problem_crop.png`: source conclusion/open-question crop.
- `figures/source_condition_crop.png`: crop of the displayed strong condition.

## Search Evidence

Cheap run indexes were searched for `2402.06657`, strong Ekeland, Ekeland
variational principle, quasi-metric/quasi-pseudometric spaces, asymmetric
normed spaces, Suzuki, reflexivity, Caristi, Takahashi, and completeness.
No exact prior packet or attempt was found.

Web searches on 2026-07-18 for the source title, `"strong Ekeland"
"asymmetric normed" Suzuki reflexivity`, `"Ekeland variational principle"
"asymmetric normed spaces" strong`, and variants involving `max(t,0)` found
the source arXiv/MDPI article and related asymmetric Ekeland literature, but no
later explicit resolution of this exact one-sided counterexample.

Human review recommendation: accept as a scoped counterexample to the naive
literal asymmetric-normed extension; do not read it as closing the full refined
asymmetric reflexivity program.
