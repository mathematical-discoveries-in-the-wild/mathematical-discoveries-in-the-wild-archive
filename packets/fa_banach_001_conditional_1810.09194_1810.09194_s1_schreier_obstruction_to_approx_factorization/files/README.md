# Conditional packet: S1-Schreier obstruction to approximate factorization

Status: `conditional_reduction`

Agent: `agent_lane_06`

Date: 2026-06-19

Source paper: Martin Mathieu and Pedro Tradacete, *Strictly singular multiplication operators on* `L(X)`, arXiv:1810.09194.

Target: Remark 6.11 asks whether every strictly singular operator on `L_p[0,1]`, `1<p<infty`, `p != 2`, is approximately `(ell_r,ell_s)`-factorizable for some `r<s`, and asks the stronger finite-dimensional-sum variant.

## Result

The packet proves a necessary obstruction:

If an operator is approximable in norm by factorizations whose middle leg is

```text
(oplus X_n)_{ell_r} -> (oplus Y_n)_{ell_s},   1<r<s<infty,
```

with `X_n,Y_n` finite-dimensional, then the operator is `S_1`-strictly singular.
In particular, a strictly singular operator on `L_p` which is not
`S_1`-strictly singular would give a counterexample to the approximate
factorization question in this reflexive exponent range.

## Conditional Dependency

The packet does **not** prove that such a higher-Schreier-rank strictly
singular operator exists on `L_p`. The remaining dependency is:

```text
Find T in S(L_p) \ S_1(L_p).
```

If this dependency is verified, the source question has a negative answer. If
instead every strictly singular operator on `L_p` is `S_1`-strictly singular,
this obstruction disappears and a positive solution would need a finer
factorization argument.

Follow-up: `solutions/partial/1810.09194_strictly_singular_lp_s1_schreier/`
proves the second alternative for classical `L_p[0,1]`: every strictly singular
operator on `L_p` is `S_1`-strictly singular. Thus this conditional route cannot
produce a counterexample on classical `L_p`.

## Why the usual FSS route fails

A tempting first obstruction was finite strict singularity. That route is
invalid here: the middle map in the source definition is an arbitrary bounded
operator `ell_r -> ell_s`, not the formal inclusion. Androulakis-Dodos-
Sirotkin-Troitsky record that for `1<r<s<infty`,
`FSS(ell_r,ell_s) != SS(ell_r,ell_s)=L(ell_r,ell_s)`. Thus non-FSS behavior can
already occur inside the permitted middle leg.

## Checks

Cheap-index searches for `1810.09194`, `strictly singular multiplication`,
`approximately factorizable`, `ell_r ell_s`, and related terms found no direct
run duplicate. Targeted web searches for the exact approximate-factorization
phrases found the source paper but no later direct answer. Local source
arXiv:math/0609039 supplied the Schreier-singular tools and the failure of the
finite-strict-singular obstruction.

## Files

- `main.tex`: packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `supporting_paper_math_0609039.pdf`: supporting Schreier-singularity paper.
- `figures/open_problem_crop.png`: rendered crop of Remark 6.11.
- `code/render_open_problem_crop.py`: reproducible crop script.

Human review should focus on the finite-dimensional-sum lemma and the use of
the standard ideal/closedness properties of `S_1`-strictly singular operators.
