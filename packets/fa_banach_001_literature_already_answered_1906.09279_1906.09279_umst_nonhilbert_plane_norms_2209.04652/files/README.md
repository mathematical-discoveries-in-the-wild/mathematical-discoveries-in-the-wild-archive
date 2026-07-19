# Literature-Already-Answered Packet: non-Hilbert UMST plane norms

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: the weaker uniformly micro-semitransitive Hilbert-characterization
subquestion raised in arXiv:1906.09279 is answered negatively by the separate
paper arXiv:2209.04652. This packet records literature status only; it is not
an original proof from the run. The stronger question whether micro-transitive
Banach-space norms must be Hilbertian remains open here.

## Original Problem Source

- F. Cabello Sanchez, S. Dantas, V. Kadets, S. K. Kim, H. J. Lee, and
  M. Martin, *On Banach spaces whose group of isometries acts
  micro-transitively on the unit sphere*, arXiv:1906.09279.
- Local source lines inspected:
  `data/parsed/arxiv_sources/1906.09279/source.tex`, lines 600--610.
- Local PDF: `source_paper.pdf`.

The source records that no examples of micro-transitive norms other than
Hilbert norms were known and says it might be possible that micro-transitivity
implies Hilbertianity. It then adds that the same might hold for the weaker
property of uniform micro-semitransitivity.

## Supporting Answer Source

- F. Cabello Sanchez and J. Cabello Sanchez, *Dynamics of the semigroup of
  contractive automorphisms of Banach spaces*, arXiv:2209.04652.
- Local source lines inspected:
  `data/parsed/arxiv_sources/2209.04652/dynamicsJMAA.tex`, lines 804--831
  and 1092--1104.
- Local PDF: `supporting_paper_2209.04652.pdf`.

## Status Match

The supporting paper defines UMST in Section 4, cites the original CDKKLM
paper, and says the only previously known UMST norms were Euclidean, which had
made it conceivable that UMST characterized Hilbert spaces. It then explicitly
states that this is not the case and proves Theorem 4.1: every `C^2` norm on
the plane whose unit sphere has strictly positive curvature at every point is
uniformly micro-semitransitive.

The same section gives polar-coordinate examples. In particular, the curve
`r = 1 + (1/17) sin(4 theta)` is a non-elliptic centrally symmetric smooth
unit sphere satisfying the theorem's hypotheses, hence it gives a
two-dimensional non-Hilbertian UMST norm.

## Scope Limitations

This packet clears only the weaker UMST possibility in the source paragraph.
It does not settle whether every micro-transitive norm is Hilbertian, nor does
it give a non-Hilbert micro-transitive example.

## Verification Notes

- Same-paper check: arXiv:1906.09279 raises the UMST/Hilbertian possibility
  and does not provide a non-Hilbert UMST example.
- Separate-source check: arXiv:2209.04652 is a distinct later paper and cites
  the original micro-transitivity paper while explicitly negating the proposed
  UMST characterization.
- Duplicate check: the cheap indexes had no exact entry for arXiv:1906.09279.
  Nearby entries cover broader Mazur rotation subcases, not this UMST
  counterexample status.
- Scope check: a two-dimensional non-Euclidean normed plane is not Hilbertian,
  so the supporting theorem answers the weaker UMST Hilbert-characterization
  question negatively.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2209.04652.pdf`: decisive supporting answer source.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:1906.09279 states the possible Hilbertian characterization for
   micro-transitive norms and, even more, for UMST norms.
2. arXiv:2209.04652 Section 4 says the UMST characterization is false.
3. arXiv:2209.04652 Theorem 4.1 and its polar examples yield non-Hilbert
   two-dimensional UMST norms.
