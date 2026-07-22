# Verification report

## Claim checked

For `F=2Z`, the measure

\[
\mu_*=(\delta_{1/4}+\delta_{3/4})/2
\]

lies in `S_e(F)` but not in `Sigma(F,zeta)`. This gives a negative answer to
Question 3.4 of arXiv:1012.4549 as stated.

Verdict: `likely valid`.

## Step checks

1. **Minimality.** The shift orbit of `chi_(2Z)` consists of exactly the even
   and odd indicator sequences. A finite periodic orbit is a minimal compact
   dynamical system. The sequence is nonconstant.

2. **Invariant measure.** The only invariant probability on this transitive
   two-cycle is the uniform measure `zeta=(delta_x0+delta_x1)/2`.

3. **Correlation class.** The cylinder `X_1(F)={b:b(0)=1}` equals `{x0}`.
   Hence a supported function has values `(c,0)`. Its lag-`j` correlation is
   `|c|^2/2` for even `j` and zero for odd `j`. Fourier uniqueness gives
   `nu_g=(|c|^2/2)m_0`, where
   `m_0=(delta_0+delta_(1/2))/2`. Conversely every nonnegative multiple is
   obtained by choosing `c`, so `Sigma(F,zeta)` is exactly this ray.

4. **Membership in the spectral envelope.** The polynomial

   \[
   f_N(t)=N^{-1/2}\sum_{k=0}^{N-1}e^{2\pi i k(2t-1/2)}
   \]

   has norm one and frequencies in `2Z`. Its squared modulus is a Fejér kernel
   pulled back by `t -> 2t-1/2`; it converges weak-star to the uniform measure
   on the two solutions of `2t=1/2 mod 1`, namely `{1/4,3/4}`.

5. **Extremality.** Every squared modulus with even frequencies is invariant
   under translation by `1/2`, hence so is every element of `S(2Z)`. If
   `mu_*=(mu_1+mu_2)/2` with invariant probabilities `mu_i`, positivity forces
   both `mu_i` to be supported on `{1/4,3/4}`. Invariance forces equal weights,
   so `mu_1=mu_2=mu_*`. Thus `mu_*` is extreme even in the larger invariant
   simplex and therefore in `S(2Z)`.

6. **Failure of the proposed inclusion.** The supports of `mu_*` and `m_0`
   are disjoint, so the probability `mu_*` is not a nonnegative multiple of
   `m_0`.

## Remaining interpretive risk

The written question assumes only that `chi_F` is minimal, which includes
nonconstant periodic sequences. The surrounding motivation emphasizes
Thue--Morse. If the author intended “aperiodic minimal” without saying so, the
packet settles only the literal formulation, not that intended strengthening.

