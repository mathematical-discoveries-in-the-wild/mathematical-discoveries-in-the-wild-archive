# Partial Packet: Complemented ell_p Subspaces Give Singular Extensions

Run: `fa_banach_001`

Status: `partial_result_likely_valid`

## Source Problem

- Spiros A. Argyros, Antonis Manoussakis, and Pavlos Motakis,
  *The HI extension of the standard HI spaces*, arXiv:2407.20030.
- Source location: PDF page 25, final discussion, Definition 10.1 and
  Problem 3; parsed source
  `data/parsed/arxiv_sources/2407.20030/source.tex`, lines 2026--2037.

W. B. Johnson's problem asks whether every infinite-dimensional separable
Banach space not isomorphic to `c_0` admits a singular extension, meaning a
superspace `Y` with `Y/X` infinite dimensional and quotient map strictly
singular.

## Result

The packet proves a permanence lemma:

If `X` contains a complemented subspace `E` that admits a singular extension,
then `X` admits a singular extension.

Using the Kalton-Peck singular extension `Z_p` of `ell_p`, this gives a
positive answer to Johnson's problem for every separable Banach space that
contains a complemented copy of `ell_p` for some `1 < p < infinity`.

## Proof Mechanism

Write `X = E \oplus F`. If

```text
0 -> E -> Z -> V -> 0
```

is a singular extension, form `Y = Z \oplus F` and embed
`X = E \oplus F` into `Y`. The quotient `Y/X` is naturally `V`. If the new
quotient map fixed an infinite-dimensional subspace of `Y`, projecting that
subspace onto `Z` would give an infinite-dimensional subspace on which the
old quotient map is bounded below, contradicting singularity.

## Scope

This is a complemented-subspace partial result. It does not settle Johnson's
problem for arbitrary separable Banach spaces not isomorphic to `c_0`, and it
does not settle Pelczynski's HI-extension problem.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source crop containing Problems 1--3 and
  Johnson's singular-extension formulation.

## Verification

The proof is analytic. The packet was compiled with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The resulting PDF was rendered to PNG and visually inspected.
