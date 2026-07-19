# Partial Result: Central Finite-Trace Exhaustions

Status: `partial_result_likely_valid`.

Source target: arXiv:1002.3672, Yoshimichi Ueda, *On the predual of
non-commutative H^\infty*.

Source question: Section 3.1 asks whether the liftability of weakly relatively
compact subsets in `M_*/A_perp` survives in the semifinite tracial setting.

Result: the liftability property holds for semifinite tracial
non-commutative `H^\infty` algebras admitting a central finite-trace
decomposition `1=sum z_n` with `z_n in D=A cap A^*` and `Tr(z_n)<infty`.
Equivalently, the theorem covers `l_infty` direct sums of finite tracial
non-commutative `H^\infty` algebras with the summed trace.

Idea: the central projections split
`M_*/A_perp` as an `l_1`-sum of the finite quotient preduals.  Ueda's finite
theorem applies on each coordinate, and weak compactness in an `l_1`-sum is
exactly coordinate weak compactness plus uniformly small tails.  The unique
extension map preserves coordinate norms, so it preserves the tail condition.

Scope: this does not solve the full semifinite problem.  The proof uses
centrality to obtain a genuine `l_1` direct-sum quotient; it does not address
noncentral finite corners, continuous central decompositions, or nontracial
non-commutative `H^\infty` algebras.

Files:
- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1002.3672.
