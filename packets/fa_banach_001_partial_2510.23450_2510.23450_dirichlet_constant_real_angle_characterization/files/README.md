# arXiv:2510.23450 -- constant real Dirichlet angle characterization

Status: `partial_likely_valid`

Agent: `agent_super_00`

Updated: 2026-07-01T00:51:08Z

## Source Target

Source paper: Hannes Meinlschmidt and Joachim Rehberg, *Sharp angle estimates for second order divergence operators*, arXiv:2510.23450.

The final comments ask for useful characterizations of when the inequality

```text
omega(t_V) <= omega(mu)
```

is sharp. The authors give a two-dimensional skew-symmetric Dirichlet example with strict inequality and note that a precise useful characterization is hard.

## Result

For the full Dirichlet space `V=W_0^{1,2}(Omega)` and a constant real coefficient matrix `M=S+K`, where `S=S^T >= m I` and `K^T=-K`, the Dirichlet form only sees `S`; the skew-symmetric part `K` vanishes by integration by parts. Hence

```text
omega(t_V) = 0,
```

while

```text
omega(M) = 0 iff K = 0.
```

Thus, in this constant real Dirichlet class, the angles coincide exactly for symmetric coefficient matrices. Every nonzero skew-symmetric part gives a strict gap.

## Scope

This is a partial characterization for constant real matrices and full Dirichlet boundary conditions. It does not address variable coefficients, mixed/Neumann boundary conditions, complex coefficients, or the complex-coefficient matrix-analysis question in the same source section.

## Files

- `main.tex` gives the formal statement and proof.
- `solution_packet.pdf` is the rendered packet.
- `source_paper.pdf` is the source arXiv paper.
- `figures/open_problem_crop.png` shows the source open-question paragraph.
- `code/render_open_problem_crop.py` regenerates the crop.

## Novelty Check

Cheap run-index search found no existing packet for arXiv:2510.23450. Exact web searches for the source title, `omega(t_V)`, `omega(mu)`, `N_p(mu)`, sector inclusions, and the source open-question wording found no later settlement. The result is a scoped extension of the source's displayed skew-symmetric example, not a full characterization of the open problem.
