# Partial result: the full `L^q`, `p=1` endpoint

Status: `partial_result_likely_valid`.

Source problem: Ivan S. Yaroslavtsev, *Local characteristics and tangency of
vector-valued martingales*, arXiv:1907.11588, Remark 12.10.

Result: For every `1<q<infinity` and every measure space `S`, if `N` and `M`
are `L^q(S)`-valued local martingales and `N` is characteristically dominated
by `M` in Yaroslavtsev's sense, then

```text
E sup_t ||N_t||_q <= C_q E sup_t ||M_t||_q.
```

This closes the `p=1` endpoint for the concrete class `L^q(S)`. It remains a
partial result relative to the source's broad UMD-space problem.

New ingredient: the previous `1<q<=2` packet used a Bernstein/Laplace
representation. The missing `q>2` case is handled here by a Poissonization
comparison for positive `L^r` sums, with `r=q/2`:

```text
E || sum_i V_i ||_r^{1/2}
    is equivalent, up to C_r,
E || compound-Poisson(sum_i law(V_i|nonzero)) ||_r^{1/2}.
```

The compound-Poisson model depends only on the aggregate occurrence measure.
Aggregate domination is therefore monotone by Poisson superposition.

Core proof idea: write each positive jump as `B_i Z_i`, where `B_i` is a
Bernoulli occurrence. Poissonizing replaces each Bernoulli by `Pois(p_i)`
copies. The lower comparison uses the events `{Pois(p_i)>=1}`, whose
probabilities are at least `(1-e^{-1})p_i`, and the fact that retaining more
than half of a deterministic positive family sees at least half of the
subadditive functional. The upper comparison decomposes the Poisson count into
layers `{Pois(p_i)>=k}`. The `k`-th layer is a thinning of the original family
with retention at most `1/k!`; scalar Rosenthal pointwise in `S` shows such a
thinning costs at most `(1/k!)^{1/q}`. Summing over layers is finite.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev `p=1` Banach-function-space
  BDG theorem.
- `supporting_paper_1707.00109.pdf`: Dirksen--Yaroslavtsev endpoint and `p>1`
  Rosenthal context.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: aggregate independent-increment
  formulation.

Human review recommendation: very high priority. The main audit target is the
Poissonization Proposition in `main.tex`; once accepted, it removes the final
square-function bottleneck isolated by the conditional packet.
