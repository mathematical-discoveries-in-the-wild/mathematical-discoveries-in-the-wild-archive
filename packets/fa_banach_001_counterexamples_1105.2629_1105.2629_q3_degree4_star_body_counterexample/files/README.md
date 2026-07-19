# Counterexample packet: degree-4 star body for Question 3

Status: likely valid counterexample.

Source paper: A. Koldobsky, G. Paouris, and M. Zymonopoulou, "Isomorphic properties of intersection bodies", arXiv:1105.2629.

Targeted question: Question 3 asks whether, if `K` is a symmetric star body of volume `1`, `1 <= k <= n-1`, and `I_k(K)` exists, then `|I_k(K)| <= |I_k(D_n)|`, where `D_n` is the Euclidean ball of volume `1`.

Result: no.  In `R^3` with `k=2`, a small even degree-4 zonal perturbation of the Euclidean ball has an explicitly constructed `2`-intersection body, and the volume of that `2`-intersection body is strictly larger than the Euclidean comparison.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of Question 3 in the source paper.
- `code/verify_moments.py`: exact rational check of the Legendre moments and expansion coefficients.
- `code/make_open_problem_crop.py`: crop generator for the source question.

Scope: this disproves Question 3 as stated for symmetric star bodies.  It does not address the convex case of Theorem 1.3, nor any variant that assumes `I_k(K)` is convex.
