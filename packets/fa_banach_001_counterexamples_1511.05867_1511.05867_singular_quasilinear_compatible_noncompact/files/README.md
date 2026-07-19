# Counterexample Packet: Compatible Operators Need Not Differ Compactly

Run: `fa_banach_001`

Result type: `counterexample_likely_valid`

## Source Problem

- Jesus M. F. Castillo, Wilson Cuellar, Valentin Ferenczi, Yolanda Moreno,
  *Complex structures on twisted Hilbert spaces*, arXiv:1511.05867.
- Source location: page 22, Problem 3.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

Problem 3 asks whether, for an arbitrary singular quasi-linear map
`Omega: ell_2 -> ell_2`, compatibility of bounded operators `(T,U)` with
`Omega` forces `T-U` to be compact.

## Counterexample

The answer is negative as stated. Let `K: ell_2 -> ell_2` be the Kalton-Peck
quasi-linear map, which is singular. Embed its range into the even-coordinate
copy of `ell_2`: set `Omega = J K`, where `J e_n = e_{2n}`. Let `T` be the
projection onto the odd-coordinate copy of `ell_2`, and let `U=0`.

Then `T Omega = 0 = Omega U`, so `(T,U)` is compatible with `Omega`. But
`T-U=T` is an infinite-rank coordinate projection, hence not compact.

The map `Omega` is still singular: if `Omega` were trivial on an
infinite-dimensional subspace, applying the bounded left inverse of `J` would
make the Kalton-Peck map trivial on that same subspace.

## Scope

This packet answers only Problem 3 in its arbitrary singular quasi-linear-map
form. It does not answer the subsequent source problems about:

- exact sequences `0 -> H -> Z_2 -> H -> 0`;
- singular centralizers on `ell_2`;
- compatible complex structures on hyperplanes of `d_Omega ell_2`;
- uniqueness of the complex structure on `Z_2`.

## Novelty Check

Before promotion, cheap run indexes were searched for `1511.05867`,
`Complex structures on twisted Hilbert spaces`, `singular quasi-linear`,
`compatible`, `T-U compact`, `Kalton-Peck`, and related phrases. No exact
packet for this arXiv id or this counterexample was found.

Bounded web searches on 2026-07-03 for exact phrases including
`"singular quasi-linear map" "T-U" compact compatible`, `"Complex structures
on twisted Hilbert spaces" "singular quasi-linear map"`, and `"Kalton-Peck"
"compatible" "T-U" compact` found no later resolution or duplicate of this
specific observation.

## Files

- `README.md`: this summary.
- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of Problem 3.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Check that the source's use of "singular quasi-linear map" matches the standard
nontrivial-on-every-infinite-dimensional-subspace definition. Under that
standard definition, the counterexample is immediate and should be accepted as
a negative answer to Problem 3 as stated.
