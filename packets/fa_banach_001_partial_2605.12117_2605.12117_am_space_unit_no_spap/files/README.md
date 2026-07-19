# AM-Spaces With Unit Fail SPAP

Status: partial negative result.

Source paper: Luis A. Garcia, Jose Lucas P. Luiz, Vinicius C. C. Miranda,
*Norm attainment for multilinear operators and polynomials on Banach
Spaces and Banach lattices*, arXiv:2605.12117.

Open problem: Question 2 asks whether there are Banach lattices with the
SPAP beyond the known class of Banach lattices with order-continuous norm
whose order is given by a basis.

Packet contents:

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop containing
  the open question.
- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build outputs.

Result:

Every infinite-dimensional AM-space with a strong unit fails the SPAP.
Indeed, SPAP at the unit forces finite-rank positive operators to converge
to the identity in operator norm, which would make the identity compact.
This rules out a large classical family, including infinite-dimensional
`C(K)` spaces with their usual unit, but it does not fully answer
Question 2.
