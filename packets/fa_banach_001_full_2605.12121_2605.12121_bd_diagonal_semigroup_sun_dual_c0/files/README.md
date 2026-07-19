# Diagonal Semigroup on the Bourgain--Delbaen Space

## Verdict

Candidate full solution, likely valid, to the residual question in Remark 4.15(2)
of Preussler--Schwenninger, arXiv:2605.12121.

The construction meets the strongest natural reading of "non-trivial" suggested
by the source's discussion of the Lotz property: its generator is unbounded.

## Source

- Philip Preussler and Felix L. Schwenninger, *Implications of structured
  continuous maximal regularity*, arXiv:2605.12121v1.
- Exact location: Remark 4.15(2), source page 24.
- Local source: `source_paper.pdf`.
- Evidence: `figures/open_problem_crop.png`.

The source asks whether the classical Bourgain--Delbaen space `Y` admits a
non-trivial `C_0`-semigroup for which the dual of the sun dual contains `c_0`.

## Result

Let `(y_n)` be the normalized Schauder basis of `Y`, with biorthogonal
functionals `(y_n^*)`. Define

```text
T(t)y_n = exp(-nt)y_n,   t >= 0.
```

Abel summation against the uniformly bounded basis projections shows that
`T(t)` is a bounded `C_0`-semigroup. Its generator satisfies
`Ay_n = -n y_n`, so the generator is unbounded.

Every `y_n^*` belongs to the sun dual because

```text
T(t)'y_n^* = exp(-nt)y_n^*.
```

Thus the sun dual is an infinite-dimensional closed subspace of
`Y' isomorphic to ell_1`. A self-contained gliding-hump argument in the packet
proves that every infinite-dimensional subspace of `ell_1` contains a
complemented copy of `ell_1`. Therefore the sun dual contains a complemented
`ell_1`, and its dual contains a complemented `ell_infinity`, hence `c_0`.

The proof actually establishes the following stronger statement: every
infinite-dimensional Banach space with a Schauder basis and dual isomorphic to
`ell_1` admits such a diagonal semigroup.

## Supporting Source

Tarbard, arXiv:1309.7469, verifies the two Bourgain--Delbaen premises used here:
the original spaces have a normalized Schauder basis, and every member of the
class containing the source's space `Y` has dual isomorphic to `ell_1`. A local
copy is included as `supporting_paper_1309.7469.pdf`.

## Novelty Check

On 2026-07-19, the four lightweight run indexes were searched for
`2605.12121`, the paper title, maximal regularity, `iISS`, Bourgain--Delbaen,
sun dual, and Lotz-property terms. No duplicate packet or attempt was found.
Bounded web/arXiv searches used the exact title and combinations of
`Bourgain--Delbaen`, `C_0-semigroup`, `sun dual`, `unbounded generator`, and
`Lotz property`. They found the source paper and background Bourgain--Delbaen
papers, but no later explicit answer. The arXiv record remains v1, submitted
2026-05-12. This is a bounded search and indexes may lag, so novelty confidence
is moderate; mathematical-validity confidence is high.

## Verification

`verification.md` gives the explicit hostile verification report. No
computation is needed. Human review should focus on:

1. the Abel-summation multiplier bound for an arbitrary Schauder basis;
2. the gliding-hump proof of complemented `ell_1` saturation;
3. matching the source's `Y` to Tarbard's Bourgain--Delbaen class `mathcal Y`.

Recommended action: send to a Banach-space/semigroup expert for human review.

