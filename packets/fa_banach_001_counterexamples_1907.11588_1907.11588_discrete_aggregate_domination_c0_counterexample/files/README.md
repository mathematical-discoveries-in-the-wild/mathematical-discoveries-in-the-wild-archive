# Counterexample: aggregate domination fails in c0

Status: candidate counterexample, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 asks whether aggregate domination of the laws of independent mean-zero Banach-valued random variables implies an `L^p` comparison of their sums. The remark also notes that even the symmetric case was not known to the author.

Result: The statement is false for the fixed Banach space `c0`, for every `1 <= p < infinity`, even with equality of the aggregate jump measures and with all variables symmetric.

Construction: For each `N`, let `eta_k = eps_k e_k`, `1 <= k <= N`, in `c0`. Let `xi_j = delta_j e_{I_j}`, `1 <= j <= N`, where `I_j` is uniform on `{1,...,N}` and `delta_j` is an independent Rademacher sign. Then

```text
sum_j P(xi_j in B) = sum_k P(eta_k in B)
```

for every Borel `B subset c0 \ {0}`. But `||sum eta_k||_infty = 1` a.s., while `||sum xi_j||_infty` is a signed occupancy maximum and has moments tending to infinity like a power of `log N / log log N`.

Limitations: This refutes the broad Banach-space discrete problem exactly as stated in Remark 12.10. It does not settle the corresponding UMD-space/general-local-martingale problem; `c0` is not UMD.

Novelty check: Cheap run indexes had no prior packet for `1907.11588`, `characteristically dominated`, or this discrete aggregate-domination problem. Web searches for the exact problem text and nearby phrases found the source paper and related comparison literature, especially Montgomery-Smith--Pruss, but no existing answer to this aggregate-domination formulation.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation sentence noting the symmetric case.
- `code/occupancy_lower_bound.py`: numerical sanity check for the lower-bound parameters.
