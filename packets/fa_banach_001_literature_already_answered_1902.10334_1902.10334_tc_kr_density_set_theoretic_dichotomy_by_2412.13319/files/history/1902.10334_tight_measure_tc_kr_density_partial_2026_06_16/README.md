# Partial Packet: TC/KR Density for Tight Measures on Arbitrary Metric Spaces

Run: `fa_banach_001`

Result type: `partial`

## Source Problem

- Sofiya Ostrovska and Mikhail I. Ostrovskii,
  *Generalized transportation cost spaces*, arXiv:1902.10334.
- Local PDF: `source_paper.pdf`.
- Source location: PDF page 11, Remark 1.14; parsed source
  `data/parsed/arxiv_sources/1902.10334/source.tex`, lines 680--746.

The source proves Theorem 1.13 for Polish metric spaces: finitely supported
transportation problems are dense in the Kantorovich-Rubinstein measure space.
Remark 1.14 says the authors do not know how to prove an analogue for general
metric spaces.

## Partial Result

The packet proves the analogue for arbitrary metric spaces under the added
assumption that the finite Borel measures under consideration are tight and
have finite first moment. This includes all finite Radon measures and recovers
the compactness input that the Polish proof obtained from Ulam's theorem.

The proof also records why the KR dual norm is still the Lipschitz-dual norm
for tight measures: tightness concentrates the two measures on a separable
sigma-compact subspace, and the usual Polish duality applies after passing to
the completion.

## Scope

This is not a full solution of Remark 1.14. It leaves open the genuinely
non-tight/general Borel-measure case on arbitrary metric spaces.

## Files

- `main.tex`: full partial theorem proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: page-11 source crop containing Remark 1.14.

## Verification

- The proof is analytic and does not use computational checks.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  was used to render the packet.
- Bounded search checked the run indexes for `1902.10334`, TC/KR,
  transportation cost, tight measures, and general metric spaces. Web searches
  for close phrases around `Kantorovich-Rubinstein tight measures arbitrary
  metric space` found standard KR-duality references but no exact packet or
  exact answer to this source remark during this loop.

## Human Review Recommendation

Check that the separable-support reduction justifies KR duality for tight
measures, and that the compact approximation proof is exactly the Polish proof
with tightness replacing Ulam's theorem.
