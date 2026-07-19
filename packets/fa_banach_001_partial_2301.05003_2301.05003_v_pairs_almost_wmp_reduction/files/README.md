# V-pairs Have the Almost Weak Maximizing Property

Result type: `partial`

Status: candidate partial result/reduction, likely valid pending human review.

Source paper:

- Mingu Jung, Gonzalo Mart\'inez-Cervantes, and Abraham Rueda Zoca,
  "Rank-one perturbations and norm-attaining operators", arXiv:2301.05003.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Source Problem Context

Question 3.7 of the source paper asks whether every `V`-pair has the weak
maximizing property (WMP). The paper also observes that the direct
operator-level idea fails: there are individual `V`-operators with
non-weakly-null maximizing sequences that do not attain their norm, although
the surrounding pair in that example is not a `V`-pair.

## Claimed Contribution

This packet proves the following reduction.

Let `(X,Y)` be a `V`-pair. If an operator `T : X -> Y` has the property that
every maximizing sequence for `T` is non-weakly-null, then `T` attains its
norm. Equivalently, every `V`-pair has the almost weak maximizing property
(`aWMP`).

Consequently, if a `V`-pair ever fails WMP, the witnessing non-norm-attaining
operator must have mixed maximizing behavior: it must have at least one
non-weakly-null maximizing sequence, but also at least one weakly-null
maximizing sequence.

## Novelty Caution

The published PDF of arXiv:2301.05003 does not state the `aWMP` reduction.
The arXiv source TeX contains a commented-out draft of essentially this
observation. This packet should therefore be treated as a precise promoted
cleanup and provenance record with modest novelty, not as a full solution of
Question 3.7.

## Files

- `main.tex`: self-contained LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: source crop around Question 3.7 and the
  obstruction remark.
- `code/crop_open_problem.py`: crop script.
- `tmp/`: build intermediates.

## Human Review Notes

Verifier focus:

- Check the standard `V`-operator convention used here: for a norm-one
  operator in a `V`-pair, there is a norm-one `S : Y -> X` and a sequence
  `y_n in S_Y` with `||T S y_n - y_n|| -> 0`. This is the approximate
  fixed-point form used in the source paper's Remark 3.8.
- Check the reflexivity/sequential compactness step for the domain of a
  `V`-pair.
- Check that the result is classified only as a partial reduction: it does not
  prove that every `V`-pair has WMP.
