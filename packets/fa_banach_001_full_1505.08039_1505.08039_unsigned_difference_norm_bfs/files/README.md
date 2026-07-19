# 1505.08039: unsigned difference norm in the Banach function space case

- arXiv id: `1505.08039`
- source title: `Difference Norms for Vector-Valued Bessel Potential Spaces with an Application to Pointwise Multipliers`
- source author: Nick Lindemulder
- packet status: `candidate_full_solution_likely_valid`
- target: Remark 4.10, the Banach-function-space question about replacing signed averaged differences by unsigned difference moduli

## Result

Under the same contextual hypotheses as source Corollary 4.9, the answer to
Remark 4.10 is positive.  If `X` is a UMD Banach function space,
`w in A_p(R^d)`, `s>0`, `m>s`, and `K` is a positive kernel satisfying the
moment and Tauberian assumptions used in Corollary 4.9, then the square
function with `K_m(2^{-j},f)` may be replaced by the unsigned modulus average

```text
D_K^m(t,f)(x) = int K(h) |Delta^m_{t h} f(x)| dh.
```

The source display appears to omit the scale `t` in `Delta^m_{t h}`; the
packet answers the intended scaled version, as indicated by the source's
domination line `|K_m(t,f)| <= d_K^m(t,f)`.

## Packet Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the arXiv PDF.
- `figures/open_problem_crop.png`: crop of Corollary 4.9 and Remark 4.10.
- `code/render_open_problem_crop.py`: small script used to regenerate the crop.

## Verification Notes

The proof is analytic.  No numerical verification is needed.  The main review
points are:

- confirm the intended correction of the missing `t` in the printed definition
  of `d_K^m(t,f)`;
- check the high-frequency estimate using Proposition 4.11 for bounded
  positive convolution kernels;
- check the low-frequency estimate against the source proof of Theorem 4.1(ii),
  especially Lemma 4.8 and the summation over `n <= 0`.

