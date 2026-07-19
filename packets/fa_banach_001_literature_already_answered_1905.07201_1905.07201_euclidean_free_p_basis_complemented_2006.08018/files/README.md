# Literature status: Euclidean Lipschitz free p-space questions from 1905.07201

Status: literature already answered for the Schauder-basis question; literature-implied answer for the Euclidean subset complementability question.

Source paper: arXiv:1905.07201, *Embeddability of ell_p and bases in Lipschitz free p-spaces for 0<p<=1*.

Later paper: arXiv:2006.08018, *Structure of the Lipschitz free p-spaces F_p(Z^d) and F_p(R^d) for 0<p<=1*.

## Questions identified

In Section 6 of arXiv:1905.07201, the authors ask:

- Question 6.5: Does `F_p([0,1]^d)` have a Schauder basis for each `d in N` and each `p in (0,1]`?
- Final Euclidean subset question: If `M subset R^d` and `p in (0,1]`, is `F_p(M)` isomorphic to a complemented subspace of `F_p(R^d)`?

## Resolution by later literature

The later paper arXiv:2006.08018 explicitly answers the Schauder-basis question positively. Its abstract and introduction say that it proves `F_p(R^d)` admits a Schauder basis for every `p in (0,1]`, gives explicit formulas for bases of both `F_p(R^d)` and `F_p([0,1]^d)`, and explicitly identifies this as a positive answer to arXiv:1905.07201, Question 6.5. Theorem 2.9 states directly that `F_p([0,1]^d)` has a Schauder basis.

The same later paper also records the Euclidean complementability result: for every `d` there is `C=C(p,d)` such that whenever `M subset N subset R^d`, the space `F_p(M)` is `C`-complemented in `F_p(N)`. Taking `N=R^d` gives a direct positive answer to the final Euclidean subset question from arXiv:1905.07201.

## Scope notes

This packet does not claim new mathematical progress. It clears two source-paper open-problem signals from the target queue:

- the basis question is explicitly answered in the later paper;
- the complementability question is answered by direct specialization of a later theorem/corollary.

This packet does not address the neighboring MAP question for finite-dimensional Banach spaces, the isometric copy of `ell_p` question, or the metric quotient question from the same source section.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:1905.07201.
- `supporting_paper_2006.08018.pdf`: later paper giving the answers.
