# Literature-Implied Partial Answer: Weak-FPP Under A Block-Basis Hypothesis

Run: `fa_banach_001`

Result type: `literature_implied_answer (partial subcase)`

## Original Problem Source

- Cleon S. Barroso, *Isometric embeddings of Banach spaces under optimal
  projection constants*, arXiv:2012.10849.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 5).

The source paper recalls the weak fixed point property and states that it is
still open whether every Banach space with an unconditional basis has the
weak-FPP. The same paper proves the shrinking `D`-unconditional subcase with
`D < sqrt(6)-1`; that same-paper theorem is not packaged here.

## Supporting Literature

- Cleon S. Barroso, *Remarks on the FPP in Banach spaces with unconditional
  Schauder basis*, arXiv:2302.11287.
- Local PDF: `supporting_paper_2302.11287.pdf`.
- Evidence images:
  - `figures/supporting_context_crop.png` (page 2), where the later paper
    phrases questions `(Q1)` and `(Q2)` and cites the 2020 source as a small
    step toward `(Q1)`.
  - `figures/supporting_theorem_crop.png` (page 8), Theorem 3.11.

Theorem 3.11 of arXiv:2302.11287 proves that if a Banach space `X` has a
Schauder basis `(e_i)` such that every block basis sequence has a subsequence
equivalent to `(e_i)`, then `X` has the weak-FPP in particular when `(e_i)` is
a `1`-suppression unconditional basis.

## Match

The `1`-suppression unconditional branch is a genuine subcase of the original
unconditional-basis weak-FPP question. Thus the later theorem gives an
affirmative literature-implied partial answer:

```text
If X has a 1-suppression unconditional Schauder basis and every block basis
sequence has a subsequence equivalent to that basis, then X has the weak-FPP.
```

This is not an exact solution of the original broad question. The extra
block-basis-equivalence hypothesis is essential to the scope recorded here.

## Limitations

- This is not an original proof from the run; it records a later literature
  implication.
- It does not settle whether every Banach space with an unconditional basis
  has the weak-FPP.
- It does not settle the same question for arbitrary `1`-suppression
  unconditional bases; the block-basis hypothesis is still required.
- The theorem also includes a `1`-spreading-basis branch, but the packet uses
  only the `1`-suppression unconditional branch as the direct subcase of the
  original unconditional-basis question.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original problem source, arXiv:2012.10849.
- `supporting_paper_2302.11287.pdf`: supporting theorem source.
- `figures/open_problem_crop.png`: original source evidence.
- `figures/supporting_context_crop.png`: later-paper context evidence.
- `figures/supporting_theorem_crop.png`: supporting theorem evidence.
- `code/crop_evidence.py`: regenerates the three evidence crops.
- `tmp/`: local render intermediates.

## Human Review Recommendation

Review the identification of the block-basis hypothesis with the theorem's
printed assumption and keep the status as a partial literature-implied answer.
Do not upgrade this packet to a full answer to the unconditional-basis
weak-FPP problem.
