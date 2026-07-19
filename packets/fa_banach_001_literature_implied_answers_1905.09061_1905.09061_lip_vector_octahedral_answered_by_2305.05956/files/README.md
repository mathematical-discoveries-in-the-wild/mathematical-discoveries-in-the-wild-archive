# Literature-Implied Answer: Vector-Valued Lipschitz Octahedrality

- status: `literature_implied_answer`
- source question: Langemets--Rueda Zoca, arXiv:1905.09061, Problem 1.3
- supporting papers: Rueda Zoca, arXiv:2207.08717; Medina--Rueda Zoca, arXiv:2305.05956

## Question

Problem 1.3 of arXiv:1905.09061 asks whether, if `Lip(M)` is octahedral and
`X` is a non-trivial Banach space, then `Lip(M,X)` is octahedral.

## Answer

Yes. The answer follows by combining two later theorems.

First, arXiv:2207.08717 records that if `Lip(M)` is octahedral, then `Lip(M)`
is universally octahedral; equivalently, `L(Y,Lip(M))` is octahedral for every
Banach space `Y`.

Second, Theorem 4.2 of arXiv:2305.05956 characterizes universal octahedral
domains: `L(Z,Y)` is octahedral for every Banach space `Y` if and only if
`Z*` is universally octahedral.

Apply this with `Z = F(M)`. Since `F(M)* = Lip(M)` is universally
octahedral, `L(F(M),X)` is octahedral for every Banach space `X`. The canonical
linearization isometry identifies `L(F(M),X)` with `Lip(M,X)`, so Problem 1.3
has an affirmative answer.

## Scope

This is not claimed as a new original proof. It is a direct identification of
an answer implied by later literature.

## Files

- `source_paper.pdf`: arXiv:1905.09061
- `supporting_paper_2207.08717.pdf`: universal octahedral range theorem and
  `Lip(M)` example
- `supporting_paper_2305.05956.pdf`: universal octahedral domain theorem
- `solution_packet.pdf`: compact status note
