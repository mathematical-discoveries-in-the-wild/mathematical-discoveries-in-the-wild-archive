# Literature-Already-Answered Packet: Reflexive Calkin Algebras

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Pavlos Motakis, Daniele Puglisi, Andreas Tolias, *Algebras of diagonal
  operators of the form scalar-plus-compact are Calkin algebras*,
  arXiv:1711.01340.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 46).

In the final "Remarks and problems" section, Problem 1 asks:

> Does there exist a Banach space the Calkin algebra of which is reflexive
> and infinite dimensional?

## Supporting Answer Source

- Pavlos Motakis, Anna Pelczar-Barwacz, *Reflexive Calkin algebras*,
  arXiv:2401.18037.
- Local PDF: `supporting_paper_2401.18037.pdf`.
- Evidence image: `figures/supporting_answer_crop.png` (page 1 abstract).

## Status

The 1711.01340 problem is already answered affirmatively by arXiv:2401.18037.

The supporting paper proves that for every Banach space `U` with a normalized
`1`-unconditional basis and no `c_0` asymptotic version, there is a Banach
space `X_U` such that

```text
Cal(X_U) is isomorphic, as a Banach algebra, to the unitization of U
with coordinate-wise multiplication.
```

Taking `U = ell_2` gives an infinite-dimensional reflexive Banach algebra, so
the resulting Calkin algebra is reflexive and infinite dimensional. The
supporting abstract states this explicitly, saying that `Cal(X)` can be
infinite-dimensional reflexive, even isomorphic to a Hilbert space.

## Limitations

- This is not an original proof from the run.
- The packet records an exact later-literature status answer to Problem 1 of
  arXiv:1711.01340 only.
- Other problems in the same 1711.01340 "Remarks and problems" section, such
  as the diagonal-plus-compact unconditional-basis problem and uncountable
  `C(K)` Calkin-algebra problem, are not claimed here.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2401.18037.pdf`: later answer source.
- `figures/open_problem_crop.png`: original problem page image.
- `figures/supporting_answer_crop.png`: supporting abstract page image.
- `tmp/`: local render intermediates.

## Human Review Recommendation

Check that "isomorphic to the unitization of `ell_2` with coordinate-wise
multiplication" is being read only as an isomorphism of Banach algebras, as in
the supporting theorem, and that this is sufficient for the original question,
which asks only for the Calkin algebra to be reflexive and infinite
dimensional as a Banach space.
