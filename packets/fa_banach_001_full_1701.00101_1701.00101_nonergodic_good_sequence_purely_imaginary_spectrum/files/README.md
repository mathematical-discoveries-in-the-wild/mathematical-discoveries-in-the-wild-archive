# Non-ergodic good sequence with purely imaginary nontrivial spectrum

Status: `full_solution_likely_valid` for the second question in Cuny--Eisner--Farkas, Question 2.7.

This packet answers the source question asking whether there is a non-ergodic good subsequence `(k_n)` of `N` such that

```text
Re c(lambda) = 0 for every lambda in T \ {1}.
```

The construction is probabilistic.  Take all integers congruent to `1 mod 3`, no integers congruent to `2 mod 3`, and independently keep each integer congruent to `0 mod 3` with probability `1/2`; enumerate the resulting random set increasingly.  Almost surely the centered random part has uniformly vanishing exponential sums, so the only nonzero nontrivial Fourier-Bohr coefficients are at the two primitive cubic roots.  They are `i sqrt(3)/3` and `-i sqrt(3)/3`.

Scope: this fully answers the second sentence of Question 2.7.  It does not answer the preceding question about whether existence of the quadratic Fourier-coefficient averages for all probability measures implies goodness.

Files:

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1701.00101.
- `figures/open_problem_crop.png`: crop of Question 2.7 in the source.
- `code/verify_residue_coefficients.py`: exact finite residue computation.

Novelty check: cheap run indexes were searched for `1701.00101`, `Wiener's lemma`, `good sequence`, `non-ergodic`, and `Re c(lambda)`.  Web searches for exact phrases from Question 2.7 and the source title found no later explicit answer in the bounded check performed on 2026-07-03.
