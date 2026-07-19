# Partial result: the `L^q`, `p=1` endpoint for `1<q<=2`

Status: `partial_result_likely_valid`.

Source problem: Ivan S. Yaroslavtsev, *Local characteristics and tangency of
vector-valued martingales*, arXiv:1907.11588, Remark 12.10.

Result: Let `1<q<=2` and let `S` be an arbitrary measure space. If `N` and
`M` are `L^q(S)`-valued local martingales and `N` is characteristically
dominated by `M` in Yaroslavtsev's sense, then

```text
E sup_t ||N_t||_q <= C_q E sup_t ||M_t||_q.
```

This removes the `p=1` endpoint obstruction for the lower half of the `L^q`
scale. It remains partial relative to Remark 12.10 because the broad UMD-space
question and the upper half `q>2` remain open here.

Main new ingredient: the endpoint square-function comparison from the
conditional packet is proved unconditionally for `1<q<=2`. For a finite
partition of `S`, write `r=q/2<=1` and

```text
Phi(v) = (sum_k a_k v_k^r)^(1/q),  v in R_+^d.
```

This is a multivariate Bernstein function. Hence it has a positive
Levy-Khintchine/Laplace representation by kernels `1-exp(-<t,v>)`. For
independent positive vectors, expectation of each kernel is
`1-prod_i E exp(-<t,V_i>)`, which is comparable to
`min(1, sum_i E(1-exp(-<t,V_i>)))`. The latter is monotone under aggregate
occurrence-measure domination. This proves the square-function comparison in
finite-dimensional weighted `ell_q`; finite conditional expectations then pass
the result to arbitrary `L^q(S)`.

Connection to the martingale problem: Yaroslavtsev's `p=1` Banach-function-space
BDG theorem identifies the `L^1` maximal size of an `L^q` martingale difference
sequence with the `L^1` size of its lattice square function. The earlier
conditional packet already isolated this as the only missing endpoint
comparison. Combining that reduction with the new square-function theorem gives
the stated general-local characteristic-domination result for `1<q<=2`.

Novelty/literature check: the run indexes contained the existing `p>1` `L^q`
packet, Hilbert all-`p` packets, an `ell_q` natural-exponent packet, the broad
`c0` counterexample, and the previous conditional endpoint reduction, but no
`L^q`, `p=1`, `1<q<=2` theorem. Web searches for exact phrases around Remark
12.10, `p=1`, `L^q`, characteristic domination, aggregate domination, and
square functions did not reveal a later paper settling this endpoint. The
standard Bernstein-function and stable-subordinator facts used in the proof are
included in the bibliography.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1707.00109.pdf`: Dirksen--Yaroslavtsev endpoint Rosenthal
  context.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev `p=1` Banach-function-space
  BDG theorem.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation containing the
  aggregate independent-increment formulation.

Human review recommendation: high priority. The main finite-dimensional
Laplace argument is short and should be checked first; the remaining martingale
step is exactly the conditional reduction from the companion packet with the
conditional lemma now supplied for `1<q<=2`.
