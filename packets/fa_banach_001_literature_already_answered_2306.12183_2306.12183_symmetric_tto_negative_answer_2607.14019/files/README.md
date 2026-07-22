# Symmetric-matrix TTO question answered negatively

Status: `literature_already_answered`

Source question: Ryan O'Loughlin and Jani Virtanen, *Crouzeix's conjecture
for classes of matrices*, arXiv:2306.12183, Question 4.1 on page 12:

> Is every symmetric matrix unitarily equivalent to a direct sum of TTOs?

Answering paper: Ryan O'Loughlin, *Semialgebraic Dimension and Truncated
Toeplitz Models for Complex Symmetric Matrices*, arXiv:2607.14019.

Corollary 4.4 on page 7 gives a negative answer for every matrix size
\(n\ge 10\).  The paper proves by semialgebraic dimension that the family of
complex symmetric matrices unitarily equivalent to the relevant truncated
Toeplitz models has strictly smaller dimension than the open family of
irreducible complex symmetric matrices.  Hence some irreducible symmetric
\(n\times n\) matrix is not unitarily equivalent to a truncated Toeplitz
operator; irreducibility then rules out a nontrivial direct-sum model as well.

Scope: the counterexamples are existential rather than explicit.  The source
question is fully answered negatively, although the cases \(4\le n\le9\)
remain unresolved and this does not settle Crouzeix's conjecture itself.

Files:

- `main.tex` and `solution_packet.pdf`: compact source-to-theorem status note.
- `source_paper.pdf`: arXiv:2306.12183.
- `supporting_2607.14019.pdf`: the answering paper.

