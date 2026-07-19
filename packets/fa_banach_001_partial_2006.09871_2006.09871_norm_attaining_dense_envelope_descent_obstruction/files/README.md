# Strong partial packet: dense envelopes and projection-descent obstruction

Status: `strong_partial_likely_valid`

Source paper: Sheldon Dantas, Mingu Jung, Oscar Roldan, and Abraham Rueda
Zoca, "Norm-attaining tensors and nuclear operators", arXiv:2006.09871.

Open question targeted: Question 6.1 asks whether, for reflexive Banach spaces
`X` and `Y`, norm-attaining tensors are dense in `X \hat{\otimes}_\pi Y`.

## Current Result

This packet supersedes the previous Hilbert-pair-only partial packet. It
records the strongest current structural partial result:

- every pair `X,Y` embeds into a dense-envelope pair `X,Y_infty`, with `Y`
  sitting isometrically and 1-complementedly in `Y_infty`, such that
  norm-attaining tensors are dense in `X \hat{\otimes}_\pi Y_infty`;
- consequently, density of projective norm-attaining tensors does not descend
  through arbitrary 1-complemented tensor subspaces;
- the failure pinpoints the defect in the later density-descent Lemma 4.1 of
  Garcia-Lirola--Guerrero-Viu--Rueda Zoca, arXiv:2407.10710;
- the original reflexive problem is reduced to a special reflexive graph
  descent / fixed-support correction problem;
- the earlier Hilbert-pair and finite Hilbert `ell_1`-sum positive subcases
  remain valid and are preserved in `history/`.

## Why This Is Still Partial

This does not solve Question 6.1. The dense-envelope construction uses
nonreflexive ambient graph/envelope spaces in general. The remaining open issue
is whether the special graph descent mechanism can be proved for reflexive
pairs, or whether a reflexive supported tensor can be built where the
fixed-support correction principle fails.

## Files

- `main.tex`: active proof packet source.
- `solution_packet.pdf`: rendered active packet.
- `source_paper.pdf`: local copy of arXiv:2006.09871.
- `supporting_paper_2407.10710.pdf`: later paper whose printed Lemma 4.1 is
  analyzed as part of the descent obstruction.
- `figures/open_problem_crop.png`: crop showing Question 6.1 in the source
  paper.
- `code/crop_open_problem.py`: reproducible crop script for the source
  question.
- `history/hilbert_pair_partial_packet_2026_06_16/`: previous Hilbert-pair
  partial packet now superseded by the stronger structural packet.
- `evidence/supplied_reports_2026_06_20/`: supplied TeX/PDF reports used to
  assemble this packet and the related proof-gap packet.

## Human Review Recommendation

Review as a likely valid strong partial result, not as a full solution. The
main checks are the trace-face correction theorem, the universal graph
stabilization, the iteration producing `Y_infty`, the use of known non-density
examples to refute arbitrary 1-complemented density descent, and the claimed
equivalence of the original reflexive question with the special graph-descent
formulation.
