# Stretched-tetrahedron counterexample to the John-position ratio conjecture

Status: `candidate_counterexample_likely_valid`

Source: Maud Szusterman, *A New Excluding Condition Towards the
Soprunov--Zvavitch Conjecture on Bezout-type inequalities*, arXiv:2302.01213.

## Result

Page 7 conjectures that, among affine images of a simplex, the regular simplex
(John position) minimizes

```text
max over facets F of Isop(F) / Isop(simplex).
```

This packet gives an explicit counterexample in dimension three. Start with a
unit-edge regular tetrahedron whose edge `v0v1` lies on the first coordinate
axis, and apply `diag(3,1,1)`. Every simplex is tangential, so the displayed
ratio equals the tetrahedral inradius divided by the facet inradius. The four
facets split into two pairs, with ratios

```text
q_A = sqrt(2/3) (3+2sqrt(3)) / (3sqrt(3)+sqrt(11))
    = 0.6199994121...

q_B = 3sqrt(2)(1+2sqrt(3)) / ((3sqrt(3)+sqrt(11))sqrt(11))
    = 0.6708149210...
```

Both are strictly below the regular-tetrahedron value
`1/sqrt(2) = 0.7071067812...`. Thus the proposed minimum is not attained at
the regular simplex.

## Scope and files

- [main.tex](main.tex): complete exact proof and bounded novelty check.
- [solution_packet.pdf](solution_packet.pdf): compiled review packet.
- [verification.md](verification.md): adversarial audit.
- [code/verify.py](code/verify.py): exact symbolic coordinate check.
- [source_paper.pdf](source_paper.pdf): source paper.
- [figures/open_problem_crop.png](figures/open_problem_crop.png): page-7 source evidence.

The counterexample addresses the intended affine-transform interpretation in
the source. If transforms were restricted to orthogonal maps, the ratio would
be invariant and the minimization tautological. This packet does **not** answer
the paper's Question 1 about non-simplex polytopes or the broader
Soprunov--Zvavitch conjecture.

Human review recommendation: verify the source's intended affine domain and
the two elementary facet classes. The exact radical inequalities and all
coordinate calculations are independently checked by the included script.
