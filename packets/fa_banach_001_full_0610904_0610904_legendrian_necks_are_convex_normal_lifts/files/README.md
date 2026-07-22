# Legendrian necks are convex normal lifts

Status: `candidate_full_solution_likely_valid`

Source: Greg Kuperberg, *From the Mahler conjecture to Gauss linking
integrals*, arXiv:math/0610904, Geom. Funct. Anal. 18 (2008), 870-892,
DOI 10.1007/s00039-008-0669-4. The conjecture is in Section 5.1 on source
PDF page 9.

## Result

Let, in every dimension (n\geq 1),

\[
 H^+=\{(x,y)\in\mathbb R^n\times\mathbb R^n:\langle x,y\rangle=1\}
\]

carry its standard split metric and contact structure. Every smooth
spacelike Legendrian neck `N` of `H+` is `K+` for a unique smooth strictly
convex body `K` containing the origin. Thus the conjecture stated in Section
5.1 is answered affirmatively (for the smooth spacelike notion of neck used
in the source).

## Proof mechanism

The normal-direction projection `(x,y) -> y/|y|` is a local diffeomorphism on
`N`; the neck condition makes its degree one, so it is a global
diffeomorphism. Parameterize by `u` in the unit sphere and write
`y(u)=u/h(u)`. The hypersurface equation and Legendrian equation give

\[
 x(u)=\nabla_S h(u)+h(u)u.
\]

The induced split metric is

\[
 g_N=h^{-1}(\nabla_S^2h+hI),
\]

so spacelikeness says that the spherical tensor `nabla_S^2 h + h I` is
positive definite. A short geodesic ODE argument then proves directly that
`h` is the support function of a smooth strictly convex body `K`, with
boundary point `x(u)` and polar supporting point `y(u)`. Hence `N=K+`.

## Verification and novelty status

- The contact and hypersurface equations were checked independently; together
  they force both pairings `y dx` and `x dy` to vanish.
- The Gauss-direction map has injective differential by spacelikeness, and the
  degree-one neck condition rules out multiple covering in dimension two.
- The global support inequality is proved in the packet rather than imported:
  along a spherical geodesic it follows from the positive forcing equation
  `F''+F>0`.
- A bounded search on 2026-07-21 covered the run registry, solution, attempt,
  and proof-gap indexes; the local source corpus; and exact web queries for
  “every Legendrian neck,” “Legendrian neck convex body,” and Kuperberg's
  terminology. It found the source paper and mirrors, but no later answer.
  This is not an exhaustive literature claim.

Recommended human review: verify that the source's implicit contact form is
the standard restriction used here (multiplying it by a nonzero scalar is
irrelevant), and verify the degree-one consequence of its definition of a
neck. The rest of the argument is elementary and self-contained.

Ledger:
`runs/fa_banach_001/ledger/results/0610904_legendrian_necks_are_convex_normal_lifts.json`.
