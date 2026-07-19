# arXiv:math/0201187 - `d_cb(H_n^k,R_n)` answered by arXiv:math/0410337

Status: `literature_already_answered`

Source/open-problem paper:

- Matthew Neal and Bernard Russo, "Contractive projections and operator spaces", arXiv:math/0201187; Trans. Amer. Math. Soc. 355 (2003), 2223-2262.
- The relevant source question is Problem 1 on PDF page 39: determine the completely bounded Banach-Mazur distance `d_cb(H_n^k,R_n)`.
- The same paper states `H_n^n = R_n`.

Supporting answer paper:

- Matthew Neal and Bernard Russo, "Representation of contractively complemented Hilbertian operator spaces and the Fock space", arXiv:math/0410337; Proc. Amer. Math. Soc. 134 (2006), 475-485.
- Its introduction states that it gives an explicit formula for the completely bounded Banach-Mazur distance from `H_n^k` to `R_n = H_n^n` and `C_n = H_n^1`, answering a question posed in `NeaRus03`.
- Theorem 3 gives
  `d_cb(H_n^k,H_n^1) = sqrt(kn/(n-k+1))`.
- The following corollary on PDF page 10 states explicitly that it is the answer to Problem 1 in `NeaRus03` and gives
  `d_cb(H_n^k,H_n^n) = sqrt(n(n-k+1)/k)`.

Conclusion:

Since `R_n = H_n^n` in the source paper, the answer to Problem 1 of arXiv:math/0201187 is

`d_cb(H_n^k,R_n) = sqrt(n(n-k+1)/k)`, for `1 <= k <= n`.

This is not a new run proof. It is an exact later-literature answer, recorded to prevent duplicate work on an already answered target.

Local files:

- `source_paper.pdf`: arXiv:math/0201187.
- `supporting_paper_0410337.pdf`: arXiv:math/0410337.
- `solution_packet.pdf`: compact rendered status note.
- Ledger: `runs/fa_banach_001/ledger/results/0201187_hnk_row_distance_answered_by_0410337.json`.
