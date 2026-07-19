# Literature-Implied Answer: Schur and RNP for Lipschitz-Free Spaces

Status: `literature_implied_answer`.

Source paper: M. Cuth, M. Doucha and P. Wojtaszczyk, *Embeddings of Lipschitz-free spaces into \(\ell_1\)*, arXiv:1909.05285.

Supporting paper: R. J. Aliaga, C. Gartland, C. Petitjean and A. Prochazka, *Purely 1-unrectifiable metric spaces and locally flat Lipschitz functions*, arXiv:2103.09370.

## Source Question

The source extraction contains two nearby signals.

First, Question 1 in the introduction asks whether a closed negligible subset of an \(\mathbb R\)-tree always has a Lipschitz-free space embedding isometrically into some \(\ell_1(\Gamma)\). This is answered negatively in the same source paper by Theorem 1, so it is only an extraction false positive.

Second, after Corollary 2.4 (`c:RNPSchurL1`), the source paper proves the equivalence of the Schur and Radon-Nikodym properties for Lipschitz-free spaces over closed subsets of \(\mathbb R\)-trees and then states that it is unknown whether these equivalences hold for general Lipschitz-free spaces. This is the question recorded here.

## Identification

The supporting paper proves a stronger general theorem. Its Theorem C in the introduction, and Theorem 4.6 (`thm:equivalences`) in the body, state that for every metric space \(M\), the completion of \(M\) is purely 1-unrectifiable if and only if \(\mathcal F(M)\) has the Radon-Nikodym property, if and only if \(\mathcal F(M)\) has the Schur property, with equivalent formulations via the Krein-Milman property and non-containment of \(L_1\).

Thus the source paper's general Schur/RNP equivalence question has an affirmative answer after the standard identification of \(\mathcal F(M)\) with the free space over the completion of \(M\).

## Provenance

This packet is classified as `literature_implied_answer`, not `literature_already_answered`. The supporting paper explicitly treats the broad Schur/RNP problem in Lipschitz-free spaces and says the equivalence had been suggested by prior work, but a source search did not find an explicit citation back to arXiv:1909.05285 or to its exact open-problem sentence.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_2103.09370.pdf`: decisive supporting paper.

