# Atomic masa max-tensor question: literature-implied positive answer

Status: `literature_implied_answer (partial subcase)`

## Source question

Simon Wassermann, *Tensor Products of Maximal Abelian Subalgebras of
C*-Algebras*, arXiv:0711.0131, Section 4, PDF page 9.  Among several questions
about masas in maximal tensor products, the paper singles out the case
`C_1 ~= C_2 ~= ell-infinity(N)` in `B(ell_2) tensor_max B(ell_2)` and observes
that a positive Kadison-Singer solution would make their tensor product
maximal abelian.

## Identification

Marcus, Spielman, and Srivastava, *Interlacing Families II: Mixed
Characteristic Polynomials and the Kadison-Singer Problem*, arXiv:1306.3969,
prove results implying a positive solution of Kadison-Singer.  Hence the
diagonal atomic masa `D = ell-infinity(N)` has the extension property in
`B(ell_2)`.  Applying Wassermann's own Theorem 2 and Corollary 3 gives

- `(D tensor 1)' = D tensor B(ell_2)` in
  `B(ell_2) tensor_max B(ell_2)`; and
- `D tensor D` is a masa in `B(ell_2) tensor_max B(ell_2)`.

This implication is identified here; the supporting authors do not discuss
Wassermann's tensor-product question.

## Scope

The diffuse-masa question and the questions for arbitrary pairs of masas are
not answered by Kadison-Singer.  A separate attempt note records the surviving
max-to-min/Calkin-kernel obstruction.

## Files

- `solution_packet.pdf`: compact review note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:0711.0131.
- `supporting_paper_1306.3969.pdf`: Marcus--Spielman--Srivastava.

Ledger: `runs/fa_banach_001/ledger/results/0711.0131_atomic_masa_max_tensor_kadison_singer.json`.
