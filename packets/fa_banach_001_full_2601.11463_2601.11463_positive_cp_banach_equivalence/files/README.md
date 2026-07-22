# Positive `C_p`-homeomorphisms and positive Banach isomorphisms coincide

Status: `candidate_full_likely_valid`

Source: Marek Cúth, Jonáš Havelka, Jakub Rondoš, and Bünyamin Sarı,
*The classification of C(K) spaces for countable compacta by positive
isomorphisms*, arXiv:2601.11463v1, Question 4.3 on page 27.

## Claimed full resolution

For countable compact spaces `K,L`, there is a positive linear homeomorphism

`C_p(K) -> C_p(L)`

if and only if there is a positive Banach-space isomorphism

`C(K) -> C(L)`.

Thus Question 4.3 has an affirmative answer. For infinite `K,L`, these
conditions are also equivalent to

`ht(K) <= ht(L) < Gamma(ht(K))`.

Here positivity is one-sided, matching the source convention: the map is
positive, but its inverse need not be positive.

## Idea of the proof

One direction is automatic but seems to have been missed: a linear
`C_p`-homeomorphism has a norm-closed graph. Uniform convergence implies
pointwise convergence, so the closed graph theorem makes both the map and its
inverse norm-bounded.

For the converse, an arbitrary positive Banach isomorphism need not be
`C_p`-continuous. The key is to inspect the particular isomorphisms constructed
in the source paper. Each output coordinate of those maps is a finite linear
combination of input evaluations. The same is true of every inverse output
coordinate: the first construction's inductive inverse simplifies to three
evaluations, and the second inverse is explicitly given by two or three
evaluations. Such coordinate-finite maps are exactly the continuous linear maps
for the pointwise topologies. Homeomorphic conjugacy and finite composition
preserve coordinate-finiteness, so the source proof of its positive Banach
classification simultaneously constructs the required positive
`C_p`-homeomorphism.

## Files

- `main.tex`: detailed proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of Question 4.3.
- `code/render_open_problem_crop.py`: reproducible crop script.
- `verifier_report.md`: independent proof audit checklist.

## Novelty check

A bounded check on 2026-07-21 searched the run indexes, the local 2000--2026
source corpus, the current arXiv page/version, and arXiv web queries for the
exact phrase `positive linear homeomorphism C_p(K)`, the paper title, its four
authors, and close positive-`C_p` classification variants. No later explicit
answer was found. The current arXiv v1 still prints Question 4.3. A July 2026
paper on `C_p` spaces over separable compact lines and a May 2026 paper citing
arXiv:2601.11463 do not address this question. Novelty confidence is moderate:
the argument is short because the decisive coordinate-finite formulas are
already present in the source paper, although the consequence is not stated
there.

## Human review recommendation

Check three points: (1) that “positive linear homeomorphism” has the same
one-sided positivity convention as the paper's positive Banach isomorphisms;
(2) that both inverses in Propositions 2.12 and 2.15 are coordinate-finite at
every point; and (3) that the proof of Theorem 2.4 uses only those maps,
homeomorphism-induced composition operators, and finite composition. If these
pass, the result fully answers Question 4.3.
