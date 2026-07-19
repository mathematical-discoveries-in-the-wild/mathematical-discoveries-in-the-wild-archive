# Partial Result: Separably Injective p-Banach Spaces Have Trivial Banach Envelope

Status: `partial_result_likely_valid`

Source paper: Félix Cabello Sánchez, Joanna Garbulińska-Wegrzyn, Wiesław
Kubiś, *Quasi-Banach spaces of almost universal disposition*,
arXiv:1309.7649.

Source question: In Section 7.4, after Proposition 7.3, the authors write that
they do not know whether there is a nontrivial separable space that is
separably injective among `p`-Banach spaces for `p<1`, and guess that there is
not.

Partial result:

For `0<p<1`, if `E` is separably injective among `p`-Banach spaces, then every
operator from `E` into any `q`-Banach space with `p<q<=1` is zero. In
particular, `E^*={0}` and the Banach envelope of `E` is trivial.

Idea:

If `S:E -> F` were nonzero for some `q`-Banach target `F`, pick `e in E` with
`S(e) != 0`. Separably injectivity extends the one-dimensional map
`span{1} subset L_p[0,1] -> E`, `1 |-> e`, to an operator
`T:L_p[0,1] -> E`. Then `S T` is a nonzero operator from `L_p` to a
`q`-Banach space, contradicting the classical Kalton zero-operator theorem
quoted in the source paper.

Limitations:

This does not prove nonexistence of nontrivial separable separably injective
`p`-Banach spaces. It shows that any such example must be genuinely
nonlocally convex in the strongest possible sense: no nonzero dual, no
nonzero Banach envelope, and no nonzero operator into any more convex
`q`-Banach target.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1309.7649.
- `figures/open_problem_crop.png`: crop of the source question and the
  adjacent Kalton zero-operator quotation.
