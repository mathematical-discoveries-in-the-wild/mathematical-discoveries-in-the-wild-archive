# Counterexample to the high-dimensional slow-epsilon orthogonality hope

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source paper: arXiv:2107.02491, Boris Burshteyn and Alexander Volberg,
*Orthogonality in normed spaces*.

## Claim

The Section 7 open question asks whether, after examples with no exactly
orthogonal high-dimensional subspace, one can still always find subspaces
which are `1 - eps_m` orthogonal for some sequence `eps_m -> 0`.

Under the natural high-dimensional reading suggested by the surrounding text,
namely `dim K_m = dim F_m - dim E_m = m` (and more generally
`dim K_m / log m -> infinity`), the answer is no.

There is a Banach space `X` and finite-dimensional subspaces
`E_m subset F_m subset X` with `dim(F_m/E_m)=m` such that every
`r`-dimensional subspace `K subset F_m` satisfies

```text
inf_{||k||=1, k in K} dist(k,E_m) <= C sqrt(log m / r).
```

In particular every `m`-dimensional `K subset F_m` has orthogonality constant
at most `C sqrt(log m / m)`, which tends to `0`, not to `1`.

## Key mechanism

The quotient map `q_m:F_m -> F_m/E_m` converts a lower distance bound
`dist(k,E_m) >= alpha ||k||` on `K` into an isomorphism from `K` onto its image
with distortion at most `1/alpha`.

We choose `F_m = ell_infty^{N_m}` and choose `E_m` so that the quotient
`F_m/E_m` is uniformly Hilbertian, using Kashin's Euclidean subspace theorem
for `ell_1^{O(m)}` and duality. Then a highly orthogonal `K` would force an
`r`-dimensional subspace of `ell_infty^{N_m}` to be very close to Hilbert.

But an elementary spherical-cap argument gives
`d(K,ell_2^r) >= c sqrt(r/log N_m)` for every
`K subset ell_infty^{N_m}`. Combining the two estimates gives the displayed
upper bound on the possible orthogonality constant.

## Interpretation caveat

The literal phrase "any subspace `K_m`" in the source's bookkeeping paragraph
cannot mean dimension-free subspaces: by the paper's Theorem 5.1
(Krein-Krasnoselski-Milman/Borsuk-Ulam), a one-dimensional exactly orthogonal
subspace always exists when `dim E < dim F`.

This packet therefore addresses the nontrivial high-dimensional interpretation
made explicit elsewhere in the source, especially the cases
`dim K = dim F - dim E` and high-dimensional `K`.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_question_crop.png` - crop of the Section 7 open question.
- `code/crop_open_question.py` - script used to create the crop.

## Novelty check

Before promotion, the run indexes were searched for `2107.02491`,
`Orthogonality in normed spaces`, `slowly going to zero`, `K_m`, and
`finitely strictly singular lambda-adjusted`. No existing packet for this
paper or this high-dimensional slow-epsilon question was found.

Web searches for exact phrases including `"2107.02491" "slowly going to zero"`,
`"Orthogonality in normed spaces" "K_m"`, and variants around
`"finitely strictly singular" "lambda-adjusted"` found the source paper and
related orthogonality papers, but no explicit later solution of the Section 7
question. Human review should still check whether this Kashin-duality
construction appears under different terminology in the asymptotic Banach-space
literature.
