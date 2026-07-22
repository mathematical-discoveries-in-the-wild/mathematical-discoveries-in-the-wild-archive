# Verification report

Verdict: `likely valid candidate counterexample / full resolution`.

## Finite-output theorem audit

1. For `p<infinity`, `C_c^infinity(R^d)` is dense in `L^p(mu)` for every
   Radon measure.  For `p=infinity`, uniform convergence in `C_0(R^d)` implies
   convergence in `L^infinity(mu)`, so assumed closability induces a closable
   operator from `C_0(R^d)`.  If equality `mu`-a.e. failed to determine the
   output, the original graph would already contain two outputs over one
   input and would be nonclosable.
2. The standard graph-annihilator argument shows that a densely defined
   closable operator has weak-star dense adjoint domain.
3. For an adjoint-domain element `phi`, the distribution
   `nu=phi mu` is a locally finite signed measure and `Delta nu` is another
   locally finite signed measure.  In the `p<infinity` case the latter is
   `g mu`; in the `p=infinity`/`C_0` case it is supplied by the Riesz
   representation theorem.
4. If both `nu` and `Delta nu` are Radon measures, localize `Delta nu`,
   convolve it with the locally integrable fundamental solution of the
   Laplacian, and subtract.  The remainder is a harmonic distribution and
   therefore smooth.  Hence `nu` is locally an `L^1` function and is
   absolutely continuous with respect to Lebesgue measure.
5. The set of `phi` for which `phi mu` is absolutely continuous is norm closed
   in `L^{q'}(mu)` when `q>1`, and weak-star closed in `L^infinity(mu)` when
   `q=1`.  Adjoint density therefore makes every compact indicator belong to
   that set.  Thus every compact restriction of `mu` is absolutely continuous,
   hence so is `mu`.

## Strong-L-infinity counterexample audit

Take `mu=Lebesgue^d+delta_0`.  This is Radon and not absolutely continuous.
For every continuous compactly supported `f`,

```text
||f||_{L^infinity(mu)} = ||f||_infinity,
```

because the essential supremum with respect to full-support Lebesgue measure
already equals the ordinary supremum.

If `u_n -> 0` in `L^p(mu)` and `Delta u_n -> w` in `L^infinity(mu)`, then:

- for finite `p`, `u_n -> 0` in `L^p(Lebesgue)`, hence in distributions;
- for `p=infinity`, continuity turns the input norm into the uniform norm, so
  again `u_n -> 0` in distributions;
- the output sequence is uniformly Cauchy and converges uniformly to a
  continuous function `f` representing `w`;
- distributionally `Delta u_n -> 0`, while uniform convergence gives
  `Delta u_n -> f` distributionally, so `f=0` and `w=0`.

This is exactly sequential closability at zero.

## Edge cases

- The finite-output proof covers `q=1`: adjoint density and closedness are
  interpreted in the weak-star topology of `L^infinity(mu)`.
- The input endpoint `p=infinity` is handled through `C_0`, avoiding any false
  density claim for `C_c^infinity` in `L^infinity(mu)`.
- The source domain is `C_c^2`; the positive theorem may be tested on its
  `C_c^infinity` restriction, while the counterexample proof works directly
  for all `C_c^2` functions.
- No sufficiency claim is made for absolutely continuous measures.

## Human-review focus

The two highest-value checks are the local lemma
`nu, Delta nu in M_loc => nu << Lebesgue` and the use of weak-star closedness
when the finite output exponent is `q=1`.
