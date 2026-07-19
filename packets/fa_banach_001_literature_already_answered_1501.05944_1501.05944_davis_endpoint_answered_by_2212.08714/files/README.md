# Literature Answer: Davis Endpoint for Noncommutative Symmetric Spaces

Status: `literature_already_answered`

Source problem: Randrianantoanina and Wu, *Martingale inequalities in
noncommutative symmetric spaces*, arXiv:1501.05944. In the final section they
ask whether, for a symmetric Banach function space `E` with `p_E=1` and
`q_E <= 2`, the noncommutative martingale Hardy spaces satisfy
`H_E(M)=h_E(M)`.

Supporting answer: Randrianantoanina, *P. Jones' interpolation theorem for
noncommutative martingale Hardy spaces*, arXiv:2212.08714. Proposition
`Davis-symmetric` and Corollary `Davis` prove that if
`E in Int(L_1,L_2)`, then
`H_E^c(M)=h_E^d(M)+h_E^c(M)` and consequently the mixed Hardy spaces coincide:
`H_E(M)=h_E(M)`. The same corollary is explicitly described as answering
`[RW, Problem 4.2]`, where `RW` is the arXiv:1501.05944 paper.

Scope of the answer: the 2015 Boyd-index formulation is answered with a sharp
threshold. If `q_E < 2`, standard Boyd interpolation gives
`E in Int(L_1,L_2)`, hence the answer is affirmative. At the boundary
`q_E=2`, the same 2022 source notes sharpness: validity of the column Davis
identity forces `E in Int(L_1,L_2)`. Thus the literal `q_E <= 2` statement is
not true for arbitrary symmetric spaces at the boundary.

Concrete boundary obstruction: take, for example,
`E = L_1 + L_{2,\infty}` on `(0,infty)`. This is a symmetric Fatou Banach
function space with Boyd indices `p_E=1` and `q_E=2`, but it is not an
interpolation space for `(L_1,L_2)` because it contains functions in weak
`L_2` that are not in `L_1+L_2`. The sharpness statement from arXiv:2212.08714
therefore rules out the Davis equality for this `E` in general.

Files:
- `source_paper.pdf`: arXiv:1501.05944, when local PDF fetch/build succeeds.
- `supporting_paper_2212.08714.pdf`: decisive later answer source, when local
  PDF fetch/build succeeds.
- `main.tex`, `solution_packet.pdf`: compact status note.

This packet does not claim a new proof. It records that the extracted target is
already resolved in later literature and should not be pursued as a new result.
