# Literature-Implied Answer: Projection Generation and Monotonically Sokolov Topology

## Source Question

- Source paper: Wieslaw Kubis, *Banach spaces with projectional skeletons*, arXiv:0802.1109.
- Target: the final-section problem asking for a topological property of `(X,Tau_D)` characterizing when a norming subspace `D` generates projections in `X`.
- Location: source PDF page 28; source TeX line 1197 in `projs_survey-ver2g-BIB.tex`.
- Source PDF retained as `source_paper.pdf`.

## Status

This is filed as `literature_implied_answer`, not as a new proof. The later
supporting paper does not appear to explicitly say it resolves Kubis's exact
problem as stated. However, Theorem 4.1 of arXiv:1805.11901 supplies the
missing topological characterization after the standard weak-star-countably
closed induced-subspace normalization already used in arXiv:0802.1109.

## Answer

For a norming linear subspace `D subset X^*` that is weak-star-countably
closed, `D` generates projections in Kubis's sense if and only if
`(X, sigma(X,D))` is monotonically Sokolov.

The implication is a direct splice of the two papers. Kubis proves that a
weak-star-countably closed norming subspace that generates projections is
induced by a projectional skeleton, and induced subspaces generate projections.
Kalenda's Theorem 4.1 in arXiv:1805.11901 proves that, for norming `D`, being
induced by a projectional skeleton is equivalent to `D` being weak-star
countably closed and `(X, sigma(X,D))` being monotonically Sokolov; it also
gives equivalent continuous-image formulations.

## Limitations

- This records a closure-normalized answer, not a complete treatment of
  arbitrary norming subspaces `D` that are not weak-star-countably closed.
- It does not address the other final-section questions in arXiv:0802.1109,
  including the general projectional-generator question, the closed-subspace
  SCP question, or the `C(omega_2+1)` Plichko-embedding question.
- The result is literature-implied rather than original to this run.

## Search Evidence

Cheap local index search found no prior packet for arXiv:0802.1109 or for the
monotonically Sokolov characterization. Web and local source searches for
`projectional skeleton`, `projectional generator`, `monotonically Sokolov`,
`Tau_D`, `sigma(X,D)`, `Corson compact norming`, and `C(omega_2+1) Plichko`
surfaced arXiv:1805.11901 as the decisive later literature anchor.

## Files

- `solution_packet.pdf`: rendered human-facing status note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original Kubis source paper.
- `supporting_paper_1805.11901.pdf`: supporting Kalenda paper.
- `code/check_implication.py`: verifies decisive text snippets in both PDFs.
