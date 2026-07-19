# Partial result: Hilbert characteristic domination for all finite p

Status: candidate partial result, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 asks whether the quasi-left-continuous characteristic-domination theorem extends to general local martingales. The source reduces the missing accessible-jump issue to a discrete independent-increment aggregate-domination problem.

Result: The general local martingale extension is true for Hilbert-valued martingales for every `1 <= p < infinity`. If `H` is a separable Hilbert space, `1 <= p < infinity`, and `N` is characteristically dominated by `M`, then

```text
E sup_t ||N_t||^p <= C_p E sup_t ||M_t||^p.
```

The new ingredient, beyond the previous Hilbert `p=2` and `p>=2` packets, is the range `1 <= p < 2`. For independent mean-zero Hilbert variables satisfying aggregate domination,

```text
sum_n P(xi_n in B) <= sum_n P(eta_n in B)
```

one has

```text
E ||sum xi_n||^p <= C_p E ||sum eta_n||^p
```

for every `1 <= p < 2`.

Proof mechanism below `2`: Hilbert symmetrization and Khintchine inequalities identify the terminal moment with the random square-function moment

```text
E ||sum Z_n||^p ~= E (sum ||Z_n||^2)^(p/2).
```

Aggregate domination then controls the square-function moment by a Laplace-transform comparison. For `alpha=p/2<1`, if `S=sum Y_i` and `U(t)=sum_i E(1-exp(-tY_i))`, then

```text
(1-exp(-1)) min(1,U(t)) <= 1 - E exp(-tS) <= min(1,U(t)).
```

Since `U(t)` depends only on the aggregate law of the `Y_i`, domination of aggregate jump laws gives domination of `E S^alpha`. This is the good-lambda/tail substitute that the naive Rosenthal route was missing.

The previously packaged `p>=2` result handles the upper range by Hilbert Rosenthal/BDG. Combining the two ranges solves the Hilbert-valued subcase of the general local martingale problem for every finite `p`.

Reduction audit: A follow-up line-by-line audit found that the naive componentwise phrase "accessible compensator of N is dominated by accessible compensator of M" is not justified by the source definition, which controls only total spatial jump compensators. The proof has been hardened to avoid that shortcut: it uses Yaroslavtsev's full decoupled tangent theorem and compares the resulting independent-increment Hilbert martingales by their full characteristics. See `reduction_audit.md`.

Limitations: This does not settle non-Hilbert UMD spaces. The previous `c0` packet shows the broad Banach-space statement is false.

Novelty check: Cheap indexes contained the earlier `c0`, Hilbert `p=2`, and Hilbert `p>=2` packets, but no Hilbert all-`p` or `p<2` packet. Literature/source checks found the source reduction in arXiv:1907.11588, Hilbert BDG tools in arXiv:1807.05573, and comparison/Rosenthal context, but no exact recorded solution of the Hilbert `1<=p<2` subcase of Remark 12.10.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev's BDG paper used for the Hilbert martingale/square-function comparison context.
- `supporting_paper_1212.1912.pdf`: Pinelis Rosenthal-type martingale comparison context for the previously packaged upper range.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation noting the symmetric discrete case.
- `code/check_laplace_partition.py`: finite random check of the Laplace partition comparison.
- `reduction_audit.md`: line-by-line source audit of the general-local-martingale reduction.
