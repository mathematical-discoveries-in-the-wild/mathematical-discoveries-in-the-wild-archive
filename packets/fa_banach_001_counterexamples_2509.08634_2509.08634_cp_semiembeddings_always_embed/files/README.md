# Semi-embeddings between \(C_p\)-spaces are always embeddings

Status: candidate counterexample / full negative answer to Problem 10 of arXiv:2509.08634.

Source paper: Jerzy Kakol, Ondrej Kurka, and Wieslaw Sliwa, "Lotz-Peck-Porta and Rosenthal's theorems for spaces \(C_p(X)\)", arXiv:2509.08634.

## Target Question

Problem 10 asks whether, for an infinite compact space \(X\), every semi-embedding
\[
T:C_p(X)\to C_p(Y)
\]
is an embedding for every compact space \(Y\) if and only if \(X\) is scattered.

## Result

The proposed characterization is false. In fact, for arbitrary Tychonoff spaces \(X\) and \(Y\), every semi-embedding \(T:C_p(X)\to C_p(Y)\) is already a topological embedding. Therefore the property in Problem 10 holds for every infinite compact \(X\), including non-scattered compacta such as \(X=[0,1]\).

## Proof Mechanism

For each \(y\in Y\), the coordinate functional \(\delta_y\circ T\) on \(C_p(X)\) is a finite linear combination of point evaluations on \(X\). These functionals generate exactly the topology induced on the range \(T(C_p(X))\). The polar condition says that a base of original \(C_p(X)\)-neighborhoods becomes closed for this weaker induced topology. Applying this to a neighborhood controlling one point \(x\in X\), and then taking the closure of the finite-coordinate kernel inside the weaker topology, forces \(\delta_x\) into the span of the coordinate functionals \(\delta_y\circ T\). Thus every point evaluation on \(X\) is continuous for the induced range topology, so the inverse of \(T\) is continuous.

## Files

- `main.tex`: review packet with theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: official arXiv PDF for arXiv:2509.08634.
- `figures/open_problem_crop.png`: crop of Problem 10 from page 4 of the source PDF.

## Verification And Novelty Notes

Local duplicate checks on `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv` found no existing packet for arXiv:2509.08634 or this semi-embedding result. Bounded web searches on 2026-06-15 for exact phrases around Problem 10, `semi-embedding C_p(X) C_p(Y)`, and `polar map C_p(X)` found no later paper explicitly answering the problem.

Human review should focus on the annihilator step:
\[
\overline{M}^{\sigma(C(X),H)}
  = \bigcap_{\lambda\in H\cap M^\perp}\ker\lambda
\]
for \(M=\{f:f|_F=0\}\). The proof then uses that \(M^\perp=\operatorname{span}\{\delta_t:t\in F\}\) is finite-dimensional, so \(H\cap M^\perp\) is pointwise closed in the algebraic dual. Review should also check the translation from closed images \(T(U)\subset C_p(Y)\) to closedness of \(U\) in the range-induced weak topology.
