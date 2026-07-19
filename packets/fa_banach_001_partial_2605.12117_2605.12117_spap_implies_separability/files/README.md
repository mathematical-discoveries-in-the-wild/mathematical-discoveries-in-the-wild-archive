# SPAP Implies Separability

Status: partial negative result.

Source paper: Luis A. Garcia, Jose Lucas P. Luiz, Vinicius C. C. Miranda,
*Norm attainment for multilinear operators and polynomials on Banach Spaces
and Banach lattices*, arXiv:2605.12117.

Open problem: Question 2 asks whether there are Banach lattices with the
SPAP beyond the known class of Banach lattices with order-continuous norm
whose order is given by a basis.

Result: every Banach lattice with the SPAP is separable. Consequently, no
nonseparable Banach lattice can supply a new example for Question 2.

Packet contents:

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop containing Question 2.
- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build outputs.

Human review notes:

The proof is short. If `(S_n)` is an SPAP sequence, the closed linear span of
the countably many finite-dimensional ranges `S_n(E)` is separable. The
modulus inequality `|(S_n-id)x| <= |S_n-id|(|x|)` implies `S_n x -> x` for
every `x in E`, so this separable subspace is all of `E`.

This is not a full answer to Question 2 because it rules out a broad class of
possible examples rather than producing an example outside the known basis
class.
