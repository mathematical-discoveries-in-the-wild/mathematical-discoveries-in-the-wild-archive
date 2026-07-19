# Finite-dimensional Banach spaces have Property (P)

Status: full answer to the finite-dimensional part of the source question,
likely valid.

Source target: arXiv:2407.07490, Debmalya Sain, Arpita Mal, Kalidas Mandal
and Kallol Paul, *On uniform Bishop-Phelps-Bollobas type approximations of
linear operators and preservation of geometric properties*.

The source paper asks:

> Is it true that each finite-dimensional Banach space X satisfies Property
> (P)? What about the infinite-dimensional case?

This packet proves the first sentence in full:

> Every finite-dimensional real Banach space satisfies Property (P).

The second sentence, the infinite-dimensional case, is not settled by this
packet. The proof is inherently finite-dimensional, using compactness of the
operator unit ball and the isometry group.

## What changed from the previous partial packet

The previous packet proved the smooth finite-dimensional case using the unique
duality map `j(x)`. The full finite-dimensional proof replaces `j(x)` by the
whole supporting-functional set

```text
J(x) = { f in S_{X*} : f(x) = 1 }.
```

If Property (P) failed, nearest-isometry normalization would give contractions
`B_n = I + t_n C_n` with dense norm-attainment sets and `C_n -> C`.
Contractivity gives `f(Cx) <= 0` for every `f in J(x)`. Dense exact
norm-attainment near `x` gives one limiting support `g in J(x)` with
`g(Cx) >= 0`. Hence

```text
max_{f in J(x)} f(Cx) = 0     for every x in S_X.
```

This says the right directional derivative of the norm along the flow
`e^{tC}` is zero at every nonzero point. Therefore `e^{tC}` is an isometry
for `t >= 0`, contradicting the nearest-isometry choice.

## Files

- `main.tex` - self-contained proof packet.
- `solution_packet.pdf` - compiled human-readable packet.
- `source_paper.pdf` - local copy of the source paper.
- `figures/open_problem_crop.png` - crop of the source open question.
- `history/packets/partial_packet_2407.07490_smooth_finite_dim_property_p_2026_06_21/` -
  previous smooth finite-dimensional partial packet moved out of the live
  partial index and preserved as history.
- `history/absorbed_packets/2407.07490_smooth_finite_dim_property_p/` -
  earlier absorbed copy of the same predecessor packet.

## Remaining open

- The infinite-dimensional part of the source question.
- Potential complex-field variants if one does not pass through the underlying
  real Banach space. The source paper assumes real scalars throughout.
