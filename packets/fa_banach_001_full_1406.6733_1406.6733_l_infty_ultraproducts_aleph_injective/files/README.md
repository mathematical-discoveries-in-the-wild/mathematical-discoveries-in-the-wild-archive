# Full Solution Packet: `L_infty` Ultraproducts Over Good Ultrafilters Are `aleph`-Injective

- status: candidate full solution, likely valid
- run: `fa_banach_001`
- source arXiv id: `1406.6733`
- source paper: Antonio Aviles, Felix Cabello Sanchez, Jesus M. F. Castillo, Manuel Gonzalez, and Yolanda Moreno, *Aleph-injective Banach spaces and Aleph-projective compacta*
- target passage: PDF page 22 / source lines 1790--1792, Open Problem (6).

## Claim

Let `U` be a countably incomplete `aleph`-good ultrafilter and let
`E = [E_i]_U` be an ultraproduct of Banach spaces.  If `E` is an
`L_{infty,lambda}`-space, then `E` is `(lambda,aleph)`-injective.
Consequently, if `E` is an `L_infty`-space, then `E` is `aleph`-injective.

This gives an affirmative answer to Open Problem (6) of Aviles--Cabello
Sanchez--Castillo--Gonzalez--Moreno.

## Method

The source paper proves the needed saturation fact: for a countably incomplete
`aleph`-good ultrafilter, fewer than `aleph` internal sets in a set-theoretic
ultraproduct with the finite intersection property have nonempty intersection.

The missing step is to use the `L_infty` hypothesis at finite level.  If `E`
is `L_{infty,lambda}`, then every operator from a subspace of a finite
dimensional Banach space into `E` extends to the whole finite dimensional
space with norm at most `lambda` times the original norm.  This follows by
putting the finite-dimensional range inside a finite-dimensional piece of `E`
that is `lambda`-isomorphic to some `ell_infty^n`, extending there by the
injectivity of `ell_infty^n`, and returning to `E`.

For a domain `X` of density `< aleph`, choose a rational dense subspace `D`
and encode the desired extension on `D` as fewer than `aleph` linearity,
agreement, and norm constraints.  Every finite subset of these constraints is
satisfied by the finite-dimensional extension step.  Good-ultrafilter
saturation realizes all constraints simultaneously inside the ultraproduct,
yielding a bounded extension on `D`, hence on `X`.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1406.6733
- `figures/open_problem_crop.png`: crop of Open Problems (5)--(6)

## Novelty Check

The run indexes were searched for `1406.6733`, `aleph-injective`,
`aleph-good`, `good ultrafilter`, `countably incomplete`, `L_infty
ultraproduct`, and related phrases.  No existing packet or attempt addresses
Open Problem (6).

External web searches on 2026-06-19 for exact phrases around `aleph-good`
ultrafilters, `L_infty` ultraproducts, and `aleph`-injectivity found the source
paper and the earlier separably-injective paper arXiv:1103.6064, but no later
paper explicitly resolving this higher-cardinal problem.

Human review should focus on the set-theoretic saturation coding: the proof
uses internal sets of coordinatewise candidate maps from a fixed rational
dense subspace into the factor spaces.  The finite satisfiability reduction is
ordinary finite-dimensional `L_infty` extension.
