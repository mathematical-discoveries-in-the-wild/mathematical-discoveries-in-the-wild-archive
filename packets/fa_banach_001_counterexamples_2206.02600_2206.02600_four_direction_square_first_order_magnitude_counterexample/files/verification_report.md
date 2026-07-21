# Verification report

Date: 2026-07-21

Verdict: pass; counterexample likely valid pending human review.

## Claim compatibility

- The source statement is Conjecture 1.7 on page 4 of arXiv:2206.02600.
- The example uses a finite-dimensional hypermetric normed space
  \(E=(\mathbb R^2,\|\cdot\|_E)\).
- \(K=[-1,1]^2\) is a compact full-dimensional convex body.
- The proved limsup bound is strictly below \(\mu_1^E(K)/4\), so it
  contradicts the exact asserted equality without assuming that the limit
  exists.

## Proof audit

1. The explicit oriented-indicator map satisfies
   \(\|\Phi(x)-\Phi(y)\|_H^2=\|x-y\|_E\).
2. The natural center has squared radius \(1+\sqrt2\).
3. The relation
   \(u_3u_3^T+u_4u_4^T=u_1u_1^T+u_2u_2^T\) produces a vector \(g\)
   orthogonal to every \(\Phi(x)\).
4. The natural center has nonzero \(g\)-component. Removing it reduces the
   squared radius exactly by \(3/[4(1+2\sqrt2)]\).
5. On a Hilbert sphere of squared radius \(R^2\), the expansion
   \(e^{2t\langle v_x,v_y\rangle}\) is a sum of nonnegative tensor-square
   kernels. This holds for finite signed Borel measures because the series is
   uniformly convergent on the bounded sphere.
6. Proposition 2.3 of the source has \(c_1=2\), giving
   \(\mu_1^E(K)=8+8\sqrt2\).

No unproved dependency remains.

## Symbolic check

Command:

    conda run --no-capture-output -n sandbox python code/verify_constants.py

The check passed. It verified the tensor relation and returned:

    <c,g> = 2
    ||g||^2 = 16/3 + 32*sqrt(2)/3
    R_0^2 = 1 + sqrt(2)
    mu_1^E(K) = 8 + 8*sqrt(2)
    strict gap = 0.391805812446...

This code checks exact constants and signs; it is not used as a substitute
for the analytic proof.

## Source and rendering check

- The source PDF is the 14-page arXiv paper and opens correctly.
- The page-4 crop contains the complete statements of Corollary 1.6 and
  Conjecture 1.7 and is readable at normal review zoom.
- The six-page solution packet compiled without undefined references or
  overfull boxes.
- All six rendered pages were visually inspected. No clipping, overlap,
  broken glyphs, or unreadable content was found.

## Novelty bound

Cheap run indexes and a bounded web/arXiv search were completed as described
in the packet. No existing resolution or matching construction was found.
This was not an exhaustive MathSciNet/zbMATH search, so novelty confidence is
moderate.
