# Sharp time decay at the bottom of the spherical spectrum

Status: `candidate_full_likely_valid`

Source: Yulia Kuznetsova and Zhipeng Song, *Shifted wave equation on
noncompact symmetric spaces*, arXiv:2504.21479v2.

Source location: Introduction, page 3.  After comparing the gapless
`t^{-nu}` estimate with the positive-gap `t^{-nu/2}` estimate, the authors
conjecture that both powers are optimal for small spatial parameter `x^+`.

## Result

The packet proves locally uniform asymptotic formulas, not just lower bounds.
Let `l` be the real rank, let `d` be the number of positive reduced roots,
and set `nu=2d+l`.  There is an explicit constant `A_c>0`, determined by the
leading homogeneous part of the Harish-Chandra Plancherel density, such that
for every compact `Q` in `G`:

```text
k_t(x) = C_G A_c phi_0(x) psi(0) Gamma(nu)
         exp(i*pi*nu/2) t^{-nu} + o_Q(t^{-nu})
```

for every admissible Schwartz amplitude `psi` with `psi(0) != 0`.

For a positive spectral gap `epsilon` and a smooth even spectral amplitude
`m` with `m(0) != 0`,

```text
k_{t,epsilon}(x)
  = C_G A_c phi_0(x)m(0) 2^{nu/2-1} epsilon^{nu/4} Gamma(nu/2)
    exp(i*t*sqrt(epsilon)+i*pi*nu/4) t^{-nu/2}
    + o_Q(t^{-nu/2}).
```

The second formula applies in particular to the Anker-Zhang Bessel amplitude
`m(r)=(r^2+epsilon)^{-alpha/2}` when `Re(alpha)>n`.  Both leading constants
are nonzero, proving the two powers pointwise sharp on every compact spatial
set, hence in the small-`x^+` regime of the conjecture.

## Mechanism

The Gindikin-Karpelevich product gives

```text
|c(r omega)|^{-2}
  = D r^{2d} product_alpha <omega,alpha_0>^2 (1+O(r^2)),  D>0.
```

After the polar Jacobian, the radial amplitude therefore has exact endpoint
order `r^{nu-1}` with a strictly positive angular coefficient.  The gapless
phase is linear and yields `t^{-nu}`.  With a positive gap, the exact change
`s=sqrt(r^2+epsilon)-sqrt(epsilon)` turns the quadratic endpoint into an
amplitude of order `s^{nu/2-1}`, yielding `t^{-nu/2}`.

## Scope

- This fully answers the first sharpness conjecture on page 3.
- It proves pointwise kernel sharpness.  It does not claim sharp lower bounds
  for every finite-`p` dispersive operator norm.
- If the amplitude vanishes at spectral zero, faster decay can occur.
- The separate conjecture that the distinguished-Laplacian `L^1` growth
  exponent `(nu-1)/2` is optimal is not addressed.

## Verification and novelty

The proof uses only spherical inversion, the Gindikin-Karpelevich formula and
the standard endpoint Fourier lemma.  The included checker audits the two
exponents, the positive-gap Jacobian coefficient, and positivity in an `A_2`
root-system model.  See `verification.md` for the adversarial check.

Cheap run indexes were searched by arXiv id, title, and the exact conjecture.
A bounded primary arXiv search covered the source paper, the exact sharpness
phrase, and the Anker-Zhang antecedent (arXiv:2010.08467).  No later paper
claiming this endpoint asymptotic or resolving the conjecture was found.  This
is not an exhaustive novelty certification.

Human review recommendation: **send to a harmonic analyst**.  The highest
value checks are the uniform factorization of the `c`-function density at the
root hyperplanes and the nonstationary treatment of the uncut Bessel tail.

