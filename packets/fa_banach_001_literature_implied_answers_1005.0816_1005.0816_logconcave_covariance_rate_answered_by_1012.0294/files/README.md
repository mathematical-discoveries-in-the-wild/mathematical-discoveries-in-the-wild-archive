# Literature-Implied Answer: sharp log-concave empirical covariance rate

Status: `literature_implied_answer`

Source question: Shahar Mendelson, *Empirical processes with bounded
`psi_1` diameter*, arXiv:1005.0816, printed page 47, equation (6.6), near the
end of the section “From a bounded diameter to concentration.” The paper
conjectures that for independent
samples `X_1,...,X_N` from any isotropic log-concave law on `R^n`, and every
`N \gtrsim n`,

```text
sup_{theta in S^{n-1}}
  | (1/N) sum_i <theta,X_i>^2 - 1 |
    <= C sqrt(n/N)
```

with high probability or in expectation.

Supporting theorem: Radosław Adamczak, Alexander E. Litvak, Alain Pajor, and
Nicole Tomczak-Jaegermann, *Sharp bounds on the rate of convergence of the
empirical covariance matrix*, arXiv:1012.0294, printed page 2. Theorem 1
(labelled `raz` in the arXiv source), together with the log-concave
specialization in Example 2,
proves the displayed estimate for every `N>=n` with probability at least
`1-2 exp(-c sqrt(n))`, with absolute constants.  This is exactly the
high-probability branch of Mendelson’s conjecture and is explicitly described
by the supporting paper as removing the previous logarithmic loss and reaching
the Gaussian rate for arbitrary `N`.

Provenance: the mathematical match is exact, but the published supporting
source does not explicitly name Mendelson’s conjecture (its TeX source contains
only a commented Mendelson bibliography entry).  The relation is therefore
recorded conservatively as an agent-identified literature implication rather
than `literature_already_answered`.

Scope: this packet resolves only equation `(sampling)` in arXiv:1005.0816.
The surrounding broad discussion about extending other Gaussian geometric
results to log-concave sampling is not a single mathematical claim.

Files:

- `source_paper.pdf`: arXiv:1005.0816.
- `supporting_paper_1012.0294.pdf`: decisive later theorem.
- `main.tex`, `solution_packet.pdf`: compact identification note.

This packet claims no new proof.
