# Smooth double-cone divergence estimate

Status: `partial_result_likely_valid`

Run: `fa_banach_001`  
Lane: `2`  
Agent: `agent_lane_02`  
Date: 2026-07-03

Source paper: Andre Guerra, Bogdan Raita, Matthew Schrecker, *Compensation
phenomena for concentration effects via nonlinear elliptic estimates*,
arXiv:2112.10657.

## Result

Question 4.12 asks whether the two-dimensional estimates of the source section
can hold for symmetric fields constrained to the double cone
`Sym^+_2 union Sym^-_2`.

This packet proves the smooth version of the determinant estimate. If
`A in C_c^\infty(R^2, Sym^+_2 union Sym^-_2)`, then

```text
int det A <= ||div A_1||_1 ||div A_2||_1.
```

Consequently, the corresponding `L^2` Gagliardo--Nirenberg estimate holds for
smooth fields valued in any closed double subcone on which
`|M|^2 <= K det M`.

## Mechanism

Set `B = sign(tr A) A`. Since a matrix in the double cone with zero trace is
the zero matrix, the sign derivative produces no distributional term for
smooth `A`. Thus `B` is positive semidefinite, `det B = det A`, and
`div B_i` is controlled by `div A_i`. The source paper's positive-cone estimate
then applies to `B`.

## Limitations

This is intentionally classified as a partial result. It answers the smooth
double-cone version of Question 4.12, but it does not settle the rough
`BV^Div` formulation discussed nearby in the source paper. For rough fields
with jumps directly from the positive to the negative cone, the sign-flip can
create a new jump contribution.

## Novelty Check

Bounded checks performed on 2026-07-03:

- cheap run indexes for `2112.10657`, `double cone`, `Sym^+_2`, `Sym^-_2`,
  `Ornstein`, and related terms;
- local parsed arXiv corpus for exact double-cone and constrained-Ornstein
  phrases;
- public web searches for exact phrases from Question 4.12 and the constrained
  Ornstein discussion.

No separate later answer was found; the only exact hit was the source paper.
