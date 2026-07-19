# Literature-Implied Answer: Uniformly Discrete `p=1` Strong Schur Bound

## Source Question

- Source paper: F. Albiac, J. L. Ansorena, J. Bima, and M. Cuth, *Lipschitz free p-spaces for 0<p<1 in the light of the Schur p-property and the compact reduction*, arXiv:2506.09786.
- Target: the uniformly separated bounded `p=1` route following Question 6.3, asking whether for each `K` there is a uniformly separated bounded metric space `M` such that `F(M)` fails the `K`-strong Schur property.
- Screenshot: `figures/open_problem_crop.png`.
- Source PDF retained as `source_paper.pdf`.

## Status

This is filed as `literature_implied_answer`, not as a new original proof.
The later paper arXiv:2604.01875 does not appear to explicitly say it is
answering arXiv:2506.09786 Question 6.3. However, its Theorem 1.1 and
Proposition 2.2 directly imply a negative answer to the uniformly separated
bounded `p=1` arbitrarily-bad-constant formulation.

## Answer

For real Lipschitz-free spaces, every uniformly separated metric space is
uniformly discrete. Cuth--Kalenda arXiv:2604.01875 proves that `F(M)` is
`3`-Schur for every uniformly discrete metric space `M`. Their Proposition
2.2 says that, for real Banach spaces, `c`-Schur implies `c`-strong Schur.
Therefore every such `F(M)` has the `3`-strong Schur property.

Consequently, in the `p=1` case there cannot be a uniformly separated bounded
metric-space example failing `K`-strong Schur for every `K`; already `K=3`
is impossible. This explains why Kalenda's example mentioned in the source
paper can fail `1`-strong Schur but still does not supply the requested
arbitrarily-bad family.

## Limitations

- This does not solve the full Question 6.3.
- This does not address the `0<p<1` analogue.
- This does not rule out non-uniformly-discrete metric spaces in the `p=1`
  setting.
- The result is literature-implied rather than original to this pipeline.

## Files

- `solution_packet.pdf`: rendered human-facing packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original source paper.
- `supporting_paper_2604.01875.pdf`: supporting later paper.
- `figures/open_problem_crop.png`: stitched screenshot of the source question.
- `figures/supporting_theorem_1_1_crop.png`: supporting theorem screenshot.
- `figures/supporting_prop_2_2_crop.png`: supporting proposition screenshot.
- `code/crop_evidence.py`: regenerates the evidence crops.
- `code/check_implication.py`: checks that the expected source/supporting PDF text snippets are present.
