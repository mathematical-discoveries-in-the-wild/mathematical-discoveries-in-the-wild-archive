# Full solution packet: periodic shadowing on `ell_p(Z)` and `c_0(Z)`

Status: `full_solution_likely_valid`

Source target: Michal Hevessy and Tomas Raunig, *Dynamical properties of weighted shifts on sequence spaces*, arXiv:2509.11852v2. The target is Question 4.13 on page 16, asking whether the periodic shadowing property for weighted backward, equivalently forward, shifts on `ell_p(Z)`, `1 <= p < infinity`, coincides with the periodic shadowing property on `c_0(Z)`.

## Result

Yes. Let `w=(w_n)` be bounded and bounded away from zero, and let `B_w` be the associated bilateral weighted backward shift. For every `1 <= p < infinity`,

```text
B_w has periodic shadowing on ell_p(Z)
    iff
B_w has periodic shadowing on c_0(Z).
```

The same equivalence holds for weighted forward shifts, since periodic shadowing is invariant under inversion and a forward shift is the inverse/reindexing of a backward shift with reciprocal weights.

## Proof mechanism

The dense-periodic-point case is already forced by the source paper: periodic shadowing is then equivalent to shadowing, and the shadowing characterization is the same on `ell_p` and `c_0`.

The remaining case has no nonzero periodic points. There, periodic shadowing is equivalent to a uniform lower bound for all cyclic pseudo-orbit defect operators

```text
D_N(x)_i = x_{i+1} - B_w x_i,   i mod N.
```

For `c_0`, this lower bound is a scalar sup-norm estimate along the diagonal orbits `(i,j) -> (i+1,j-1)` of the space-time lattice. Homogeneity converts it into a uniform bound on the finite Green matrices. Those Green matrices have uniformly bounded row sums; applying the same estimate to the inverse shift gives the matching time-resolved column bounds. The Schur test and Minkowski's inequality lift the estimate to the mixed norm `sup_i ||x_i||_p`, with a constant independent of the period `N`. Hence `c_0` periodic shadowing implies `ell_p` periodic shadowing. The reverse direction follows from the source paper's necessary scalar condition for `ell_p` plus its complete `c_0` characterization.

## Files

- `main.tex` and `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_question_page15.png` and `figures/open_question_page16.png`: rendered source pages containing the `c_0` characterization and Question 4.13.
- `code/verify_finite_green_transfer.py`: finite cyclic matrix sanity check for the diagonalization and Schur-transfer mechanism.

## Literature check

Checked local run indexes for `2509.11852`, the title, `periodic shadowing`, `weighted backward shifts`, `ell_p`, and `c_0`; no duplicate packet or exact answer was present. Web searches for the exact question and close phrases found the arXiv paper, a seminar page, ResearchGate mirror, and summary/review pages, but no later paper answering Question 4.13.

Human review recommendation: verify the finite Green-matrix transference lemma, especially the passage from the `c_0` cyclic defect estimate to the time-resolved Schur bounds used for the mixed `sup_time ell_p` norm.
