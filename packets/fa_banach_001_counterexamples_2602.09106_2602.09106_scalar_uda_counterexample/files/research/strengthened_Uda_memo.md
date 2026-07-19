# Strengthened versions of the `U(d,a) <= C d a` question

Date: 2026-06-08.

This note follows up on the scalar counterexample packet.  It is a
research memo, not a promoted solution packet: it records what can be
proved cleanly, what the source paper already implies, and where a
counterexample would still have to hide.

Source paper:

- William B. Johnson and Tomasz Kania, "Uniform Property (S)",
  arXiv:2602.09106.
- Local parsed source: `data/parsed/arxiv_sources/2602.09106/main.tex`.

## Executive summary

The scalar counterexample shows that the printed question is false
without an extra hypothesis: in `R`, for every `0 < d < 2` the admissible
pair in the infimum is forced to be antipodal.

The most important strengthened conclusion found in this follow-up is:

> The infinite-dimensional version is true for every non-superreflexive
> Banach space.  In fact Johnson--Kania's Theorem C proves
> `U_X(d;a) <= ((4a)/(2+d) wedge 1)d`, hence `U_X(d;a) <= 2 d a`.

Consequently, any counterexample to the infinite-dimensional
strengthening must be superreflexive.  Any counterexample to the
connected-sphere strengthening must also avoid the simple flat-face
mechanism below.

## Definitions

For a normed space `X`,

```text
U_X(x,y;a) = sup_{||z|| <= a} | ||x+z|| - ||y+z|| |,

U_X(d;a) = inf_{x,y in S_X, ||x-y|| >= d} U_X(x,y;a).
```

The printed open problem asks whether there is a universal constant `C`
such that `U_X(d;a) <= C d a`.

## Known positive result from the source paper

Theorem C in the source paper states that if `X` is not superreflexive,
then

```text
U_X(d;a) <= ((4a)/(2+d) wedge 1)d,       0 < d <= 2, a > 0.
```

This immediately gives the desired product estimate with universal
constant `2`:

- if `a <= (2+d)/4`, then `((4a)/(2+d))d <= 2ad`;
- if `a >= (2+d)/4`, then `a >= 1/2`, so `d <= 2ad`.

Thus the infinite-dimensional strengthening is settled positively in
the non-superreflexive case.  The source proof uses James' uniformly
non-square theorem to pass through almost-isometric `ell_infinity^2`
geometry, equivalently a diameter-two line segment in an ultrapower.

## A direct flat-face criterion

The following elementary lemma isolates the geometric mechanism behind
Theorem C.

**Lemma.** Suppose the unit sphere of `X` contains a line segment
`[v,w]` with `||v-w|| = L > 0`.  Then for every `0 < d <= L`,

```text
U_X(d;a) <= (4a/(L+d)) d  <= (4/L) a d.
```

In particular, if `L=2`, then `U_X(d;a) <= 2ad` for all `0<d<=2` and
all `a>0`.

**Proof.** Parametrize the segment by
`p(s) = (1-s)v + s w`, `0 <= s <= 1`.  Put

```text
x = p((1-d/L)/2),        y = p((1+d/L)/2).
```

Then `x,y in S_X` and `||x-y||=d`.  Moreover

```text
y = t x + (1-t) w,       t = (L-d)/(L+d).
```

Fix `z` with `||z|| <= a` and, by symmetry, assume
`||x+z|| <= ||y+z||`.  Convexity gives

```text
||y+z||
 <= t ||x+z|| + (1-t)||w+z||
 <= t ||x+z|| + (1-t)(1+a)
 =  ||x+z|| + (1-t)(1+a-||x+z||).
```

Since `||x+z|| >= 1-a`, the last factor is at most `2a`, and
`1-t = 2d/(L+d)`.  Therefore

```text
||y+z|| - ||x+z|| <= 4ad/(L+d).
```

Taking the supremum over `z` and then the infimum over admissible pairs
proves the claim.

This gives a clean sufficient condition for the "admissible small
distance" idea: mere existence of pairs at distance `d` is not what the
proof uses; it uses pairs lying on a controlled spherical segment.

## Hilbert spaces

The connected, strictly convex model case is also positive.

Let `H` be a real Hilbert space with dimension at least `2`.  Choose
`x,y in S_H` with `||x-y||=d`.  For every `z`,

```text
||x+z||^2 - ||y+z||^2 = 2 <x-y,z>.
```

If `a <= 1/2`, then for `||z|| <= a` the denominator
`||x+z|| + ||y+z||` is at least `2(1-a) >= 1`, so

```text
| ||x+z|| - ||y+z|| | <= 2 a d.
```

If `a >= 1/2`, the trivial estimate
`| ||x+z|| - ||y+z|| | <= ||x-y|| = d` gives `d <= 2ad`.
Thus

```text
U_H(d;a) <= 2ad.
```

This rules out the idea that connectedness or strict convexity by itself
creates a scalar-like obstruction in the most symmetric case.

## Absolute-sum inheritance

A useful permanence observation:

If `X = Y op_p Z` for `1 <= p <= infinity` and `Y` satisfies
`U_Y(d;a) <= Cda`, then `X` satisfies the same bound.

For `x,y in S_Y`, view them as `(x,0),(y,0) in X`.  A perturbation in
`X` has the form `(u,v)`.  For `1 <= p < infinity`,

```text
||(x,0)+(u,v)|| = ( ||x+u||^p + ||v||^p )^(1/p),
```

and the scalar map `s -> (s^p + ||v||^p)^(1/p)` is 1-Lipschitz on
`[0,infinity)`.  The case `p=infinity` is the same with
`s -> max{s, ||v||}`.  Hence

```text
| ||(x,0)+(u,v)|| - ||(y,0)+(u,v)|| |
  <= | ||x+u|| - ||y+u|| |.
```

Taking suprema gives `U_X((x,0),(y,0);a) <= U_Y(x,y;a)`.

## What remains genuinely open from this sprint

I did not find a proof or counterexample for the full connected-sphere
strengthening:

```text
dim X >= 2, or S_X connected, and X has uniform property (S)
  ==> ?  U_X(d;a) <= C d a with universal C.
```

Nor did I find a proof or counterexample for the full
infinite-dimensional strengthening in the superreflexive case.

The reductions above make the remaining target much sharper.  A
counterexample, if it exists, cannot be:

- one-dimensional;
- non-superreflexive;
- a space with a diameter-two spherical segment;
- Hilbert;
- an absolute `ell_p` sum containing a good summand.

It must therefore be a superreflexive geometry whose unit sphere has no
long flat face, and for which the infimum over small-distance pairs
cannot find a Hilbert-like or flat-like pair.  The numerical probes in
`lp2_modulus_probe.py` did not suggest an `ell_p^2` counterexample:
balanced pairs are bad for large `p`, but near-axis pairs become very
flat and drive the infimum down.

## Recommendation

The existing scalar packet should remain labeled as a literal
counterexample to the printed problem.  Its limitation paragraph can be
strengthened: the infinite-dimensional variant is already resolved
positively for all non-superreflexive spaces by the source paper, so the
only unresolved infinite-dimensional direction is superreflexive.
