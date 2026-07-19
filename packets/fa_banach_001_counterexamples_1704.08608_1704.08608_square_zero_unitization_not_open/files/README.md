# A zero-dimensional maximal ideal space does not force open multiplication

Status: candidate counterexample to the first clause of Open Problem 3 in arXiv:1704.08608.

Source paper: Szymon Draga and Tomasz Kania, "When is multiplication in a Banach algebra open?", arXiv:1704.08608.

## Target Question

Open Problem 3 asks:
\[
\text{Do commutative, unital Banach algebras with zero-dimensional maximal ideal space have (uniformly) open multiplication?}
\]
It then asks the stronger follow-up where idempotents are linearly dense.

## Result

The first clause has a negative answer as written. Let \(E=\mathbb C^2\) with the supremum norm and define
\[
A=\mathbb C\oplus E,\qquad
(\lambda,x)(\mu,y)=(\lambda\mu,\lambda y+\mu x),
\]
with norm \(\|(\lambda,x)\|=|\lambda|+\|x\|_\infty\). This is the unitization of a square-zero algebra.

The maximal ideal space of \(A\) is a singleton, hence zero-dimensional, but multiplication in \(A\) is not open. It is therefore not uniformly open.

## Proof Mechanism

All elements of the ideal \(0\oplus E\) square to zero, so every character kills \(E\), leaving only the scalar character. However, near the nilpotent element \(a=(0,e_1)\), products of two nearby elements cannot reach small vectors in the transverse direction \(e_2\) with scalar coordinate zero. The scalar equation forces one scalar factor to vanish; the remaining vector factor would then have to lie in \(\mathbb C e_2\), which is distance \(1\) from \(e_1\).

## Files

- `main.tex`: review packet with theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: official arXiv PDF for arXiv:1704.08608.
- `figures/open_problem_crop.png`: crop of Open Problem 3 from page 14.

## Verification And Novelty Notes

Local duplicate checks on the run indexes found no existing packet for arXiv:1704.08608 or this square-zero unitization counterexample.

Bounded web searches on 2026-06-15 for exact and near-exact phrases including `"zero-dimensional maximal ideal space" "open multiplication" Banach algebra`, `"square-zero" "open multiplication" "Banach algebra"`, and `"Do commutative, unital Banach algebras with zero-dimensional maximal ideal space"` found no later explicit answer. Novelty confidence is medium because the example is elementary and may be folklore.

Human review should check whether the source problem intended an unstated semisimplicity hypothesis. The packet answers the printed formulation, not the stronger dense-idempotent follow-up.
