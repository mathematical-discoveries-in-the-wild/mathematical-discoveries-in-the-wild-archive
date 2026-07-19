# Literature-implied status: Question CIC in arXiv:1410.4527

Status: `literature_implied_answer (claimed full affirmative answer to Question CIC by arXiv:2605.00530; human verification recommended)`.

## Source question

Michael Cwikel and Richard Rochberg, "Nigel Kalton and complex interpolation of compact operators", arXiv:1410.4527.

The target is Question CIC in Section 1. In the paper's notation, \((X_0,X_1)\blacktriangleright(Y_0,Y_1)\) means that every linear operator \(T:X_0+X_1\to Y_0+Y_1\) which is compact \(X_0\to Y_0\) and bounded \(X_1\to Y_1\) is compact
\[
[X_0,X_1]_\theta\to [Y_0,Y_1]_\theta,\qquad 0<\theta<1.
\]
Question CIC asks whether this holds for all Banach couples.

## Supporting literature

Evgeniy Pustylnik, "A new approach to interpolation of compact linear operators", arXiv:2605.00530, posted 2026-05-01.

Checked local source passages:

- `data/parsed/arxiv_sources/2605.00530/Pustilnyk-Arxiv.tex`, lines 270-284: the preprint states that two-sided compactness is automatic under standard interpolation of bounded operators, while one-sided compactness needs condition (2).
- lines 336-344: condition (2) is the interpolation norm estimate
  \[
  \|T\|_{A\to B}\le W(\|T\|_{A_0\to B_0},\|T\|_{A_1\to B_1}),
  \]
  with \(W(\alpha,\beta)\to0\) as \(\beta\to0\) for bounded \(\alpha\); the complex interpolation functor is explicitly said to satisfy it with \(W(\alpha,\beta)=\alpha^{1-\theta}\beta^\theta\).
- lines 346-349: the Main Theorem concludes compactness of the interpolated embedding under these hypotheses.
- lines 598-610: the final reduction passes from embeddings to arbitrary operators by factoring through image spaces.

## Identification

Question CIC is exactly the one-sided compactness problem for the complex interpolation functor and arbitrary Banach couples. Pustylnik's Main Theorem applies to one-sided compact embeddings whenever condition (2) holds; the source explicitly records that condition (2) holds for the complex method. The final image-space reduction then transfers the embedding result to arbitrary linear operators. Therefore, if Pustylnik's preprint is correct as stated, it gives an affirmative answer to Question CIC.

This is an agent-identified implication. The supporting paper does not appear, in the checked text, to cite arXiv:1410.4527 or to phrase the result as resolving "Question CIC". Because arXiv:2605.00530 is a very recent broad preprint claiming progress on a long-standing open problem, human verification is recommended before marking the problem settled.

## Packet contents

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: source/open-problem paper arXiv:1410.4527.
- `supporting_paper_2605.00530.pdf`: supporting preprint.
