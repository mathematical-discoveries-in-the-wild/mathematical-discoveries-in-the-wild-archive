# Greedy rearrangement largest SOT subspace is \(L^\infty\)

Status: `full_solution_likely_valid`

Source paper: Keaton Hamm, Ben Hayes, and Armenak Petrosyan, "An Operator theoretic approach to the convergence of rearranged Fourier series", arXiv:1809.08217.

Target question: Problem 8 on source PDF page 15 asks for the largest subspace on which the greedy rearrangement of the Fourier series, ordered by decreasing absolute value of the Fourier coefficients, converges in SOT for every continuous function.

Claim: The largest such subspace of \(L^2(\mathbb T)\) is exactly \(L^\infty(\mathbb T)\). More strongly, if \(g\in L^2(\mathbb T)\setminus L^\infty(\mathbb T)\), then there is a continuous function \(F\) such that the greedy partial sums of the Fourier series of \(F\) fail to converge to \(F\) in \(L^2(|g|^2)\). The construction works for any tie-breaking rule compatible with decreasing coefficient magnitudes.

Main idea: The source paper's Corollary 6.10 produces, on every positive-measure set, a bounded flat trigonometric polynomial whose sign transform has fixed \(L^2\)-mass on that set. Split the flat block into the positive and negative sign classes. After an arbitrarily small coefficient-size perturbation, the greedy algorithm must take one sign class before the other. At that intermediate greedy time the omitted half has fixed mass on a chosen level set of an unbounded \(g\). Scaling the blocks down keeps the final function continuous; choosing the level sets farther out where \(|g|\) is larger keeps the weighted error bounded below, in fact unbounded along a subsequence.

Files:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1809.08217.
- `figures/open_problem_crop.png`: crop of Corollary 6.10 and Problem 8 from source PDF page 15.

Novelty check: The lightweight run indexes had no existing packet for arXiv:1809.08217 or the greedy operator-SOT subspace question. Web searches for "Greedy rearrangement Fourier series", "Ulyanov problem rearranged Fourier series", "thresholding greedy algorithm trigonometric system", and nearby quasi-greedy/weighted formulations found related greedy Fourier literature but no exact statement of this operator-SOT largest-subspace characterization.
