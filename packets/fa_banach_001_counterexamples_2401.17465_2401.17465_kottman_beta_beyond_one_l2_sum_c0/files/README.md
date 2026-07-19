# Counterexample: Kottman-domain beta positivity beyond one

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source paper: arXiv:2401.17465, Florent P. Baudier and Gilles Lancien,
*An asymptotic analog of a local-to-global phenomenon for uniformly convex
renormings*.

## Claim

The strengthened Kottman-domain version of the paper's Theorem 1.2 is false.
Let

```text
X = ell_2 \oplus_2 c_0.
```

Then `K(X) >= sqrt(2)`, and the natural norm of `X` satisfies
`\bar beta_X(t) > 0` for every `t in (1, sqrt(2))`. In particular, it has
one-point asymptotic beta positivity at some `t0 in (1,K(X))`.

However, `X` contains a closed copy of `c0`, so it is nonreflexive. Since
property `(beta)` implies reflexivity, `X` cannot admit an equivalent
property-`(beta)` norm.

## Key Mechanism

The `c0` coordinate cannot support infinite unit-ball separated sequences
above scale `1`: in every sequence in `B_{c0}` and for every `c>1`, two terms
are within `c` in sup norm.

Thus, in `ell_2 \oplus_2 c0`, any sequence separated by `t>1` has a pair whose
`c0` parts are closer than `t`, so the remaining separation must appear in the
Hilbert coordinate. A two-point compactness lemma for `H \oplus_2 Z` then
forces at least one of the two midpoints with any fixed `x in B_X` to drop
uniformly below `1`.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of the arXiv source paper.
- `figures/open_problem_crop.png` - crop of the final Kottman-domain question.
- `history/previous_attempt_2401.17465_kottman_domain_beta_extension_probe.md`
  - earlier failed attempt, nested here for audit continuity.

## Novelty Check

The local run indexes were searched for `2401.17465`, `Kottman`,
`pushed beyond 1`, `property beta`, and the earlier attempt slug. No durable
solution or proof-gap packet for this target was found.

Bounded web searches on June 26, 2026 for exact and nearby phrases around
`2401.17465`, `property beta`, `Kottman's constant`, `Rolewicz`, and `c0`
returned the source arXiv page and no explicit later answer to this question.

## Human Review

Likely valid. Please audit the two-point Hilbert-sum midpoint lemma and confirm
that the source's informal "pushed beyond 1" question is intended to include
the natural formulation "some `t0 in (1,K(X))`".
