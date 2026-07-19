# Metrizable C(K) Case of Problem 7.3

Source: arXiv:2602.12934, "Packings in classical Banach spaces" by
Carlo Alberto De Bernardi, Tommaso Russo, Seyda Sezgek, and Jacopo
Somaglia.

Status: full solution to the parenthesized metrizable version of Problem 7.3.
The nonmetrizable compact case is not claimed.

Claim proved:

> If K is compact metrizable, then gamma^*(C(K)) = 1.

Packet contents:

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: real page-width screenshot crop from the
  original PDF showing Problem 7.3.
- `main.tex`: LaTeX source for the solution packet.
- `solution_packet.pdf`: compiled proof packet.
- `tmp/`: LaTeX build artifacts and temporary rendered page images.

Proof idea:

Let P be the Cantor-Bendixson perfect kernel of K. If P is empty, K is
zero-dimensional and the source paper already gives gamma^*(C(K)) = 1.
If P is nonempty, then P is perfect compact metric, so C(P) has
gamma^* = 1 by the source paper's separable octahedral result. Use a
norm-one Dugundji extension E:C(P)->C(K), and add the subgroup H of
continuous 2Z-valued functions vanishing on P. The subgroup E[D_P]+H is
2-separated. Density follows by correcting only on a compact clopen
neighbourhood of the set where the residual function is larger than
1+alpha; that neighbourhood lies in the scattered zero-dimensional
remainder K\\P.

No computational verification was needed.
