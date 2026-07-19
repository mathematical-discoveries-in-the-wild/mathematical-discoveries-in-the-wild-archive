# Question Gonzalo: complemented basic subsequence subcase

Status: `partial_result_likely_valid`

Source target: Jose Rodriguez and Abraham Rueda Zoca, *Weak precompactness in projective tensor products*, arXiv:2305.06089.

## Result

The source asks whether, for weakly null sequences `(x_n)` in `X` and `(y_n)` in `Y`, weak convergence of `(x_n tensor y_n)` in `X tensor_pi Y` forces weak nullity.

This packet proves an affirmative local subcase: it is enough that one of the two factor sequences has a subsequence whose closed span is complemented and has the approximation property. In particular, it is enough that one factor sequence has a complemented basic subsequence.

Equivalently, if one of the factor spaces has the property that every seminormalized weakly null sequence admits a complemented basic subsequence, then Question `Gonzalo` has an affirmative answer for that factor paired with an arbitrary Banach space.

## Scope

This strengthens the earlier AP/injective-kernel packet in a sequence-local direction. The whole factor `X` or `Y` need not have AP; only the complemented closed span of one subsequence is used.

It does not solve the remaining hard case where neither factor sequence has a norm-null subsequence nor a complemented AP subsequence. In that region, the previous kernel obstruction remains: any counterexample must converge weakly to a nonzero element killed by all elementary tensor functionals.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source question.

## Novelty check

The run indexes were checked for `2305.06089`, `Gonzalo`, `complemented basic`, `complemented subsequence`, and related projective-tensor keywords. The source paper contains an unconditional-complemented partial answer; this packet removes unconditionality under the stronger hypothesis that the tensor sequence is weakly convergent, using the local AP of the complemented basic span.

