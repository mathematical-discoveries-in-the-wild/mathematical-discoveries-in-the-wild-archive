# Partial Solution Packet: Exact Density Obstruction for Bounded Versus Precompact Sequences

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- model: `GPT5.6`
- agent: `agent_lane_10`
- source arXiv id: `2104.07152`
- source paper: Leandro Candido, *Complementations in C(K,X) and ell_infinity(X)*
- target passage: arXiv PDF page 8, Section 5, Problem 5.1 and Remark 5.3

## Result

The packet gives a complete density-level characterization for the two spaces
in the source problem.

For every infinite-dimensional Banach space `X` of density `kappa` and every
infinite set `Gamma` of cardinality `lambda`,

```text
dens rc_Gamma(X)              = max(kappa, 2^lambda),
dens ell_infinity(Gamma, X)   = kappa^lambda,
```

where `rc_Gamma(X)` is the space of bounded `Gamma`-families whose range is
relatively compact.

For an infinite compact Hausdorff space `K`, put `kappa = w(K)`. The standard
identifications in the source paper turn this into

```text
dens C(K, ell_infinity)       = max(kappa, continuum),
dens ell_infinity(C(K))       = kappa^aleph_0.
```

Candido's Theorem 5.2 also shows that a positive answer for infinite `K`
forces `ell_infinity` to embed into `C(K)`, hence `kappa >= continuum`.
Consequently,

```text
C(K, ell_infinity) isomorphic to ell_infinity(C(K))
    implies kappa >= continuum and kappa^aleph_0 = kappa.
```

Thus no example can have `w(K)^aleph_0 > w(K)`. In particular, there is no
example of countable cofinality. This goes beyond the metric obstruction in
the source and reduces any positive construction to fixed-point cardinals for
countable exponentiation.

## Scope

Problem 5.1 omits the word "infinite", but the paragraph immediately after it,
Theorem 5.2, and Remark 5.3 all formulate the substantive question for
infinite `K`. This is necessary: finite nonempty `K` gives a trivial positive
example because both spaces are finite powers of `ell_infinity`.

This packet does **not** settle existence for the surviving weights. In
particular, `kappa = continuum` always passes the density test. The operator
formulation

```text
K(ell_1, C(K)) isomorphic to L(ell_1, C(K))
```

remains unresolved here.

## Method

The proof has two elementary but exact counting steps.

- A precompact family is uniformly approximable by a finite-range family.
  Finite-range maps with values in a dense set give the upper bound
  `max(kappa, 2^lambda)`. Constant families contain `X`, while scalar
  multiples of one fixed vector contain `ell_infinity(Gamma)`, giving the
  matching lower bound.
- Every infinite-dimensional Banach space of density `kappa` has a uniformly
  separated subset of its unit sphere of cardinality `kappa`. All
  `Gamma`-families valued in that subset form a uniformly separated subset of
  `ell_infinity(Gamma,X)` of cardinality `kappa^lambda`. The reverse bound
  comes from coordinatewise approximation by a dense subset.

The equality `dens C(K) = w(K)` is included with a proof, and the
countable-cofinality consequence is proved by a specialized diagonal form of
König's argument.

## Files

- `main.tex`: theorem, proof, consequences, and limitations
- `solution_packet.pdf`: rendered proof packet
- `source_paper.pdf`: local copy of arXiv:2104.07152
- `figures/open_problem_crop.png`: genuine crop of Problem 5.1, Theorem 5.2,
  and Remark 5.3
- `verification.md`: independent dependency and edge-case audit

## Novelty Check

The run indexes were searched for arXiv id `2104.07152`, the exact paper
title, `bounded sequences`, `precompact sequences`, `C(K,ell_infinity)`,
`ell_infinity(C(K))`, and the operator-space reformulation. No existing run
packet addresses this problem or the density formulas above.

Bounded external searches on 2026-07-23 used the exact phrases
`"space of bounded sequences in C(K)" "precompact sequences" isomorphic`,
`"C(K,ell_infty)" "ell_infty(C(K))"`, the paper title with citations, and
`"K(ell_1,X)" "L(ell_1,X)" isomorphic`. They located the source paper and its
published version, but no later work explicitly answering Problem 5.1 or
stating this density obstruction. This is evidence rather than a guarantee of
novelty.

## Human Review Focus

The main review item is the scope and usefulness of the cardinal obstruction,
not a hidden analytic estimate. The two density formulas are fully proved.
A reviewer should confirm that the claimed advance is described as a
necessary condition and exact density characterization only, never as a
solution of the surviving isomorphism problem.

