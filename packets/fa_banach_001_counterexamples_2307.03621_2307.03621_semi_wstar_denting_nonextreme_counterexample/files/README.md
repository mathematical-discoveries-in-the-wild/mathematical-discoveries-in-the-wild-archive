# Counterexample Packet: Semi weak-star denting need not imply extreme

Run: `fa_banach_001`

Result type: `counterexample`

## Source Problem

- Sudeshna Basu and Susmita Seal,
  *Ball separation characterization of ball dentability and related
  properties*, arXiv:2307.03621, v4.
- Local PDF: `source_paper.pdf`.
- Source location: PDF page 13; parsed source
  `data/parsed/arxiv_sources/2307.03621/Ball_sep_arxiv.tex`, lines 818--835.

Remark 4.3 says that a semi weak-star denting point of `B_{X^*}` is a norm
limit of extreme points, and asks whether every such point must itself be
extreme.

## Counterexample

The packet constructs a four-dimensional real Banach space `Y` whose unit ball
`K` has:

- a boundary point `p` that is not extreme, since it is the midpoint of two
  distinct points of `K`;
- a sequence of exposed points `c(1/n)` converging in norm to `p`.

Exposed points of a compact finite-dimensional convex body are denting points.
Since the definition of semi denting only asks for small slices contained near
the point, not necessarily containing the point, the norm limit `p` of denting
points is semi denting. Taking `X=Y^*`, finite dimensionality makes the
weak-star topology on `X^*=Y` coincide with the norm topology. Thus `p` is a
semi weak-star denting point of `B_{X^*}` but is not extreme.

## Files

- `main.tex`: full counterexample proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: page-13 source crop with Definition 4.1 and
  Remark 4.3.

## Verification

- The proof is analytic and finite-dimensional; no computational verifier is
  needed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  was used to render the packet.
- Bounded novelty checks were run against the run indexes and web phrases such
  as `"semi w* denting" extreme point`, `"semi weak* denting" "extreme point"`,
  and `"semi denting point" "extreme point" Banach`; no exact prior answer was
  found during this loop.

## Human Review Recommendation

Check the finite-dimensional convex-body construction, especially the exposure
of the points `c(r)` and the final passage from norm semi denting to weak-star
semi denting via finite dimensionality.
