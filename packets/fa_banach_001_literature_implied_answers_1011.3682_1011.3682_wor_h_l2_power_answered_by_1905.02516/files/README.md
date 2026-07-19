# Literature-Implied Answer: Hilbert L2 worst-case power function

status: literature_implied_answer

run: fa_banach_001

source arXiv id: 1011.3682

supporting arXiv id: 1905.02516

## Identification

In arXiv:1011.3682, Section 2.1 ("Double Hilbert Case"), Open Problem 1 asks whether

```text
ell^{wor-H}(r,2) = 1 for every r > 1/2.
```

The later paper arXiv:1905.02516, "Function values are enough for L2-approximation", proves that for Hilbert-space `L2` approximation, if the approximation numbers have polynomial order `s > 1/2`, then the sampling numbers have the same polynomial order. In the source notation, this implies `ell^{wor-H}(r,2)=1` for every `r>1/2`.

## Scope

This answers Open Problem 1 of arXiv:1011.3682 affirmatively. It does not answer the source paper's other Open Problems for `p != 2`, Banach worst-case power functions, randomized settings, average-case `p != 2`, or the fixed-`n` supremum ratio problem.

## Files

- `main.tex` - compact status note.
- `solution_packet.pdf` - rendered status note.
- `source_paper.pdf` - arXiv:1011.3682.
- `supporting_paper_1905.02516.pdf` - arXiv:1905.02516.

## Provenance

The supporting paper does not appear to cite arXiv:1011.3682 directly in the checked TeX source. It explicitly answers the equivalent Krieg-Wasilkowski-Wozniakowski / Novak-Wozniakowski open question about equality of polynomial orders for Hilbert `L2` sampling and arbitrary linear information. The link to arXiv:1011.3682 is an agent-identified reformulation through the source's power-function definition.
