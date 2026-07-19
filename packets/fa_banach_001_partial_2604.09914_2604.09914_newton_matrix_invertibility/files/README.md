# Positive Definiteness of the Semidiscrete MMP Newton Matrix

Status: `partial_result_likely_valid`

Source paper: Guillaume Bonnet and Yanir A. Rubinstein, *Quantitative Stability and Numerical Resolution of the Moment Measure Problem*, arXiv:2604.09914.

Extracted question: Section 4.3 leaves for future work the invertibility of the regularized Newton matrix
`M_nu(Phi)=nabla^2 E_nu(Phi)+u u^T+sum_i v_i v_i^T` used in Algorithm 4.1, as well as convergence of the damped Newton method.

Packet result: The matrix `M_nu(Phi)` is positive definite for every `Phi in U`, assuming the source paper's standing finite-support hypotheses: the support points affinely span `R^d` and all Laguerre cells have nonempty interior. This answers the invertibility part of the future-work sentence. It does not prove convergence of Algorithm 4.1 or any boundary-distance/damping criterion.

Main files:

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:2604.09914.
- `figures/open_problem_crop_page22_matrix_definition.png`: source crop defining `M_nu`.
- `figures/open_problem_crop_page23_future_work.png`: source crop with the future-work sentence.
- `code/check_d1_newton_matrix.py`: non-proof one-dimensional numerical sanity check.

Verification:

```sh
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/2604.09914_newton_matrix_invertibility/code/check_d1_newton_matrix.py
```

The script sampled 1500 one-dimensional full-cell configurations with no failures and minimum regularized eigenvalue about `0.12924`. The proof in the packet is analytic and does not depend on this script.
