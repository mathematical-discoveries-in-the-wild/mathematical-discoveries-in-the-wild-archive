# Metric Wedge Obstructions for the Lipschitz-Free Uniform `(S)` Question

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- William B. Johnson, Tomasz Kania, "Uniform Property (S)",
  arXiv:2602.09106.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper asks for a characterization of pointed metric spaces whose
Lipschitz-free Banach spaces have uniform property `(S)`.

This packet proves an infinite-family obstruction. If a pointed metric
space `M` splits as a metric wedge `A \vee B`, and one wedge component `A`
is finite with `|A| >= 3`, then `F(M)` fails property `(S)`, hence fails
uniform property `(S)`. In particular, this gives infinite metric-space
examples whenever the other component `B` is infinite.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the
  open-problem list from page 19 of the source paper.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The main points to verify are:

- the standard isometric decomposition
  `F(A \vee B) = F(A) \oplus_1 F(B)` for metric wedges;
- the finite polyhedral facet obstruction from the existing finite-metric
  packet;
- the fact that the obstruction survives in the `l_1`-sum because the same
  `F(B)` norm term is added to both perturbed norms.

This is not a full characterization of Lipschitz-free spaces with uniform
property `(S)`.
