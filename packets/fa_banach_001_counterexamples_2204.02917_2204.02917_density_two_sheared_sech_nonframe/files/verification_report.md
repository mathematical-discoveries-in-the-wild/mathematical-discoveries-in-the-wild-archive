# Verification report

Verdict: `passed - candidate counterexample likely valid`

Date: 2026-07-21  
Agent: `agent_lane_08`  
Model: `GPT5.6`

## Command

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2204.02917_density_two_sheared_sech_nonframe/code/verify_zero_box.py
```

## Certified checks

- Symmetric interval summation through (n=240), with explicit geometric tails.
- \(|\Re F(a_0,c_0)|<10^{-40}\) and \(|\Im F(a_0,c_0)|<10^{-40}\).
- Directed enclosures for (F_a) and (F_c).
- Every entry of (A J_0-I) has absolute value below (10^{-9}).
- Uniform Hessian bounds (B_{aa}=400), (B_{ac}=2100), (B_{cc}=14000) on the proof box.
- Scalar Taylor remainder at most (9.3\times10^{-9}).
- Preconditioned row remainders at most (1.711\times10^{-9}) and (3.374\times10^{-10}).
- Strict Poincare--Miranda face margins at least (9.9828\times10^{-7}) and (9.9966\times10^{-7}).

The script printed `CERTIFIED` and exited with status zero.

## Independent structural checks

- The simultaneous Zak-zero obstruction was derived directly from the Zak images of the density-two Gabor atoms.
- The forced second zero was checked by pairing indices (k\leftrightarrow1-k).
- The covariance
  \(C_q^{-1}\pi(x,\omega)C_q\doteq\pi(x,\omega-qx)\)
  was recomputed directly.
- The lattice determinant is (a_*\cdot(2a_*)^{-1}=1/2), hence its density is (2).
- A 60-decimal exploratory sum found the zero near
  \((a,c)=(1/\sqrt{28},15/28)\); the promoted proof does not assume that this center is an exact zero.

## Reviewer focus

The only machine-trust layer is `mpmath.iv` directed interval arithmetic for finite elementary-function evaluations. The infinite series tail and the Taylor remainder are bounded symbolically in the proof and reproduced in the script. A reviewer who prefers Arb/MPFI should rerun the same finite certificate there; the face margins exceed the nonlinear error by more than two orders of magnitude.

