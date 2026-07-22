# Verification report

Verdict: `likely valid stronger partial result; human review recommended`.

## Claims checked

For Carter's Hermitian weighted Orlicz algebra `A=L^Phi(G,omega)` on a
locally elliptic group:

- every clopen subset of `Prim_*(A)` is synthetic;
- every finite closed family of admissible primitive points is synthetic;
- hence every finite or clopen coadjoint-orbit subset is synthetic for a
  p-adic unipotent matrix group.
- compactness alone is not sufficient: Malliavin's theorem yields a compact
  nonsynthesis subset for the unweighted abelian case `U_2(k)=(k,+)`.

## Clopen proof audit

1. **Corner properties.** For a compact-open subgroup `H`,
   `B_H=e_H*A*e_H` is unital with identity `e_H`. It is Hermitian because a
   nonreal resolvent for a self-adjoint corner element is obtained by adding
   `1-e_H` in the unitization and compressing the inverse. It is semisimple
   because `A` embeds faithfully in its group C-star envelope.
2. **Primitive corner correspondence.** Compression identifies
   `Prim_*(B_H)` with the open set of primitive representations of `A` for
   which `pi(e_H)` is nonzero. Intersecting a clopen `C` with this open set
   remains clopen in the corner spectrum.
3. **Central idempotent.** For a clopen split `Y` and `Y^c` of the corner
   spectrum, let `I=ker(Y)` and `J=ker(Y^c)`. Their intersection is zero. If
   `I+J` were proper, a simple module of the unital corner would give a
   primitive ideal in both hulls. Hence `I+J=B_H`. Writing
   `e_H=p+q`, with `p in I` and `q in J`, gives complementary central
   idempotents. Star-closedness and uniqueness make them self-adjoint.
4. **Locally finite approximation.** The compactly supported locally constant
   corner is dense. Every one of its elements lies in a finite-dimensional
   Hecke C-star algebra with unit `e_H`.
5. **Spectral separation.** Self-adjoint Hecke approximants `d_n -> p` commute
   with `p` because `p` is central. Their spectra split into clusters near
   zero and one. The spectrum computed in the finite Hecke algebra equals the
   corner spectrum: a missing finite-dimensional eigenvalue would have a
   nonzero spectral projection killed by an inverse in the corner.
6. **Riesz projections.** The projection `r_n` for the cluster near one lies
   in the same finite Hecke algebra and converges to `p` in the Orlicz norm.
   On representations in `C`, `pi(d_n) -> pi(p)=0`, so `pi(r_n)=0` for large
   `n`.
7. **Source ideal membership.** Every locally constant compactly supported
   element of `ker(C)` lies in `j(C)`: its finite-Hecke central support is
   annihilated on `C` and is recovered exactly by Carter's `A_gamma`
   functional calculus. Thus `r_n in j(C)` and closedness gives `p in j(C)`.
8. **Globalization.** If `f in ker(C)`, then `e_H*f*e_H=p_H*(e_H*f*e_H)` by
   separation through all irreducible representations. Hence each smoothed
   element lies in `j(C)`. Carter's approximate identity gives convergence
   to `f`.

## Finite-set proof audit

- CCR makes each represented `e_H` a compact orthogonal projection, hence
  finite rank.
- For fixed `H` and finitely many representations, evaluation of the corner
  has finite-dimensional range. A bounded linear lift corrects dense Hecke
  approximants into the common kernel.
- No uniform bound in `H` is needed: correction is completed at each fixed
  corner before the approximate-identity limit.

## Edge cases

- `C` may be clopen but noncompact; compactness is not used.
- A compact-open subset of a non-Hausdorff primitive space is covered only
  when it is also closed, as required by Carter's definition of `j(C)`.
- The clopen theorem does not require CCR or admissibility.
- The finite theorem permits infinite-dimensional irreducible
  representations when their compact-open fixed-vector spaces are finite.
- No result is claimed for infinite closed sets with nonempty boundary.

## Sharpness audit

- `Phi(t)=|t|` and `omega=1` give the unweighted algebra `L^1(k)` inside the
  source framework.
- The additive group of a non-archimedean local field is noncompact and
  Pontryagin self-dual.
- Malliavin proved failure of spectral synthesis for `L^1(G)` on every
  noncompact locally compact abelian `G`; de Leeuw--Mirkil record the stronger
  compact-set formulation for every nondiscrete dual.
- Such failure gives an ideal `I` with hull `C` and
  `I` strictly contained in `ker(C)`. Carter's minimal-hull theorem gives
  `j(C) subset I`, so `j(C)` is strictly smaller than `ker(C)`.

## Computation

No numerical computation is used. Verification is symbolic and reduces to
finite-dimensional Hecke algebras only after fixing a compact-open corner.

## Primary human-review focus

Verify the corner primitive-spectrum correspondence and the equality of the
finite-Hecke and corner spectra for each self-adjoint approximant. If both
pass, the Riesz-projection and closure steps are standard Banach-algebra
arguments.
