# Finite Metric Spaces for the Lipschitz-Free Uniform `(S)` Question

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- William B. Johnson, Tomasz Kania, "Uniform Property (S)",
  arXiv:2602.09106.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper asks for a characterization of pointed metric spaces
whose Lipschitz-free Banach spaces have uniform property `(S)`.

This packet proves the finite metric-space subcase:

- if `|M| <= 2`, then `F(M)` has uniform property `(S)` (with the
  zero-dimensional case interpreted vacuously);
- if `|M| >= 3`, then `F(M)` fails even property `(S)`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the
  open-problem list from page 19 of the source paper.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The proof uses two standard facts about finite Lipschitz-free spaces:
`dim F(M)=|M|-1`, and the unit ball is the convex hull of the finitely
many molecules `(delta_x-delta_y)/d(x,y)`. The remaining argument is the
elementary observation that a finite-dimensional polyhedral norm in
dimension at least two fails property `(S)`.

This is only a finite-metric subcase. It does not address infinite
pointed metric spaces.
