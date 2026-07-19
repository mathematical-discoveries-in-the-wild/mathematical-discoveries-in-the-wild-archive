# Basis-free Lipschitz Malliavin chain rule

Status: `full_result_likely_valid`

Source paper: Matthijs Pronk and Mark Veraar, *Tools for Malliavin calculus in
UMD Banach spaces*, arXiv:1204.2946.

## Result

Pronk and Veraar prove a Lipschitz chain rule for `F in D^{1,p}(E_0)` under the
assumption that `E_0` has a Schauder basis, and ask in Remark 3.11 whether this
basis assumption can be avoided.

This packet proves that the basis assumption can be removed:

- for every Banach domain `E_0`, every UMD range `E_1`, and every Lipschitz
  `phi:E_0 -> E_1`, one has `phi(F) in D^{1,p}(E_1)` whenever
  `F in D^{1,p}(E_0)`;
- the pointwise derivative estimate
  `||D phi(F)(omega)||_{gamma(H,E_1)} <= Lip(phi) ||DF(omega)||_{gamma(H,E_0)}`
  holds almost surely;
- there is a bounded linear operator

```text
T_F: gamma(H,E_0) -> L^infty(Omega; gamma(H,E_1))
```

  with `||T_F|| <= Lip(phi)` such that the canonical amplification of `T_F` to
  `L^p(Omega; gamma(H,E_0))` sends `DF` to `D(phi(F))`.

This is the operator-valued conclusion of Pronk--Veraar Proposition 3.10, now
without a Schauder basis, separability, or approximation property assumption on
`E_0`.

## Proof Idea

The first step avoids approximating the entire Banach space.  Since
`F in D^{1,p}(E_0)` is defined as the closure of smooth finite-dimensional
random variables, approximate `F` itself by smooth random variables `F_n` whose
values lie in finite-dimensional subspaces.

On each finite-dimensional range, convolution gives smooth Lipschitz
approximations of `phi` with the same Lipschitz constant.  The smooth chain
rule and the ideal property of gamma-radonifying operators give uniform
derivative bounds.  Reflexive compactness and Mazur's lemma pass both
membership and the pointwise derivative bound to the limit.

The new final step removes the previous separability restriction.  The random
variable `DF` is strongly measurable, so its essential range lies in a
separable subspace `S` of `gamma(H,E_0)`.  On `S`, choose a measurable norming
functional for `DF`, giving a scalar contraction
`A:S -> L^infty(Omega)`.  Since scalar `L^infty` spaces are 1-injective
(Goodner--Kelley--Nachbin), extend `A` to all of `gamma(H,E_0)`.  Multiplying
this scalar extension by the normalized derivative
`D(phi(F))/||DF||` gives the desired operator `T_F`.

## Scope

The packet answers the `L(gamma(H,E_0), L^infty(Omega; gamma(H,E_1)))`
formulation in the source proposition.  It does not claim the stronger and
different random-operator-field assertion
`L^infty(Omega; L(gamma(H,E_0), gamma(H,E_1)))`, whose measurability subtleties
are explicitly noted in the source remark.

## History

The immediately preceding separable-domain partial packet is preserved at
`history/partial_packets/1204.2946_lipschitz_chain_rule_separable_domain/`.
That historical packet proved the membership theorem for arbitrary `E_0` and
the full operator-factor conclusion for separable `E_0`; the present packet
supersedes it by removing the separability restriction.

## Search Evidence

Cheap run indexes were searched for `1204.2946`, `Malliavin`, `UMD`,
`Lipschitz chain rule`, `basis`, and related stochastic integration terms.  Web
searches on 2026-06-23 for exact and close phrases such as
`"We do not know if the assumption that E_0 has a basis can be avoided"`,
`"Lipschitz" "Malliavin" "chain rule" "Schauder basis" "UMD"`, and
`"T_F" "gamma(H,E_0)" "Lipschitz" "Malliavin"` found the source paper but no
later exact resolution.

## Files

- `source_paper.pdf`: arXiv:1204.2946.
- `figures/open_problem_crop.png`: source Remark 3.11 containing the question.
- `main.tex` and `solution_packet.pdf`: proof packet.
- `history/partial_packets/1204.2946_lipschitz_chain_rule_separable_domain/`:
  superseded predecessor packet.
