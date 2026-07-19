# Fully (2;2,...,2)-Summing L-infinity Multilinear Forms: Literature-Implied Answer

Status: `literature_implied_answer`

Source paper: Daniel M. Pellegrino, `Cotype and nonlinear absolutely summing
mappings`, arXiv:math/0307311.

Supporting paper: Geraldo Botelho, Carsten Michels, and Daniel Pellegrino, `New
inclusion and coincidence theorems for summing multilinear mappings`,
arXiv:0810.0947.

## Source Question

In Section 4 of arXiv:math/0307311, after defining `r`-fully absolutely
summing multilinear mappings, the source paper asks whether every scalar
`n`-linear mapping on `L_infinity` spaces is fully `(2;2,...,2)`-summing. The
question appears on page 10 of `source_paper.pdf`.

The source paper then proves only a partial version: its following result gives
the `f(2)`-fully/mixed-index conclusion. Since "fully" in the definition means
the `r=n` all-indices version, this does not settle the question for `n >= 3`.

## Supporting Answer

The later paper arXiv:0810.0947 uses the modern terminology "multiple
summing" for the same all-indices/fully summing condition. In Section 4.3,
Corollary 4.10, page 9, it proves that if `E_1,...,E_n` are `L_infinity`
spaces and `F` has cotype 2, then

```text
L(E_1,...,E_n;F) = L_ms,r(E_1,...,E_n;F)  for all 2 <= r <= infinity.
```

Taking `F = K` and `r = 2` gives exactly the scalar fully
`(2;2,...,2)`-summing answer to the source question.

## Provenance

This is not an original lane result. The supporting paper does not explicitly
frame Corollary 4.10 as answering the sentence from arXiv:math/0307311, but it
does cite the source paper and proves a formally stronger multiple-summing
coincidence theorem. The relation recorded here is agent-identified by matching
the source paper's fully all-indices definition with the supporting paper's
multiple-summing notation.

## Files

- `source_paper.pdf`: arXiv:math/0307311.
- `supporting_paper_0810.0947.pdf`: arXiv:0810.0947.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `tmp/`: LaTeX build intermediates.

## Scope

The packet records a complete literature answer to the scalar question as
stated: every scalar-valued continuous `n`-linear mapping on `L_infinity`
spaces is fully `(2;2,...,2)`-summing. It also records the stronger
vector-valued cotype-2 range theorem from the supporting paper. It does not
claim novelty or address unrelated summability exponents.
