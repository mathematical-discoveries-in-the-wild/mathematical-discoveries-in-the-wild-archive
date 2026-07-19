# Partial Packet: Convergent-Sequence Subcase Of Problem WU

Run: `fa_banach_001`

Status: candidate partial result.

Source paper: Jerzy Kakol, Manuel Lopez-Pellicer, Wieslaw Sliwa,
"On weak*-basic sequences in duals and biduals of spaces C(X) and Quojections",
arXiv:2601.19873.

Source target: Problem 12, asking whether `C_p(X)^*` admits a weak-star basic
sequence for every infinite compact space `X`.

## Packet Contents

- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop from page 7 of
  the source PDF showing Problem 12.
- `main.tex`: human-readable LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates only.

## Result

If a compact Hausdorff space `X` contains a nontrivial convergent sequence
`x_n -> x`, then `C_p(X)^*` contains a weak-star basic sequence. A direct
sequence is

```text
mu_n = delta_{x_n} - delta_x.
```

The proof shows that the weak-star closed linear span of `(mu_n)` is exactly
its algebraic span, and that the coefficient functionals are continuous.

## Limitations

This is not a full solution of Problem 12. It does not treat compact spaces
without nontrivial convergent sequences.

Novelty risk is high: the source paper's later metrizable-quotient theorem
appears to imply this subcase once restriction to the convergent compact
subset is recognized as an infinite-dimensional metrizable quotient. This
packet should therefore be counted as a constructive partial verification, not
as an original full answer.

## Human Review Recommendation

Review as a likely valid partial result. The main proof obligations are the
closed-span calculation in `C_p(X)^*` and the continuity of the coefficient
functionals.
