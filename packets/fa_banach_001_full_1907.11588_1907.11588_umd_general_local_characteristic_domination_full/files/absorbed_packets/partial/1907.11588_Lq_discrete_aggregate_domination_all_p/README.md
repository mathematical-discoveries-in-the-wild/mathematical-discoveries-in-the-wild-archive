# Partial result: discrete aggregate domination in `L^q` for all `p>1`

Status: candidate partial result, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 reduces the open general-local-martingale characteristic-domination problem to a discrete independent-increment aggregate-domination question. Previous packets handled `c0` negatively, Hilbert spaces positively for all finite `p`, and `ell_q` general local martingales at `p=q`.

Result: Let `1<p,q<infinity` and let `X=L^q(S)` over an arbitrary measure space. If independent mean-zero `X`-valued random variables `(xi_i)` and `(eta_i)` satisfy

```text
sum_i P(xi_i in B) <= sum_i P(eta_i in B)
```

for every Borel `B subset X \ {0}`, then

```text
E ||sum_i xi_i||_X^p <= C_{p,q} E ||sum_i eta_i||_X^p.
```

The same holds for maxima over partial sums, by Doob's inequality.

Proof mechanism: Dirksen-Yaroslavtsev's `L^q`-valued Rosenthal theorem identifies the `L^p` norm of an independent mean-zero sum with a sum/intersection norm `s_{p,q}` built from three aggregate gauges:

```text
S_q     = ||(sum_i E |z_i|^2)^{1/2}||_q
D_q,q   = (sum_i E ||z_i||_q^q)^{1/q}
D_p,q   = (sum_i E ||z_i||_q^p)^{1/p}.
```

The key new lemma is that the full Rosenthal sum/intersection norm is monotone under aggregate law domination. For intersection pieces this is immediate. For sum pieces, take a near-optimal decomposition of the dominating variables and restrict its split law by the Radon-Nikodym derivative of the dominated aggregate measure. This transports decompositions without increasing any of the three gauges.

Limitations:

- This packet proves the discrete independent-increment bottleneck, not yet the full general-local-martingale theorem.
- The proof covers `1<p<infinity`; the endpoint `p=1` is not settled here.
- A follow-up audit is still needed to combine this jump comparison with continuous covariance domination in full `L^q` local martingales.

Novelty/literature check: Cheap run indexes contained the `c0`, Hilbert, and `ell_q p=q` packets, but no `L^q` all-`p>1` aggregate-domination packet. Literature search found Dirksen-Yaroslavtsev arXiv:1707.00109, which proves the decisive `L^q`-valued Rosenthal theorem, but no explicit aggregate-domination consequence for Remark 12.10. Searches used: `characteristically dominated ell_q martingales`, `characteristically dominated L^q martingales`, `aggregate domination independent random variables ell_q`, and comparison-inequality searches around Zinn/Montgomery-Smith/Pruss.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1707.00109.pdf`: Dirksen-Yaroslavtsev `L^q`-valued Burkholder-Rosenthal paper.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation noting the symmetric discrete case.
- `code/grouping_simulation.py`: finite grouping sanity check; non-proof evidence only.
