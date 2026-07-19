# Verifier report

Status: **PASS for the claimed removal of Type L; human expert review required.**

## Claim-by-claim audit

1. **Exact target - pass.** The final remark on page 16 of arXiv:2211.01479 asks whether the restriction that `H` be a Type L sub-semihypergroup can be removed from Theorem 3.5. The claimed theorem gives exactly the missing implication `(3) => (1)` without Type L.

2. **Normalized restriction is a mean - pass.** If `alpha=m(chi_H)>0` and `e_H(phi)(mu)=phi(mu_H)`, then `m_0=alpha^{-1}m composed with e_H` is positive and `m_0(1_H)=alpha^{-1}m(chi_H)=1`.

3. **Exact defect identity - pass.** For `nu in P(H)`, its extension `bar_nu=nu^e`, and `Q_nu(mu)=(bar_nu*(mu_{H^c})^e)_H`, bilinearity and `H*H subset H` give

   `e_H(L_nu phi)-L_{bar_nu}e_H(phi)=-phi composed with Q_nu`.

4. **Incoming-mass functional - pass.** The functional `g_nu=L_{bar_nu}chi_H-chi_H` is positive. For every positive `mu`, convolution of `bar_nu` with the `H`-part of `mu` stays in `H` and retains its total mass, so

   `g_nu(mu)=(bar_nu*(mu_{H^c})^e)(H)=||Q_nu(mu)||`.

5. **Lattice domination - pass.** The map `Q_nu` is positive, hence `|Q_nu(mu)| <= Q_nu(|mu|)`. Therefore the modulus in the dual Banach lattice satisfies

   `|phi composed with Q_nu| <= ||phi|| g_nu`.

6. **Mean-zero defect - pass.** Topological left `H`-invariance applies to `bar_nu`, whose support lies in `H`, and gives `m(g_nu)=0`. Positivity of `m` and the preceding domination imply `m(phi composed with Q_nu)=0`.

7. **TLIM conclusion - pass.** Combining the zero defect with `m(L_{bar_nu}e_H(phi))=m(e_H(phi))` proves `m_0(L_nu phi)=m_0(phi)` for every `nu in P(H)` and `phi in M(H)^*`.

## Adversarial failure modes

- Closedness of `H` is used as in the source definition of a sub-semihypergroup, so measures supported in `H` convolve to measures supported in `H`.
- The argument uses topological `H`-invariance for all probability measures supported in `H`, not merely invariance under point masses.
- The domination is an order statement in `M(K)^*`, not just an estimate on positive test measures. It follows from positivity of `Q_nu` and `|Q_nu(mu)| <= Q_nu(|mu|)`.
- No Type L inverse-set identity, involution, identity element, commutativity, or hypergroup axiom is used.
- The argument does not address whether left amenability implies topological left amenability.

## Novelty audit

The run registry, solution, attempt, and proof-gap indexes were searched for arXiv:2211.01479, Type L sub-semihypergroups, and topological left `H`-invariant means. The local arXiv corpus was searched for the same terminology, including the author's later arXiv:2404.18261. Exact-phrase web searches checked the arXiv record, the 2024 Forum Mathematicum publication, author publication listings, and later semihypergroup amenability/fixed-point material. No later answer to the Type L question was found. This bounded search does not establish originality.

## Recommended human checks

1. Verify the dual Banach-lattice modulus step under the source's complex-measure conventions.
2. Confirm that the source's notation `chi_H` is exactly the mass functional used here for every closed sub-semihypergroup.
3. Search MathSciNet/zbMATH citation chains and the 2024 survey chapter for an equivalent incoming-mass argument under different terminology.
