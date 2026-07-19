# Codimension-2 Full Interval for Non-Attaining Projections in C[0,1]

## Verdict

Candidate full solution, likely valid, for Question 6.2 of Kania--Lewicki
arXiv:2604.10771 in the case `n=2`.

For every
```text
2 < Lambda <= 1 + lambda_2 = 7/3
```
there is a codimension-2 subspace `Y` of the real space `C[0,1]` such that
`lambda(Y,C[0,1]) = Lambda` and no minimal projection onto `Y` exists.

## Source

- Tomasz Kania and Grzegorz Lewicki, *Finite-codimensional subspaces of
  Daugavet spaces: projection constants and minimal projections*,
  arXiv:2604.10771.
- Source question: Question 6.2, page 14 of the locally compiled source PDF.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Exact Target

Question 6.2 asks, for each fixed `n`, whether every value in
`(2, 1 + lambda_n]` occurs as the projection constant of a codimension-`n`
subspace of the real space `C[0,1]` for which no minimal projection exists.
The packet settles this question for `n=2`, using the classical value
`lambda_2=4/3`.

## Result

For `0 < t <= 1`, let
```text
V_t = {x in l_1^3 : x_1 + x_2 + t x_3 = 0}.
```
Its unique minimal projection in `l_1^3` has norm
```text
r(t) = (1+t)^2 / (1+t+t^2),
```
and `r(t)` runs through `(1,4/3]`.

Place an isometric copy `W_t` of `V_t` in `M[0,1]` as measures constant on three
successive intervals. Then `lambda(W_t,M[0,1])=r(t)`, but `W_t` admits no
weak-star continuous minimal projection. The obstruction is elementary:
weak-star continuity would provide continuous coefficient functions whose
averages on the first two intervals are forced onto two disjoint exposed faces
of the two-dimensional ball
```text
|(a+tb)| + |a| + |b| <= r(t).
```
Continuity at the common endpoint is impossible.

Kania--Lewicki's Daugavet duality theorem then transfers `Y_t = W_t^\perp` to
`C[0,1]`, giving
```text
lambda(Y_t,C[0,1]) = 1 + r(t)
```
and no minimal projection.

## Novelty Check

Cheap run indexes contained only the earlier failed attempt
`attempts/2604.10771_codim2_endpoint_regular_hexagon_route.md`, which used the
same finite-dimensional family but stopped at the block-duplication uniqueness
barrier. Bounded web searches on 2026-06-29 for the arXiv id, title, codimension
2/full interval phrases, and the `ker(1,1,t)` projection-constant route found no
later explicit solution.

## Limitations

This is a full answer to Question 6.2 only for `n=2`. It does not address the
remaining fixed codimensions `n >= 3`.

## Verification

The proof is analytic and finite-dimensional. The packet includes:

- a weighted dual certificate for the projection constant of `V_t`;
- the equality case, proving uniqueness of the finite-dimensional minimizer;
- the exposed-face discontinuity argument excluding weak-star continuous
  minimal projections onto `W_t`;
- the final transfer via the source paper's Daugavet duality theorem.

Human review should focus on the weak-star coefficient/face argument and the
use of the source paper's minimal-projection equivalence.

