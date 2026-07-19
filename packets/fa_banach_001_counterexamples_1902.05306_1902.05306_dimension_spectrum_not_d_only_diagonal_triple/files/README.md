# Counterexample packet: dimension spectrum not encoded by D alone

Status: `candidate_counterexample_likely_valid`

Source target: Michal Eckstein and Bruno Iochum, "Spectral Action in Noncommutative Geometry", arXiv:1902.05306.

Extracted question: Chapter 5, Problem 5 asks whether the inclusion
`Sd subset union_k P(zeta_{|D|^{-k},D})`, observed in worked-out examples, is a general fact or a special property of those examples.

Result: under the source paper's broad definition of regular spectral triple and abstract pdo calculus, the inclusion is not general. A diagonal spectral triple with `D e_n = n e_n` and a diagonal unitary `U e_n = n^i e_n` has
`zeta_{U,D}(s)=zeta(s-i)`, so the dimension spectrum contains `1+i`. The D-only probe functions `zeta_{|D|^{-k},D}(s)=zeta(s+k)` have only real poles `1-k`.

Mechanism: the algebra generator `U` commutes with `D`, hence it is a regular order-zero pdo. It contributes oscillatory Dirichlet coefficients `n^i`, shifting the Riemann zeta pole off the real line while leaving the spectrum of `D` unchanged.

Packet contents:
- `main.tex`: self-contained counterexample proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1902.05306.
- `figures/open_problem_crop.png`: source crop from page 123 of the book PDF, Chapter 5 Problem 5.
- `code/check_poles.py`: small sanity check listing the D-only and algebra-visible pole locations.

Novelty check: searched run indexes for arXiv:1902.05306 and spectral-action/noncommutative-geometry/dimension-spectrum phrases; no direct duplicate was found. Web searches for close variants of "dimension spectrum encoded in D" and "diagonal spectral triple dimension spectrum Dirichlet series" did not surface a later explicit answer.

Scope limitation: the example is degenerate as a metric geometry because `[D,A]=0`. It refutes the unrestricted "general fact" question as stated, but leaves open any strengthened version requiring nondegeneracy, reconstruction-type axioms, or a more geometric class of spectral triples.
