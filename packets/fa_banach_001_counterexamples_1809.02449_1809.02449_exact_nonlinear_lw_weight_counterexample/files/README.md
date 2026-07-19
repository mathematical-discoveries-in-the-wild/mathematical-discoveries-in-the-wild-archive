# Exact determinant weight does not give nonlinear Loomis--Whitney constant 1

Status: `candidate_counterexample_likely_valid`, pending human review.

Source: Anthony Carbery, Timo S. Hanninen, and Stefan Ingi Valdimarsson,
*Multilinear duality and factorisation for Brascamp--Lieb-type inequalities
with applications*, arXiv:1809.02449; JEMS 25 (2023), 2057--2125.

The question on source PDF page 48 asks whether the nonlinear
Loomis--Whitney inequality has exact constant `1` after inserting the
pointwise determinant weight, provided the neighborhood is sufficiently
small.  The packet gives a negative answer already for `n=3`.

The three polynomial submersions are

```text
pi_1(x,y,z) = (y+xz, z-xy)
pi_2(x,y,z) = (z+xy, x-yz)
pi_3(x,y,z) = (x+yz, y-xz).
```

Their determinant weight is positive near the origin.  Gaussian tests at
scale `sigma` have normalized ratio

```text
1 + (3/4) sigma^2 + O(sigma^4).
```

The gain is polynomial, while restricting the integral to any prescribed
neighborhood loses only `exp(-c/sigma^2)`.  Hence no shrinking neighborhood
restores the proposed constant `1`.

Files:

- `solution_packet.pdf`: review packet
- `main.tex`: theorem and proof
- `source_paper.pdf`: original paper
- `figures/open_problem_crop.png`: source question from PDF page 48
- `code/check_symbolic_expansion.py`: exact symbolic identity check
- `code/make_open_problem_crop.py`: reproducible source crop

The symbolic script confirms the displayed determinant, sum-of-squares, and
Gaussian coefficient.  It is a verifier only; the packet proves the
identities and the localization argument analytically.

