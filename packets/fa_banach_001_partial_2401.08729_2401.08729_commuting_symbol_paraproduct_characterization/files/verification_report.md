# Verification report

Verdict: **likely valid partial result**.

Scope checked: Theorem 1 and its simultaneously diagonalizable matrix
corollary in `main.tex`.

## Proof audit

1. For a scalar symbol, the summands
   `d_k beta E_{k-1} f` are orthogonal martingale differences in `L_2`.
   Their squared norm is therefore the scalar Carleson embedding form.
2. Indicator testing gives the lower Carleson estimate; the scalar stopping
   time embedding gives the upper estimate.  The difference between sums
   over `k>n` and `k>=n` costs only a `d`-dependent factor because a mean-zero
   function constant on `d` children has maximum square at most `d` times its
   parent average.
3. Left multiplication by an abelian symbol algebra is a commuting normal
   representation on `L_2(M)`.  Its spectral decomposition turns every finite
   paraproduct truncation into scalar paraproduct fibers tensored with
   identities, so the operator norm is the essential supremum of scalar
   norms.
4. The positive column-BMO square function lies in the same abelian algebra;
   its norm is the essential supremum of the scalar fiber square functions.
5. Uniform finite-truncation estimates extend the operator from finite
   martingales.  Conversely, orthogonal output projections recover every
   finite truncation from a bounded full paraproduct.

No computational check is relevant.  The source crop and all five rendered
packet pages were visually inspected; there are no clipped formulas, missing
references, or LaTeX warnings in the final build.

## Residual review point

For a completely nonseparable ambient algebra, a reviewer may prefer to
rewrite the spectral-decomposition paragraph as a cyclic decomposition of the
abelian left representation, or directly as an abelian von Neumann tensor
product.  This is a presentation/general-measure-space point, not a missing
mathematical dependency.  The standard separable-predual case and all matrix
corollaries are immediate from the written proof.

