# Verification Report

Verdict: `likely valid`

Mathematical confidence: 99/100

Novelty confidence: moderate; the topology facts are classical, while the
exact spectral consequence was not found in the bounded search.

## Exact-definition match

The current arXiv v2 defines `sigma_ap(B)` using a net in `D(B)` which does
not converge to zero and whose residual tends to zero. `sigma_bap(B)` requires
that net to be bounded; the sequential variants use sequences. The proof uses
exactly these definitions and does not substitute norm-normalized vectors.

## Full theorem checks

1. **Subspaces inherit the strongest topology.** Let `Y` be a subspace of
   `X` and `q` any seminorm on `Y`. Choose an algebraic complement and
   projection `P:X->Y`. Then `q o P` is a seminorm on `X`, hence continuous;
   its restriction is `q`. Thus every seminorm on `Y` is continuous for the
   induced topology.
2. **All linear maps out of a subspace are continuous.** If `L:Y->F` is
   linear and `p` is a continuous seminorm on `F`, then `p o L` is a seminorm
   on `Y`, hence continuous. This is the standard seminorm criterion for
   continuity of `L`.
3. **Injective resolvent difference.** If `lambda` is not an eigenvalue, then
   `T=lambda-B` is injective. Its algebraic inverse
   `S:ran(T)->X` is linear and is continuous by checks 1--2. Therefore
   `T x_i -> 0` implies `x_i=S(Tx_i)->0`. No approximate eigen-net can witness
   `lambda`.
4. **Reverse inclusion.** A nonzero eigenvector gives a constant net and
   constant sequence. Finite sets are bounded in every topological vector
   space, so the witness belongs to both bounded variants.
5. **No hidden operator hypothesis.** The proof never uses closedness,
   density of the domain, completeness, sequentiality, or boundedness. It is
   therefore legitimate—and stronger—to state the result for every linear
   operator.
6. **Concrete non-Banach example.** `phi=C^(N)` with the locally convex
   direct-sum topology is the countable-dimensional space with the strongest
   locally convex topology. It is a strict LF-space and hence complete; it is
   a standard Montel `(DF)`-space. It cannot be normable in infinite
   dimension because all algebraic linear functionals are continuous in the
   strongest topology, unlike on an infinite-dimensional normed space.

## Montel obstruction retained as a cross-check

For the rapidly decreasing sequence space `s` and `(Bx)_n=e^{-n}x_n`:

- `p_k(Bx)<=p_k(x)`, so `B` is continuous and closed.
- `p_0(e_m)=1` while `p_k(Be_m)=m^k e^{-m}->0`, so zero is a sequential
  approximate eigenvalue.
- If `(x_i)` is bounded and `Bx_i->0`, boundedness in `p_{k+1}` controls the
  tail uniformly in `p_k`, and coordinatewise convergence controls the finite
  head. Thus `x_i->0`, excluding every bounded approximate eigen-net.

This confirms that the positive theorem is not accidentally a consequence of
completeness, nuclearity, or Montel compactness.

## Novelty-search bounds

Searched through 2026-07-19:

- run ledger and solution indexes;
- local parsed arXiv source corpus;
- arXiv:2509.11931v2 and its reference list;
- arXiv/web exact phrases `approximate point spectrum` plus
  `strongest locally convex topology`, `finest locally convex topology`,
  `locally convex direct sum`, and `phi`;
- standard strongest-topology literature, including Kąkol--Saxon (2002).

No exact prior spectral-collapse statement or answer to Remark 5.17(a) was
found. This supports promotion as a candidate full answer, not a definitive
claim of publication-level novelty.

No unresolved mathematical gap was found.
