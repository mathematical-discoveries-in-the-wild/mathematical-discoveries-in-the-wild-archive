# Exact scale covariance forces degenerate landmark kernels

Status: partial_result_likely_valid (complete theorem for a precise subquestion).

Source paper: Mario Micheli and Joan Alexis Glaunes, Matrix-valued Kernels for Shape Deformation Analysis, arXiv:1308.5739.

## Result

Let K(x,y)=kappa(x-y) be a continuous translation-invariant positive-definite matrix-valued kernel. Suppose the associated landmark Hamiltonian flow is exactly covariant under every spatial dilation, even after allowing an arbitrary positive scalar rescaling of time and momenta:

    Q(t)=lambda q(C_lambda t),    P(t)=A_lambda p(C_lambda t).

Then kappa must be constant. Conversely, every constant positive-semidefinite matrix kernel is exactly dilation covariant, so this is a sharp classification. Every such block Gram matrix for two or more landmarks is singular. In the source paper's stronger RKHS class V embedded in C_0^1, the only such kernel is the zero kernel.

The proof uses only the first Hamilton equation and a two-landmark initial condition. It first forces kappa(lambda x)=h_lambda kappa(x). Positive definiteness makes kappa(0) nonzero for a nonzero kernel, evaluation at zero gives h_lambda=1, and continuity as lambda tends to zero makes kappa constant.

## Scope

This completely rules out exact scale covariance for every usable fixed, continuous, stationary positive-definite landmark kernel in the source's class. It does not solve the paper's broader kernel-design program and does not exclude:

- a family of kernels whose length scale transforms with the dilation;
- approximate or finite-range scale robustness;
- configuration-dependent or nonstationary normalization;
- singular or conditionally positive-definite kernels outside the stated RKHS setting.

## Files

- main.tex: full proof packet.
- solution_packet.pdf: compiled proof packet.
- source_paper.pdf: source arXiv paper.
- figures/open_problem_crop.png: source conclusion and scale-invariance direction.
- code/verify_scale_obstruction.py: deterministic exact-rank and example checks.
- verification.md: commands, outputs, and review guidance.

## Verification

The theorem is analytic. The script checks the constant-kernel Gram ranks exactly over the rationals, illustrates failure of the required homogeneity for a Gaussian kernel, and checks the elementary zero-diagonal positive-definiteness obstruction. The source crop and every page of the compiled packet are visually inspected.
