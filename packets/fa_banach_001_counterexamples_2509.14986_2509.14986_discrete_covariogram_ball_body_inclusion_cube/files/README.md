# Unit-cube counterexample to the discrete covariogram Ball-body inclusion

Status: `counterexample_likely_valid` (human review required).

Source: David Alonso-Gutiérrez, Eduardo Lucas, and Javier Martín Goñi,
*A discrete approach to Zhang's projection inequality*, arXiv:2509.14986 / 
Canadian Journal of Mathematics (2025), Section 6, printed and PDF page 34.

The source says it is unknown whether the continuous normalized inclusion

`binom(n+q,n)^(1/q) K_q(g_K) subset binom(n+p,n)^(1/p) K_p(g_K)`

continues to hold for the p-th Ball bodies of the discrete covariogram
`g_tilde_K`, for `0<p<q`.

It does not. In every dimension `n>=1`, take `K=[0,1]^n`, direction `e_1`,
`p=1`, and `q=2`. The discrete covariogram is `2^(n-1)` along `r e_1` for
`0<r<=1` and zero for `r>1`, whereas its value at zero is `2^n`. Consequently

`rho_{K_p(g_tilde_K)}(e_1)^p = 1/2`

for every `p>0`. The proposed inclusion would require

`sqrt((n+1)(n+2))/2 <= (n+1)/2`,

which is false for every `n>=1`.

The result is all-dimensional, although the one-dimensional interval
`K=[0,1]` already disproves the universal assertion. It does not contradict
the source's proved replacement theorem, which introduces `K+C_n` and an
additional lattice-count dilation.

Artifacts:

- `solution_packet.pdf`: self-contained counterexample proof;
- `source_paper.pdf`: original target paper;
- `figures/open_problem_crop.png`: source screenshot of the unknown inclusion;
- `code/verify_unit_cube.py`: exact arithmetic and lattice-layer checks for
  dimensions 1 through 20.

The novelty search was bounded: the run indexes and searches over arXiv,
Cambridge, the exact title/id, `discrete covariogram`, `Ball bodies`, and
`inclusion` found no later resolution or counterexample. Human review should
focus on the half-layer count and the normalization constants at `p=1,q=2`.

