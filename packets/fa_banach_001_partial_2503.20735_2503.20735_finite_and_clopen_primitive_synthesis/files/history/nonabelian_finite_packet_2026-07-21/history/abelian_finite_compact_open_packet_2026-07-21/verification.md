# Verification report

Verdict: `likely valid partial result; human review recommended`.

## Claim checked

For an abelian locally elliptic group `G` and a Hermitian weighted Orlicz
algebra `A = L^Phi(G,omega)` satisfying `Phi in Delta_2` and
`1/omega in L^Psi(G)`, every finite or compact-open subset of `dual(G)`
satisfies `ker(C) = j(C)` for Carter's ideal `j(C)`.

## Independent proof checks

1. **Test-function density.** Under `Delta_2`, compactly supported functions
   are dense in the Orlicz space. The compact-open basis of a locally elliptic
   group uniformly approximates continuous compactly supported functions by
   compactly supported locally constant functions. Local boundedness of the
   weight converts uniform approximation on a fixed compact set to weighted
   Orlicz-norm approximation.
2. **Fourier stability.** For compact-open `K <= G`,
   `Fourier(1_(x+K)) = measure(K) conjugate(chi(x)) 1_(K^perp)`. Thus the
   compactly supported locally constant test algebra is Fourier invariant.
3. **Continuous character evaluations.** Orlicz-Holder and
   `1/omega in L^Psi` give `abs(Fourier(f)(chi)) <= ||f||_1 <= H ||f||_A`.
4. **Exact source-ideal cutoff.** If compact-open `U` misses `C`, scale
   `e_U = Fourier^{-1}(1_U)` to a self-adjoint `h` of `L^1`-norm at most one.
   Carter's `A_gamma` cutoff can be chosen zero near zero and one at the
   nonzero value of `Fourier(h)`. Representation compatibility gives
   `phi{h} = e_U`, so `e_U` belongs to `m(C)`, hence to `j(C)`.
5. **Finite sets.** Pairwise disjoint compact-open neighborhoods provide
   Kronecker Fourier interpolants. Correcting dense test approximants by their
   finitely many character values forces vanishing near the finite set, while
   the corrections tend to zero in `A`.
6. **Compact-open sets.** The idempotent with Fourier transform `1_C` removes
   the entire Fourier restriction to `C`. Banach algebra submultiplicativity
   preserves convergence of the corrected approximants.
7. **Reverse inclusion.** Every generator of `j(C)` is annihilated by all
   characters in `C`, so `j(C) <= ker(C)` exactly as in Carter's Theorem 7.1.

## Edge cases

- The zero approximant has empty Fourier support and is harmless.
- Finite subsets are closed because `dual(G)` is Hausdorff.
- Compact-open subsets are closed and their indicators are valid Fourier test
  functions.
- No discreteness or compactness of `G` is assumed beyond local ellipticity.

## Computation

No computation is used or needed; the verification is entirely symbolic.

## Primary human-review focus

Confirm that the source's `A_gamma` cutoff proposition permits the prescribed
value `phi(a)=1` after choosing `0<a<2*pi`, and confirm the standard global
`Delta_2` density statement for the exact Orlicz norm convention used in the
paper.

