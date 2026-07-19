# 0801.4557 Dungey averaged A_alpha Ritt conjecture answered by 1504.00563

Status: `literature_already_answered`

Source/open-problem paper:

- Nick Dungey, *Subordinated discrete semigroups of operators*, arXiv:0801.4557.
- On PDF page 19, after Theorem 6.1, Dungey defines
  `B = epsilon^{-1} int_0^epsilon A_alpha d alpha` and conjectures that `B` belongs to the Ritt probability class `A` for every `epsilon in (0,1]`.

Supporting answer:

- Alexander Gomilko and Yuri Tomilov, *On discrete subordination of power bounded and Ritt operators*, arXiv:1504.00563.
- The introduction explicitly says that the paper answers Dungey's open question about
  `f_epsilon(lambda)=1 - epsilon^{-1} int_0^epsilon (1-lambda)^alpha d alpha`.
- Theorem 7.1 gives a geometric criterion for regular Hausdorff functions.
- Example 7.4 applies it to
  `h_epsilon(lambda)=1 - epsilon^{-1} int_0^epsilon (1-lambda)^alpha d alpha`
  and concludes that `h_epsilon(T)` is Ritt for every power-bounded operator `T`, stating that this settles Dungey's conjecture. The endpoint `epsilon=1` is covered immediately after by the `h_1` paragraph.

Identification:

The generating function of Dungey's probability `B` is exactly `h_epsilon`.  By Dungey's Theorem 3.1, `B in A` is equivalent to the statement that `Psi(B;T)=h_epsilon(T)` is a Ritt operator for every power-bounded operator `T` on every Banach space.  Gomilko--Tomilov prove precisely this operator statement, with an angle estimate.

Files:

- `source_paper.pdf`: Dungey arXiv:0801.4557.
- `supporting_paper_1504.00563.pdf`: Gomilko--Tomilov arXiv:1504.00563.
- `figures/open_problem_crop.png`: Dungey's page 19 conjecture evidence.
- `figures/supporting_answer_crop.png`: Gomilko--Tomilov Example 7.4 answer evidence.
- `solution_packet.pdf`: compact status note.
- Ledger record: `runs/fa_banach_001/ledger/results/0801.4557_dungey_b_average_ritt_answered_by_1504.00563.json`.

Scope:

This is not a new run proof. It is an explicit later literature answer to the source conjecture.
