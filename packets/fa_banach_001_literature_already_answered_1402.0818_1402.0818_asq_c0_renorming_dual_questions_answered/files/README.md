# Literature status: ASQ renorming and dual-ASQ questions from 1402.0818

Status: `literature_already_answered`

This packet records two questions/open ends in Abrahamsen--Langemets--Lima,
`1402.0818`, "Almost square Banach spaces", that were explicitly answered by
later ASQ papers.

## Source questions

Source paper: Trond A. Abrahamsen, Johann Langemets, and Vegard Lima,
"Almost square Banach spaces", arXiv:1402.0818.

1. In Section 2, immediately after Theorem 2.9 (`thm:c0-asq`, source lines
   526--561), the authors prove the separable case and note that they do not
   know whether the same ASQ renorming result holds for a general Banach space
   containing `c_0`.
2. In Section 6, Question 6.6 (`quest`, source lines 1438--1442), the authors
   ask whether a dual space `X^*` can be ASQ.

## Supporting answers

Supporting paper 1: Julio Becerra Guerrero, Gines Lopez-Perez, and Abraham
Rueda Zoca, "Some results on almost square Banach spaces", arXiv:1512.00610.

- The introduction explicitly says the paper gives a positive answer to the
  separability-removal question from `1402.0818`.
- Theorem 2.2 (`renormageneral`) proves that every Banach space containing an
  isomorphic copy of `c_0` admits an equivalent ASQ norm.
- Corollary 2.3 (`carac0asq`) gives the exact characterization: a Banach space
  admits an equivalent ASQ norm if and only if it contains an isomorphic copy
  of `c_0`.

Supporting paper 2: Trond A. Abrahamsen, Petr Hajek, and Stanimir Troyanski,
"Almost square dual Banach spaces", arXiv:1912.12519.

- The introduction explicitly cites `1402.0818`, Question 6.6, and says the
  paper gives a positive answer to whether ASQ spaces can be dual.
- Theorem 3.4 (`thm:bidual-ell-infty-asq`) constructs a bidual ASQ renorming of
  `ell_infty`.
- Theorem 3.7 (`thm:dual-c0-asq-renorming`) proves that a dual Banach space
  admits a dual ASQ norm if and only if it contains an isomorphic copy of `c_0`.

## Scope

This is not a new proof packet. It records already-known literature answers
and keeps the queue from spending more time on these exact open-problem
signals. The separate LASQ/WASQ separation question in `1402.0818` is not
settled or classified by this packet.

## Files

- `source_paper.pdf`: arXiv:1402.0818.
- `supporting_paper_1512.00610.pdf`: arXiv:1512.00610.
- `supporting_paper_1912.12519.pdf`: arXiv:1912.12519.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

Ledger record:
`runs/fa_banach_001/ledger/results/1402.0818_asq_c0_renorming_dual_questions_answered.json`
