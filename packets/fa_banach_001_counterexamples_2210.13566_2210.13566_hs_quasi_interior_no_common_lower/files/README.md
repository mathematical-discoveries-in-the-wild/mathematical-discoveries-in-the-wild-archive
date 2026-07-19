# Counterexample packet: no common quasi-interior lower bound

Status: `counterexample_likely_valid`

Source: Jochen Glueck and Andrii Mironchenko, *Stability criteria for positive semigroups on ordered Banach spaces*, arXiv:2210.13566.

Extracted target: after Theorem 8.4 the source asks whether, in the ordered-Hilbert setting of that theorem, every two quasi-interior points `u,v` in the cone dominate a common quasi-interior point `w`.

Result: negative. In the real Hilbert space of self-adjoint Hilbert-Schmidt operators on `ell_2`, with the usual positive cone, there are two quasi-interior points `A,B` such that no nonzero positive `C` satisfies `C <= A` and `C <= B`. Hence there is certainly no common quasi-interior lower bound.

Core mechanism: choose an injective positive diagonal Hilbert-Schmidt operator `A` whose square-root range is the weighted dense range `R = {x : sum n^2 |x_n|^2 < infinity}`. A Baire-category argument gives a unitary `U` with `R cap U R = {0}`. Set `B = UAU*`. Injective positive Hilbert-Schmidt operators are exactly the quasi-interior points of the positive Hilbert-Schmidt cone, while Douglas' range inclusion lemma forces every positive common lower bound `C` to satisfy `Ran(C^{1/2}) subset R cap U R = {0}`.

Novelty check: bounded search of the run indexes and web queries for the exact source question, quasi-interior common lower bounds, positive Hilbert-Schmidt cones, operator ranges, and Douglas range inclusion found no exact prior packet or later explicit answer. The proof uses standard operator theory but the application to the source question appears to be new in this run.

Files:

- `main.tex` - full proof packet.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - local copy of the source paper if available/generated.

Human review recommendation: verify the Baire-category transverse-range lemma and the characterization of quasi-interior points in the self-adjoint Hilbert-Schmidt cone.
