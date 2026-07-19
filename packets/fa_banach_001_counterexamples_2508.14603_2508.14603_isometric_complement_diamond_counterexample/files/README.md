# Counterexample Packet: A Complement Need Not Have Isometric Representatives

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2508.14603`
- source paper: Janko Bracic and Marko Kandic, *Similarities of subspace lattices in Banach spaces*
- target passage: PDF page 12, Section 3.3, where the paper singles out the question of whether a complement can consist of isometric operators.

## Claim

The isometric-complement variant has a negative answer, even for a
two-dimensional complex Banach space and the diamond lattice

```text
{0, span(e1), span(e2), X}.
```

There is an algebraic complement of `Grp(Alg(L))` in `Col(L)`, but no
complement whose nontrivial element is an isometry.

## Construction

Take `X = C^2` with norm

```text
||(z,w)|| = max(|z|, |w|, |z + w/2|).
```

Let `M = C e1`, `N = C e2`, and
`L = {0, M, N, X}`. The collineation group consists of the invertible operators
that either preserve both axes or swap them. The subgroup `Grp(Alg(L))` is the
diagonal subgroup, so the quotient is `S_2`, and a non-isometric algebraic
complement is immediate.

If an isometric complement existed, its nontrivial element would be an isometry
swapping `M` and `N`, hence would satisfy

```text
U e1 = a e2,    U e2 = b e1,    |a|=|b|=1.
```

For `x = e1 + (1/8)e2`, the norm is `17/16`, but

```text
||Ux|| = ||(b/8, a)|| <= 1.
```

This contradiction rules out every isometric complement.

## Scope

This answers the source's isometric-complement question in the negative under
its literal generality. It does not settle the broader question of whether
`Grp(Alg(L))` is complemented in `Col(L)` for Volterra nests on `L^p[0,1]`,
`1<p<infinity`.

## Files

- `main.tex`: full counterexample packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2508.14603
- `figures/open_problem_crop.png`: crop of the source question
- `code/make_open_problem_crop.py`: script used to regenerate the crop
- `code/verify_counterexample.py`: exact arithmetic sanity check

## Novelty Check

The run indexes were searched for `2508.14603`, the paper title, subspace
lattice, collineation, similarity, complemented subgroup, isometric complement,
isometric operators, and diamond lattice keywords. No exact packet for this
question was present.

External phrase searches on June 28, 2026 for combinations of `"isometric
complement"`, `"subspace lattice"`, `"collineations"`, and `"Grp(Alg"` did not
locate a published answer. Human review should still treat this as a bounded
novelty check because the source paper is recent.

## Human Review Recommendation

Check the interpretation of the page-12 question. The packet gives a complete
negative answer for arbitrary complex Banach spaces and arbitrary subspace
lattices. If the intended question was only about the later Volterra nests or
about natural Hilbert-space nests, this should be classified as a small
scope-counterexample rather than a resolution of that narrower problem.
