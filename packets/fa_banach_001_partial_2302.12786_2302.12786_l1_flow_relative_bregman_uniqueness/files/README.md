# 2302.12786: Relative-Bregman uniqueness for the L1 flow

Status: `partial_result_likely_valid`; `nonlinear_weak_strong_uniqueness`; `anisotropic_quadratic_full_subcase`; human review requested.

Source: Antonin Chambolle and Matteo Novaga, *L1-gradient flow of convex functionals*, arXiv:2302.12786, SIAM J. Math. Anal. 56 (2024), 5747–5781, DOI 10.1137/22M1527556.

## Result

The source leaves uniqueness of its strongly convex L1-gradient flow open outside monotone solutions and the isotropic Dirichlet energy.

This packet proves a quantitative relative-Bregman estimate for uniformly elliptic nonlinear integrands with globally Lipschitz Hessian. If one comparison flow satisfies `D v_t in L1_t L∞_x`, then

`E_F(u(t)|v(t)) <= E_F(u(s)|v(s)) exp[(K/gamma) integral_s^t ||D v_t||∞]`.

Hence the flow is unique in this weak–strong/classical regularity class. The result applies to genuinely nonlinear examples such as

`F(xi) = |xi|^2/2 + epsilon sum_j log cosh(xi_j)`.

When `F(xi)=xi·M xi/2` with any constant symmetric positive-definite matrix `M`, the nonlinear commutator vanishes. The packet therefore obtains unconditional energy contraction and uniqueness for the complete strongly elliptic anisotropic quadratic class, for common Dirichlet or homogeneous Neumann data. It also records whole-family convergence of the minimizing movements in this subcase.

## Core mechanism

For `A=grad F`, differentiation of the one-sided Bregman divergence gives

`d_t B_F(Du|Dv) = [A(Du)-A(Dv)]·D(u_t-v_t) + R_F(Du,Dv)·D v_t`.

Monotonicity of `∂(||·||_1^2/2)` makes the integrated first term nonpositive. Lipschitz continuity of `D^2F` makes `R_F` quadratic in `Du-Dv`; uniform convexity makes the Bregman energy quadratic in the same difference. Grönwall closes the estimate.

## Scope

This is not a full answer in the source paper’s weak solution class. The source gives `u_t in L2_loc H1`, which does not provide the `L1_t L∞_x` bound on `D u_t` used to control the nonlinear commutator. The quadratic corollary is unconditional because that commutator is identically zero.

## Novelty check

A bounded search on 2026-07-22 used the exact title, arXiv id, DOI, quoted open phrase, and close uniqueness/strong-convexity terms across arXiv, SIAM, CVGMT, and web search. The 2024 version still states full uniqueness as open; no later explicit resolution was found. Novelty confidence for the relative-entropy method is moderate, so the packet makes no priority claim.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: page-1 source crop containing the open statement.
- `code/check_bregman_identity.py`: seeded algebra/sign regression check.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `verification_report.md`: verification record and review focus.
