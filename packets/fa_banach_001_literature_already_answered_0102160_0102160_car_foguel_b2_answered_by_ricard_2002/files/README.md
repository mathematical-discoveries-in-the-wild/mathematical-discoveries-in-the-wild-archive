# Literature Answer: the CAR Foguel--Hankel \(B_2\) condition

Status: `literature_already_answered`.

## Original question

Catalin Badea, *Operators near completely polynomially dominated ones and
similarity problems*, arXiv:math/0102160.

Theorem 1.4 introduces

\[
B_2(\alpha)=\sum_{k\geq0}(k+1)^2|\alpha_k|^2
\]

for the CAR-valued Foguel--Hankel operator \(R(Y_\alpha)\).  On page 5 of the
22-page arXiv PDF the paper asks whether finiteness of \(B_2\) implies that
\(R(Y_\alpha)\) is similar to a contraction.  Page 14 repeats that the
question is still open after proving the stronger \(B_3<\infty\) condition.

## Answer

Yes.  Eric Ricard's distinct later paper, *On a Question of Davidson and
Paulsen*, Journal of Functional Analysis 192 (2002), 283--294, DOI
10.1006/jfan.2001.3899, gives the missing converse.  Its abstract explicitly
says that it answers the Davidson--Paulsen question about similarity to a
contraction for this class of CAR-valued Foguel--Hankel operators.  Combined
with the necessity already recorded in Badea's Theorem 1.4, the resulting
criterion is exactly

\[
R(Y_\alpha)\text{ is similar to a contraction}
\quad\Longleftrightarrow\quad B_2(\alpha)<\infty.
\]

There is also later full-text corroboration.  Chalmoukis--Stylogiannis,
arXiv:2005.01660, Theorem 4.1 and the paragraph immediately after it (PDF
pages 14--15), state Ricard's decisive Hankel Schur-multiplier theorem and
explicitly note that it answers the Davidson--Paulsen CAR Foguel--Hankel
similarity question.

This is an explicit literature answer, not a new proof from this run.

## Evidence and availability

- The source question was checked directly on PDF pages 5 and 14.
- Ricard's journal metadata and answer-identifying abstract were checked via
  DOI/Crossref and the author's institutional HAL record `hal-00475270`.
- HAL has a bibliographic record but no deposited file; the publisher's
  full-text endpoint requires an API key.  No Ricard PDF is therefore claimed
  as locally verified.
- The later open-access corroborating PDF was checked directly on pages
  14--15 and is included here.

## Files

- `source_paper.pdf`: arXiv:math/0102160.
- `supporting_paper_chalmoukis_stylogiannis_2021.pdf`: later full-text
  corroboration, arXiv:2005.01660 / Results in Mathematics 76 (2021), 173.
- `main.tex` and `solution_packet.pdf`: compact status note.
- `tmp/hal_404_response.html`: retained diagnostic showing that the HAL record
  currently exposes no deposited article file.

