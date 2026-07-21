# Verification report

## Claim audited

For the periodic one-dimensional Allen--Cahn equation

```text
du=(Delta u+u-u^3)dt+sqrt(2)u^2dW
```

and deterministic constant initial data `u_0=x_0>0`, the global solution has

```text
E sup_{0<=t<=T} ||u(t)||_L2^2 = infinity
```

for every `T>0`.

## Mathematical audit

1. **Invariant mode.** On constant functions the Laplacian vanishes and all
   remaining coefficients are pointwise. Thus `u(t,x)=X_t` reduces the SPDE
   exactly to `dX=(X-X^3)dt+sqrt(2)X^2dW`.
2. **Itô calculation.** For `Y=X^{-1}`, direct differentiation gives
   `dY=(-Y+3/Y)dt-sqrt(2)dW`. Therefore
   `R=Y/sqrt(2)` satisfies `dR=(-R+3/(2R))dt+dB` after replacing `W` by `-B`.
3. **OU identification and globality.** The last equation is the radial SDE of
   a four-dimensional OU process. The identity
   `e^t Z_t=z_0+B_tilde((e^(2t)-1)/2)` and polarity of points for four-dimensional
   Brownian motion show that its radius never reaches zero. Continuity then
   makes `X=1/(sqrt(2)|Z|)` finite on every compact interval.
4. **One-time small balls.** On `[T/2,T]`, the four-dimensional Gaussian
   densities of `Z_t` are uniformly bounded above and bounded below on the
   unit ball. Hence `P(|Z_t|<=epsilon)` is comparable to `epsilon^4`.
5. **Two-time estimate.** At lag `h`, the conditional covariance is
   `q_h I_4`, where `q_h=(1-e^(-2h))/2` is comparable to `h`. The Gaussian
   density bound gives
   `P(|Z_t|<=epsilon | Z_s)<=min(1,C epsilon^4 h^(-2))`.
6. **Occupation second moment.** Integrating the previous bound and the
   one-time upper bound gives `E O_epsilon^2<=C epsilon^6`, while
   `E O_epsilon>=c epsilon^4`. Cauchy--Schwarz yields a hitting probability at
   least `c epsilon^2`.
7. **Divergence.** On a hit, `sup X_t^2>=1/(2epsilon^2)`. Substitution
   `epsilon=(2y)^(-1/2)` gives `P(sup X_t^2>=y)>=c/y` for large `y`; layer cake
   makes the expectation infinite.
8. **SPDE norm.** A constant function has squared `L^2` norm equal to the
   torus volume times `X_t^2`, so the scalar divergence is exactly the desired
   SPDE divergence.

No step uses simulation or an asymptotic independence assumption.

## Reusable exact check

Run from the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2501.18561_critical_allen_cahn_l2_supremum_counterexample/code/verify_reduction.py
```

The script performs three exact symbolic identity checks (the reciprocal
generator, the radial rescaling, and the OU reciprocal) and one exact
piecewise-integral calculation. All checks pass. This supports the algebra; it
does not replace the probabilistic proof.

## Source and scope audit

- Source PDF: arXiv:2501.18561v5, dated 2025-08-28.
- Exact location: page 92, Problem 4 and the paragraph immediately below it.
- The source explicitly says that the `p=2` supremum estimate is excluded in
  general, asks whether it holds under the variational assumptions, and says
  the displayed Allen--Cahn model is unknown at `gamma^2=2`.
- The counterexample uses smooth deterministic data and the exact critical
  coefficient, so the right side of the proposed estimate is finite.
- The result does not address Problem 5 (continuous dependence in the energy
  space), nor any subcritical estimate with `gamma^2<2`.

## Bounded novelty search (2026-07-21)

The following were checked:

- cheap run indexes for `2501.18561`, `critical variational SPDE`, `Allen-Cahn`,
  `quadratic noise`, `gamma^2=2`, and `radial Ornstein-Uhlenbeck`;
- the current official arXiv record and v5 source;
- exact-phrase web searches for the source problem title and the displayed
  model at the critical coefficient;
- searches combining reciprocal transforms, radial OU processes, and
  quadratic multiplicative noise;
- the closest 2026 arXiv reaction--diffusion result returned by the search,
  whose abstract concerns local theory rather than this energy estimate.

No exact later answer was found. The search was deliberately bounded and does
not establish bibliographic priority.
