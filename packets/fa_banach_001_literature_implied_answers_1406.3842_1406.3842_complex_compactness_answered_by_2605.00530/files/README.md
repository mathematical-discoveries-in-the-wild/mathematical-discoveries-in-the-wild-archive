# 1406.3842 complex compactness question answered by 2605.00530

Status: `literature_implied_answer` (preprint claim; needs human verification)

## Source question

- Source paper: Michael Cwikel, Mario Milman, Richard Rochberg, "A brief survey of Nigel Kalton's work on interpolation and related topics", arXiv:1406.3842.
- Location: page 2, Section 2.
- Question: if a linear operator is bounded on both endpoint spaces of a Banach couple and compact on one endpoint, must it be compact on the interpolation space? The source says that for the complex method this question remained unanswered in 2014.

## Supporting literature

- Supporting paper: Evgeniy Pustylnik, "A new approach to interpolation of compact linear operators", arXiv:2605.00530, posted 2026-05-01.
- Location: pages 2 and 7-8.
- The paper states condition (2),
  \[
  \|T\|_{A\to B}\le W(\|T\|_{A_0\to B_0},\|T\|_{A_1\to B_1}),
  \]
  with \(W(\alpha,\beta)\to0\) as \(\beta\to0\) for bounded \(\alpha\). It notes that complex interpolation satisfies this with \(W(\alpha,\beta)=\alpha^{1-\theta}\beta^\theta\), proves compactness for embeddings under this hypothesis, and then passes from embeddings to arbitrary operators.
- The source question phrases compactness at \(A_0\); Pustylnik writes the proof with compactness at \(A_1\). For the complex method this is the same one-sided question after swapping the endpoints, replacing \(\theta\) by \(1-\theta\).

## Scope and caution

This packet is not an original proof from this run. It records that the target appears to be answered by later literature after direct identification. The supporting paper does not appear to cite arXiv:1406.3842 explicitly, so the packet belongs in `literature_implied_answers/`, not `literature_already_answered/`.

Because arXiv:2605.00530 is a very recent preprint that claims a broad resolution of a classical problem, the recommendation is human verification of the proof before treating the problem as settled in run summaries.

## Local files

- `source_paper.pdf`: arXiv:1406.3842.
- `supporting_paper_2605.00530.pdf`: arXiv:2605.00530.
- `solution_packet.pdf`: compact status note.
