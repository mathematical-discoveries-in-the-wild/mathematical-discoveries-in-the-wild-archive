# Verification report

## Verdict

**Likely valid full solution**, pending human review.

For weakly convergent Borel probability measures `mu_n => mu` on a separable
Banach space `X`, the construction yields one separable reflexive Banach
subspace `Y`, compactly embedded in `X`, which carries every measure and the
weak convergence and admits an equivalent Fréchet-differentiable norm.

## Proof audit

1. **Skorokhod coupling.** Since `X` is Polish, realize the laws by
   `xi_n -> xi` almost surely in `X`.
2. **Difference random variable.** The sequence
   `D=(xi_n-xi)_n` lies in `c_0(X)` almost surely. Its finite truncations are
   measurable and converge to it in the `c_0(X)` norm, so `D` is measurable.
3. **Reflexive supports.** Apply Buldygin's theorem, as recalled by the source,
   to the laws of `xi` in `X` and `D` in `c_0(X)`. This gives compact
   injections from separable reflexive spaces `R` and `Z` carrying the two
   laws.
4. **Uniform coordinate tails.** If `J:Z -> c_0(X)` is compact and
   `A_n=Q_n J`, compactness of `J(B_Z)` implies
   `sup_(n>=N)||A_n|| -> 0`. The finite-net proof is included.
5. **Block construction.** Choose finite blocks `I_k` with
   `sup_(n in I_k)||A_n|| <= 4^(-k)` for `k>=2`. Let
   `E=(direct sum_k ell_1(I_k;Z))_ell_2` and
   `Tz=sum_k 2^k sum_(n in I_k) A_n z_n`.
6. **Reflexivity.** Each block is a finite direct sum of reflexive `Z`; the
   outer `ell_2` sum is separable and reflexive.
7. **Boundedness and compactness.** The block operator norms are at most
   `beta_k=2^k sup_(n in I_k)||A_n||`, with `(beta_k) in ell_2`. Finite block
   truncations are compact and converge to `T` in operator norm.
8. **Coordinate convergence.** For `n in I_k`, representing `A_n z` using
   `2^(-k)z` in the `n`th block coordinate gives range norm at most
   `2^(-k)||z||`. Hence all difference coordinates converge to zero in the
   assembled range norm.
9. **Final quotient.** On `H=R direct-sum_2 E`, the sum of the two compact
   maps into `X` is compact. The quotient by its kernel is separable and
   reflexive, injects compactly into `X`, contains `xi` and every `xi_n`, and
   has `xi_n -> xi` almost surely.
10. **Borel lifting.** Lusin-Souslin makes the compactly embedded range Borel
    in `X` with Borel inverse, so the variables and measures are genuinely
    defined on `Y`.
11. **Weak convergence and renorming.** Almost-sure convergence in `Y` implies
    weak convergence of laws by dominated convergence. A separable reflexive
    space has separable dual and hence an equivalent Fréchet-smooth norm;
    equivalent renorming preserves all established properties.

No numerical or computer-assisted argument is used.

## External inputs

- Skorokhod representation on Polish spaces.
- V. V. Buldygin, *The supports of probability measures in separable Banach
  spaces*, Theory Probab. Appl. 29 (1985), 546-549,
  doi:10.1137/1129067. The source paper explicitly recalls the required
  reflexive compact-support form.
- Lusin-Souslin for continuous injections between Polish spaces.
- The classical smooth-renorming theorem for spaces with separable dual.

## Novelty search

Bounded search date: **22 July 2026**.

Searched arXiv and web indexes using:

- arXiv id `1505.06235`, the exact title, and the concluding open-question
  wording;
- Buldygin's title and DOI;
- combinations of `compactly embedded`, `reflexive subspace`, `Fréchet
  differentiable norm`, `support`, and `weak convergence of probability/Radon
  measures`.

The search found the source paper, Buldygin's single-measure support theorem,
and related later work imposing additional moment or uniform-integrability
hypotheses, but no paper explicitly resolving this exact question. Novelty
confidence is **moderate**; exhaustive priority is not claimed.

## Scope and reviewer focus

- The theorem covers probability sequences, the exact scope of source
  question C.
- It does not claim the analogous result for arbitrary nets of sigma-finite
  measures mentioned separately in the source.
- Primary review focus: confirm the precise form of Buldygin's theorem, the
  compactness of the block operator, and the Borel lifting through the final
  quotient range.
- Recommendation: **verify and circulate**.
