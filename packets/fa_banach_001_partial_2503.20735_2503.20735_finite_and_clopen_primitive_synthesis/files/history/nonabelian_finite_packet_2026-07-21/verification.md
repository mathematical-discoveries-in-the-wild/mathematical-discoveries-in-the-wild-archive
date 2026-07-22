# Verification report

Verdict: `likely valid substantial partial result; human review recommended`.

## Claim checked

For Carter's Hermitian weighted Orlicz algebra `A=L^Phi(G,omega)` on a
locally elliptic CCR group, every finite closed subset of `Prim_*(A)` is a set
of synthesis. Since p-adic unipotent matrix groups are CCR and have `T_1`
primitive spectrum, every finite subset of their coadjoint-orbit space is
covered.

## Independent proof checks

1. **Compact-open smoothing.** Carter's Proposition 2.16(ii) supplies the
   normalized compact-neighbourhood indicators as an approximate identity in
   `A`. Compact-open subgroups are cofinal at the identity, and their
   indicators are self-adjoint idempotents. Therefore
   `e_H*f*e_H -> f` in `A`.
2. **CCR gives finite corners.** In an irreducible representation `pi`,
   `pi(e_H)` is the orthogonal projection onto the `H`-fixed vectors. CCR
   gives `pi(C^*(G))=K(H_pi)`, so this projection is compact and hence has
   finite rank.
3. **Exact kernel correction.** For fixed `H` and a finite family `pi_i`, the
   map on the corner `e_H*A*e_H` takes values in a finite direct sum of matrix
   algebras. The locally constant compactly supported corner is dense, so its
   image equals the full finite-dimensional image. A linear right inverse is
   automatically bounded and corrects approximants to lie exactly in the
   common kernel.
4. **Finite Hecke containment.** Every compactly supported locally constant
   function belongs to a finite-dimensional convolution star algebra obtained
   from a compact open `K` and an open normal subgroup `H` of `K`.
5. **Central support.** If a representation annihilates an element `d` of a
   finite-dimensional C-star algebra, its kernel contains the ideal generated
   by `d`, and therefore contains the central support projection `p_d`.
6. **Membership in Carter's generator.** Scale `p_d` to `a p_d` with
   `0<a<2*pi` and `||a p_d||_1<=1`. Every representation in `C` annihilates
   it. Carter's `A_gamma` cutoff can be zero near zero and one at `a`, and the
   explicit power-series calculus gives `phi{a p_d}=p_d`. Thus
   `p_d in m(C)` and `d=p_d*d in j(C)`.
7. **Closure.** Corrected test functions converge to each smoothed kernel
   element, and compact-open smoothing converges to the original element.
   Since `j(C)` is closed, `ker(C)<=j(C)`. Carter already proves the reverse
   inclusion.
8. **Closedness of finite sets.** A CCR C-star algebra has maximal primitive
   ideals, hence a `T_1` primitive spectrum. Carter's homeomorphisms transfer
   this to `Prim_*(A)` and to the coadjoint-orbit space.

## Stress tests and edge cases

- The proof permits infinite-dimensional irreducible representations; only
  the compact-open fixed-vector spaces must be finite dimensional.
- A representation may restrict degenerately to a finite Hecke algebra. Its
  kernel is still a two-sided star ideal, which is all the central-support
  argument needs.
- The linear lift depends on `H` and need not be uniformly bounded as `H`
  shrinks. Uniformity is unnecessary: first prove each fixed smoothed element
  belongs to `j(C)`, then use closedness and the approximate identity.
- The theorem does not assert synthesis for infinite discrete, compact-open,
  or arbitrary closed subsets in the nonabelian primitive spectrum.

## Computation

No numerical computation is used. The verification is symbolic and
finite-dimensional at each fixed compact-open corner.

## Primary human-review focus

Confirm the equality between the dense corner image and the full corner image
before choosing the finite-dimensional right inverse, and check the formula
`phi{a p}=p` against Carter's nonunital periodic functional-calculus
normalization.

