# Literature-Already-Answered Packet: 1711.01340 Problem 5

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Pavlos Motakis, Daniele Puglisi, Andreas Tolias, *Algebras of diagonal
  operators of the form scalar-plus-compact are Calkin algebras*,
  arXiv:1711.01340.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 47).

Published Problem 5 asks for a Banach space `X` with an unconditional basis not
equivalent to the unit vector basis of `c_0` such that the unitization of `X`
is isomorphic, as a Banach algebra, to a Calkin algebra.

## Supporting Answer Source

- Pavlos Motakis, Anna Pelczar-Barwacz, *Reflexive Calkin algebras*,
  arXiv:2401.18037.
- Local PDF: `supporting_paper_2401.18037.pdf`.
- Evidence images:
  - `figures/supporting_theorem_crop.png` (page 4, Theorem 1.2 and examples).
  - `figures/supporting_problem5_crop.png` (page 13, explicit reference to
    the earlier Problem 5).

## Answer

The problem is answered affirmatively by arXiv:2401.18037.

Take `X = ell_2` with its standard orthonormal basis. This basis is normalized
and `1`-unconditional, and `ell_2` is not isomorphic to `c_0`. Theorem 1.2 of
arXiv:2401.18037 applies to `U = ell_2` and produces a Banach space
`mathfrak{X}_{ell_2}` such that

```text
Cal(mathfrak{X}_{ell_2})
```

is isomorphic, as a Banach algebra, to the unitization of `ell_2` with
coordinate-wise multiplication. Thus `X = ell_2` is the requested witness for
Problem 5 of arXiv:1711.01340.

The supporting paper also explicitly notes that the earlier Problem 5 asked
whether any such spaces beyond `c_0` existed and that this is indeed true by
Theorem 1.2.

## Limitations

- This is a later-literature answer, not an original proof from the run.
- The packet answers only the existential Problem 5 from arXiv:1711.01340.
- It does not answer the broader arXiv:2401.18037 open problem asking whether
  the unitization of every Banach space with a normalized unconditional basis
  and coordinate-wise multiplication is a Calkin algebra.
- The same supporting theorem was already used in the run to answer the
  separate published Problem 1 on reflexive infinite-dimensional Calkin
  algebras; this packet records the distinct published Problem 5 consequence.

## Files

- `README.md`: packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2401.18037.pdf`: later answer source.
- `figures/open_problem_crop.png`: original Problem 5 page image.
- `figures/supporting_theorem_crop.png`: later theorem page image.
- `figures/supporting_problem5_crop.png`: later explicit Problem 5 status image.
- `code/make_evidence_crops.py`: reproduces the evidence crops.
- `tmp/`: local render intermediates.

## Human Review Recommendation

Check that the intended algebra structure is the coordinate-wise multiplication
on `ell_2` and its unitization, and that the problem's existential wording does
not require the constructed Banach space whose Calkin algebra is the
unitization to itself have an unconditional basis.
