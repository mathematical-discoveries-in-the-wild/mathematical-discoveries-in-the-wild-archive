# Partial result: free-LCS `V*` variants and the weak sequential-precompact split

- Source paper: Saak Gabriyelyan, *Gelfand--Phillips type properties of locally convex spaces*, arXiv:2406.07178.
- Source problem: Problem 3.18, asking for a characterization of Tychonoff spaces `X` for which the free locally convex space `L(X)` has one of the `V^*_(p,q)`-type properties.
- Packet status: consolidated candidate partial result, likely valid.
- Consolidates and supersedes the earlier packets `2406.07178_free_lcs_vstar_functionally_finite` and `2406.07178_free_lcs_wsvstar_restriction_separability`.

## Result

Let `1 <= p <= q <= infinity` and let `X` be Tychonoff. The following are equivalent:

1. Every functionally bounded subset of `X` is finite.
2. `L(X)` has `V^*_(p,q)`.
3. `L(X)` has `EV^*_(p,q)`.
4. `L(X)` has `sV^*_(p,q)`.
5. `L(X)` has `sEV^*_(p,q)`.

Thus the ordinary weakly compact and weakly sequentially compact variants are completely characterized.

For the weaker weak sequential-precompact variants, the finite-functionally-bounded condition is sufficient but not necessary. More generally, if every countable functionally bounded `S subset X` has separable restriction Banach space

```text
E_S = closure({f|_S : f in C(X)}) in ell_infty(S),
```

then every bounded subset of `L(X)` is weakly sequentially precompact. Hence `L(X)` has `wsV^*_(p,q)` and `wsEV^*_(p,q)` for all `p <= q`.

In particular, every compact metrizable `K` satisfies the weak variants. Taking `K=[0,1]` gives a concrete separation: `L([0,1])` has all `wsV^*` and `wsEV^*` variants, while it fails `V^*`, `EV^*`, `sV^*`, and `sEV^*`.

## Proof mechanism

For the compact/sequential variants, the positive direction is finite-dimensional: EV* sets are bounded, and bounded subsets of `L(X)` have functionally bounded support plus uniformly bounded coefficient `ell_1` norm. If all functionally bounded subsets of `X` are finite, every EV* set is trapped in a compact subset of a finite-dimensional coordinate span.

The converse uses an infinite functionally bounded set `D={x_i}` and weighted partial sums

```text
a_m = sum_{i <= m} 2^{-i-1} x_i.
```

The set `{a_m}` is a universal `(p,q)-V^*` set, but it converges pointwise on `C(X)` to the infinite measure `sum_i 2^{-i-1} delta_{x_i}`, which is not an element of `L(X)`. This prevents relative weak compactness and relative weak sequential compactness.

For the weak sequential-precompact positive theorem, a sequence in a bounded subset of `L(X)` has countable functionally bounded support `S`. If `E_S` is separable, the sequence becomes a uniformly bounded sequence in `E_S'`; the weak-star dual ball is compact metrizable, so a weak-star convergent subsequence exists. Testing against restrictions of functions in `C(X)` gives a weakly Cauchy subsequence in `L(X)`.

## Full-result push notes

I made a further direct push on the missing converse for the weak variants. The natural route would be: nonseparable `E_S` should yield a bounded sequence of finitely supported measures with no weakly Cauchy subsequence whose adjoint map `C(X) -> ell_infty` is `(q,p)`-convergent. This is exactly the operator characterization of `wsV^*`.

The obvious candidates do not work. Point masses and block averages over `beta N` have no weakly Cauchy subsequences, but block/coordinate indicator functions are weakly `1`-summable and keep the `V^*` seminorm bounded away from zero, so these sets are not `V^*`. Summable-weight sign families go the other way: they satisfy the `V^*` estimates but diagonal selection plus dominated convergence gives weakly Cauchy subsequences. I do not see a justified extraction theorem bridging this gap, so the consolidated packet does not claim a full `wsV^*` characterization.

## Verification notes

- Literature checked: arXiv:2406.07178, arXiv:2402.08860, arXiv:2403.02016, local run indexes, and web searches for `wsV`, `weak property sV`, `V^* free locally convex space L(X)`, `weakly sequentially precompact L(X) free locally convex`, and Problem 3.18.
- The LaTeX packet renders successfully to `solution_packet.pdf`.
- The packet includes the original source PDF and an open-problem crop.

## Files

- `main.tex`: consolidated proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: crop of Problem 3.18.
