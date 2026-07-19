# Literature-Implied Answer: Near-Tight Riesz Partition Exponent

Status: `literature_implied_answer`.

Source paper: Marcin Bownik, Pete Casazza, Adam W. Marcus, Darrin Speegle,
`Improved bounds in Weaver and Feichtinger Conjectures`, arXiv:1508.07353.

Supporting paper: Mohan Ravichandran and Nikhil Srivastava,
`Asymptotically Optimal Multi-Paving`, arXiv:1706.03737.

## Identified Question

In Section 4, after Theorem 4.8, the source paper asks for the optimal
dependence on `epsilon` in the `R_epsilon`/near-tight Riesz partition problem.
Theorem 4.8 gives partitions of a unit-norm Bessel sequence with Bessel bound
`B` into `O(B epsilon^{-4})` Riesz sequences with bounds `1-epsilon` and
`1+epsilon`. Remark 4.9 records that `Omega(epsilon^{-2})` blocks are necessary
and asks whether the exponent can be reduced.

## Answer

The later Ravichandran--Srivastava multi-paving theorem implies the optimal
upper bound `O(B epsilon^{-2})`.

Indeed, Theorem 4.7 of the source paper first partitions the unit-norm Bessel
sequence into `O(B)` Riesz sequences with fixed universal bounds. On each such
piece, the Gram matrix `G` has diagonal `1` and spectrum in a fixed interval
`[a,b]`. Thus `A=G-I` is a zero-diagonal Hermitian matrix/operator of
universally bounded norm. Applying Ravichandran--Srivastava paving to `A` and
`-A` gives `O(epsilon^{-2})` further pieces on which `||P(A)P|| <= epsilon`.
Equivalently, each refined Gram submatrix lies between `(1-epsilon)I` and
`(1+epsilon)I`, which is exactly the desired near-tight Riesz condition.

This is an agent-identified implication, not a statement explicitly advertised
by the supporting authors as an answer to the 2015 remark.

## Files

- `main.tex`: compact status note with theorem and proof.
- `solution_packet.pdf`: rendered compact status note.
- `source_paper.pdf`: arXiv:1508.07353.
- `supporting_paper_1706.03737.pdf`: arXiv:1706.03737.

## Verification

LaTeX rendered with `pdflatex` on 2026-07-18.

