# Finite-Dimensional Domains and Hilbert-Range BPBp-RSE

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Helena del Rio, "Bollobas-type theorems for range strongly exposing
  operators", arXiv:2512.10442.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Question 5.11 asks whether `(X,Y)` has the BPBp(-RSE) whenever `X` is
finite-dimensional and `Y` is uniformly convex.

This packet proves the Hilbert-range subcase:

> If `X` is finite-dimensional and `H` is a real or complex Hilbert space,
> then `(X,H)` has the BPBp-RSE.

The proof first shows the classical BPBp for `(X,H)`. Every norm-one
operator `T:X -> H` has range contained in a Hilbert space of dimension at
most `dim X`; the finite-dimensional BPBp theorem gives a modulus for each
of the finitely many Hilbert dimensions `1,...,dim X`, and their minimum
works uniformly for the ambient Hilbert space. Since Hilbert spaces are
uniformly convex, Corollary 2.8 of the source paper upgrades BPBp to
BPBp-RSE.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of Question 5.11 from page 32.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The partial result is intentionally narrow. It does not solve the arbitrary
uniformly convex range case. The attempted broader compactness route is
recorded in `../../../../attempts/2512.10442_finite_dim_uniformly_convex_bpbp_rse.md`.

The key review point is the uniform modulus step over Hilbert subranges:
for fixed `dim X=n`, all `m`-dimensional Hilbert ranges are isometric for
each `1 <= m <= n`, so only finitely many finite-dimensional BPBp moduli
are needed.
