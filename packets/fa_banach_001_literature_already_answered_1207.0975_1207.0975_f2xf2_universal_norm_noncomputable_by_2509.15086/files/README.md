# 1207.0975: F2 x F2 Universal Norm Noncomputable

Status: literature_already_answered.

Source/open-problem paper: Tobias Fritz, Tim Netzer, and Andreas Thom,
*Can you compute the operator norm?*, arXiv:1207.0975.

Source question: Question 4.1 asks whether, for
`Gamma = F_2 x F_2`, the function
`Z Gamma -> R`, `a |-> ||a||_u`, is computable.

Supporting answer paper: Isaac Goldbring and Thomas Sinclair,
*On definability of C*-tensor norms*, arXiv:2509.15086.

Answer: No. Goldbring--Sinclair, Corollary `FNTquestion`, proves that for
every `n >= 2`, including `n = infinity`, the standard presentation of
`C*(F_n x F_n)` is not computable. Immediately after the corollary they state
that the case `n = 2` answers the question of Fritz, Netzer, and Thom.

Identification: The standard presentation of `C*(F_2 x F_2)` has generated
points given by finite rational `*`-polynomials in the canonical generators.
Computability of that presentation is exactly an algorithm for approximating
the universal C*-norm of such group-ring elements to arbitrary precision, which
is the function asked for in Question 4.1 of the source paper.

Local files:

- `source_paper.pdf`: arXiv:1207.0975.
- `supporting_paper_2509.15086.pdf`: arXiv:2509.15086.
- `solution_packet.pdf`: compact literature-status note.

Novelty note: This packet records an already-known answer in later literature,
not a new result of the run.
