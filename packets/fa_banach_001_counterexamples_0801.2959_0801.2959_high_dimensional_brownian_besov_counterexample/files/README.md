# High-Dimensional Brownian Counterexample to the Proposed Besov Comparison

Status: candidate full counterexample, likely valid.

Hytönen and Veraar ask in Remark 6.1 of arXiv:0801.2959 whether their
dimension-free upper estimate

```text
E ||W||_{B^{1/2}_{p,infinity}} <= C sqrt(p) E ||W(1)||
```

has a dimension-free reverse inequality. It does not. For standard Brownian
motion with values in `X = ell_2^d`, the source's Theorem 6.1 and the Gaussian
moment estimate give

```text
E ||W||_{B^{1/2}_{p,infinity}}  ~  sqrt(d) + sqrt(p),
sqrt(p) E ||W(1)||              ~  sqrt(p d).
```

Taking `d = p = n` makes the ratio tend to zero. The packet also records the
correct universal replacement:

```text
E ||W||_{B^{1/2}_{p,infinity}}
  ~ E ||W(1)|| + sqrt(p) sigma(W(1)),
```

where `sigma` is the weak Gaussian standard deviation.

## Packet contents

- `solution_packet.pdf`: source question, corrected theorem, and proof.
- `source_paper.pdf`: arXiv:0801.2959v1.
- `figures/open_problem_crop.png`: source PDF page 15, Theorem 6.1 and Remark 6.1.
- `code/make_open_problem_crop.py`: reproducible source crop.
- `code/check_chi_scaling.py`: exact chi-moment numerical sanity check.
- `verification.md`: independent proof audit and search bounds.

Run the sanity check from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0801.2959_high_dimensional_brownian_besov_counterexample/code/check_chi_scaling.py
```

The script uses the exact gamma-function formula for chi moments. It is
corroboration only; the packet's proof is analytic.

## Novelty status

A bounded search on 22 July 2026 covered the run's four cheap indexes, the
35,297-paper deterministic source-signal corpus, exact arXiv/web queries for
the source title, authors, quoted unresolved sentence, and formula keywords,
and visible later papers citing the source. It found the original paper and
downstream uses of its Besov regularity theorem, but no later paper answering
Remark 6.1 or giving this high-dimensional counterexample. Novelty confidence
is moderate, not definitive; the argument itself is elementary once Theorem
6.1 is combined with the weak/strong Gaussian moment decomposition.

## Human review recommendation

Check three points: (1) the source convention makes all unsubscripted
comparison constants universal; (2) Theorem 6.1 is uniform in `X`, `p`, and
`W`; and (3) the standard Gaussian moment equivalence is
`||G||_{L^p} ~ E||G|| + sqrt(p) sigma(G)`. The `ell_2^d` contradiction then
follows immediately.
