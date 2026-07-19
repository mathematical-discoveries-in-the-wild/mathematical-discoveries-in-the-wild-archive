# Literature-Already-Answered Packet: Greedy-Envelope Counterexamples

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Fernando Albiac, José L. Ansorena, Pablo M. Berná, Przemysław
  Wojtaszczyk, *Greedy approximation for biorthogonal systems in
  quasi-Banach spaces*, arXiv:1903.11651; Dissertationes Mathematicae 560
  (2021), 1--88.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

In the arXiv PDF crop the questions are numbered Problems 12.5 and 12.6.
The later answer paper cites the published numbering as Problems 13.5 and
13.6. This packet records both labels to avoid a numbering mismatch.

## Supporting Answer Source

- Fernando Albiac, José L. Ansorena, Miguel Berasategui, Pablo M. Berná,
  *When Greedy Approximation Breaks: Counterexamples in Quasi-Banach Spaces*,
  arXiv:2510.13693.
- Local PDF: `supporting_paper_2510.13693.pdf`.
- Evidence crop: `figures/supporting_answer_crop.png`.

## Status

The two checked problems are already answered negatively by arXiv:2510.13693.

- Question A / AABW Problem 13.5 / AAT Problem 16: No. A quasi-Banach space
  can have an almost greedy Schauder basis whose image in the Banach envelope
  is not quasi-greedy.
- Question B / AABW Problem 13.6 / AAT Problem 14: Yes. There is a
  quasi-Banach space with an almost greedy basis that is not a Schauder basis
  under any rearrangement.

## Limitations

- This is not an original solution from the run.
- This packet does not claim the bidemocratic refinement appearing inside
  AABW's original Problem 12.5.
- The supporting paper explicitly notes that Question B remains open when
  restricted to Banach spaces.

## Files

- `main.tex`: review packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2510.13693.pdf`: later answer source.
- `figures/open_problem_crop.png`: AABW Problem 12.5 crop.
- `figures/open_problem_12_6_crop.png`: AABW Problem 12.6 crop.
- `figures/supporting_answer_crop.png`: later answer crop.

## Human Review Recommendation

Check that the numbering mismatch is harmless: the arXiv source crop shows
Problems 12.5 and 12.6, while arXiv:2510.13693 cites the published numbering
as Problems 13.5 and 13.6. Also check that the packet is restricted to the
general Banach-envelope question, not the bidemocratic refinement.
