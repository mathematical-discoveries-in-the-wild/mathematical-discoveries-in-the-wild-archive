# n=2 sharpness for Feshchenko's marginal-subspace conjecture

Run: `fa_banach_001`  
Agent: `agent_lane_04`  
Source: Ivan Feshchenko, "When is the sum of complemented subspaces
complemented?", arXiv:1606.08048  
Status: `partial_result_likely_valid`

## Claim

The packet proves the `n=2` case of Feshchenko's Conjecture in Section 3.4.
For the only symmetric zero-diagonal `2 x 2` matrix with spectral radius one,
namely
\[
E=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
there is a probability space and two sub-sigma-algebras `A,B` such that
`psi'(A,B)=0` and
\[
L^p_0(A)+L^p_0(B)
\]
is not closed in `L^p` for every `p in [1,infty]`.

## Idea

Use the edge set of an infinite bipartite path as the probability space.
The row and column sigma-algebras have `psi'=0` because many row-column atom
pairs are disjoint. The support graph is connected, so the centered row and
column marginal spaces intersect only at zero.

On longer and longer finite path intervals, choose a triangular potential
`theta_k`. The row function `theta_k(row)` and the column function
`-theta_k(column)` almost cancel on every edge, with error bounded by the
Lipschitz step size of the triangle. After centering, their `L^p` norms stay
bounded below relative to the block mass, while the norm of their sum is
smaller by a factor tending to zero. Hence the addition map from the direct
sum of the two centered marginal spaces is not bounded below, so its range is
not closed.

## Novelty Check

Cheap run indexes had no exact entry for arXiv:1606.08048. Web searches on
2026-06-29 for the source title, the `psi'` marginal-subspace conjecture, and
phrases around "sum of marginal subspaces" did not find a later paper resolving
this `n=2` sharpness case. Novelty confidence is moderate; the construction is
elementary and may overlap folklore examples of nonclosed row/column sums, but
the packet records the explicit match to Feshchenko's Section 3.4 conjecture.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: source page containing the conjecture.

## Human Review

Recommended review focus:

- Check the graph/path probability construction and the lower-bound estimates
  for the centered triangular test functions.
- Check that the centered row and column spaces have zero intersection for
  every `p`, including `p=infty`.
- Confirm whether the explicit `n=2` conjecture case is already known in the
  marginal-subspace literature under another name.
