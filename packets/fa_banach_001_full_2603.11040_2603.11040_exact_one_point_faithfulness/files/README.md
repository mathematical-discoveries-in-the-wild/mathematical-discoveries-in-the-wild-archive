# Full result: exact one-point faithfulness

status: `full_solution_likely_valid`

source: Sujit Sakharam Damase and James Eldred Pascoe,
*On positive definite thresholding of correlation matrices*,
arXiv:2603.11040v1.

target: the source defines the faithfulness constant and gives only a
degree-two lower bound when the thresholding set is the singleton
`K={epsilon}`. This packet computes the exact optimum and all equality cases
for every sphere dimension `n>=3`.

## Result

Let `G_k` be the normalized Gegenbauer polynomials and

`m_n(epsilon) = min_{k != 1} G_k(epsilon)`.

For every `n>=3` and `0<epsilon<1`,

`tau_{{epsilon},n} = -m_n(epsilon)/(epsilon-m_n(epsilon))`.

Every optimizer is supported on degree one and the degrees attaining the
minimum. Hence a two-mode optimizer always exists. For every fixed `n>=3`,
degree two is the unique minimizer for all sufficiently small positive
`epsilon`. In that range the source's quadratic lower bound is exactly sharp,
the optimizer is unique, and

`tau = (1-n epsilon^2)/(1-n epsilon^2+(n-1)epsilon)`.

## Proof idea

The Schoenberg coefficients form a probability vector. The one vanishing
constraint gives

`0 = a_1 epsilon + sum_{k != 1} a_k G_k(epsilon)`.

Replacing every off-linear Gegenbauer value by their minimum immediately
gives the sharp upper bound; putting all remaining mass at a minimizing
degree attains it. Equality forces precisely that support. At zero, the exact
values

`G_{2r}(0)=(-1)^r (1/2)_r/((n-1)/2)_r`, `G_{2r+1}(0)=0`

make degree two the strict minimizer. Uniform Darboux decay on a neighborhood
of zero preserves this ordering for small positive thresholds.

## Verification and novelty

- The current arXiv page was checked on 2026-07-19 and remains v1.
- The source's one-point theorem states only the quadratic lower bound.
- Cheap indexes and bounded primary-source searches for the exact
  faithfulness formula found no existing answer or packet.
- The included numerical script checks the minimizing-degree formula across
  sample dimensions and thresholds; it is a sanity check, not part of the
  proof.
- The packet does not claim to solve the source's separate final conjecture
  about discontinuous positive definite functions.

## Files

- `main.tex` / `solution_packet.pdf`: complete proof and scope statement.
- `source_paper.pdf`: official current arXiv PDF.
- `code/check_one_point_optimum.py`: finite-degree numerical smoke test.
