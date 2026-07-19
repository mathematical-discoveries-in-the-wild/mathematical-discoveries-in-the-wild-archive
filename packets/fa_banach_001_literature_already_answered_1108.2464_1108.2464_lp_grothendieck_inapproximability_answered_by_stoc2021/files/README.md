# Literature Status: the `1<p<2` Lp Grothendieck approximation problem

Status: `literature_already_answered (conditional negative answer)`

This is a literature-identification packet, not a new proof produced by the
run.

## Source question

Subhash Khot and Assaf Naor, *Grothendieck-type inequalities in
combinatorial optimization*, arXiv:1108.2464v1 (2011), later published in
*Communications on Pure and Applied Mathematics* 65 (2012), 992-1035.

In Section 5, printed page 26 (PDF page 27), after defining

\[
M_p(A)=\max_{\lVert t\rVert_p\leq 1}\sum_{i,j=1}^n a_{ij}t_it_j
\]

for an input matrix with zero diagonal, the authors ask whether, for fixed
`1<p<2`, one can approximate `M_p(A)` in polynomial time within an `O(1)`
factor. They also state that no hardness-of-approximation result was then
known.

## Supporting answer

Vijay Bhattiprolu, Euiwoong Lee, and Assaf Naor, *A Framework for Quadratic
Form Maximization over Convex Sets through Non-Convex Relaxations*, STOC
2021, pp. 870-881, DOI
[10.1145/3406325.3451128](https://doi.org/10.1145/3406325.3451128); full draft
dated October 28, 2022.

Section 8.1 of the full draft, especially Proposition 8.5(1), (4), and (5),
proves that for every fixed `q>2`, assuming the Small Set Expansion Hypothesis
and `P != NP`, there is no polynomial-time constant-factor approximation for
the `2 -> q` norm; the result transfers to the `q* -> q` norm and then to
quadratic maximization over the `ell_{q*}` unit ball, even when the input
matrix has zero diagonal. Taking `q=p*` gives `q*=p` for every fixed
`1<p<2`, which is exactly the source problem.

The supporting authors explicitly describe this as hardness for the
`ell_p` Grothendieck problem that had been left open and separately cite the
Khot-Naor survey as the exposition of the zero-diagonal endpoint context.

## Scope

The answer is conditional on SSEH (and `P != NP` in the stated constant-gap
form). It rules out the requested constant-factor algorithm under those
standard complexity assumptions; it is not an unconditional separation and
does not prove that no such algorithm exists in an absolute mathematical
sense.

## Evidence and files

- [`source_paper.pdf`](source_paper.pdf): arXiv:1108.2464, Section 5,
  printed page 26 / PDF page 27.
- [`supporting_paper_stoc2021.pdf`](supporting_paper_stoc2021.pdf): full
  2022 draft of the STOC 2021 paper, Section 8.1, Proposition 8.5, printed
  pages 75-76 / PDF pages 79-80.
- [`solution_packet.pdf`](solution_packet.pdf): compact rendered status note.
- Ledger:
  `runs/fa_banach_001/ledger/results/1108.2464_lp_grothendieck_inapproximability_answered_by_stoc2021.json`.

Search bounds used for identification: the local run indexes, the exact
phrases `M_p(A)`, `L_p Grothendieck problem`, and `1<p<2`, and the later
authors' full draft and published STOC metadata. The exact result was found in
the later paper itself; no claim of a new result is made.
