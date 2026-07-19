# Common-affine residual class and smooth obstruction for Qmap concavity

Status: **candidate partial result; likely valid; human review requested**

Source: Matthieu Fradelizi, Lampros Gavalakis, and Martin Rapaport,
*Entropic versions of Bergström's and Bonnesen's inequalities*,
arXiv:2501.10309v1. The question is in Remark 9, equation (18), page 7.

## Result

The quotient in equation (18) is exactly
\`exp(2 h(W_n | W^{n-1}))\`. This gives two complementary conclusions.

1. If \`X_n = a^T X' + U\` and \`Y_n = a^T Y' + V\`, with the same regression
   vector \`a\`, residuals independent of their respective first blocks, and one
   residual Gaussian, then the source map is concave. The first blocks may be
   arbitrary and non-Gaussian. The proof reduces the quotient to scalar
   entropy power and applies Costa concavity through a perspective transform.
2. Concavity fails without structural hypotheses, even for iid random vectors
   with positive smooth densities. Let the last coordinate be
   \`4 S + sigma Z\`, where \`S\` is Rademacher and \`Z\` is standard Gaussian,
   and let the first block be independent Gaussian. For all sufficiently small
   \`sigma > 0\`, midpoint concavity fails between \`lambda = 1/4\` and \`3/4\`.

The obstruction is rigorous and asymptotic: at \`lambda=1/4\` there are four
distinct equally weighted small-noise modes, while at \`lambda=1/2\` two modes
merge. Their discrete entropies are \`2 log 2\` and \`(3/2) log 2\`, so the ratio
of midpoint to endpoint entropy powers tends to \`1/2\`.

## Scope

This does not characterize every class for which equation (18) is concave and
does not settle the Ball--Nayar--Tkocz log-concave conjecture. The negative
example is deliberately non-log-concave. The result supplies a non-Gaussian
positive class and a sharp warning that smoothness, symmetry, and iid structure
alone do not suffice.

## Files

- \`main.tex\`, \`solution_packet.pdf\`: full proof packet.
- \`verification.md\`: explicit adversarial verification report.
- \`source_paper.pdf\`: original arXiv source PDF.
- \`figures/open_problem_crop.png\`: page-7 source evidence.
- \`code/explore_gaussian_mixtures.py\`: non-rigorous numerical sanity check.

Ledger: \`runs/fa_banach_001/ledger/results/2501.10309_qmap_affine_residual_and_smooth_obstruction.json\`.

