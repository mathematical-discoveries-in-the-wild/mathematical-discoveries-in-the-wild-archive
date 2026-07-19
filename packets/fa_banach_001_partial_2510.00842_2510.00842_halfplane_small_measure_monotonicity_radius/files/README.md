# Partial packet: half-plane small-measure monotonicity radius

Status: `candidate_partial_likely_valid`

Source target: Maud Szusterman, "Monotonicity of the Gaussian measure under Banaszczyk transforms", arXiv:2510.00842.

Extracted question: Question 4.1 asks whether there is an increasing radius function `r:(0,1)->(0,+infty)` such that, whenever `gamma_n(K)>=p` and `||u||_2<=r(p)`, the modified Banaszczyk transform satisfies `gamma_n(K circ u)>=gamma_n(K)`. The appendix notes that, for `p<1/2`, it is unclear whether the planar hypograph reduction is equivalent to the weaker half-plane test statement.

Result: The weaker half-plane test statement is true for every `0<p<1`. More explicitly, for each `p` there is `rho_p>0` such that every half-plane `H subset R^2` with `gamma_2(H)>=p` satisfies `gamma_2(H circ u)>=gamma_2(H)` for all `||u||_2<=rho_p`. The packet gives a concrete Mills-ratio sufficient criterion for such radii.

Scope: This is a partial answer only. It does not prove Question 4.1 for all convex bodies or for all non-increasing concave planar hypographs, and it does not prove the source paper's symmetric linear-in-`p` conjecture.

Packet contents:
- `main.tex`: self-contained partial theorem proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local PDF compiled from the arXiv source.
- `figures/open_problem_crop.png`: source crop from page 7 containing Question 4.1 and the weaker half-plane statement.

Novelty check: Local run indexes and parsed-source searches for `2510.00842`, `Banaszczyk transform`, `K circ u`, `Gaussian monotonicity`, `r_p`, `half-plane`, and `symmetric slabs` found no prior packet for this target. No external web novelty search was performed for this partial packet; novelty confidence should be treated as bounded by the local corpus.
