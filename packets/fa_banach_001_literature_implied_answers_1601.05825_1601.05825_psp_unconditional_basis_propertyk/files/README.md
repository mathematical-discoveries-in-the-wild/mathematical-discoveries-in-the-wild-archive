# Literature-Implied Answer Packet: PSP Unconditional-Basis Subcase of Property (K)

Run: `fa_banach_001`

Result type: `literature_implied_answer (partial subcase)`

Status note: this is a literature-implied affirmative subcase of Aviles--Rodriguez
Problem 2.18, not a full solution to the unconditional-basis problem.

## Source Problem

- Antonio Aviles and Jose Rodriguez, *Convex combinations of weak*-convergent
  sequences and the Mackey topology*, arXiv:1601.05825, 2016.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 11, Problems 2.16--2.18).

Problem 2.18 asks whether every Banach space with an unconditional basis and
no subspace isomorphic to `c_0` has property `(K)`.

## Supporting Literature

- Jose Rodriguez, *Cesaro convergent sequences in the Mackey topology*,
  arXiv:1812.10079, 2018/2019.
- Local PDF: `supporting_paper_1812.10079.pdf`.
- Evidence images:
  - `figures/supporting_mu_to_k_crop.png`: property `(\mu^s)` implies property `(K)`.
  - `figures/supporting_psp_mu_crop.png`: every Banach lattice with PSP and weak unit has property `(\mu^s)`.

## Literature Status

The supporting paper implies the following partial answer:

If a Banach space `X` has an unconditional basis and, with its associated
coordinate Banach-lattice order, has the positive Schur property (PSP), then
`X` has property `(K)`. Adding the original hypothesis that `X` contains no
copy of `c_0` gives an affirmative PSP subcase of Problem 2.18.

This does not answer the full Problem 2.18. The PSP assumption is an extra
lattice hypothesis.

## Bounded Search

- Checked the run registry, solution, attempt, and proof-gap indexes for
  `1601.05825`, `1812.10079`, `property (K)`, `positive Schur property`,
  `unconditional basis`, `c_0`, and related Mackey-topology terms.
- Web searches for exact phrases from the three 2016 open problems found the
  source paper and later property `(K)` papers, but no full answer to
  Problem 2.18.
- The 2019 Rodriguez paper was inspected locally from arXiv source/PDF; it
  supplies the PSP/weak-unit theorem used here.

## Files

- `README.md`: this packet summary.
- `main.tex`: review packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_1812.10079.pdf`: supporting literature source.
- `figures/open_problem_crop.png`: original problem crop.
- `figures/supporting_mu_to_k_crop.png`: supporting implication crop.
- `figures/supporting_psp_mu_crop.png`: supporting PSP theorem crop.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Treat this as a narrow literature-implied partial answer. Verify that the
coordinate lattice associated with an unconditional basis has a weak unit, and
that the PSP hypothesis is clearly marked as an added assumption rather than
part of the original problem.
