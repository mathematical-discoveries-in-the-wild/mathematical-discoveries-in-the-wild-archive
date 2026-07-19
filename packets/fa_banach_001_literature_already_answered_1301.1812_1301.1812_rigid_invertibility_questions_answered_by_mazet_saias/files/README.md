# Literature status: rigid invertibility questions already answered

Status: `literature_already_answered`

Source paper: arXiv:1301.1812, George Costakis, Antonios Manoussos and
Ioannis Parissis, *Recurrent Linear Operators*.

Supporting answer: arXiv:2101.03751, Pierre Mazet and Eric Saias,
*Sur le spectre des operateurs rigides*; published as *On the spectrum of
rigid operators*, Ergodic Theory Dynam. Systems 43 (2023), 1351--1362.

## Identification

Question 2.22 on page 12 of the source arXiv PDF asks whether every rigid
operator is invertible; failing that, it asks whether the inverse of an
invertible rigid operator must also be rigid.

Mazet and Saias explicitly restate the same two questions from Costakis,
Manoussos and Parissis (with a numbering discrepancy: they refer to Question
2.20), state that both answers are negative, and prove a block-diagonal
spectrum theorem.  The case `r=0` gives a rigid non-invertible operator, and
the cases `0<r<1` give invertible rigid operators whose inverses cannot be
rigid because their spectra leave the closed unit disk.

## Files

- `main.tex` - compact literature-status note.
- `solution_packet.pdf` - rendered status packet.
- `source_paper.pdf` - original arXiv:1301.1812 source question paper.
- `supporting_paper_2101.03751.pdf` - decisive Mazet--Saias answer paper.
- `supporting_paper_2403.17904_context.pdf` - later Saavedra--Stadlbauer
  context paper noting the same Mazet--Saias answer.
- `figures/open_problem_crop.png` - source question crop.
- `figures/supporting_answer_crop.png` - Mazet--Saias page 2 answer crop.
- `figures/supporting_answer_q2_continuation_crop.png` - page 3 continuation.

## Search Bounds

The run indexes were searched for `1301.1812`, `rigid invertible`,
`non-invertible rigid`, `Recurrent Linear Operators`, and close variants.
Web/arXiv searches were run for the exact question text and for
`On the spectrum of rigid operators Mazet Saias`.  The later arXiv:2403.17904
paper pointed to Mazet--Saias, and arXiv:2101.03751 explicitly answers the two
source questions.
