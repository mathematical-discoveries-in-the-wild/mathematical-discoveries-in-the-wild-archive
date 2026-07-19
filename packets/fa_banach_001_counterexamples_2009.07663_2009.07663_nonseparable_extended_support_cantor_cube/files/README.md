# Nonseparable extended support for a functional on a Lipschitz space

Status: `candidate_counterexample_to_separability_subquestion_likely_valid`

Source paper: Ramon J. Aliaga and Eva Pernecka, "Integral representation and
supports of functionals on Lipschitz spaces", arXiv:2009.07663.

## Source Question

In the concluding remarks, Question 1 asks:

> For a complete metric space `M` and a functional `phi in Lip_0(M)^*`, is
> `S(phi)` a separable subset of `M^U`? Or does `S(phi)` at least satisfy the
> countable chain condition?

This packet gives a ZFC counterexample to the separability part. It does not
refute the ccc fallback; in fact the constructed support has ccc because it is
the support of a finite Radon measure.

## Result

There is a bounded complete metric space `M` and a positive functional
`phi in Lip_0(M)^*` such that the extended support `S(phi)` is not separable.

The example can be chosen with `M` uniformly discrete. Let `K = {0,1}^I` for an
uncountable set `I`, let `Gamma` be the dense set of finite-support points of
`K`, and equip `Gamma` with the discrete metric. Then `M^U = beta Gamma`.
The dense inclusion `Gamma -> K` extends to a continuous surjection
`beta Gamma -> K`. Lifting the full-support Bernoulli product measure on `K`
to a Radon probability on `beta Gamma` gives a functional whose extended
support maps continuously onto the nonseparable cube `K`, hence is itself
nonseparable.

## Scope

This answers "is `S(phi)` separable?" negatively, even for positive
measure-induced functionals on bounded complete metric spaces.

It leaves open the second alternative in the source question: whether every
extended support satisfies ccc. The present example is consistent with that
weaker possibility.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of the concluding questions.
- `code/render_open_question_crop.py`: crop reproduction script.

## Verification

No computational verification is needed. Local indexes were searched for
`2009.07663`, the title, extended support, countable chain condition, and
Cantor-cube/nonseparable-support phrases; no duplicate packet was found.

Bounded web searches on 2026-06-21 for exact phrases from Question 1 and the
paper title found no later explicit answer to this separability subquestion.
