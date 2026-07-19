# Full Result: Range-Weak-Compactness Quantification Implies Bendova Grothendieck

## Source Question

- Source paper: Hana Krulisova, *C*-algebras have a quantitative version of Pelczynski's property (V)*, arXiv:1605.04900.
- Location: page 9, Section 5, after the displayed inequality involving
  `wck_{X'}({x_n' : n in N})`.
- Question: whether the quantitative Grothendieck property
  `wck_{X'}({x_n'}) <= c delta_{w*}(x_n')` implies Bendova's
  `c`-Grothendieck inequality `delta(x_n') <= C delta_{w*}(x_n')` for a
  larger constant.

## Answer

Yes. For every Banach space `X` and every bounded sequence `(x_n')` in `X'`,
with `A = {x_n' : n in N}`,

```text
delta(x_n') <= delta_{w*}(x_n') + 4 wck_{X'}(A).
```

Consequently, if `wck_{X'}({x_n'}) <= c delta_{w*}(x_n')` holds for every
bounded sequence in `X'`, then `X` is `(1+4c)`-Grothendieck in Bendova's sense.

The proof uses only the canonical embeddings `X' -> X'''`, the restriction map
from `X'''` to `X'`, and the definition of `wck` via weak-star cluster points.

## Files

- `main.tex`: full solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source question on page 9.

## Review Focus

Review should check the constant in the elementary annihilator lemma:
if `h in X'''` annihilates the canonical copy of `X`, then
`||h|| <= 2 dist(h, X')`. The rest of the proof is a direct cluster-point
argument. The packet does not claim to solve the separate open problem asking
whether C*-algebras have the property `(V_q)_{omega*}`.
