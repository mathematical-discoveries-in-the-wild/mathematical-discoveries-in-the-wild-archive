# Literature-Already-Answered Packet: unique non-symmetric subsymmetric basis

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: later literature gives an affirmative answer to Problem 1.1 of
arXiv:1910.02414. This packet records a literature-status match, not an
original proof from the run.

## Original Problem Source

- Fernando Albiac, Jose L. Ansorena, Stephen J. Dilworth, Denka Kutzarova,
  *A dichotomy for subsymmetric basic sequences with applications to Garling
  spaces*, arXiv:1910.02414; Trans. Amer. Math. Soc. 374 (2021), no. 3,
  2079--2106.
- Local PDF: `source_paper.pdf`.

The source asks in Problem 1.1 whether there exists a Banach space in which
all subsymmetric basic sequences are equivalent to one basis and that basis is
not symmetric.

## Supporting Answer Source

- Peter G. Casazza, Stephen J. Dilworth, Denka Kutzarova, Pavlos Motakis,
  *On uniqueness and plentitude of subsymmetric sequences*, arXiv:2112.09602.
- Local PDF: `supporting_paper_2112.09602.pdf`.

## Status Match

The supporting paper explicitly cites the question from Kutzarova--Mityagin--
Papathanasiou and from arXiv:1910.02414, then states that it answers the
question positively. The answer is the subsymmetrization `Su(T*)` of
Tsirelson's original Banach space. Its canonical basis is subsymmetric but not
symmetric, and every subsymmetric basic sequence in `Su(T*)` is equivalent to
that basis.

This answers Problem 1.1 only. The neighboring finite-number Problems 1.2 and
1.3 in arXiv:1910.02414 are not claimed here.

## Idea Of The Answer

The later paper uses a subsymmetric version of Tsirelson's original space.
The construction already supplies a canonical subsymmetric basis that is not
symmetric. The main verification is rigidity: any normalized subsymmetric block
sequence in `Su(T*)` must retain enough large coordinates to be dominated by,
and then equivalent to, the canonical basis. Since every subsymmetric basic
sequence in a space with a basis is equivalent to a normalized block basis,
this proves uniqueness up to equivalence.

## Verification Notes

- Same-paper check: arXiv:1910.02414 asks Problem 1.1 and does not answer it;
  its Garling spaces instead have continuum many subsymmetric basic sequences.
- Separate-source check: arXiv:2112.09602 is a later paper and cites both
  `KMP` and `AADK` for the question.
- Exact implication: if `Su(T*)` has a non-symmetric subsymmetric basis and
  every subsymmetric basic sequence in `Su(T*)` is equivalent to it, then it
  satisfies Problem 1.1 exactly.
- Scope limitation: this packet does not address the two-subsymmetric-bases
  question or the general finite `n>1` question.

## Search Bounds

- Searched the run lightweight indexes for `1910.02414`, `2112.09602`,
  `subsymmetric`, `unique subsymmetric`, `non-symmetric`, `Su(T*)`, and
  `Tsirelson`; no existing packet or attempt covered this exact result.
- Inspected the arXiv:1910.02414 source around Problems 1.1--1.3.
- Inspected the arXiv:2112.09602 source around the abstract, introduction,
  and the theorem stating uniqueness of subsymmetric sequences in `Su(T*)`.
- Web/arXiv search on 2026-06-14 for the exact title and question phrasing
  surfaced arXiv:2112.09602 as the direct later answer.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2112.09602.pdf`: later answer source.
- `figures/open_problem_crop.png`: rendered crop of Problem 1.1 in the source.
- `figures/supporting_answer_crop.png`: rendered crop of the supporting paper's
  explicit positive-answer paragraph.

## Human Review Recommendation

Verify the exact-source chain:

1. arXiv:1910.02414 Problem 1.1 asks for a Banach space whose subsymmetric
   basic sequences are all equivalent to a single non-symmetric basis.
2. arXiv:2112.09602 cites the question from arXiv:1910.02414 and says it
   answers it positively.
3. arXiv:2112.09602 proves that `Su(T*)` has a non-symmetric subsymmetric
   canonical basis and that every subsymmetric sequence in `Su(T*)` is
   equivalent to that basis.
