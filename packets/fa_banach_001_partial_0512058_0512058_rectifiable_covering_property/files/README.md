# Partial solution packet: rectifiable covering property

## Source

- Paper: Emanuel Milman, *Generalized Intersection Bodies*
- arXiv: `math/0512058`
- Source location: Covering Property Conjecture, Section 5, page 37 of the
  arXiv PDF.

## Classification

- Status: `partial_result_likely_valid`
- Result type: partial positive answer / geometric-measure reduction.
- Scope: the Covering Property Conjecture for compact finite
  `k`-rectifiable covering sets in `G(n,n-k)`.

## Result

Let `m = n-k`. Suppose `Z` is a compact countably `k`-rectifiable subset of
`G(n,m)` with finite `H^k` measure and

```text
union_{E in Z} (E cap S^{n-1}) = S^{n-1}.
```

Then a scalar multiple of `H^k|_Z` is a finite positive measure supported on
`Z` and satisfies

```text
R_m^*(mu) >= 1.
```

Thus Milman's covering-property conjecture is true once the covering family is
finite `k`-rectifiable. This matches the source paper's suggested Hausdorff
measure route and reduces the remaining obstruction to proving rectifiability
and finite `H^k` measure for minimal covers.

## Proof Idea

Consider the incidence set

```text
Sigma_Z = {(E, theta) : E in Z, theta in E cap S^{n-1}}.
```

If `Z` is `k`-rectifiable, then `Sigma_Z` is `(n-1)`-rectifiable because each
fiber has dimension `m-1 = n-k-1`. The projection
`pi(E,theta)=theta` maps `Sigma_Z` onto the whole sphere. By the area formula,
almost every point of the sphere has a preimage at which the approximate
Jacobian of `pi` is positive. Since `pi` is a fixed smooth projection on the
compact incidence bundle, that Jacobian is uniformly bounded above. Therefore
the pushforward of `H^k|_Z` times the fiber measure has density bounded below
by a positive constant. But this pushforward is exactly `R_m^*(H^k|_Z)`.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/covering_property_conjecture_crop.png`: crop of the source
  conjecture and the beginning of Remark 5.12.
- `code/verify_dimension_count.py`: small sanity check for the incidence
  dimension count and the elementary tangent estimate.
- `tmp/pdfs/`: render/build intermediates.

## Limitations

This does not prove the full Covering Property Conjecture for arbitrary closed
covering sets. It proves the conjecture under the natural regularity condition
that the covering set is finite `k`-rectifiable. The `BP_k^n = I_k^n`
equivalence problem from the same source was later answered negatively by
Milman's `math/0701779`; the lower-dimensional Busemann-Petty endpoint and
the linear inclusion questions are not settled here.

