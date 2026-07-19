# Counterexample packet: alpha-one weighted Minkowski without normalization

Status: `candidate_counterexample_likely_valid`

Source target: Liudmyla Kryvonos and Dylan Langharst, "Weighted Minkowski's Existence Theorem and Projection Bodies", arXiv:2111.10923.

Extracted open signal: Remark 2.25 observes that for a 1-homogeneous measure the weighted surface area measure is 0-homogeneous, so the scaling argument that removes the normalizing constant fails and "this case remains open."

Result: the unnormalized 1-homogeneous extension is false. In the plane, for the even 1-homogeneous Radon measure
`d mu(x)=|x|^{-1} dx`, there is no symmetric convex body `K` satisfying
`dS_K^mu = 2 dtheta` on `S^1`.

Mechanism: if such a `K` existed and `h` is its support function, planar support-function calculus gives
`h + h'' = 2 sqrt(h^2 + (h')^2)`.
For `y=h'/h`, this becomes the autonomous ODE
`y' = 2 sqrt(1+y^2) - 1 - y^2`.
A periodic solution of a one-dimensional autonomous ODE is constant; periodicity of `h` then forces `y=0`, which would make the constant on the right equal to `1`, not `2`.

Packet contents:
- `main.tex`: self-contained counterexample proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2111.10923.
- `figures/open_problem_crop.png`: source crop from page 25, Remark 2.25.
- `code/check_ode_obstruction.py`: tiny symbolic/numeric sanity check for the ODE obstruction.

Novelty check: searched the run indexes for arXiv:2111.10923 and weighted Minkowski/projection-body keywords; no direct duplicate was found. Web searches for close phrases around "1-homogeneous", "weighted surface area measure", "remains open", and the paper title did not surface a later answer.

Scope limitation: this does not challenge the paper's normalized theorem with a factor `c_{mu,K}`. It disproves the natural unnormalized alpha-one extension of Lemma 2.24/Remark 2.25.
