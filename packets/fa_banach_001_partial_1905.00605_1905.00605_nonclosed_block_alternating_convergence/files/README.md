# Nonclosed block sums with convergent alternating approximation

Status: `partial_result_likely_valid`

Source target: Christian Bargetz and Emir Medjic, *On the rate of convergence of iterated Bregman projections and of the alternating algorithm*, arXiv:1905.00605.

## Result

The source introduction records Deutsch's open question about whether the closedness of the sum of subspaces is necessary in the Banach-space alternating approximation theorem. This packet gives a scoped negative/partial result:

> For every real `p` with `1 < p < infinity` there are closed subspaces `M,N` of an infinite-dimensional uniformly convex and uniformly smooth Banach space `X` such that `M+N` is not closed, but the alternating residual algorithm
> `x_{2k+1}=(I-P_M)x_{2k}`, `x_{2k+2}=(I-P_N)x_{2k+1}`
> converges in norm to `0` for every `x in X`.

The construction takes an `ell_p`-sum of finite-dimensional strictly convex blocks. In each block the two selected subspaces span the whole block, so Stiles' finite-dimensional theorem gives convergence to zero. The block tilts tend to zero, making the global sum `M+N` nonclosed. Since each residual map reduces norm and convergence holds in every block, dominated convergence gives global convergence.

## Scope

This does not solve the full arbitrary-pair problem without the closed-sum hypothesis. It shows that closedness is not logically necessary for convergence, even in an infinite-dimensional uniformly convex and uniformly smooth setting. The remaining hard problem is to characterize which nonclosed pairs still converge, or whether all pairs in such spaces converge.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source passage around the extracted open question.

## Novelty check

Before promotion, the run indexes were searched for `1905.00605`, `iterated Bregman projections`, `alternating algorithm`, `Bregman projection`, `closedness of the sum`, and Deutsch/Pinkus alternating-projection phrases. Web search for the exact source title and close variants of the closed-sum question found the source paper but no exact later answer. This packet should be reviewed as a modest block-diagonal partial result rather than a full settlement.
