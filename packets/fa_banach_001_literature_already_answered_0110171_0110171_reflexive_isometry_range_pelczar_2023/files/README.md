# Literature Status: Reflexive Isometry Range Need Not Be 1-Complemented

- status: literature_already_answered
- source arXiv: math/0110171
- source paper: Beata Randrianantoanina, *Norm One Projections in Banach Spaces*
- supporting arXiv: 2309.15261
- supporting paper: Anna Pelczar-Barwacz, *A reflexive Banach space with an uncomplemented isometric subspace*
- packet path: `runs/fa_banach_001/solutions/literature_already_answered/0110171_reflexive_isometry_range_pelczar_2023/`

## Source Question

In Section `Relations with isometries`, Question `qisometry`, the survey asks:

> Let `X` be a Banach space and `T:X -> X` be an isometry. Is the range
> `T(X)` 1-complemented in `X`?

The survey notes that the general Banach-space question is already negative
for `C[0,1]`, but says that the reflexive case remained open: it was not known
whether every isometry in a reflexive Banach space is a Wold isometry, and
hence whether the range must be 1-complemented.

## Supporting Answer

Pelczar-Barwacz, arXiv:2309.15261, Theorem 0.1 constructs a reflexive Banach
space `X` with a basis `(e_i)` such that the map `e_i -> e_{2i}` extends to an
isometry from `X` onto `Y = closure(span{e_{2i}: i in N})`, while `Y` is not
complemented in `X`. In particular `Y` is not 1-complemented.

Thus the inclusion of this isometric copy gives an isometry on a reflexive
Banach space whose range is not 1-complemented. This negatively answers the
reflexive version that the 2001 survey identified as open.

## Provenance

This is not an original partial result. The decisive theorem is the later
Pelczar-Barwacz construction. A 2024 paper, arXiv:2407.15112, explicitly points
out the same implication and cites the survey's Section 5.g as related
background, confirming that the literature knows this connection.

## Files

- `source_paper.pdf`: original survey, arXiv math/0110171.
- `supporting_paper_2309.15261.pdf`: supporting paper, arXiv:2309.15261.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
