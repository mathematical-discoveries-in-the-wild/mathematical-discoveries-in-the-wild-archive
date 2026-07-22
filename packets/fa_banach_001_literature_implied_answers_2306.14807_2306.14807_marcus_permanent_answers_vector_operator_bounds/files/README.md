# Marcus permanent inequality answers Problems 1 and 2 of arXiv:2306.14807

Status: `literature_implied_answer (full answers to Problems 1 and 2)`

Source: Stephan Ramon Garcia, Ryan O'Loughlin, and Jiahui Yu,
*Symmetric and Antisymmetric Tensor Products for the Function-Theoretic
Operator Theorist*, arXiv:2306.14807. Problems 1 and 2 are on source page 18,
Section 10.

Supporting result: Marvin Marcus, *The permanent analogue of the Hadamard
determinant theorem*, Bulletin of the American Mathematical Society 69 (1963),
494-496, DOI 10.1090/S0002-9904-1963-10975-1. Marcus proves that for every
Hermitian positive-semidefinite matrix (G),

\[
  \operatorname{per}G \geq \prod_{i=1}^n G_{ii}.
\]

Vehbi E. Paksoy, *A Permanent Inequality for Positive Semidefinite Matrices*,
Electronic Journal of Linear Algebra 39 (2023), 71-77, DOI
10.13001/ela.2023.7701, is included locally as the accessible supporting PDF.
Its Theorem 2.4 records the Gram-matrix/symmetric-tensor identity, and formula
(3.15) records the Marcus-Minc diagonal-product bound.

## Identification

For the Gram matrix (G=(\langle x_i,x_j\rangle)), orthogonal projection by
the symmetrizer gives

\[
 \|x_1\odot\cdots\odot x_n\|^2
   =\frac{1}{n!}\operatorname{per}G.
\]

Marcus's inequality therefore gives

\[
 \|x_1\odot\cdots\odot x_n\|
 \geq \frac{1}{\sqrt{n!}}\prod_i\|x_i\|,
\]

which is exactly Problem 1. The constant is sharp whenever the Hilbert space
contains (n) mutually orthogonal nonzero vectors.

For a unit vector (x), the definition of the symmetric operator product gives

\[
 (A_1\odot\cdots\odot A_n)x^{\otimes n}
   =(A_1x)\odot\cdots\odot(A_nx).
\]

Problem 1 applied to (A_1x,\ldots,A_nx), followed by a supremum over unit
(x), proves the inequality in Problem 2.

The supporting authors did not identify these as answers to arXiv:2306.14807;
the implication is agent-identified. Problems 3-9 of the source paper are not
addressed by this packet.

Ledger:
`runs/fa_banach_001/ledger/results/2306.14807_marcus_permanent_answers_vector_operator_bounds.json`.

