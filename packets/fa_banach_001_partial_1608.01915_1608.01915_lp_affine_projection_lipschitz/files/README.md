# Dimension-free affine projection bounds on `ell_p^n` balls

Status: `candidate_partial_likely_valid`

Source paper: Tuomas Hytonen and Assaf Naor, *Heat flow and quantitative differentiation*, arXiv:1608.01915.

Target: Question 19 / `Q:proj lip`, which asks whether the orthogonal projection from `L_2(B_X)` onto affine functions is bounded on Lipschitz functions on an isotropic convex body `B_X`, uniformly over the Banach target.

Result: the answer is affirmative for the full finite-dimensional `ell_p^n` scale, `1 <= p <= infinity`, with constants independent of `n` and depending only on `p` for finite `p` (and an explicit `3/2` bound for `p=infinity`). The proof establishes the scalar estimate by coordinate slice integration by parts and then uses the source paper's scalar-to-Banach reduction for arbitrary targets.

Files:

- `main.tex`: solution packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_page15.png`, `figures/open_problem_page16.png`: source crops containing Question 19.
- `code/check_gamma_constants.py`: numerical sanity check for the finite-`p` Gamma-ratio constant.

Novelty/status note: exact cheap-index checks for `1608.01915`, the title, and distinctive `Q:proj lip` phrases had no prior run hit. A bounded web search for exact affine-projection / Wasserstein-symmetry phrases found the source paper but no later direct answer. This packet should be reviewed as a new partial result, not as a full answer to Question 19 for arbitrary isotropic convex bodies.
