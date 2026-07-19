# Partial solution packet: step-two Carnot endpoint L1 exponent

Status: likely valid partial solution.

Source paper: Seung-Yeon Ryoo, "Quantitative nonembeddability of groups of polynomial growth into uniformly convex spaces", arXiv:2207.11305.

Open question targeted: Question 38 / Question 42 in the source paper asks for finite exponents in the endpoint \(L^1\) vertical-horizontal inequality for general nonabelian nilpotent Lie groups.

Claim proved here: If \(G\) is any nonabelian step-two Carnot group and \(v\in V_2=[V_1,V_1]\), then the functional endpoint inequality holds with exponent \(q=4\):
\[
\left(\int_0^\infty
\frac{\left(\int_G |f(g\exp(tv))-f(g)|\,dg\right)^4}{t^3}\,dt
\right)^{1/4}
\le C_{G,v}\int_G |\nabla_H f(g)|\,dg
\]
for every smooth compactly supported scalar function \(f\). Consequently all exponents \(q\ge 4\) are admissible in this step-two Carnot subcase.

Proof idea: write \(v\) as a finite sum of elementary brackets \([a_j,b_j]\). Each \(\operatorname{span}\{a_j,b_j,[a_j,b_j]\}\) is a copy of the three-dimensional Heisenberg algebra. Applying the Naor--Young \(H^3\) \(L^4\) vertical-perimeter theorem on left cosets controls the vertical oscillation in each elementary bracket direction. Since all layer-two directions are central, a telescoping sum controls translation by \(v\).

Limitations: The packet does not compute the optimal exponent for a general step-two Carnot group. In particular, higher-dimensional Heisenberg groups have the sharper known exponent \(q=2\). The packet also does not solve the endpoint problem for higher-step Carnot groups or arbitrary nilpotent Lie groups.

Novelty check: Before promotion, the cheap run indexes were searched for arXiv:2207.11305, "step-two Carnot", "vertical perimeter", "L^1", "Naor", "Young", and Heisenberg variants. Web searches were also run for "step two Carnot vertical perimeter L1", "vertical versus horizontal step 2 Carnot L1", "vertical perimeter Carnot groups Naor Young step two", and close variants. The search found the known Heisenberg results of Naor--Young, but no packet or obvious literature result stating this step-two Carnot extension.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source/open-problem paper, arXiv:2207.11305.
- `supporting_paper_2004.12522.pdf`: Naor--Young supporting theorem, arXiv:2004.12522.
- `figures/open_problem_crop.png`: crop of the source question.
- `figures/supporting_h3_theorem_crop.png`: crop of the supporting Heisenberg theorem.

Human review recommendation: verify the coset-disintegration step and the scaling from the standard \(H^3\) theorem to arbitrary elementary bracket subgroups. These are the only nontrivial transfer points.
