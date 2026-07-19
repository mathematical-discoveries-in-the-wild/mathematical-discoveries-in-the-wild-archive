# Full Result: Residual Norm-Weak USC Points for M-Embedded Spaces

Status: `full_solution_likely_valid`

Source paper: T. S. S. R. K. Rao, "Computing sub differential limits of operators on Banach spaces", arXiv:2212.09650.

Source question: after Proposition 9, the paper says:

> We do not know how to determine the largeness of points of norm-weak usc for the preduality map on `X**` in the category sense, when `X` is a `M`-ideal in its bidual.

## Result

Let `X` be a non-reflexive Banach space which is an M-ideal in its bidual. Then the norm-weak upper-semicontinuity points for the preduality map on `X**` contain a dense `G_delta` subset of `X**`. In particular, they are residual.

This fully answers the source category-largeness question for non-reflexive M-embedded spaces.

## Idea

Rao's Proposition 9(b) proves norm-weak usc for every `tau in X**` such that:

```text
tau attains its norm on X*
and
d(tau, X) < ||tau||.
```

The missing category observation is that these two conditions hold generically. Since `X` is M-embedded, `X*` has the Radon-Nikodym property. Bourgain's theorem, equivalently the Stegall variational principle in the standard norm-attainment form, implies that norm-attaining functionals on `X*` contain a dense `G_delta` subset of `(X*)* = X**`. The strict inequality `d(tau,X)<||tau||` defines a dense open subset of `X**`. Their intersection is dense `G_delta`, and Rao's Proposition 9(b) applies there.

## History

The folder `history/c0_partial_packet_2026_06_20/` preserves the earlier `X=c0` partial packet. That proof gave a concrete positive category answer for `c0`; the present theorem subsumes it and also avoids relying on an infinite strict-plateau openness claim.

## Evidence

- Source criterion and definition: arXiv:2212.09650, Introduction, page 3.
- Source category question and Proposition 9: arXiv:2212.09650, page 9.
- Supporting residual norm-attainment theorem: Jung-Martin-Rueda Zoca, arXiv:2203.04023, Proposition 2.1(a), recalling Bourgain/Stegall.
- Structural input: standard HWW fact that M-embedded `X` has `X*` with the Radon-Nikodym property.
- Local/web novelty checks did not find an explicit prior statement of this full category answer.

## Files

- `main.tex`
- `solution_packet.pdf`
- `source_paper.pdf`
- `supporting_paper_2203.04023.pdf`
- `figures/definition_context_page3.png`
- `figures/open_problem_context_page9.png`
- `history/c0_partial_packet_2026_06_20/`
