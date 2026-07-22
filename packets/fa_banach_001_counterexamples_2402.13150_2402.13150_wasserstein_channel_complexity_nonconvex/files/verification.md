# Verification report

Verdict: `candidate_counterexample_likely_valid`.

## Source match

- Official source: arXiv:2402.13150v4, printed page 18, Section 5.1.
- Equation (37) defines `C_W(Phi)=max_rho d_A(rho,Phi(rho))`.
- The next page explicitly says that whether this quantity is convex is open.
- Section 3.1 chooses the symmetric qubit cost from all three Pauli matrices;
  this is exactly the cost used in the packet.
- Section 2 supplies the pure-marginal and self-cost formulas used to derive
  the displayed expression for `d_s^2`.

## Exact symbolic check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2402.13150_wasserstein_channel_complexity_nonconvex/code/verify_counterexample.py
```

The script checks, with exact SymPy arithmetic:

1. `C_s=8(I-|Omega><Omega|)` and spectrum `{0,8,8,8}`;
2. the `sigma_x`, `sigma_y`, and `sigma_z` pure-input contributions;
3. `d_s^2=4t+4sqrt(t(1-t))`;
4. at `t=1/4`, the squared lower bound is `1+sqrt(3)`;
5. the squared convexity upper bound is `1/2`, leaving the positive exact gap
   `1/2+sqrt(3)`.

Result: `VERDICT: all exact symbolic checks passed`.

This computation is redundant and finite-dimensional. The packet proves each
identity algebraically, so correctness does not depend on SymPy.

## Adversarial checks

- **Channel validity:** `Id`, unitary conjugation by `sigma_x`, and their
  convex mixture are completely positive trace-preserving maps.
- **Correct affine comparison:** `Lambda_t=(1-t)Id+tX` lies on the channel
  segment whose convexity inequality is tested.
- **Max versus one test state:** using `rho_0` produces a lower bound on the
  maximum, which is the correct direction.
- **Endpoint estimate direction:** `C_W(X)<=2sqrt(2)` makes the convexity
  right-hand side no larger than `sqrt(2)/2`; an exact value of `C_W(X)` is
  unnecessary.
- **Diameter estimate:** `d_s^2=D_s^2-(nonnegative self-costs)<=D_s^2`, and
  `0<=C_s<=8I` gives `D_s^2<=8` for every coupling.
- **Normalization:** there is no missing factor `1/2` in the source cost
  definition. The source's spectral decomposition has eigenvalue 8 with
  multiplicity three, matching the packet.
- **Definiteness:** the proof needs only nonnegativity and zero self-distance;
  nevertheless, the full Pauli triple is the paper's standard nondegenerate
  symmetric qubit cost.

## Novelty bound

On 22 July 2026, the cheap run indexes and bounded web searches used the exact
source sentence, arXiv ids `2402.13150` and `2511.20450`, the source title and
authors, and combinations of `quantum Wasserstein complexity`, `convex`,
`channel`, `quadratic divergence`, and `Pauli`. No prior answer to this exact
question was found. Results about order-one/Hamming-Wasserstein complexity are
definitionally different. This supports, but cannot certify, novelty.

## Human-review focus

Recheck the source normalization in the pure-state formula and the identity
`sum_j sigma_j tensor sigma_j^T = 4|Omega><Omega|-I`. Everything else is a
direct scalar inequality.
