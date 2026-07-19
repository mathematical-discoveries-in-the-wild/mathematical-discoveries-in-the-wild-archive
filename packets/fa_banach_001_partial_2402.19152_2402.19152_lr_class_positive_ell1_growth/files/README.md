# Candidate Partial Result: Natural `L_r` Class Has Positive `ell_1` Growth

Source paper: E. Garcia-Sanchez, D. H. Leung, M. A. Taylor, and P.
Tradacete, *Banach lattices with upper `p`-estimates: free and injective
objects*, arXiv:2402.19152.

Result type: `partial`

Status: candidate partial result, likely valid, pending human review.

## Open Question

Question 2.12 asks whether, for each `r in (1,2)`, there is a class
`C_r` such that the sequence `(|delta_{e_k}|)`, where `(e_k)` is the unit
vector basis of `ell_2`, behaves like the unit vector basis of `ell_r` in
`FBL^{C_r}[ell_2]`.

The packet does not solve this full existence question.

## Candidate Contribution

For every `1 <= q <= 2`, let `C_q = {L_q[0,1]}`. If
`u_k = |delta_{e_k}|` in `FBL^{C_q}[ell_2]`, then for every finitely
supported nonnegative scalar sequence `(a_k)`,

```text
|| sum_k a_k u_k || = sum_k a_k.
```

Consequently, for `r in (1,2)`, the natural choice
`C_r = {L_r[0,1]}` cannot make the sequence behave like `ell_r`: the
positive partial sums grow like `n`, not like `n^(1/r)`.

## Why This Is Only Partial

The authors ask whether some class `C_r` exists. This result only rules
out the obvious single rearrangement-invariant class `{L_r[0,1]}`. More
complicated or engineered classes are not excluded.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Question 2.12.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `code/check_positive_growth.py`: finite Walsh/Rademacher sanity check.
- `tmp/`: LaTeX and rendering intermediates.

## Literature Check

On June 8, 2026, an exact web search for the interpolation question found
the source paper and publication mirrors, but no later paper explicitly
answering Question 2.12. This is not a literature-already-answered case.

## Human Review

Recommended check: verify that the Rademacher map
`e_k -> r_k` is a contraction `ell_2 -> L_q[0,1]` for `q <= 2`, and that
the upper estimate uses only the universal norm definition and the
lattice homomorphic identity `hat T(|delta_e|)=|Te|`.
