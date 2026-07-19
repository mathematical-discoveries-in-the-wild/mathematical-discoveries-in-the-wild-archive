# Literature-implied partial classification: the no-`c0` case

## Status

`literature_implied_answer (large structural subcase)`.

Le Merdy asks in `arXiv:1003.1587`:

> When `X` does not have property `(alpha)`, characterize bounded invertible
> operators `T:X -> X` such that `k in Z -> T^k` extends to a bounded
> homomorphism `C(T) -> B(X)`.

For the large subcase where `X` contains no copy of `c0`, the answer is:

> `T` has such an extension if and only if `sigma(T) subset T` and `T` is a
> scalar-type spectral operator.

This applies in particular to many non-`alpha` finite-cotype spaces discussed
near the source question, including Schatten `S^p` for `1 <= p < infinity`,
`p != 2`.

## Identification

The supporting input is Kriegler-Le Merdy, `arXiv:0901.1025`.

- Lemma 3.8: any bounded representation `u:C(K)->B(X)` with
  `T=u(kappa)` factors through `C(sigma(T))`; moreover the induced calculus has
  the spectral mapping property and is an isomorphism onto its range.
- Remark 3.10: such a representation makes `T*` scalar-type of class `X`, and
  `T` is scalar-type spectral exactly when all orbit maps
  `f -> v(f)x` are weakly compact.
- Corollary 3.11: if `X` contains no `c0`, the weak compactness obstruction
  disappears because every bounded map `C(K)->X` is weakly compact.

Adapting the compact set from a sectorial spectrum to `K=sigma(T) subset T`
gives the stated characterization.

## Scope

This is not a full answer to the arbitrary non-property-`(alpha)` problem.
It classifies the no-`c0` subcase. Spaces containing `c0`, and quantitative
`R`-/`gamma`-bounded variants of the extension property, remain outside this
packet.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper `arXiv:1003.1587`.
- `supporting_paper_0901.1025.pdf`: supporting `C(K)`-representation paper.
- `figures/source_question_crop.png`: source question.
- `figures/supporting_scalar_type_crop.png`: supporting scalar-type criterion.

