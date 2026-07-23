# Verification Report

## Verdict

`candidate partial result - likely valid`

The semialgebraic and analytic steps were audited independently. The theorem
proves finite-component structure but does not decide whether a genuine gap
`t0<t1` exists.

## Source-Scope Audit

The source paper proves:

- every unital quantum dynamical semigroup is eventually mixed unitary;
- if it is not mixed unitary for all times, it is non-mixed-unitary on an
  initial punctured interval `(0,t0)`;
- the first re-entry `t0` is mixed unitary;
- all times from some finite `t1>=t0` onward are mixed unitary.

The open remark asks whether `t0=t1` must hold and suggests that, otherwise,
the intermediate mixed-unitary times might be discrete. The packet addresses
the topology of that intermediate set only.

## Semialgebraicity Audit

Work in real coordinates on the finite-dimensional real vector space of
Hermiticity-preserving superoperators.

- `U(d)` is defined by the real polynomial equations `U*U=I`.
- The coordinate matrix of `Ad_U` is polynomial in the real and imaginary
  parts of `U`.
- If the ambient dimension is `N`, Caratheodory's theorem uses at most `N+1`
  unitary channels in any convex representation.
- The existence of coefficients and unitaries satisfying the convex
  representation is therefore a finite first-order formula over the real
  closed field.
- Tarski-Seidenberg makes its projection, `MU(d)`, semialgebraic.

No unbounded number of Kraus/unitary variables is hidden in the argument.
Compactness follows independently from compactness of `U(d)` and
finite-dimensional convex hulls.

## Analytic Zero-Set Audit

After quantifier elimination, membership in `MU(d)` is a Boolean combination
of finitely many sign conditions on polynomials `P_j`.

For fixed finite-dimensional generator `L`,

```text
f_j(t) = P_j(exp(tL))
```

is real analytic on the whole real line. On a compact interval:

- an identically zero `f_j` has a constant sign status;
- a nonzero `f_j` has finitely many zeros, because an infinite zero set in a
  compact interval has an accumulation point and the identity theorem then
  forces identical vanishing.

Outside the finite union of those zeros, every sign is constant. Thus
membership is constant on each complementary interval. Closedness of
`MU(d)` supplies closed components.

## Semigroup Audit

- `0` is a mixed-unitary time because `Phi_0` is the identity channel.
- Continuity of `t -> exp(tL)` and closedness of `MU(d)` make the time set
  closed.
- Composition of two convex combinations of unitary conjugations is another
  such convex combination, so the time set is additive.
- The source's eventual-mixed-unitarity theorem supplies a final ray.

These facts combine with the compact-interval analytic argument to give
finitely many components globally.

## Interval-to-Ray Audit

If `[a,b]` consists of mixed-unitary times, additivity gives
`[ma,mb]` for every positive integer `m`. Consecutive intervals overlap once

```text
m(b-a) >= a.
```

Taking `m >= ceil(a/(b-a))` yields the claimed final ray. The endpoint
arithmetic is inclusive.

## Edge Cases

- If every time is mixed unitary, the time set is the single ray
  `[0,infinity)`.
- Polynomial sign functions that vanish identically do not introduce
  infinitely many boundary points.
- Jordan blocks and complex eigenvalues in `L` cause no problem: matrix
  exponential coordinates remain real analytic.
- The theorem is for fixed finite `d`; finite-dimensionality is essential to
  the semialgebraic argument.
- A finite union theorem does not imply `t0=t1`; isolated points or separated
  intervals are not excluded.
- No numerical computation is part of the proof.

## Literature Audit

The local and bounded external search terms are recorded in `README.md` and
`main.tex`. No exact prior statement was found. Human literature review is
still required before asserting publication-level novelty.

