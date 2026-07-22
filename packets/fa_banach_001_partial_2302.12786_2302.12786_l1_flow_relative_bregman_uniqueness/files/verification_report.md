# Verification report

Verdict: `partial_result_likely_valid`; expert review recommended.

## Manual proof checks

1. Confirmed the sign convention from the source: `q=div grad F(Du)` belongs to `∂(||·||_1^2/2)(u_t)`. Monotonicity therefore gives a nonpositive integrated flux term after integration by parts.
2. Expanded the time derivative of the one-sided Bregman divergence independently. The only nonlinear term is `grad F(a)-grad F(b)-D2F(b)(a-b)`, paired with `b_t`.
3. Checked constants: Hessian Lipschitz constant `K` gives remainder at most `K|a-b|^2/2`; gamma-convexity gives Bregman divergence at least `gamma|a-b|^2/2`; hence the Grönwall coefficient is `K/gamma`.
4. Checked the Dirichlet boundary term and the natural Neumann flux boundary term.
5. Checked the Neumann constant ambiguity separately through the L1 duality-map sign relation and connectedness.
6. For constant quadratic Hessian, verified that the Taylor remainder is exactly zero, so the extra strong regularity is unnecessary.

## Computational regression check

Command:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/2302.12786_l1_flow_relative_bregman_uniqueness/code/check_bregman_identity.py
```

The script uses 10,000 seeded random four-dimensional inputs for the nonlinear integrand `|xi|^2/2 + 0.7 sum log cosh(xi_j)`. It compares a centered finite-difference derivative of the Bregman divergence against the asserted identity and checks a valid global Taylor-remainder bound. This is a sign/algebra regression, not proof evidence.

Observed output:

```text
seed=230212786 samples=10000
max_identity_error=4.576e-09
max_taylor_bound_ratio=0.351053
PASS
```

The final six-page PDF was rendered to PNG page images and inspected page by page. No clipping, overlap, missing glyph, unreadable crop, or broken reference was found.

## Human-review focus

- Confirm the chain rule at the stated `AC([0,T];H1)` regularity, or narrow the theorem to smooth solutions if preferred.
- Inspect the Neumann constant-rigidity lemma, especially the positive-measure zero set case.
- Confirm that the Section 4 estimates of the source paper extend verbatim from the identity matrix to a constant SPD matrix.
- Do not read the nonlinear theorem as an unconditional statement for all minimizing-movement limits; the needed `D v_t in L1_t L∞_x` is not established by the source paper.
