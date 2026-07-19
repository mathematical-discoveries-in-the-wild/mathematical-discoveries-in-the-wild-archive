# Partial result: `q>2` with deterministic dominating square magnitudes

Status: `partial_result_likely_valid`.

Source problem: Ivan S. Yaroslavtsev, *Local characteristics and tangency of
vector-valued martingales*, arXiv:1907.11588, Remark 12.10.

Result: Let `q>2`, put `r=q/2`, and let `v_1,...,v_m` be deterministic
positive elements of `L^r(S)`. If independent positive `L^r(S)`-valued random
variables `(V_i)` have aggregate occurrence measure dominated by

```text
delta_{v_1} + ... + delta_{v_m},
```

then

```text
E || sum_i V_i ||_r^{1/2} <= C_q || sum_j v_j ||_r^{1/2}.
```

Equivalently, if the square magnitudes `|X_i|^2` of an independent
`L^q(S)`-valued family are aggregate dominated by deterministic magnitudes
`|u_j|^2`, then

```text
E || (sum_i |X_i|^2)^{1/2} ||_q
    <= C_q || (sum_j |u_j|^2)^{1/2} ||_q.
```

This gives a genuine upper-half subcase of the endpoint square-function
bottleneck left after the `1<q<=2` Bernstein packet. It applies, for example,
to comparison martingales whose jump magnitudes are deterministic and whose
signs are random. It does not solve the full `q>2` endpoint because the
dominating family in the source problem may itself have random magnitudes.

Proof mechanism: after writing `V_i=|X_i|^2`, apply scalar Rosenthal's
inequality pointwise in `S`:

```text
E (sum_i V_i(s))^r
    <= C_r [ (sum_i E V_i(s))^r + sum_i E V_i(s)^r ].
```

Deterministic aggregate domination gives
`sum_i E V_i <= sum_j v_j` in the lattice order and
`sum_i E V_i^r <= sum_j v_j^r <= (sum_j v_j)^r`. Integrating and taking the
`1/(2r)` power proves the square-function estimate.

What remains: for arbitrary random dominating families, the same Rosenthal
upper bound produces a deterministic functional involving
`sum_j E |Y_j|^2` and `sum_j E |Y_j|^q`, but `E ||(sum_j |Y_j|^2)^{1/2}||_q`
does not automatically lower-bound that functional because rare large jumps
are seen differently by the small `1/2` moment. This is the precise obstruction
left by this route.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1707.00109.pdf`: Dirksen--Yaroslavtsev Rosenthal context.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev `p=1` BDG endpoint.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: aggregate independent-increment formulation.

Human review recommendation: review as a narrow but rigorous `q>2` partial
subcase. The main audit point is the passage from aggregate domination of
square magnitudes to the two lattice moment inequalities used in the pointwise
scalar Rosenthal bound.
