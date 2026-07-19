# Strictly Convex `L_1(mu,X)` `CWO-S` Extension

Status: likely valid strengthened partial result for arXiv:2503.09182.

Source question: Haller--Kuuseok--Poldvere prove that `L_1(mu,X)` has
property `CWO-S` when `X` is weakly uniformly rotund, and ask whether this
remains true when `X` is merely assumed to have property `CWO-S`.

Result: The theorem remains true for every strictly convex Banach space `X`:

```text
if mu is non-zero sigma-finite and X is strictly convex,
then L_1(mu,X) has property CWO-S.
```

This strengthens the source theorem beyond `wUR` in the natural direction
highlighted by the source question, because strictly convex spaces have
`CWO-S`, but need not be `wUR`.

Core idea: If `z = lambda x + nu y` is a norm-one point of a convex
combination in `L_1(mu,X)`, equality in the `L_1` triangle inequality holds
almost everywhere. Strict convexity forces `x(omega)`, `y(omega)`, and
`z(omega)` to lie on the same positive ray almost everywhere. Partition the
direction map `z/||z||` into small-diameter pieces; on each piece the local
averages of `x`, `y`, and `z` have norm-small deterministic errors. General
weak functionals are handled by composing the finitely many functionals
defining the weak neighbourhoods with multiplication by characteristic
functions of the partition pieces.

Scope caveat: This is not a full solution of the source question for all
`CWO-S` target spaces. In non-strictly-convex `CWO-S` spaces, pointwise
equality in the triangle inequality need not force a common direction, so the
main mechanism here disappears. The injective tensor-product question also
remains open.

Packet contents:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:2503.09182.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/crop_open_problem.py`: crop-generation script.

Novelty check: Local indexes contain the prior arbitrary `l1`-sum/atomic
partial packet and a separate tensor partial packet for arXiv:1806.10693, but
no strict-convex `L_1(mu,X)` upgrade. Bounded web searches for strict-convex
`CWO-S` Bochner variants did not find an exact match. Novelty confidence is
moderate pending expert review.
