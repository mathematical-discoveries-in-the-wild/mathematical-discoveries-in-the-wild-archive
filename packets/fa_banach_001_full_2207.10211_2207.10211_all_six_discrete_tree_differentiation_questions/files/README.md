# All six open questions on discrete differentiation

Status: `full_solution_likely_valid`

Source: Robert F. Allen and Colin M. Jackson, *The differentiation operator
on discrete function spaces of a tree*, arXiv:2207.10211, Section 6, page 17.

## Claimed contribution

This packet completely answers all six open questions in the source paper.

- Question 1: **yes**. On a weighted Hilbert function space one has
  `||C_b|| = sqrt(2)` and `||D|| = 2`, so the conjectured identity
  `||D|| = 1 + ||C_b||` fails.
- Question 2: **no**, in the stronger form that `D` is never power-bounded on
  a discrete function space.
- Question 3: **no**. The range of `C_b` cannot separate the root from any of
  its children, so `C_b` is never surjective.
- Question 4: **no**. A discrete function space invariant under `D` is
  necessarily infinite-dimensional, and the nonzero spectral point `1` of
  `D` is not an eigenvalue; hence `D` cannot be compact.
- Question 5: **exact formulas**. If `D` is bounded on `L_mu^infinity(T)`, let
  `rho_mu` be the uniform asymptotic descendant/ancestor growth rate of `mu`
  away from the root. Then
  `sigma(C_b) = {1} union closed_disk(0,rho_mu)` and
  `sigma(D) = {0} union closed_disk(1,rho_mu)`. On every discrete Hardy
  `T_p(T)`, the corresponding formulas are the closed unit disk and the
  closed disk centered at `1` of radius `1`.
- Question 6: **no** for both named path-tree spaces, as an immediate instance
  of the universal compactness obstruction.

## Files

- `solution_packet.pdf`: human-facing proof packet
- `main.tex`: packet source
- `source_paper.pdf`: original arXiv paper
- `figures/open_problem_crop.png`: full-width source crop of page 17
- `VERIFICATION.md`: adversarial proof audit
- `code/verify_weighted_hilbert.py`: finite-truncation numerical check
- `code/crop_source_evidence.py`: reproducible evidence crop

## Verification

The proof was checked step by step against the source definitions. The finite
binary-tree computation confirms `||C_b|| = sqrt(2)` and the exact test-vector
identity `||D y_N||^2 = 4 - 3/N`; this computation is a check, not a proof.

Recommended human focus: verify the pointwise-growth induction, the exclusion
of finite-dimensional invariant functional spaces, and the compact-spectrum
argument. For Question 5, verify the one-level resolvent estimate for the
operator-weighted shift, the root block decomposition, and the indexing of
`rho_mu`. Current mathematical verdict: likely valid.

## Novelty scope

A bounded search on 2026-07-22 covered the run indexes, exact-title and
exact-question searches, close operator-theoretic keyword searches, and the
later arXiv paper 2308.11016 that cites the source. The extension search also
covered exact weighted/Hardy spectrum phrases and operator-weighted shifts on
`l_infinity`. No later source explicitly stating these resolutions was found.
Novelty confidence is moderate; an exhaustive priority search is not claimed.

Ledger:
`runs/fa_banach_001/ledger/results/2207.10211_all_six_discrete_tree_differentiation_questions.json`
