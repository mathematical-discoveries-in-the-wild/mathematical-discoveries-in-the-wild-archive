# Verification report

Verdict: candidate full counterexample, likely valid.

## Claim audited

There is no universal constant `c > 0` such that every Banach-valued Brownian
motion and every `p >= 1` satisfy

```text
E ||W||_{B^{1/2}_{p,infinity}} >= c sqrt(p) E ||W(1)||.
```

The stronger replacement formula in the packet is

```text
E ||W||_{B^{1/2}_{p,infinity}}
  ~ E ||W(1)|| + sqrt(p) sigma(W(1)).
```

## Proof audit

1. The source defines unsubscripted `lesssim` and `eqsim` using universal
   constants. Its Theorem 6.1 therefore gives, uniformly in `X`, `p`, and `W`,
   the Besov expectation comparable to the `L^p` norm of `||W(1)||`.
2. For any centered Banach-valued Gaussian `G`, Gaussian concentration gives
   the upper moment estimate `||G||_{L^p} <= E||G|| + C sqrt(p) sigma(G)`.
   The two lower bounds follow from monotonicity of moments and from applying
   a unit dual functional of nearly maximal variance. Hence the corrected
   two-sided formula has universal constants.
3. For `G = g_d` standard Gaussian in `ell_2^d`, `sigma(G)=1` and
   `E||G|| ~ sqrt(d)`. Therefore the Besov expectation is at most a universal
   multiple of `sqrt(d)+sqrt(p)`.
4. If the proposed reverse comparison held, setting `d=p=n` would force a
   quantity of order `sqrt(n)` to dominate one of order `n`, a contradiction.

No unproved lemma remains. The only external input beyond the source theorem
is the standard Gaussian concentration/moment inequality, cited in the packet.

## Computational sanity check

`code/check_chi_scaling.py` evaluates

```text
(E ||g_n||_2^n)^(1/n) / (sqrt(n) E ||g_n||_2)
```

using the chi-distribution gamma formula for `n = 4, 16, ..., 4096`. The
values decrease below `0.03`, in agreement with the analytic limit zero. This
calculation is not used as proof.

## Novelty/literature bounds

- Local: `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  `proof_gaps/index.tsv`, and the deterministic source-signal corpus.
- External: exact searches for arXiv:0801.2959, the paper title and authors,
  the quoted phrase “two sided comparison here,” and Brownian/Besov moment
  formula variants; visible primary papers citing the source were inspected.
- Found: the original 2008 source and later works using its regularity result.
- Not found: an explicit answer to Remark 6.1 or this `ell_2^d` family.

Searches were bounded rather than exhaustive, so novelty confidence is
moderate. Mathematical validity does not depend on novelty.

## Human-review focus

Verify the intended quantifier in “two sided comparison”: the packet answers
the universal, dimension-free interpretation dictated by the source's stated
notation. It does not deny that a fixed nonzero Gaussian `W(1)` admits a lower
constant depending on the ratio `sigma(W(1))/E||W(1)||`.
