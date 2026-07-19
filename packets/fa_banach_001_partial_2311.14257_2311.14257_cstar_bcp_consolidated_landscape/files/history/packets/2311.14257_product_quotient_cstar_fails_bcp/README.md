# Product Quotient C*-Algebras Fail BCP

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_product_quotient_cstar_fails_bcp/`

## Result

Let `(E_n)` be any sequence of nonzero normed spaces. Then

`ell_infty(E_n) / c_0(E_n)`

fails BCP.

In particular, for every sequence `(A_n)` of nonzero C*-algebras, the C*-algebra

`prod_n A_n / directsum_n A_n`

fails BCP.

Moreover, BCP and UBCP are not preserved by C*-quotients: if `A` is any
nonzero separable C*-algebra, then `ell_infty(A)` has UBCP, but
`ell_infty(A)/c_0(A)` fails BCP.

## Why This Matters

This gives a broad negative family for the C*-algebra question. It generalizes
the classical `ell_infty/c_0` obstruction and captures many sequence-algebra
coronas, including `A_infty / c_0(A)` for every nonzero C*-algebra `A`.

Together with the positive continuous-field packets, it sharpens the emerging
picture: countably controlled continuous fields can have BCP exactly when the
base has a countable pi-basis, while product corona quotients are robustly on
the negative side. It also shows that quotient-stable invariants cannot by
themselves characterize BCP for C*-algebras.

## Proof Intuition

Given countably many centers in the quotient, represent them by bounded
sequences. For each center, choose infinitely many coordinates where its
fiber norm is close to its quotient norm. Diagonalize through the centers.
At the selected coordinate, choose a unit vector in the fiber pointing
opposite enough to the center coordinate. The resulting bounded sequence has
quotient norm one and stays outside every ball `B(center, ||center||)`.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a clean negative partial theorem. The main checks are the
Hahn-Banach one-coordinate escape lemma and the diagonal construction ensuring
each center is attacked along infinitely many coordinates.
