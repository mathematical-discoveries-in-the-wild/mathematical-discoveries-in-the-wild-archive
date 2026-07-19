# Question Gonzalo: AP/injective-kernel positive subcase

Status: `partial_result_likely_valid`

Source target: Jose Rodriguez and Abraham Rueda Zoca, *Weak precompactness in projective tensor products*, arXiv:2305.06089.

## Result

The source asks whether, for weakly null sequences `(x_n)` in `X` and `(y_n)` in `Y`, weak convergence of `(x_n tensor y_n)` in `X tensor_pi Y` forces weak nullity.

This packet proves the affirmative answer whenever the canonical map

```text
X tensor_pi Y -> X tensor_epsilon Y
```

is injective. In particular, this holds if either factor has the approximation property.

The proof is short: every elementary tensor functional `x* tensor y*` evaluates on `x_n tensor y_n` as `x*(x_n)y*(y_n)`, hence tends to zero. Therefore any weak limit is killed in the injective tensor product. Injectivity of the canonical map forces the weak limit to be zero.

## Scope

This is a partial result for Question `Gonzalo` in the source paper. It does not solve the case where the projective-to-injective map has nontrivial kernel. In that remaining case, any counterexample would have to converge weakly to a nonzero element of that kernel.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source question.

## Novelty check

The run indexes were checked for `2305.06089`, the paper title, `weak precompactness`, `projective tensor products`, `weakly null`, `Dunford-Pettis`, and related tensor-product keywords. Web searches for the exact title, the source question, and `weakly null x_n tensor y_n projective tensor approximation property` did not surface an exact later answer. Treat this as a modest AP/injective-kernel subcase for human review.

