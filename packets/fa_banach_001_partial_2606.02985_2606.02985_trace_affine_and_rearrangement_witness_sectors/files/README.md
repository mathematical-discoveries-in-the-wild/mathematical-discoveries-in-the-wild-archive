# Explicit witness sectors of the random-embedding conjecture

Status: `partial_result_likely_valid; human_review_needed`

Source: Ben Hayes, David Jekel, and Srivatsav Kunnawalkam Elayavalli,
*Questions on the structure of random embeddings of L(F_2)*,
arXiv:2606.02985v1 (2026).

## Result

Conjecture 1.2 of the source holds, both almost surely and in the stated
expectation form, for two infinite classes of auxiliary-unitary witness
polynomials:

1. every self-adjoint trace-affine polynomial, equivalently every polynomial
   of total witness degree at most one modulo cyclicity of the trace;
2. every sum of separated single-conjugation terms
   `A_j(U)V_jB_j(U)V_j^*`, with self-adjoint base polynomials `A_j,B_j` and a
   different witness `V_j` for each term.

The first class reduces exactly to trace norms by polar decomposition. The
second reduces exactly to pairings of decreasing eigenvalue rearrangements.
Almost-sure *-moment convergence of independent Haar matrices then gives the
large-matrix limit; uniform boundedness gives convergence of expectations.

## Scope

The full conjecture remains open. The result does not treat mixed witness
words, higher witness degree, or simultaneous affine and conjugation terms in
one witness. Those interactions encode the difficult existential-embedding
content of the source question.

## Packet contents

- `main.tex` and `solution_packet.pdf`: full partial theorem and proof.
- `source_paper.pdf`: arXiv:2606.02985v1.
- `figures/open_problem_crop.png`: Conjecture 1.2 on source page 3.
- `code/verify_unitary_optimizers.py`: finite matrix optimizer checks.
- `verification_report.md`: proof audit and limitations.
