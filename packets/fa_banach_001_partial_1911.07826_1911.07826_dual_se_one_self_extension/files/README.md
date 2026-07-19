# Bidual-Complemented Spaces With `se(X)=1` Have the Self-Extension Property

Status: `partial_result_likely_valid`

Source:

- Juan Bosco Garcia-Gutierrez, Francisco Javier Garcia Pacheco, Paula Piniella, and Fernando Rambla-Barreno, "Non-Hilbert Banach spaces with the self-extension property", arXiv:1911.07826.
- Source location: final open questions after Corollary 5.4 / source TeX line 453; PDF page 11.
- Local source PDF: `source_paper.pdf`.
- Source crop: `figures/open_problem_crop.png`.

## Result

The source asks whether the equality `se(X)=1` implies that `X` has the
self-extension property. This packet proves an affirmative answer for every
Banach space that is 1-complemented in its bidual.

Precisely, if there is a norm-one projection `P:X** -> X` whose restriction to
the canonical copy of `X` is the identity, and if `se(X)=1`, then every bounded
operator `T:Y -> Y` on a subspace `Y` of `X` has an extension `S:X -> X` with
`||S||=||T||`. Therefore `X` has the self-extension property.

In particular, this applies to all dual Banach spaces, because if `X=E^*` then
restriction from `E***` to `E` is a norm-one projection from `X**=E***` onto
`X=E^*`.

## Proof Idea

For a fixed `Y` and `T`, the condition `se(X)=1` gives extensions whose norms
are at most `(1+epsilon)||T||`. In arbitrary `X`, a pointwise weak-star compactness
argument in `X**` gives an exact norm-preserving extension `R:X -> X**`. If `X`
is 1-complemented in `X**`, composing `R` with the norm-one projection
`P:X** -> X` returns an `X`-valued extension without increasing the norm. The
reverse inequality comes from restriction to `Y`.

## Novelty Check

Cheap run indexes had no exact row for arXiv:1911.07826. Local searches for
`self-extension property`, `self-extension coefficient`, `se(X)=1`,
`k-self-extensible`, and the source title found only this source paper and
unrelated/self-extension uses. Web searches for the same phrases, including
dual and reflexive variants, likewise found the source paper and the 1998
Lyapunov/self-extension precursor, but no exact statement that the `se(X)=1`
question is answered for dual or bidual-complemented Banach spaces.

## Human Review Recommendation

Check the compactness passage: the pointwise weak-star subnet is taken in
`prod_{x in X} C||x|| B_{X**}`, and the sequence index tends to infinity along
the subnet, so the final norm bound is exactly `||T||`. The remaining step uses
only the norm-one projection `X** -> X`. The result does not answer the source
question for arbitrary Banach spaces that are not known to be contractively
complemented in their bidual, nor the separate questions about hyperplanes or
existence of spaces with `se(X)=infty`.
