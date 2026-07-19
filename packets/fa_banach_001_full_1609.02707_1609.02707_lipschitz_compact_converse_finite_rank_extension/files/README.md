# Full Solution Candidate: Lipschitz-Compact Converse via Finite-Rank Extension

Status: `candidate_full_solution_likely_valid`

This packet addresses the open converse stated on page 6 of Rueda--Sanchez-Perez,
`The approximation property and Lipschitz mappings on Banach spaces`
(arXiv:1609.02707), immediately before Proposition 4.

The source proves that the `I`-Lipschitz approximation property of a pointed
metric space `X` implies uniform approximation of every `I`-Lipschitz compact
map `phi: Z -> X` after composing with the Dirac map `delta_X`.  The open
converse is also true.  Given a relatively `I`-Lipschitz compact test set
`K` in `X`, view `K union {0}` as a rescaled pointed metric space so that it
is contained in the unit ball.  The assumed compact-map approximation gives a
finite-rank Lipschitz map on that small space.  Since its range is
finite-dimensional, scalar McShane extensions of its coordinate functions
extend it to a finite-rank Lipschitz map on all of `X`, preserving the
approximation on `K`.

Scope note: this packet solves the Proposition 4 converse signal only.  It
does not address the separate classical approximation-property problem on
page 2 concerning whether
`K(E;E) = closure(E' tensor E)^{tau_b}` implies that `E` has the AP.

Files:

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet for review.
- `source_paper.pdf`: arXiv PDF for 1609.02707.
- `figures/open_problem_crop.png`: page-6 crop containing the open-problem statement.

