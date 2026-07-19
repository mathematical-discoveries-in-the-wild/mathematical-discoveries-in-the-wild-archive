# Literature status: discrete Lipschitz-free p-spaces have AP

Status: literature already answered.

Source paper: arXiv:2005.06555, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*.

Later paper: arXiv:2506.09786, *Lipschitz free p-spaces for 0<p<1 in the light of the Schur p-property and the compact reduction*.

## Question identified

In the Open Problems section of arXiv:2005.06555, the authors ask whether every discrete metric space `M` has `F(M)` with AP, and more generally whether `F_p(M)` has AP for every `p in (0,1]`. The later paper cites this as `AACD21, Question 6.3`.

## Resolution by later literature

arXiv:2506.09786 explicitly says that its compact-reduction theorem answers `AACD21, Question 6.3` positively.

The decisive statement is Theorem `thm:discreteCase`: if `M` is a complete metric space with at most finitely many accumulation points, then `F_p(M)` has the approximation property for all `p in (0,1]`. In the proof, the authors invoke Proposition 4.1 of the source paper and the comment before Question 6.3 to reduce the question to complete discrete metric spaces; the resulting finite-rank approximation argument then proves AP.

Thus the source paper's discrete-metric-space AP question is already answered positively in later literature. The supporting authors explicitly knew they were answering the source question, so this belongs in `literature_already_answered`, not `literature_implied_answers` and not `partial`.

## Scope notes

This packet does not claim new mathematical progress.

The resolved scope is the AP question for discrete metric spaces and `0<p<=1`, i.e. the source's Question 6.3. This packet does not settle the neighboring countable proper MAP question, the existence question for non-AP `F_p(M)`, or the later net/isomorphism/open-basis questions in arXiv:2005.06555.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:2005.06555.
- `supporting_paper_2506.09786.pdf`: later paper giving the answer.

