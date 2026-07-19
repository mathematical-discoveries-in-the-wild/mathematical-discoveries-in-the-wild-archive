# Partial result: Hilbert-valued characteristic domination in L2

Status: candidate partial result, likely valid.

Source paper: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588.

Target: Remark 12.10 asks whether the quasi-left-continuous characteristic-domination theorem extends to general local martingales. The source reduces the missing piece to a discrete independent-increment aggregate-domination problem.

Result: The general local martingale extension is true for Hilbert-valued martingales at exponent `p=2`. If `H` is a separable Hilbert space and `N` is characteristically dominated by `M`, then

```text
E ||N_tau||^2 <= E ||M_tau||^2
```

for every bounded stopping time `tau`, and consequently

```text
E sup_t ||N_t||^2 <= 4 E sup_t ||M_t||^2.
```

The proof uses the Hilbert martingale square identity: the terminal second moment is exactly the initial square norm plus the trace of the continuous quadratic covariation plus the second moment of the jump compensator. Characteristic domination controls each of those three terms.

Discrete corollary: For independent mean-zero Hilbert-valued variables satisfying the aggregate domination condition in Remark 12.10, the desired terminal comparison holds at `p=2` with constant `1`.

Limitations: This does not settle the UMD problem for all `p`, nor for non-Hilbert UMD spaces. The previous `c0` packet shows the broad Banach-space statement is false for every finite `p`; this packet identifies a positive Hilbert endpoint where the general local martingale problem survives.

Novelty check: Cheap run indexes had no previous `1907.11588` Hilbert `L2` packet. Web searches found the source paper, Montgomery-Smith--Pruss comparison literature, and Rosenthal/Pinelis moment tools, but no exact recorded answer to the Hilbert `p=2` general-local-martingale subcase.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: continuation noting the symmetric discrete case.
