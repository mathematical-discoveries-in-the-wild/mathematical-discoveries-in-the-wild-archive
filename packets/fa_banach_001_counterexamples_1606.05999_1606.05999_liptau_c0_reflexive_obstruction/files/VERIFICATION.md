# Verification report

## Source and scope

- Target: Question 5.1 of arXiv:1606.05999, source PDF page 20.
- Claimed result: full negative answer.
- Unclaimed result: Question 5.2 (the Schur property of a projective tensor
  product) is untouched.

## Theorem 2.9 hypothesis audit

Take `H = ell_2`, `M = B_H`, `tau` the weak topology, base point zero, and
`d(u,v) = ||u-v||_2^(1/2)`.

- bounded and pointed: immediate;
- separable: the norm metric is separable, hence so is its snowflake;
- complete: a `d`-Cauchy sequence is norm Cauchy;
- compact metrizable `tau`: the unit ball of separable reflexive `ell_2` is
  weakly compact and weakly metrizable;
- lower semicontinuity: the norm, hence its square root, is weakly lower
  semicontinuous;
- property (P): verified directly. If `delta=||u-v||>0`, choose a unit vector
  `h` with `<u-v,h>=delta` and put
  `phi_rho(s)=sqrt(max(s,0)+rho)-sqrt(rho)`. The function `phi_rho` is ordinary
  Lipschitz and satisfies
  `|phi_rho(s)-phi_rho(t)| <= sqrt(|s-t|)`. Thus its composition with
  `<z-v,h>` has snowflake Lipschitz norm at most one and is little Lipschitz;
  its increment from `v` to `u` is
  `sqrt(delta+rho)-sqrt(rho) -> sqrt(delta)=d(u,v)`.

The source's statement immediately before the corollary following Theorem 2.9
also explicitly identifies this weak-star-ball/nontrivial-gauge family as a
special case, providing an independent consistency check.

The gauge check is direct: `sqrt(t)` is continuous, increasing, subadditive,
vanishes at zero, dominates `t` on `[0,1]`, and
`sqrt(t)/t -> infinity` as `t -> 0+`.

## Embedding calculation

For `(Jx)(u) = <u,x>`:

\[
\frac{|(Jx)(u)-(Jx)(v)|}{d(u,v)}
\leq \|x\|_2 d(u,v).
\]

This simultaneously proves:

- the global upper bound `||Jx|| <= sqrt(2)||x||`, since the diameter in `d`
  is `sqrt(2)`;
- the little-Lipschitz limit, since the right side tends uniformly to zero
  with `d(u,v)`;
- weak continuity, separately, because `Jx` is a coordinate functional.

For nonzero `x`, choose `u=x/||x||` and `v=0`. Then `d(u,0)=1` and the
quotient equals `||x||`. Hence `||Jx|| >= ||x||`, so `J` is bounded below
and its image is closed.

## Obstruction to an embedding into c0

If `T: lip_tau(M) -> c_0` were an isomorphic embedding, `T o J` would embed
`ell_2` as a closed subspace of `c_0`. Every closed subspace of `c_0` has the
Dunford--Pettis property. The image of `ell_2` is reflexive, so its identity
is weakly compact. Dunford--Pettis would make that identity completely
continuous, contradicting the weakly-null, norm-one orthonormal basis (after
transport through the isomorphism). Therefore no such `T` exists.

## Residual review risk

The main item for human checking is the elementary three-case proof of the
one-half Hölder estimate for `phi_rho` (both inputs nonpositive, both
nonnegative, or straddling zero). No numerical experiment or hidden limiting
interchange is used.
