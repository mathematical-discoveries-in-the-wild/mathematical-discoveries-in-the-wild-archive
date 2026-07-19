# Partial packet: first limit BRS spaces have SHAI

## Source

- Paper: William B. Johnson, N. Christopher Phillips, and Gideon Schechtman, *The SHAI property for the operators on \(L^p\)*.
- arXiv: `2102.03966`.
- Source problem: Problem `\ref{Prob:BRSspacesSHAI}` asks whether complemented subspaces of \(L^p\), and in particular the \(\aleph_1\) Bourgain--Rosenthal--Schechtman examples, have the SHAI property.

## Classification

- Status: `partial_result_likely_valid`.
- Scope: proves the SHAI property for the first limit Bourgain--Rosenthal--Schechtman/Rosenthal space \(R_\omega^p\), equivalently for its centered part \(R_\omega^{p,0}\) and then for \(R_\omega^p=\mathbb K\oplus R_\omega^{p,0}\).
- Limitation: this does not settle arbitrary complemented subspaces of \(L^p\), arbitrary unconditional-basis complemented subspaces, or all BRS spaces \(R_\alpha^p\).

## Main Idea

The centered first limit BRS space is the independent sum of finite-dimensional Bernoulli mean-zero blocks \(H_n=L_p^0(\{0,1\}^n)\).  For each infinite \(A\subseteq\mathbb N\), the \(m\)-th block \(H_m\) embeds isometrically and complementably into \(H_{a_m}\), where \(A=\{a_1<a_2<\cdots\}\).  A continuum almost-disjoint family of such \(A\)'s gives continuum many complemented self-copies whose projection products are finite rank.  Since finite-rank operators vanish in every nonzero quotient of \(\mathcal L(X)\), the Johnson--Phillips--Schechtman density argument still runs even though the copied ranges are not whole FDD block spans.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper `2102.03966`.
- `supporting_paper_2606.10260.pdf`: first-limit BRS realization used for the Bernoulli block model.
- `supporting_paper_1811.06865.pdf`: finite direct-sum permanence reference for SHAI.
- `figures/open_problem_crop.png`: crop of the source problem statement.
- `code/crop_open_problem.py`: crop helper.

## Verification Notes

Cheap indexes were searched for `2102.03966`, `SHAI`, `L^1`, `C_\infty`, `complemented subspace of L^p`, and BRS keywords.  Existing run memory only had the separate `C(K)` SHAI conditional packet for `2007.14112`.  Local later-source search found no exact SHAI settlement for the BRS subquestion, but did find the BRS finite-block realization used here.

Human review should focus on the block-copy projection estimates in Lemma 2.2 and the finite-rank-overlap replacement in the quotient argument.
