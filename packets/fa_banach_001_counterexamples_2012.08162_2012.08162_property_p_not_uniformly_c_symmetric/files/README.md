# Counterexample: Property (P) Does Not Give Uniform C-Symmetry

Run: `fa_banach_001`

Agent: `agent_lane_00`

Status: `candidate_counterexample_likely_valid`

## Source conjecture

Conjecture 3.11 of Chmielinski--Khurana--Sain, *Local approximate
symmetry of Birkhoff-James orthogonality in normed linear spaces*,
arXiv:2012.08162, asserts that in finite dimensions property (P) at every
extreme point is equivalent to global C-approximate symmetry.

## Counterexample

Let `K` be the centrally symmetric convex body with upper boundary

```text
u(x)=-1+2 sqrt(1+x) on [-1,0],
u(x)=1              on [0,1],
```

and lower boundary `-u(-x)`. Use `K` as the unit ball of `R^2`.

Property (P) holds at every sphere point. Nevertheless, for

```text
x_r=(r^2-1,2r-1),   y_r=(r,1),   1/2<r<1,
```

we have `x_r perpendicular_B y_r`, while the least reverse approximate
orthogonality constant equals `2r-1`. These constants tend to one, so no
global constant below one exists.

## Consequence

This is a two-dimensional nonpolyhedral counterexample to Conjecture 3.11.
It shows why the source's polyhedral and smooth hypotheses cannot simply be
removed: a sequence of smooth support directions can accumulate at a corner
where an additional support functional makes property (P) hold only at the
limit.

## Files

- `main.tex`: full proof and human-review note.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2012.08162.
- `figures/open_problem_crop.png`: Conjecture 3.11 from source PDF page 16.
- `figures/unit_ball_geometry.png`: construction and sample tangent pair.
- `code/verify_geometry.py`: deterministic numerical geometry checks.
- `verification.md`: analytic and computational verification record.
