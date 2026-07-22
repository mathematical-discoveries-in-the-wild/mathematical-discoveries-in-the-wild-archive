# Literature answer: intermediate Gelfand numbers for Schatten embeddings

Status: `literature_already_answered`.

## Original question

Aicke Hinrichs, Joscha Prochno, and Jan Vybíral, *Gelfand numbers of
embeddings of Schatten classes*, arXiv:2011.06554. In Section 4.6, p. 21 of
the arXiv PDF, the authors leave open a good lower bound for

\[
c_n(\mathcal S_p^N\hookrightarrow\mathcal S_q^N),
\qquad 1\le p\le2\le q\le\infty,
\]

in the intermediate range
`c_(p,q) N^2 <= n <= N^2 - c N^(1+2/q) + 1`.

## Explicit later answer

Joscha Prochno and Michał Strzelecki, *Approximation, Gelfand, and
Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050,
explicitly say on p. 5 that their first result "closes a gap" in the 2020
paper and provides the missing asymptotically matching lower bound.

- Theorem A (p. 6) and Proposition 3.1 (p. 19) give

  \[
  c_n(\mathcal S_p^N\hookrightarrow\mathcal S_q^N)
  \gtrsim N^{-1/2-1/p}\sqrt{N^2-n+1}
  \]

  for `(1-c)N^2 <= n <= N^2-cN^(1+2/q)+1`, matching the earlier upper
  bound. For `1 <= p <= 2`, the lower-bound constant can be taken to be 1.

- Proposition 3.2 (p. 20) supplies the complementary lower bound

  \[
  c_n(\mathcal S_p^N\hookrightarrow\mathcal S_q^N)
  \gtrsim \min\{1,N^{3/2-1/p}/\sqrt n\}
  \]

  through `n <= (1-c)N^2`.

Together these results cover the full intermediate strip asked about in the
source. The supporting authors explicitly cite the original paper and identify
their contribution as closing its gap, so this is an exact
`literature_already_answered` match rather than an agent-inferred implication.

## Files

- `main.tex`, `solution_packet.pdf`: compact theorem-level identification.
- `source_paper.pdf`: arXiv:2011.06554.
- `supporting_paper_2103.13050.pdf`: the answering paper.
- Ledger: `runs/fa_banach_001/ledger/results/2011.06554_schatten_gelfand_intermediate_answered_2103.13050.json`.

No part of this packet is claimed as a new mathematical result.
