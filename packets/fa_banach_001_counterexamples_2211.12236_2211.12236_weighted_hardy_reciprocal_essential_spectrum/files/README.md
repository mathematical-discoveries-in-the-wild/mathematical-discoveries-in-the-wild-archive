# Weighted-Hardy counterexample to the reciprocal and essential-spectrum conjectures

Status: `candidate_counterexample_likely_valid`; `human_review_recommended`.

Source: Guangfu Cao, Li He, and Ji Li, *Evaluation functions and composition
operators on Banach spaces of holomorphic functions*, arXiv:2211.12236.
The live questions are in Section 6 on PDF pages 26--27.

## Result

All three general assertions in the source's final remarks fail, even for a
weighted Hardy Hilbert space `B = H^2(beta)` on the unit disk with

```text
1/2 <= beta(n+1)/beta(n) <= 2.
```

The weights make increasingly long ascents with ratio `2` and descents with
ratio `1/2`, returning to weight `1` between consecutive mountains.  For
`psi(z) = 3/2 - z`:

- normalized evaluation kernels converge weakly (hence weak-star) to zero as
  `z` approaches the unit circle;
- `psi` is a multiplier and `|psi(z)| >= 1/2` on the disk;
- `1/psi` does not belong to `H^2(beta)`;
- `0` belongs to the essential spectrum of `M_psi`; but
- the boundary cluster set is the circle `3/2 - T`, which does not contain
  zero.

Thus the essential-spectrum inclusion from the source can be strict, the
ordinary spectrum can strictly exceed the closure of the multiplier range,
and both Conjectures 2 and 3 are false as stated.

## Mechanism

With respect to the normalized monomials, multiplication by `z` is a unilateral
weighted shift.  Around every valley of the weight sequence it looks, for an
increasingly long interval, like a bilateral shift having weights `1/2` to the
left and `2` to the right.  The adjoint therefore has disjoint approximate
eigenvectors at `3/2`, so `3/2 I - M_z` is not Fredholm.  The high peaks also
force the coefficient series of `1/(3/2-z)` out of the function space, while
the repeated valleys make the reproducing-kernel norms diverge at the boundary.

## Novelty boundary

The run indexes, the local 2000--present arXiv corpus, exact web searches for
arXiv:2211.12236 and its reciprocal/essential-spectrum questions, and forward
publication records were checked on July 21, 2026.  No direct answer or this
counterexample was found.  Lindstrom--Miihkinen--Norrbo (arXiv:2002.07035)
prove the desired spectral formulas for several structured spaces under
additional inverse-closedness or derivative-norm hypotheses; this example
shows those extra hypotheses cannot be discarded.  Bourdon
(arXiv:1211.4190) supplies standard weighted-Hardy background but does not
address the later conjectures.  The weighted-shift mechanism is classical, so
expert literature review remains appropriate.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop_page26.png` and
  `figures/open_problem_crop_page27.png`: source screenshots.
- `code/check_block_weights.py`: numerical/formula sanity check.

