# Partial result: Hilbert characteristic domination for p >= 2

Status: candidate partial result, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 asks whether the quasi-left-continuous characteristic-domination theorem extends to general local martingales. The source identifies the missing accessible-jump issue as a discrete independent-increment aggregate-domination problem.

Result: The general local martingale extension is true for Hilbert-valued martingales for every `p >= 2`. If `H` is a separable Hilbert space, `p >= 2`, and `N` is characteristically dominated by `M`, then

```text
E sup_t ||N_t||^p <= C_p E sup_t ||M_t||^p.
```

The new ingredient is a full positive answer to the discrete aggregate-domination problem in Hilbert space for `p >= 2`:

```text
sum_n P(xi_n in B) <= sum_n P(eta_n in B)
    implies
E ||sum xi_n||^p <= C_p E ||sum eta_n||^p.
```

Proof mechanism: Hilbert-valued Rosenthal/BDG estimates reduce independent sums to two deterministic moment characteristics,

```text
(sum E ||Z_n||^2)^(p/2) + sum E ||Z_n||^p.
```

Aggregate domination controls both terms by integrating `||x||^2` and `||x||^p` against the aggregate measures. This fills the discrete gap in Remark 12.10 for Hilbert spaces and `p >= 2`; the continuous and quasi-left-continuous pieces are already handled in the source paper.

Limitations: This does not settle Hilbert `1 <= p < 2`, non-Hilbert UMD spaces, or the full UMD problem. The previous `c0` packet shows the broad Banach-space statement is false.

Novelty check: Cheap indexes contained the prior `c0` counterexample and the Hilbert `p=2` packet, but no Hilbert `p>=2` packet. Literature checks found Yaroslavtsev's BDG paper, Pinelis/Rosenthal moment tools, and Montgomery-Smith--Pruss comparison inequalities, but no exact recorded solution of this Hilbert `p>=2` subcase of Remark 12.10.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev's BDG paper used for the Hilbert martingale comparison/reduction context.
- `supporting_paper_1212.1912.pdf`: Pinelis Rosenthal-type martingale comparison context.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation noting the symmetric discrete case.
