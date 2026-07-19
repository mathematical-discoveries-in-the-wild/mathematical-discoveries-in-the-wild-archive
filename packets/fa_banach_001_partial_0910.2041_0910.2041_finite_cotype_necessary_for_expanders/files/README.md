# Partial Packet: Finite Cotype is Necessary for Nonlinear Expander Families

Run: `fa_banach_001`

Status: `partial_result_likely_valid`

## Source Problem

- Manor Mendel and Assaf Naor,
  *Towards a calculus for non-linear spectral gaps*,
  arXiv:0910.2041.
- Source location: PDF page 20; parsed source
  `data/parsed/arxiv_sources/0910.2041/zigzag-arxiv-v1.tex`, lines 1238--1247.

The source asks for geometric conditions on metric spaces that admit expander
families with respect to those spaces. It says that, for normed spaces, it is
tempting to conjecture that having such an expander is equivalent to finite
cotype.

## Result

The packet proves the necessary direction for Banach spaces:

If a Banach space `X` admits a bounded-degree graph family with unbounded
cardinality and uniformly bounded nonlinear Poincare constants with respect to
`||.||_X^2`, then `X` has finite cotype.

Equivalently, if `X` has no finite cotype, then no bounded-degree graph family
of unbounded size can be an expander family with respect to `X`.

## Proof Mechanism

By the Maurey-Pisier theorem, if `X` has no finite cotype then the spaces
`ell_infty^n` embed into `X` with uniformly bounded distortion for all `n`.
Every `n`-vertex graph embeds isometrically into `ell_infty^n` via the
distance-coordinate map. For bounded-degree graphs, average graph distance is
at least a constant multiple of `log n`, while every edge has length one.
Testing the nonlinear Poincare inequality on this embedding forces the
Poincare constant to grow like `(log n)^2`.

## Scope

This does not prove the converse finite-cotype direction. It records that the
finite-cotype condition in the source conjecture is genuinely necessary.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source crop containing the conjectural
  finite-cotype equivalence.

## Verification

The proof is analytic. The packet was compiled with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The resulting PDF was rendered to PNG and visually inspected.

