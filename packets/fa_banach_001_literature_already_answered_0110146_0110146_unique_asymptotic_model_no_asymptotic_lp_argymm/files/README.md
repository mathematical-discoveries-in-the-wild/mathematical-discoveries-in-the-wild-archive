# Literature-Already-Answered Packet: Unique Asymptotic Models

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an exact later-literature answer to a Halbeisen--Odell
problem from arXiv:math/0110146. It is not a new proof from this run.

## Source Problem

- Lorenz Halbeisen and Edward Odell, *On asymptotic models in Banach spaces*,
  arXiv:math/0110146.
- Local PDF: `source_paper.pdf`.
- Evidence image:
  - `figures/open_problem_crop.png` (PDF page 31, item `(5.2.1)`; source TeX
    labels this as Problem 6.1).

The source asks whether a Banach space whose asymptotic models are all
uniformly equivalent to `ell_p` or `c_0` must contain an asymptotic `ell_p` or
`c_0` subspace.

## Supporting Literature

- S. A. Argyros, A. Georgiou, A. Manoussakis, and P. Motakis, *The complete
  separation of the two finer asymptotic `ell_p` structures for
  `1 <= p < infinity`*, arXiv:2106.12323.
- Local PDF: `supporting_paper_2106.12323.pdf`.
- Evidence images:
  - `figures/supporting_abstract_complete_answer_crop.png` (page 1 abstract:
    finite-`p` construction and complete-answer statement).
  - `figures/supporting_problem_restatement_crop.png` (page 2: the
    Halbeisen--Odell problem restated).
  - `figures/supporting_theorem_1_4_crop.png` (page 3: Theorem 1.4).

## Literature Status

The finite-`p` part has a negative answer. For every `1 <= p < infinity`,
Argyros--Georgiou--Manoussakis--Motakis construct a reflexive Banach space
with an unconditional basis that admits `ell_p` as a unique asymptotic model
but contains no Asymptotic `ell_p` subspace.

The `c_0` side is positive under the no-`ell_1` hypothesis by
Freeman--Odell--Sari--Zheng, as recorded in the supporting paper's abstract.

## Proof Idea

The source problem asks whether array-level asymptotic uniqueness forces a
global asymptotic game structure inside some subspace. The later paper shows
that, for finite `p`, it does not: the norm is built so arrays of normalized
blocks still have the unique `ell_p` asymptotic model, while every subspace
contains a well-founded tree segment whose norm is too small for an
Asymptotic `ell_p` estimate. Thus the array property survives, but the
hereditary global asymptotic property fails in every subspace.

## Limitations

- This packet records a known later answer, not a new construction from this
  run.
- The finite-`p` answer is negative. The `c_0` statement is positive only in
  the standard non-`ell_1` setting cited by the supporting paper.
- Other open problems from Section 5.2/6 of the Halbeisen--Odell paper are not
  claimed here.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_2106.12323.pdf`: later paper answering the problem.
- `figures/open_problem_crop.png`: source problem crop.
- `figures/supporting_abstract_complete_answer_crop.png`: supporting abstract
  crop.
- `figures/supporting_problem_restatement_crop.png`: restated problem crop.
- `figures/supporting_theorem_1_4_crop.png`: finite-`p` theorem crop.
- `code/crop_evidence.py`: regenerates the evidence crops.
- `tmp/`: LaTeX build intermediates.

## Verification And Search Notes

Before packaging, the run lightweight indexes were searched for `0110146`,
`asymptotic model(s)`, `Halbeisen`, `Odell`, `Rosenthal`, `normalized weakly
null`, and `spreading model`. The only hits were adjacent asymptotic-structure
packets, not this problem. Local arXiv sources were then searched for
`Problem 6.1`, `unique asymptotic model`, `Halbeisen and Odell`, and
`complete answer`, which identified arXiv:2106.12323 as an explicit later
answer.

## Human Review Recommendation

Treat the finite-`p` part of Halbeisen--Odell's asymptotic-model subspace
question as already answered negatively by arXiv:2106.12323. Keep this as
literature-status memory rather than counting it as an original solve.
