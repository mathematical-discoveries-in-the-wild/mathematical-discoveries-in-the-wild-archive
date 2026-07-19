# Literature answer: classical Schreier space lacks uniform lambda

Run: `fa_banach_001`

Status: `literature_already_answered (classical Schreier uniform-lambda subquestion)`

This packet records an exact later-literature answer. It is not an original
proof from the run.

## Original question

- L. Antunes, K. Beanland, and H. V. Chu, *On the geometry of higher order
  Schreier spaces*, arXiv:1903.03492.
- Location: PDF page 9, immediately before Theorem 3.1 in the section
  “The lambda-property for Schreier spaces.”
- Local copy: `source_paper.pdf`.

The source states that it had not determined whether the classical Schreier
space (X_{\mathcal S_1}) has the uniform lambda-property. The same paragraph
also asks whether (X_{\mathcal F}) has the lambda-property for every regular
family (\mathcal F).

## Separate supporting answer

- K. Beanland and H. V. Chu, *The Schreier Space Does Not Have the Uniform
  Lambda-Property*, arXiv:1904.10384; later published in *Proceedings of the
  American Mathematical Society* 149 (2021), 5131-5137,
  DOI `10.1090/proc/14766`.
- Location: PDF page 1, Theorem 1.1; proof in Section 3, especially pages 4-6.
- Local copy: `supporting_paper_1904.10384.pdf`.

The supporting paper explicitly says its Theorem 1.1 solves the problem
restated in arXiv:1903.03492. It constructs unit vectors (x_n) and proves

\[
  \lambda(x_n)\le \frac{n+1}{n^2}\longrightarrow 0,
\]

so (X_{\mathcal S_1}) does not have the uniform lambda-property. Its Theorem
1.2 also proves the analogous negative result for the dual.

## Scope

This clears exactly the classical (X_{\mathcal S_1}) uniform-lambda
subquestion. It does not answer the source's broader question for arbitrary
regular families. The supporting paper itself lists the corresponding
higher-order Schreier-space question as future research and conjectures a
negative answer.

## Search and verification

- Cheap run indexes were searched for both arXiv ids and the phrases “higher
  order Schreier,” “uniform lambda,” and “Schreier spaces”; no prior packet was
  found.
- An exact web search for `Schreier space uniform lambda-property` returned
  arXiv:1904.10384 and the AMS publication page.
- The papers are distinct; the answer paper was posted on 23 April 2019 after
  the question paper's 8 March 2019 posting.
- The supporting authors explicitly identify the source as a restatement of
  the problem, so this belongs in `literature_already_answered`, not
  `literature_implied_answers`.

## Human review recommendation

Check PDF page 9 of the source against Theorem 1.1 on page 1 of the supporting
paper. The identification is direct and exact; no theorem translation is
needed.

