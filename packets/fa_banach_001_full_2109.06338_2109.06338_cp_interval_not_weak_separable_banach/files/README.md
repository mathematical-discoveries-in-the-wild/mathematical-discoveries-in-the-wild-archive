# No Weak Banach Model for `C_p[0,1]`

Result type: `full`

Status: candidate full solution, likely valid pending human review.

Source paper:

- Jerzy Kakol, Arkady Leiderman, Artur Michalak, "A note on Banach spaces
  `E` admitting a continuous map from `C_p(X)` onto `E_w`", arXiv:2109.06338.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Problem 3.10 asks whether there is a separable Banach space `E` such that
`E_w` is homeomorphic to `C_p[0,1]`.

This packet proves a negative answer. In fact it proves the stronger statement
that if `K` is any uncountable compact metrizable `C`-space, then `C_p(K)` is
not homeomorphic to `E_w` for any Banach space `E`.

## Main Mechanism

Krupski's finite-support method for distinguishing `C_p(K)` from weak
topologies on `C(L)` can be run against a compact Hilbert cube of nonzero
functionals inside `E*`. The inverse homeomorphism assigns finitely many
weak coordinates to each point of `K`; a separation argument forces every
functional in a large fiber of the support map to lie in one fixed
finite-dimensional span. Strong infinite-dimensionality gives a fiber that is
not a `C`-space, while the finite-dimensional span makes the same fiber a
finite-dimensional compactum, hence a `C`-space.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop of Problem 3.10 from page
  12 of the source paper.
- `code/check_packet_assets.py`: reproducibility check for local packet assets
  and source-problem strings.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Literature Check

Bounded check performed on July 3, 2026:

- cheap run indexes searched for `2109.06338`, `C_p[0,1]`, `E_w`,
  `separable Banach`, `weak topology`, and `homeomorphic`;
- local parsed arXiv sources searched for exact and close phrases around
  `E_w is homeomorphic to C_p[0,1]` and `C_p([0,1]) weak topology separable
  Banach`;
- web search was run for the exact Problem 3.10 phrase and close variants.

The search found the source paper, Krupski's related `C_w(K)` obstruction, and
nearby `C_p`/weak-topology literature, but no later paper explicitly answering
Problem 3.10 or the stronger arbitrary-Banach formulation.

## Human Review Notes

Primary points to verify:

- the finite-support decomposition theorem is being used in the same
  parameter form as in Krupski/Marciszewski/van Mill, with the compact
  parameter space a weak-star compact subset of `E*`;
- the compact parameter set avoids the zero functional, so the support family
  is finite on each decomposition piece;
- the separation step uses only weak-star continuous functionals, hence
  elements of `E`;
- the dimension step uses the standard facts that finite products of compact
  metrizable `C`-spaces are `C`-spaces and that a compactum mapping onto a
  `C`-space with all fibers `C`-spaces is itself a `C`-space.
