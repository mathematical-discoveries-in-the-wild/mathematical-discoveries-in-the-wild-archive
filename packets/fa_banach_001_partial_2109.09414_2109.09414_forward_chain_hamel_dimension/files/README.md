# Forward Orthogonal Chains Compute Hamel Dimension in Smooth Spaces

status: partial_result_likely_valid

source: arXiv:2109.09414, Lj. Arambasic, A. Guterman, B. Kuzma, R. Rajic, S. Zhilina, "What does Birkhoff-James orthogonality know about the norm?"

packet: `runs/fa_banach_001/solutions/partial/2109.09414_forward_chain_hamel_dimension/solution_packet.pdf`

## Result

For every smooth real or complex normed space `X`, the projective Birkhoff-James di-orthograph determines the full Hamel dimension of `X`.

Define a forward orthogonal chain in the di-orthograph to be a well-ordered family of vertices `(v_alpha)` such that `v_alpha -> v_beta` whenever `alpha < beta`.  Then the supremum of the cardinalities of such chains is exactly `dim X`.

This strengthens the dimension-recognition part of the source paper from finite dimension/infinite dimension to the exact algebraic cardinal dimension, under the smoothness hypothesis.

## Scope

This is a partial result relative to the source paper's broad property-recognition question.  It does not classify arbitrary norm properties, nor does it remove smoothness.  The smoothness assumption is essential to this proof because it turns each edge `x -> y` into the single equation `f_x(y)=0` for the unique supporting functional `f_x`.

## Verification

- The proof is self-contained modulo the standard James supporting-functional criterion recalled in the source paper.
- No computational verification was used.
- The source-paper question crop is in `figures/open_problem_crop.png`.
- The source PDF is stored as `source_paper.pdf`.

## Novelty Check

Checked the run indexes for `2109.09414`, Birkhoff-James orthogonality, Hamel dimension, forward chains, transitive cliques, and dimension-cardinal language.  No exact duplicate was found.

Web searches on 2026-07-18 found the 2024 follow-up "Birkhoff-James classification of norm's properties", which develops finite-dimensional property recognition and treats dimension finiteness, smooth points, maximal faces, supremum norms, and Radon-plane examples.  I did not find a statement identifying the exact infinite Hamel dimension cardinal with the supremum of well-ordered forward orthogonal chains in smooth spaces.

## Human Review Recommendation

Review as a likely valid partial theorem.  The main point to check is the smoothness restriction in the upper bound: uniqueness of supporting functionals is used to make a forward chain linearly independent.
