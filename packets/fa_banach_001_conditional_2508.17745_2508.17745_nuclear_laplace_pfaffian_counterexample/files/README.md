# Nuclear-Laplace conditional counterexample

Source: Galyna V. Livshyts, Manuel Fernandez V, and Stephanie Mui,
*On the Smallest Singular Value of Log-Concave Random Matrices*,
arXiv:2508.17745v1, open question on PDF page 4.

Status: `conditional counterexample reduction, likely valid`.

## Result

Let `X_n` have density proportional to

```text
exp(-||X||_*)
```

on real `n x n` matrices, and rescale it by its common entry standard
deviation so that its vectorization is isotropic. This law is log-concave,
centered, and bi-orthogonally invariant.

For the coefficient-one ordered singular-value ensemble, define `Z_n` as the
partition function and `B_n` as its boundary integral at the least singular
value `0`. The packet proves:

- the density at zero of the least singular value is exactly `d_n=B_n/Z_n`;
- `d_n` is an explicit ratio of de Bruijn Pfaffians with incomplete-beta
  entries;
- the entire least-singular-value density satisfies the quantitative bound
  `g_n(x) >= exp(-n*x) d_n`;
- if `d_n` is unbounded, the isotropically normalized matrices contradict any
  universal estimate `P(s_n <= epsilon/sqrt(n)) <= C epsilon + exp(-c n)`.

Thus the source problem is reduced to one scalar asymptotic statement:

```text
B_n/Z_n -> infinity along some sequence.
```

Exact rational computation through `n=40` and high-precision computation
through `n=200` support this strongly: the ratio rises from `1` to about
`3.1689236577`, with behavior numerically close to `sqrt(2 log n)`.
Computation is evidence, not a proof of unboundedness.

## Files

- `main.tex`: complete conditional argument and the exact Pfaffian reduction.
- `solution_packet.pdf`: rendered review packet.
- `verification.md`: proof audit and remaining dependency.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source open-problem passage.
- `code/pfaffian_ratio.py`: exact rational de Bruijn computation.
- `code/pfaffian_ratio_mp.py`: larger high-precision audit.

## Human review recommendation

Send to a specialist in Pfaffian ensembles, skew-orthogonal polynomials, or
asymptotic random matrix theory. The only missing mathematical step is proving
that the displayed Pfaffian ratio is unbounded. All counterexample scaling and
small-window estimates after that lemma are elementary and quantitative.
