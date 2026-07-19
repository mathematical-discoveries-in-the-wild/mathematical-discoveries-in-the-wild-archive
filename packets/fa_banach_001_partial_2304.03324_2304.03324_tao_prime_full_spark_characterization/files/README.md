# Strong partial result: exact Banach Tao support-sum criteria

Status: `strong_partial_result_likely_valid`

Source paper: K. Mahesh Krishna, *Functional Donoho-Stark-Elad-Bruckstein-Ricaud-Torresani Uncertainty Principle*, arXiv:2304.03324.

Open problem addressed: Problem 3.2 asks for the Tao uncertainty-principle version for Banach spaces of prime dimension.

Result: for arbitrary finite p-Schauder frames, every support-sum lower bound is characterized exactly by a deletion/spanning condition on the remaining analysis functionals. In the natural p-orthonormal-basis formulation used in the source, this specializes to: the exact support-sum inequality

```text
|supp theta_f x| + |supp theta_g x| >= d + 1
```

for every nonzero `x` is equivalent to the transition matrix between the two coordinate systems being full spark. Therefore prime dimension alone is not a Banach-space substitute for Tao's Fourier theorem; the structural replacement is the full-spark condition. In particular, taking the same p-orthonormal basis twice on `ell_p^r`, with `r > 1` prime, gives `1 + 1 < r + 1` for a coordinate vector.

Packet contents:

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:2304.03324.
- `figures/open_problem_crop.png`: crop of Problem 3.2.

Novelty check: run indexes had no exact `2304.03324` hit. A broad local search found many unrelated support/prime/uncertainty hits but no packet for this source. Web searches on 2026-06-28 for the exact problem wording and "Functional Tao uncertainty principle" surfaced the source paper and nearby Krishna followups, but no later answer to Problem 3.2.
