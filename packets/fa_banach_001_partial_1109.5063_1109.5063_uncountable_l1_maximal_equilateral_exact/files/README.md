# Exact maximal-equilateral number of uncountable `ell_1(Gamma)`

Status: **candidate partial result, likely valid; human review requested**.

## Result

Let `Gamma` be uncountable. Then

```text
m(ell_1(Gamma)) = 5,
```

where `m(X)` is the least cardinality of a maximal equilateral subset of `X`.

Swanepoel--Villa, arXiv:1109.5063, prove the upper bound `m(ell_1(Gamma)) <= 5` and point out why their smooth-point construction giving `m=4` in separable `ell_1` cannot apply to uncountable `Gamma`. The packet supplies the matching lower bound.

## Mechanism

For four equilateral points, sort their four scalar values at each coordinate. The three consecutive gaps give two singleton cuts and one `2--2` cut. Pairwise equidistance forces the total singleton-cut weight to be the same at all four labels and the total weight of each of the three `2--2` partitions to be the same. The coordinatewise midpoint of the two middle values is therefore equidistant from all four points at a radius strictly smaller than the side length. Since the union of four supports is countable, an unused coordinate raises all four distances by the same amount and extends the set.

The source's five-point Hadamard configuration is reproduced and shown directly to be maximal in the full uncountable space.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python code/verify.py
```

The script solves the cut-weight linear system symbolically, checks exact rational symmetrized examples with all three coordinate gaps present, and verifies the ten distances in the five-point configuration. The formal proof, not the computation, handles arbitrary supports and coordinates.

## Scope and novelty

This is a complete exact-value theorem for the uncountable `ell_1(Gamma)` case, but only an adjacent partial result toward the paper's finite-dimensional Conjecture 8. That conjecture remains open here.

Cheap run indexes were searched for arXiv:1109.5063 and the core maximal-equilateral terminology. Bounded web searches on 21 July 2026 used exact variants of `m(ell_1(Gamma))=5`, `uncountable ell_1 maximal equilateral`, and four-point `L_1` cosphericity. They found the source paper, related infinite-dimensional equilateral-set papers, and a 2010 expository five-point noncospherical example, but no later paper proving this exact value or the four-point extension lemma. This is not an exhaustive novelty certification.

## Human-review focus

Check the coordinate cut bookkeeping (especially tied scalar values and convergence of the nonnegative gap sums), then the deduction that the common center radius is strictly below the side length. The explicit five-point maximality argument is elementary.
