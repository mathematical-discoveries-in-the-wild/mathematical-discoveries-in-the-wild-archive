# Eventually monotone variable-exponent iterated Lp spaces are UMD

Status: `partial_result_likely_valid`

Source paper: Yanqi Qiu, *On the UMD constants for a class of iterated
L_p(L_q) spaces*, arXiv:1112.0739.

## Result

Qiu asks for conditions under which the variable-exponent inductive limits

```text
X[(p_i)] = lim L_{p_n} ... L_{p_2} L_{p_1},
Z[(p_i)] = lim L_{p_1} L_{p_2} ... L_{p_n}
```

are UMD.

This packet proves a positive partial answer: if the exponent sequence is
eventually monotone and stays in a compact subinterval of `(1,infinity)`, then
both `X[(p_i)]` and `Z[(p_i)]` are UMD.

The proof uses Qiu's Remark 5.7, which says that a consecutive monotone block
inside a finite mixed-norm tower can be replaced by its two endpoints without
changing the `UMD_s` constant.  Therefore an eventually monotone tail
`p_N,...,p_n` collapses to `p_N,p_n` at every finite level.  The remaining
finite-level spaces contain only a fixed finite prefix and one variable
exponent in a compact interval, so their UMD constants are uniformly bounded.
Uniform finite-level UMD constants pass to the inductive limit.

## Scope

This does not solve Qiu's full variable-exponent problem.  It leaves open
oscillatory sequences with infinitely many turns, the possible sufficiency of
Qiu's necessary product condition `prod_i c(p_i,p_{i+1}) < infinity`, and the
exact computation of `c(p,q)`.

## Search Evidence

Cheap run indexes were searched for `1112.0739`, `UMD constants`, `iterated
L_p(L_q)`, `X[(p_i)]`, `Z[(p_i)]`, and the product condition.  No exact packet
or attempt existed.  Local source search found the variable-exponent problem
only in arXiv:1112.0739.  Targeted web searches for exact phrases including
`Under which condition is X[(p_i)]`, `Z[(p_i)] UMD`, and `prod_i c(p_i,
p_{i+1})` found no later exact answer beyond the source paper.

## Files

- `source_paper.pdf`: arXiv:1112.0739.
- `figures/open_problem_crop.png`: source problem and necessary conditions.
- `figures/monotone_remark_crop.png`: Qiu's monotone-block UMD constant remark.
- `main.tex` and `solution_packet.pdf`: proof packet.
