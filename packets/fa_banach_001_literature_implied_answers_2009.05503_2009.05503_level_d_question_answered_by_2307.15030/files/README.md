# Literature-implied answer: logarithmic-degree level inequality on \(S_n\)

status: literature_implied_answer

source: Yuval Filmus, Guy Kindler, Noam Lifshitz, and Dor Minzer,
*Hypercontractivity on the symmetric group*, arXiv:2009.05503.

supporting answer: Peter Keevash and Noam Lifshitz,
*Sharp hypercontractivity for symmetric groups and its applications*,
arXiv:2307.15030.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/2009.05503_level_d_question_answered_by_2307.15030/`

ledger: `runs/fa_banach_001/ledger/results/2009.05503_level_d_question_answered_by_2307.15030.json`

## Identification

Section 7.1 of arXiv:2009.05503 asks for a quantitatively sharper level-
\(d\) inequality and, in particular, whether the degree-\(d\) Fourier weight
has size at most \(\varepsilon^{2-o(1)}\) when
\(d=c\log(1/\varepsilon)\) for sufficiently small constant \(c>0\).

Keevash--Lifshitz, Theorem 4.1, proves a sharp level-\(d\) inequality for
biglobal functions. If the original Boolean function is
\((2d,\varepsilon)\)-global, then every restriction of size at most \(d\)
has \(L^2\)-norm at most \(\varepsilon\) and, by Booleanity, \(L^1\)-norm at
most \(\varepsilon^2\). Hence it is
\((2,\varepsilon^2,\varepsilon,d)\)-biglobal in the later notation.
Substitution in Theorem 4.1 gives

\[
  \|f^{=d}\|_2^2
  \leq \varepsilon^4
  \left(\frac{4\cdot10^6\log(1/\varepsilon)}{d}\right)^d
\]

whenever \(d\leq\min\{\frac14\log(1/\varepsilon),10^{-5}n\}\).
For \(d=c\log(1/\varepsilon)\) and sufficiently small fixed \(c\), this is
\(\varepsilon^{4-c\log(4\cdot10^6/c)}\), which is stronger than the
requested \(\varepsilon^{2-o(1)}\) upper-bound regime.

The equality sign in the source's displayed question cannot be literal (for
example, the zero function is an immediate exception); the packet answers the
intended upper-bound question indicated by the surrounding discussion.

## Files

- `main.tex`: compact theorem-identification note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2009.05503.
- `supporting_paper_2307.15030.pdf`: the answering paper.

