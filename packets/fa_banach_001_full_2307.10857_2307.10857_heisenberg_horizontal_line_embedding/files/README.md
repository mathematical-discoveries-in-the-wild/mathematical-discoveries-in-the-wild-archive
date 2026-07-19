# Full packet: Heisenberg horizontal-line embedding

- Source: Kevin Wildrick, "Bochner Partial Derivatives,
  Cheeger-Kleiner Differentiability, and Non-Embedding", arXiv:2307.10857.
- Extracted target: Problems 5.3, 5.4, and 5.5 ask whether the
  sub-Riemannian Heisenberg group admits any Banach embedding with a
  nontrivial Bochner-differentiable map/velocity, and in particular whether
  one can embed it so that one horizontal line is a literal vector line.
- Packet status: `full_solution_likely_valid`.
- Packet path:
  `runs/fa_banach_001/solutions/full/2307.10857_heisenberg_horizontal_line_embedding/`.

## Result

Problem 5.5 has an affirmative answer. Let `L` be the horizontal line
`ell(s)=(s+0i,0)` in the Heisenberg group. There is a Banach space
`V=R \oplus_\infty ell^\infty` and a bi-Lipschitz embedding
`I:H->V` such that

```text
I(ell(s)) = s v
```

for all real `s`, where `v=(1,0)`.

The construction is general: if a metric space contains an isometric copy of
`R` that is the image of a 1-Lipschitz retraction, subtract the Kuratowski
embedding of the retracted point from the Kuratowski embedding of the point.
The extra coordinates vanish on the line but still separate the whole metric
space up to a factor of 2.

## Consequences

- Problem 5.5 is answered yes.
- Problem 5.4 is answered yes: the horizontal velocity at the identity is
  nonzero and differentiates to `v` under this embedding.
- Problem 5.3 is answered yes: for any bounded Euclidean domain, the map
  `x -> ell(x_1)` is nonconstant and its embedded image has constant Bochner
  partial derivative in the first coordinate and zero derivatives in the
  others.

This does not contradict the source's main theorem, which says that no
embedding makes all Lipschitz maps into a Cheeger fractal have Bochner partial
derivatives.

## Evidence And Verification

- `source_paper.pdf` is the source arXiv PDF.
- `figures/problems_5_3_to_5_5_crop.png` shows the source Problems 5.3-5.5 on
  PDF page 5.
- `code/make_problem_crop.py` regenerates the crop using PyMuPDF.
- `solution_packet.pdf` is built from `main.tex`.

## Novelty Check

The cheap run indexes were searched for `2307.10857`, the paper title,
Bochner partial derivatives, Cheeger-Kleiner differentiability,
`iota`-Radon-Nikodym, nonzero velocity, and the exact Problem 5.5 horizontal
line phrase. No prior packet, attempt, or proof-gap answered this target.
Local full-source fixed-string searches found only the source questions
themselves. A bounded web search on 2026-07-01 for the exact horizontal-line
formula and the source title with "single vector" did not surface a later
answer.

## Human Review Focus

Check the convention for the standard Carnot-Caratheodory metric: the
coordinate retraction `(z,t)->(Re z+0i,0)` must be 1-Lipschitz. Under the usual
normalization this follows immediately from length control of horizontal
curves, and the rest of the proof is metric.
