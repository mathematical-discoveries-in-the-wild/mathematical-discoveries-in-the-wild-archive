# Compact ordered spaces give C(K,p) BFPP failure

Status: likely valid partial result, pending human review.

Source paper: Antonio Aviles, Maria Japon, Christopher Lennard, Gonzalo
Martinez-Cervantes, Adam Stawski, "The ball fixed point property in spaces of
continuous functions", arXiv:2506.17995.

Question addressed: final Question (i) asks whether there exists an infinite
compact space `K` and a non-isolated point `p in K` such that

```text
C(K,p) = {f in C(K): f(p)=0}
```

has the ball fixed point property.

Partial result:

If `K` is a compact linearly ordered topological space and `p` is non-isolated,
then `C(K,p)` fails BFPP.

The proof chooses a closed one-sided ordinal skeleton `F` converging to `p`.
The usual ordinal shift gives a fixed-point-free nonexpansive map on
`C(F,p)`.  For compact ordered spaces, restriction `C(K,p) -> C(F,p)` has a
norm-one linear right inverse, obtained by interpolating over the convex
components of `K \ F`.  Composing the bad ordinal map with restriction and
extension gives a bad map on `C(K,p)`.

Scope:

This extends the previous ordinal compact packet from ordinal spaces to all
compact ordered spaces, including connected ordered compacta and long-line
type examples.  It does not settle arbitrary compact Hausdorff spaces with
non-isolated `P`-points, because the proof uses the order to get both the
closed ordinal skeleton and the norm-one interpolation extension.

Files:

- `main.tex`: full write-up.
- `solution_packet.pdf`: rendered partial-result packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_question_i_crop.png`: crop of the source final questions.

Human review recommendation:

Check the ordered interpolation extension lemma, especially continuity at
points of `F` that are limits of many convex gaps.  The transfer from the
ordinal skeleton is then formal.
