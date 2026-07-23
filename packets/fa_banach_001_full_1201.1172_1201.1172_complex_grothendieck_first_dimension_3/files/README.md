# Full solution packet: the first nontrivial complex finite Grothendieck dimension is 3

Status: `candidate_full_solution_likely_valid_needs_human_review`

## Source problem

Nengkun Yu, Runyao Duan, and Quanhua Xu, *Bounds on the distance between a
unital quantum channel and the convex hull of unitary channels, with
applications to the asymptotic quantum Birkhoff conjecture*, arXiv:1201.1172.
On PDF page 12 the authors recall $K_2=1$ and ask for the first integer
$d$ for which the complex finite Grothendieck constant $K_d$ is greater
than one.

## Result

The first integer is $d=3$. The packet gives an explicit Hermitian
$3\times3$ coefficient matrix and a rank-two Gram witness whose vector
value is $8\sqrt6/3$. Every scalar-phase value is strictly smaller.

The scalar estimate is exact and elementary. After one phase is normalized,
weighted Cauchy--Schwarz reduces the problem to maximizing a three-cycle
Hermitian quadratic form. Fixing one phase reduces that maximum to

\[
a+\sqrt{30-10a}\leq \frac{11}{2}.
\]

The only possible equality phases for this last estimate do not satisfy the
equality condition in weighted Cauchy-Schwarz. Compactness therefore gives a
strict support-function separation. Since $K_1=1$ is immediate and the source
records the known $K_2=1$, this fully answers its first-dimension question.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: source question on PDF page 12.
- `code/verify_witness.py`: exact symbolic checks and a non-proof numerical
  sanity check.
- `tmp/`: LaTeX and page-render intermediates.

## Novelty check

The bounded check searched the run indexes, the local parsed arXiv corpus,
and arXiv/web queries for the exact first-integer question, complex $K_3$,
and $3\times3$ extremal Schur multipliers. It also inspected Erik
Christensen's arXiv:2410.20112 (latest local text dated March 2026), which
gives rank restrictions for extremal Schur multipliers but no $K_3>1$
witness or answer to this question. No prior answer was found. Novelty
confidence is moderate, not definitive.

## Human review focus

Check the support-function equivalence defining $K_3>1$, the orientation of
the inner-product convention in the Gram witness, and the scalar equality-case
calculation. The proof does not rely on numerical optimization.
