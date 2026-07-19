# Clopen ordinal towers give C(K,p) BFPP failure

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

If `p` admits a continuous well-ordered clopen neighborhood tower
`(U_alpha)_{alpha<kappa}` with `U_0=K`, intersection `{p}`, and nonempty
annuli `A_alpha=U_alpha \ U_{alpha+1}`, then `C(K,p)` fails BFPP.

The fixed-point-free map samples one point `x_alpha` in each annulus.  It puts
the value `1` on `A_0`, shifts sampled values forward on successor annuli, and
puts the ordinal limsup of previous sampled values on limit annuli.  This gives
a nonexpansive self-map of the unit ball.  A fixed point would force all sampled
values to be `1`, contradicting continuity at `p`.

Scope:

This strengthens the lane-15 ordinal compact partial in a different direction:
it gives an abstract P-point/tower mechanism.  It does not settle arbitrary
non-isolated P-points, because such points need not admit a well-ordered
clopen tower base.

Files:

- `main.tex`: full write-up.
- `solution_packet.pdf`: rendered partial-result packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_question_i_crop.png`: crop of the source final questions.

Human review recommendation:

Check the continuity of the annulus-constant map at `p` and the use of
`limsup_{alpha -> lambda}` at limit annuli.  Those are the main proof points.
