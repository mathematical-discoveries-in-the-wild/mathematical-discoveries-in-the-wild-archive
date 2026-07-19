# Ideal Reduced Products Fail BCP Under Disjoint Refinement

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_ideal_reduced_product_bcp_obstruction/`

## Result

Let `I` be a proper ideal on `N`, containing all finite sets, with the
countable disjoint-refinement property: every sequence of `I`-positive sets
`S_k` admits pairwise disjoint `I`-positive subsets `T_k subset S_k`.

Then for every sequence `(E_n)` of nonzero normed spaces, the reduced product

`ell_infty(E_n) / c_I(E_n)`

fails BCP.

Consequently, for every sequence `(A_n)` of nonzero C*-algebras, the C*-reduced
product

`prod_n A_n / directsum_I A_n`

fails BCP.

## Why This Matters

This abstracts the diagonal escape mechanism behind the `ell_infty/c_0`
product quotient packet. The ordinary `c_0` quotient corresponds to the finite
ideal, which has the disjoint-refinement property. The theorem also explains
why ultraproducts require different ideas: maximal ideals do not have two
disjoint positive sets, so the center-by-center diagonal splitting is blocked.

## Proof Intuition

For a proposed countable ball cover, each center has many coordinates where its
reduced-product norm is nearly visible. The ideal hypothesis lets us carve
pairwise disjoint large pieces, one piece for each attack. On the piece assigned
to a center, choose unit vectors in the fibers pointing away from that center.
The assembled sequence has quotient norm one and stays outside every proposed
ball.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a general partial theorem adjacent to the C*-algebra question. The
key checks are the reduced-product norm formula and the use of the
disjoint-refinement property to assign pairwise disjoint positive attack sets.
