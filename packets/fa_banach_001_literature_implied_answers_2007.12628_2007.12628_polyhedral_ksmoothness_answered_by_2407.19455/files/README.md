# 2007.12628 Polyhedral k-Smoothness Subcase Answered

Status: `literature_implied_answer (finite-dimensional polyhedral / suggested ell_infty^n to ell_1^n subcase)`.

Source paper: A. Mal, S. Dey, and K. Paul, *Characterization of k-smoothness of operators defined between infinite-dimensional spaces*, arXiv:2007.12628.

Supporting paper: D. Sain, S. Sohel, and K. Paul, *On k-smoothness of operators between Banach spaces*, arXiv:2407.19455.

## Identification

The source paper ends with a question asking for necessary and sufficient conditions for a norm-one operator `T in L(X,Y)` to be a multi-smooth point of finite order. It explicitly suggests the case `X = ell_infty^n`, `Y = ell_1^n`, `n >= 3`, and says many cases remain unanswered.

## Answer Evidence

Sain--Sohel--Paul introduce the index of smoothness `i_R(T)` and prove in Theorem 1.8 that, under the stated reflexive/M-ideal hypotheses, `T` is `k`-smooth if and only if `i_{M_T}(T)=k`. In Section II they specialize to real finite-dimensional polyhedral Banach spaces, give a three-step finite procedure for determining the order of smoothness of any `T in L(X,Y)`, and conclude that the order problem between finite-dimensional polyhedral Banach spaces is completely solved in a computationally effective way.

Since real `ell_infty^n` and real `ell_1^n` are finite-dimensional polyhedral Banach spaces, this directly covers the suggested source subcase `L(ell_infty^n, ell_1^n)`.

## Scope

This is not a full answer to the arbitrary Banach-space question in arXiv:2007.12628. It records a literature-implied answer to the explicitly suggested finite-dimensional polyhedral subcase. The supporting authors cite the source paper as prior work, but the exact mapping from the final source question to the `ell_infty^n`/`ell_1^n` corollary is recorded here as an agent-identified implication.

## Files

- `main.tex`: compact status note with the finite-rank criterion for `ell_infty^n -> ell_1^n`.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:2007.12628.
- `supporting_paper_2407.19455.pdf`: arXiv:2407.19455.
