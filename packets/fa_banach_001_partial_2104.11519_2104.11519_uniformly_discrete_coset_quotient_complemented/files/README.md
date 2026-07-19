# Uniformly Discrete Coset Quotients for the Bounded-Subgroup Question

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Marek Cuth, Michal Doucha, "Projections in Lipschitz-free spaces
  induced by group actions", arXiv:2104.11519.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Question 5.5 asks whether, for an amenable locally compact or SIN metric
group `G` and a bounded subgroup `H`, one always has
`F(G/H)` isomorphic to a complemented subspace of `F(G)`.

This packet proves a uniformly discrete quotient subcase:

- if `G` has a left-invariant metric `d`;
- if `H` is bounded, with `B = sup_{h in H} d(e,h) < infinity`;
- if the usual coset quotient metric
  `D(gH,fH) = inf_{h,k in H} d(gh,fk)` is a genuine uniformly discrete
  metric on `G/H`;

then `F(G/H,D)` is isomorphic to a complemented subspace of `F(G,d)`.
The projection constant is at most `1 + 2B/a`, where `a` is the
separation constant of the quotient.

The proof does not use amenability, local compactness, or the SIN
hypothesis; the extra hypothesis is the uniform discreteness of the
coset quotient.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop of Question 5.5
  from page 21 of the source paper.
- `tmp/`: LaTeX build intermediates.

## Human Review Notes

The proof is a Lipschitz-section argument. Boundedness of `H` gives an
additive estimate for any transversal `s:G/H -> G`:
`d(su,sv) <= D(u,v) + 2B`. Uniform discreteness converts this additive
error into a multiplicative Lipschitz bound. The linearization of the
section then gives a right inverse to the quotient map on Lipschitz-free
spaces, hence a projection.

This does not settle the general bounded-subgroup question. The main
remaining case is when the quotient has arbitrarily small nonzero
distances, where the additive `2B` loss does not yield a Lipschitz
section.
