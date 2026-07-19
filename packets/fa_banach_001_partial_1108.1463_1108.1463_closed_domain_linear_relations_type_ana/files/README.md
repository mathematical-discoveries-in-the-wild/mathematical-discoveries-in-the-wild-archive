# Candidate Partial Result: Boundary Reduction for Type (ANA) Linear Relations

Source paper: Heinz H. Bauschke, Jonathan M. Borwein, Xianfu Wang,
and Liangjin Yao, *Construction of pathological maximally monotone
operators on non-reflexive Banach spaces*, arXiv:1108.1463.

Result type: `partial`

Status: strengthened candidate partial result, likely valid, pending
human review.

## Source Question

The source paper ends with four open questions. Question (iii) asks:

> Is every maximally monotone linear relation necessarily of type (ANA)?

Here (ANA) denotes almost negative alignment.

## Candidate Contribution

Let `X` be a real Banach space and let `A: X => X*` be a maximally
monotone linear relation. Write `D = dom A` and `M = closure(D)`.

The packet proves that `A` is of type (ANA) at every outside point
`(w,w*)` with either `w notin M` or `w in D`. Therefore any possible
counterexample to the source question must fail at a boundary point

```text
w in closure(dom A) \ dom A.
```

As an immediate corollary, if `dom A` is closed, then `A` is of type
(ANA). This contains the previous closed-domain theorem and makes the
remaining obstruction precise.

## Proof Idea

Maximality gives `A(0)=closure(dom A)^\perp`. Hence, after restricting
functionals to `M=closure(dom A)`, the relation becomes a single-valued
maximally monotone linear operator

```text
T: dom A subset M -> M*
```

with dense domain.

If `w notin M`, the positive distance from `w` to `M` gives a norming
annihilator in `M^\perp`; adding a large multiple of that annihilator
inside the fiber of `A` forces almost perfect negative alignment.

If `w in dom A`, a direct scaling argument works on the normed domain:
for `z* = T w - w*|_M`, choose a domain vector almost norming `-z*` and
move only a small amount in that direction. Hahn-Banach lifts the
resulting functional back to `X*` with the same norm, preserving the ANA
ratio.

The only place where both mechanisms fail is the genuine boundary case
`w in closure(dom A) \ dom A`.

## Files

- `source_paper.pdf`: arXiv:1108.1463 PDF.
- `supporting_paper_1407.1100.pdf`: Stephen Simons, *"Densities" and
  maximal monotonicity I*, arXiv:1407.1100.
- `figures/open_problem_crop.png`: crop of the source-paper open
  question list.
- `code/make_open_problem_crop.py`: reproducible crop helper.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates.

## Verification Notes

The proof is analytic and uses no computation. The main review points
are:

- verify `A(0)=closure(dom A)^\perp`;
- verify the reduction to a dense-domain single-valued operator on
  `closure(dom A)`;
- verify the two ANA constructions: quotient-distance outside
  `closure(dom A)` and small-scaling inside `dom A`;
- verify that no claim is made for boundary points in
  `closure(dom A) \ dom A`.

## Human Review

Recommended verdict: treat as a sharper partial theorem/reduction for
question (iii), not a full solution. A full proof would need to settle
the dense-domain boundary case for maximally monotone linear operators.
