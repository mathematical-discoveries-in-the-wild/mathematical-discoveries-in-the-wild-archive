# ALUR Universality Reduction for Generating Operators

Status: `partial_result_likely_valid`

Source paper: V. Kadets, M. Martin, J. Meri, and A. Quero, *Generating
operators between Banach spaces*, arXiv:2306.02645.

## Result

The source asks whether, for a cardinal `Gamma`, there is a Banach space
`Y` with `dens(Y)=Gamma` such that `Gen(X,Y)` is nonempty for every Banach
space `X` with `dens(X) <= Gamma`.

This packet proves the following necessary condition:

If such a `Y` exists, then `Y` must contain an isometric copy of every ALUR
Banach space `X` with `dens(X) <= Gamma`.  In particular, `Y` must contain
isometric copies of all Hilbert spaces `ell_2(kappa)` for `kappa <= Gamma`.

## Proof Idea

The source already proves that when the domain `X` is ALUR, every generating
operator `G:X -> Y` is an isometric embedding.  Therefore a positive solution
to the density-character question cannot use non-isometric generating
operators to bypass universality on the ALUR subcategory.

## Scope

This does not solve the source question.  It records a sharp necessary
condition and blocks a natural escape route: any positive answer is at least
as strong as isometric universality for all ALUR spaces of the same density
bound.

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:2306.02645.

