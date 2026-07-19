# Counterexample Packet: Nonunital `K(X)` Cannot Be a Calkin Algebra

Run: `fa_banach_001`

Status: `counterexample_likely_valid` to the final non-unitized question in arXiv:2403.04137, Section 7, page 22.

## Source

Pavlos Motakis and Daniele Puglisi, *The compact operators on `c_0` as a Calkin algebra*, arXiv:2403.04137.

The source asks Problem 3:

> Is the unitization of `K(ell_2)` isomorphic as a Banach algebra to the Calkin algebra of some Banach space?

It then adds:

> More generally, if `X` is a Banach space with a shrinking Schauder basis, is `K(X)` isomorphic to the Calkin algebra of some Banach space?

## Answer As Written

The final non-unitized question has a negative answer. Take `X = ell_2`.
It has a shrinking Schauder basis and is infinite-dimensional, so `K(ell_2)`
has no multiplicative identity. Every nonzero Calkin algebra
`L(Y)/K(Y)` is unital, with identity `I_Y + K(Y)`. If a Banach algebra is
isomorphic to a unital algebra, then it is itself unital, by pulling back the
identity. Hence `K(ell_2)` is not isomorphic as an algebra to any nonzero
Calkin algebra.

The same argument works for every infinite-dimensional Banach space `X`: if
`K(X)` had an identity, it would be `I_X`, forcing `I_X` to be compact, hence
`X` finite-dimensional.

## Scope And Caveat

This packet does **not** answer the preceding unitized problem for
`K(ell_2)`, and it does not answer the likely intended unitized generalization
for spaces with shrinking bases. It records a literal obstruction to the final
sentence as written.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source statement.
- `code/make_evidence_crop.py`: reproduces the crop.

Ledger:
`runs/fa_banach_001/ledger/results/2403.04137_kx_nonunital_calkin_obstruction.json`.

## Novelty Check

Cheap run indexes were searched for `2403.04137`, the source title, `K(ell_2)`,
`unitization`, `shrinking Schauder basis`, `nonunital`, and Calkin keywords.
Web searches on 2026-06-20 for the exact source phrase and close variants found
only the source paper / unrelated Calkin material, not this recorded literal
obstruction. The novelty confidence is limited because this is an elementary
wording-level obstruction and may reflect a typo in the source's final sentence.
