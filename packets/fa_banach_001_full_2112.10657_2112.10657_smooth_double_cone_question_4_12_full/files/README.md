# Smooth double-cone estimates for Question 4.12

Status: `full_solution_likely_valid (smooth Question 4.12)`

Run: `fa_banach_001`  
Lane: `2`  
Agent: `agent_lane_02`  
Date: 2026-07-18

Source paper: Andre Guerra, Bogdan Raita, Matthew Schrecker, *Compensation
phenomena for concentration effects via nonlinear elliptic estimates*,
arXiv:2112.10657.

## Result

Question 4.12 asks whether the two-dimensional estimates of Section 4 can hold
for symmetric fields constrained to the double cone
`Sym^+_2 union Sym^-_2`.

This packet gives a positive answer for the exact smooth formulation. If
`A in C_c^\infty(R^2, Sym^+_2 union Sym^-_2)`, then both rowwise estimates hold:

```text
int det A <= ||div A_1||_1 ||div A_2||_1,
int det A <= ||curl A_1||_1 ||curl A_2||_1.
```

Consequently, the corresponding `L^2` Gagliardo--Nirenberg estimates hold for
smooth fields valued in any closed double subcone on which
`|M|^2 <= K det M`.

## Mechanism

For `tau = tr A`, use the smooth branch-flip approximation
`B_eps = eta_eps(tau) A`, where
`eta_eps(t) = t / sqrt(t^2 + eps^2)`. Because a matrix in the double cone with
zero trace is zero, `B_eps` is smooth, compactly supported, and positive
semidefinite. Also `det B_eps -> det A`, while the extra derivative terms in
the rowwise divergence and curl tend to zero in `L^1`. The source paper's
positive-cone div and curl estimates apply to `B_eps`, and passing to the limit
gives the double-cone estimates.

## Scope

This is a full answer to the smooth Question 4.12 as stated in Section 4.4.
It is not a solution of the separate rough `BV^Div` problem discussed nearby.
For rough fields with jumps directly from the positive to the negative branch,
the branch flip can create a new jump contribution.

## Novelty Check

Bounded checks performed on 2026-07-18:

- cheap run indexes for `2112.10657`, `double cone`, `Sym^+_2`, `Sym^-_2`,
  `Question 4.12`, and related terms;
- local parsed arXiv corpus for exact double-cone and constrained-Ornstein
  phrases;
- public web searches for exact phrases from Question 4.12 and the source
  arXiv id.

No separate later answer was found; exact hits led back to the source paper.
The earlier partial packet is preserved under `history/partial/`.
