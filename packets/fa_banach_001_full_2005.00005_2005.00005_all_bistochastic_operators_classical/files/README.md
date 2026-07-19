# All bistochastic quantum random-variable operators over `mu I_H` are classical

Status: `candidate_full_solution_likely_valid`

Source paper: Sarah Plosker and Christopher Ramsey, "Bistochastic operators and
quantum random variables", arXiv:2005.00005.

## Source Question

In Section 5, after proving that every classical bistochastic operator on
`L^1(X,mu)` extends entrywise to a bistochastic operator on
`L^1_H(X,mu I_H)`, Plosker--Ramsey write:

> We have no example of a bistochastic operator on `L^1_H(X,mu I_H)` that does
> not arise in this way.

The source passage is line 1088 of `data/parsed/arxiv_sources/2005.00005/source.tex`.

## Result

For every finite measure space `(X,Sigma,mu)` and every finite-dimensional or
separable Hilbert space `H`, every Plosker--Ramsey bistochastic operator on
`L^1_H(X,mu I_H)` is the entrywise extension of a unique classical
bistochastic operator on `L^1(X,mu)`.

Thus the "no example" sentence has a positive answer in the full source-paper
setting `nu = mu I_H`: there are no exotic bistochastic operators.

## Proof Outline

For measurable `E,F`, define

```text
Theta_{F,E}(A) = int_F B(chi_E A) dmu.
```

This is a positive map on `B(H)` dominated by `mu(E) id`. The key infinite-
dimensional lemma proves that the positive order interval `[0, c id]` in
positive maps `B(H)->B(H)` is one-dimensional; hence
`Theta_{F,E}=a(E,F) id`.

The scalars `a(E,F)` define the scalar Markov kernel data of a classical
bistochastic operator `S`. A dominated-localization lemma then avoids any false
infinite-dimensional density step: for fixed `F`, the map
`T_F(f)=int_F Bf dmu` is dominated by `f -> int_X f dmu`, and the rank-one
`P/Q` block inequalities force

```text
T_F(f) = int_X h_F f dmu
```

for all positive quantum random variables `f`, not only bounded/simple ones.
This gives all matrix coefficients of `Bf` as `S` applied to the corresponding
scalar matrix coefficients.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local source-paper PDF.
- `figures/open_problem_crop.png`: crop of the source "no example" passage.
- `history/finite_dimensional_partial_packet/`: superseded finite-dimensional
  packet that led to the full proof.

## Verification and Novelty Check

Local run indexes were searched for `2005.00005`, the title, "bistochastic",
"quantum random variables", "Plosker", "Ramsey", and the exact "no example"
sentence. The only duplicate hit was the finite-dimensional packet now kept in
`history/`.

A bounded web search on 2026-06-21 for the exact source sentence and close
phrases around `L^1_H(X,mu I_H)` and "bistochastic operators and quantum random
variables" found only the source arXiv record or source-paper mirrors, not a
later answer.

Human review should focus on the dominated-localization lemma in the infinite-
dimensional case and on the final identification of equality from all
matrix-coefficient integrals.
