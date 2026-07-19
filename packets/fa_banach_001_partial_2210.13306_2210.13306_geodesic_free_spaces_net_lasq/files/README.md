# Partial Solution Packet: Geodesic Lipschitz-Free Spaces Satisfy the Net-LASQ Conclusion

## Status

`partial_result_likely_valid`

This packet proves a solved subcase of Question 2.3 from arXiv:2210.13306.  The
source asks whether every LASQ Banach space has the weakly-null-net conclusion
proved there for positive LASQ Banach lattices.  We prove that the conclusion
holds for every Lipschitz-free space over a geodesic metric space.

This is not a full solution for arbitrary LASQ Banach spaces, and it does not
settle the non-geodesic length-space examples that separate LASQ from WASQ.

## Source Question

Source paper:

- Stefano Ciaci, *Locally almost square Banach lattices*, arXiv:2210.13306.

Question 2.3 asks whether, if a Banach space `X` is LASQ, then for every
`y in S_X` there exists a weakly null net `(x_alpha)` in `X` such that

```text
||x_alpha|| -> 1,   ||y + x_alpha|| -> 1,   ||y - x_alpha|| -> 1.
```

## Result Proved Here

Let `M` be a geodesic metric space.  Then for every `y in S_{F(M)}` there is a
weakly null net `(mu_alpha)` in `F(M)` such that

```text
||mu_alpha|| -> 1,   ||y + mu_alpha|| -> 1,   ||y - mu_alpha|| -> 1.
```

The proof uses the finite-support geodesic theorem of Kaasik--Veeorg
(arXiv:2210.09158): for every finite-support unit vector in `F(M)`, a
weakly-null square sequence exists.  The new observation is an abstract density
lemma: pointwise weakly-null square sequences on a dense subset of the sphere
promote to weakly-null square nets at every sphere point.

## Why This Matters

The sequence version is much harder because moving from finite-support vectors
to all vectors requires one sequence to satisfy all functionals at once.  Nets
avoid that diagonal bottleneck: for each finite weak neighborhood and tolerance,
one may approximate the target point by a good dense point and then move far
enough along its sequence.

Thus the packet explains why the geodesic finite-support theorem already gives
the exact net-form conclusion requested in arXiv:2210.13306 for the geodesic
Lipschitz-free subcase.

## Novelty / Duplicate Check

Checked the run indexes for `2210.13306`, `locally almost square`, `LASQ`,
`weakly null net`, and related terms.  No existing packet for this exact
geodesic-free-space net promotion was found.  The nearby packet
`2301.07943_source_norm_not_lasq` concerns the different LASQ-versus-D2P
problem.

Local source search found arXiv:2210.09158's finite-support geodesic result but
no all-point net promotion.  Web exact-phrase searches for `"weakly null net"
"LASQ"` and close variants did not reveal a separate answer.

## Files

- `main.tex` - self-contained proof note.
- `solution_packet.pdf` - compiled packet.
- `source_paper.pdf` - arXiv:2210.13306.
- `supporting_paper_2210.09158.pdf` - Kaasik--Veeorg finite-support theorem.

## Human Review Recommendation

Review as a likely valid partial result.  The main points to check are:

1. The density lemma's directed-net construction.
2. The use of finite-support density in Lipschitz-free spaces.
3. The citation scope of Kaasik--Veeorg's geodesic finite-support proposition.

