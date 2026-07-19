# Exact norm of the unresolved Lorentz sequence embedding

Status: **candidate full solution, likely valid; human review requested**

Source: Anna Kneselová, *Maximal non-compactness of embeddings between
sequence spaces*, arXiv:2510.24290, Theorem 3.4(3) and the question on PDF
page 15.

## Result

For `0 < p1 < p2 <= infinity` and `p1 < q1 < q2 <= infinity`, let
`I: ell^{p1,q1} -> ell^{p2,q2}` be the identity embedding and put

`B_N = sum_{n=1}^N n^(q1/p1-1)`.

If `q2<infinity`, put

`A_N = sum_{n=1}^N n^(q2/p2-1)`,

where `q2/p2=0` when `p2=infinity`. Then

`||I|| = max_N A_N^(1/q2) / B_N^(1/q1)`.

If `q2=infinity`, then

`||I|| = max_N N^(1/p2) / B_N^(1/q1)`.

The maximizing test vectors are initial-segment indicators. The maxima exist
because the displayed ratios tend to zero. In particular, the source upper
bound

`(q1/p1)^(1/q1-1/q2)`

is strictly larger than the true norm throughout the off-diagonal range
`p1<p2`; it is never optimal there.

## Proof Intuition

After replacing the decreasing rearrangement `a*` by
`z_n=(a_n*)^q1`, the source norm becomes a linear weighted budget while the
target norm becomes a weighted `ell_r` norm with `r=q2/q1>1`. Every decreasing
null sequence `z` is the positive sum of its jumps times initial-segment
indicators. Minkowski's inequality therefore bounds every vector by the worst
initial segment, and those same initial segments attain the bound.

## Packet Contents

- `solution_packet.pdf` / `main.tex`: theorem, proof, strictness, and review
  notes;
- `source_paper.pdf`: the latest arXiv PDF used for the extraction;
- `figures/theorem_3_4_case_3.png`: source estimate and proof context;
- `figures/open_problem_crop.png`: the explicit open sentence on page 15;
- `code/verify_exact_norm.py`: finite-dimensional random-jump sanity checks;
- `verification.md`: verifier report and novelty-search bounds.

## Human Review Recommendation

Verify the jump-decomposition/Minkowski step, including passage to infinitely
many jumps, and the argument that each initial-block ratio is strictly below
the source constant. No unproved mathematical dependency remains. Novelty is
provisional: the exact source question and nearby primary literature were
searched, but older general weighted-monotone-cone results may contain the
abstract lemma without applying it to this 2025 question.
