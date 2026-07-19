# Literature-Implied Status: Tingley problems from arXiv:1712.09192

status: literature_implied_answer (mixed: one full source problem, one partial subcase)
run_id: fa_banach_001
agent_id: agent_lane_16
source_arxiv_id: 1712.09192
supporting_arxiv_ids: 1804.10674; 1803.00763
updated_at: 2026-06-28T20:35:17Z

## Source Questions

Mori's Section 6 lists three open problems after proving Tingley-type results
for von Neumann algebra preduals and self-adjoint von Neumann parts.

1. `problem-C*`: if `A` is a unital C*-algebra and
   `Phi:S(A)->S(A)` is a surjective isometry fixing every invertible norm-one
   element, must `Phi` be the identity?
2. Tingley's problem for `A_sa` and `B_sa` when `A,B` are unital C*-algebras.
3. Tingley's problem for Haagerup noncommutative `L^p(M)`, `1<p<infty`,
   `p != 2`.

## Identification

Mori--Ozawa, arXiv:1804.10674, prove that every unital complex C*-algebra,
as a real Banach space, has the Mazur-Ulam property. This answers
`problem-C*`: the sphere isometry extends to a real linear surjective isometry;
because it fixes all invertible norm-one elements, it fixes all unitaries, and
Russo--Dye then forces the extension to be the identity.

Fernandez-Polo--Jorda--Peralta, arXiv:1803.00763, solve the Schatten-class
instance of the noncommutative `L^p` problem. Their abstract and main theorem
state that every surjective isometry between unit spheres of `C_p(H)` spaces
for `1<p<infty`, `p != 2`, extends to a complex linear or conjugate linear
surjective isometry.

## Scope

This packet does not claim a new proof. It records literature status and a
direct identification:

- `problem-C*` is answered by the later Mori--Ozawa C*-algebra MUP theorem.
- The noncommutative `L^p` problem is answered for `M=B(H)` with the standard
  trace, i.e. for Schatten classes `C_p(H)`.
- The general self-adjoint part problem for unital C*-algebras and the full
  Haagerup `L^p(M)` problem for arbitrary von Neumann algebras remain outside
  this packet.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1712.09192.
- `supporting_paper_1804.10674.pdf`: Mori--Ozawa.
- `supporting_paper_1803.00763.pdf`: Fernandez-Polo--Jorda--Peralta.
