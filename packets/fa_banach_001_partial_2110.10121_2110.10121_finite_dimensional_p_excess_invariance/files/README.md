# Finite-dimensional p-excess invariance for approximately dual p-ASFs

status: likely_valid_partial_result

run: fa_banach_001

agent: agent_lane_02

source_arxiv: 2110.10121

source_title: Approximately Dual p-Approximate Schauder Frames

source_authors: K. Mahesh Krishna and P. Sam Johnson

target: Problem 3.3, whether approximately dual p-approximate Schauder frames have the same p-excess

packet_type: partial

## Result

Problem 3.3 has an affirmative answer when the underlying Banach space is finite dimensional. In fact, the approximately-dual hypothesis is not needed in this subcase.

If `dim X=d<infty` and a p-ASF is indexed by `N`, then its p-excess is infinite. More generally, for the finite-index analogue with exactly `N>=d` frame atoms, every finite p-ASF has p-excess `N-d`.

## Why This Is Not A Full Solution

The source problem is asked for general separable Banach spaces. The argument here uses finite-dimensional compactness of the analysis range in `ell^p` and Cauchy-Binet on large finite partial frame operators. It does not decide the infinite-dimensional case, where the extra condition that the remaining functionals span `X^*` remains the serious obstruction.

## Evidence And Verification

- Source question appears as Problem 3.3 on page 9 of the source PDF; see `figures/open_problem_crop.png`.
- The proof is contained in `main.tex`.
- `code/finite_matrix_stress.py` performs finite-dimensional random stress checks for exact dual matrix models. It is not used as proof.
- Bounded novelty check: local run indexes and attempts showed no packet for arXiv:2110.10121; web search for `"p-Exc" "approximately dual"`, `"Approximately Dual p-Approximate Schauder Frames" "excess"`, and `"p-excess" "p-approximate Schauder frames"` found the source paper and the Hilbert-frame excess paper, but no later answer to Problem 3.3.

## Human Review Recommendation

Review as a finite-dimensional partial result. The main point to check is the norm convergence of finite partial frame operators in finite dimension and the Cauchy-Binet common-subset step.
