# Literature-Implied Answer: C*-Case Of The Isometry Rigidity Question

Source: arXiv:2003.11567, Bruno M. Braga, "On Banach algebras of band-dominated operators and their order structure".

Status: `literature_implied_answer (partial C*-subcase; strengthened to bijective coarse equivalence)`.

## Question Identified

Section 7 of the source paper asks whether a Banach-space isometry of uniform Roe algebras already forces coarse equivalence. In Problem 7.1 (`Prob2`) this is asked for strictly convex Banach spaces with 1-symmetric bases. The paper then notes that the authors do not know the answer even for `E = l_2`, and asks the weaker C*-case in Problem 7.2 (`ProblemIsometryRig`): if `C_u^*(X)` and `C_u^*(Y)` are isometric as Banach spaces and are also isomorphic as ordered Banach spaces, must `X` and `Y` be coarsely equivalent?

## Supporting Literature

Baudier--Braga--Farah--Khukhro--Vignati--Willett, arXiv:2106.11391, "Uniform Roe algebras of uniformly locally finite metric spaces are rigid", proves as Theorem 1 (`T1`) that if `C_u^*(X)` and `C_u^*(Y)` are *-isomorphic, then `X` and `Y` are coarsely equivalent.

Vignati, arXiv:2602.01998, "The rigidity problem for uniform Roe algebras", strengthens this as Theorem `thmi:main`: if `C_u^*(X)` and `C_u^*(Y)` are *-isomorphic, then `X` and `Y` are bijectively coarsely equivalent.

## Identification

Under the standard complex-linear reading of "isometric as Banach spaces", a surjective isometry `T:C_u^*(X)->C_u^*(Y)` gives, by Kadison's theorem, a unitary `u=T(1)` such that `a -> u^*T(a)` is a unital Jordan *-isomorphism. Uniform Roe algebras contain the compact operators as an essential simple ideal, hence they are prime C*-algebras. A Jordan *-isomorphism onto a prime C*-algebra is either multiplicative or anti-multiplicative. In the anti-multiplicative case, composing with the matrix transpose anti-automorphism of `C_u^*(Y)` gives an actual *-isomorphism. Theorem `thmi:main` of arXiv:2602.01998 then gives bijective coarse equivalence. The earlier arXiv:2106.11391 theorem already gave coarse equivalence; the 2026 theorem upgrades the conclusion.

Thus the C*-subcase of Problem 7.1 has a positive literature-implied answer with the stronger conclusion of bijective coarse equivalence, and Problem 7.2 has a positive answer even without its additional ordered-Banach-space-isomorphism hypothesis.

## Scope Limitations

This packet does not answer the full Problem 7.1 for arbitrary strictly convex Banach spaces with 1-symmetric bases. The Kadison step is genuinely C*-algebraic and uses the Hilbert-space uniform Roe algebra `C_u^*(X)`.

## Files

- `source_paper.pdf`: arXiv:2003.11567.
- `supporting_paper_2106.11391.pdf`: arXiv:2106.11391.
- `supporting_paper_2602.01998.pdf`: arXiv:2602.01998.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
