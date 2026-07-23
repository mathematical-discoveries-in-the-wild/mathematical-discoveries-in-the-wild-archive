# Verifier report

Verdict: PASS — candidate counterexample likely valid.

Claim verified: for every pair of continuous nonnegative weights that vanish
on upper half-lines, the product of the two Legendre-dual polar-volume
quantities has infimum zero on the full finite super-coercive class. If both
weights are nonzero at positive levels, the product has infinite supremum
even on even radial `C^1` strictly convex functions normalized by
`u(0)=min u=0`.

Logical audit:

1. The shifted quadratic `u_c(x)=|x|^2/2+c` and its conjugate
   `u_c*(y)=|y|^2/2-c` are finite, smooth, strongly convex, origin symmetric,
   and super-coercive.
2. Its two valuation arguments are exactly `|y|^2/2+c` and
   `|x|^2/2-c`. Choosing `c` at or above the first weight’s upper-support
   threshold makes the first factor identically zero.
3. The second factor remains finite: only a bounded ball can contribute, and
   the weight is bounded on the compact argument interval attained there.
4. For `u_p(x)=|x|^p/p`, `q=p/(p-1)`, the conjugate and valuation arguments
   are exactly `|y|^q/q`, `|y|^q/p`, and `|x|^p/q`.
5. Polar coordinates give the packet’s two formulas with prefactors
   `(n*kappa_n/q) p^(n/q)` and `(n*kappa_n/p) q^(n/p)`. The substitutions and
   exponents were recomputed independently.
6. Positivity on fixed compact subintervals of `(0,infinity)` gives uniform
   positive lower bounds for both Mellin moments. Hence the product is at
   least a constant times `q^(n/p-1)`, which diverges because
   `n/p-1 -> n-1 > 0` for `n>=2`.
7. Nonnegativity is used correctly to identify the infimum as zero. The
   additional positive-level nontriviality is stated exactly where needed for
   the upper obstruction.

Computational audit:

- Command:
  `conda run --no-capture-output -n sandbox python code/verify_radial_families.py`
- The script tested five Mellin exponents by Simpson quadrature. Relative
  errors ranged from about `4.3e-15` to `2.6e-8`.
- For the sample weight `(1-t)_+`, dimensions `n=2,3`, and six values
  `p=1.5,1.2,1.1,1.05,1.02,1.01`, the product increased from `14.389` to
  `30239.7` in dimension two and from `39.4784` to `3.85656e6` in dimension
  three.
- The shifted-quadratic first factor is zero exactly for `c=1` with this
  sample weight.

Source and novelty audit:

- The source crop contains Theorem 1.3* and the complete question on PDF
  page 4.
- Cheap run indexes showed no duplicate.
- Bounded arXiv/web searches found no direct answer. The apparently closest
  later paper, arXiv:2412.05001, concerns different Brunn–Minkowski and
  isoperimetric inequalities; its full text contains neither “polar volume”
  nor the target arXiv id.

Scope warning: the source phrase “a similar inequality” is deliberately
broad. The packet proves a complete negative result for an unrestricted
positive-lower/finite-upper product inequality in the source’s nonnegative
upper-supported valuation class. It does not settle every one-sided,
differently normalized, differently combined, or outside-weight-class
variant.
