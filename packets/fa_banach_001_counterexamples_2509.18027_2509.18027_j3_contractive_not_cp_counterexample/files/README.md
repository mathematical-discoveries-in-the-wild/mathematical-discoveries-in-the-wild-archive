# A contractive but not completely positive map on `OS(J3)`

Status: `candidate_counterexample_likely_valid`

Source: Dey, Dhang, and Mukherjee, *Matricial ranges, dilations, and
unital contractive maps*, arXiv:2509.18027.

## Result

Conjecture 6.10 is false. There exists `X in M3` such that

```text
||alpha X + beta X*|| <= sqrt(|alpha|^2 + |beta|^2)
```

for every pair of complex scalars, while the unital self-adjoint map
`phi: OS(J3) -> OS(X)` with `phi(J3)=X` is not 3-positive. It is contractive
by Theorem 5.1 of the source paper but is not completely positive.

The matrix `X` is obtained existentially from the Effros--Winkler matrix
Hahn--Banach theorem by separating the source paper's matrix

```text
B0 = [[0, 0, 1/sqrt(3)],
      [sqrt(2/3), 0, 0],
      [0, 1/sqrt(3), 0]]
```

from the matrix-convex hull of the two-by-two equality generators. The
packet proves independently that `B0` has no equality dilation.

## Files

- `main.tex` and `solution_packet.pdf`: self-contained proof and render.
- `source_paper.pdf`: source arXiv paper.
- `supporting_separation_reference_1407.8198.pdf`: Theorem 2.2 restating the
  Effros--Winkler separation theorem.
- `figures/open_problem_crop.png`: Conjecture 6.10 on source page 21.
- `code/check_finite_identities.py`: finite matrix sanity checks.
- `verification_report.md`: dependency and verification report.

## Novelty check

Run indexes were searched for arXiv:2509.18027, the title, `J3`, `matricial
range`, and `unital contractive map`. A bounded web search on 2026-07-22 used
the exact phrases `Conjecture 6.10`, `Is every unital contractive map from
OS(J3)`, the title plus `counterexample`, and the arXiv id plus `Effros
Winkler`. It found the source preprint and summaries but no later resolution
or discussion of this argument.

## Human review

Recommended verdict: likely valid finite-dimensional counterexample. Review
the levelwise closedness of the generated matrix-convex hull and the use of
the monic Effros--Winkler separator at level three.
