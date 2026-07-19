# Rank-one equivalence and reflexive BAP targets for arXiv:2404.06497

Status: `strengthened_partial_result_likely_valid`

Source paper: N. J. Laustsen and P. Tradacete, *Banach lattices of positively homogeneous functions induced by a Banach space*, arXiv:2404.06497.

Target: printed Question 4.2 asks for which Banach spaces `F` one has
`\overline{I_{w^*}[F]} = H_{w^*}^p[F]`; printed Question 6.3 asks whether admissible composition
operators `C_\Phi` preserve the closed ideals `\overline{I_{w^*}}`.

## Results

1. For each fixed target space `F`, Question 6.3 for all infinite-dimensional domains `E` and all
admissible maps `Phi: F^* -> E^*` is equivalent to Question 4.2 for `F`.

The reverse implication is rank-one: if `f in H_{w^*}^p[F]`, choose `x_0 in E` and `x_0^* in E^*`
with `x_0^*(x_0)=1`, and set `Phi_f(y^*) = f(y^*) x_0^*`. Then
`C_{Phi_f}(delta_{x_0}) = f`. Thus any failure of Question 4.2 immediately gives a rank-one
counterexample to Question 6.3.

2. For every reflexive real Banach space `E` with the bounded approximation property, and every
`1 <= p < infinity`,
`\overline{I_{w^*}[E]} = H_{w^*}^p[E]`.

The proof uses the measure representation of `H^p[E]`: each control function
`f_mu^p(x*) = (int |x*(x)|^p dmu(x))^{1/p}`. The weak compact unit ball is Eberlein compact, so the
representing Radon measure is carried by a separable support. BAP then supplies a uniformly bounded
finite-rank sequence `T_n -> I` on that support. The compressed functions factor through
finite-dimensional subspaces, hence lie in `FBL^p[E] subset overline(I_{w^*}[E])`, and the
`FBL^p`-norm error is controlled by `(int ||(I-T_n)x||^p dmu(x))^{1/p}`.

## Scope

This does not solve Question 4.2 for all Banach spaces. It gives a broad positive target class,
including Hilbert spaces for all finite `p`, and shows that Question 6.3 is exactly as hard as
Question 4.2 target-by-target.

## Files

- `main.tex`: full partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2404.06497.
- `figures/questions_4_1_4_2_crop.png`: source crop with Questions 4.1 and 4.2.
- `figures/question_6_3_crop.png`: source crop with the rank-one example and Question 6.3.

## Verification

The source PDF was downloaded from arXiv on 2026-06-23. The crop pages were visually checked.
No computational verification is involved. Human review should focus on the rank-one norm estimate,
the use of Lemma 6.1(ii) from the source paper, and the reflexive-BAP finite-rank
approximation argument, especially the Eberlein compact separable-support reduction.
