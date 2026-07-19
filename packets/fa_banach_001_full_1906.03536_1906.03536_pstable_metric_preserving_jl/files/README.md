# p-stable metric-preserving JL conjecture

Status: likely valid full solution under the fixed-threshold interpretation of
`||x-y||_p = Omega(1)`.

Source paper: Michael P. Casey, "Linear Dimension Reduction Approximately
Preserving a Function of the 1-Norm", arXiv:1906.03536, Electronic Journal of
Statistics.

Open problem targeted: Conjecture 1.0.2 on page 3 of the source PDF.  The
source asks whether the Cauchy theorem remains true for `1<p<2` after replacing
the Cauchy entries by iid standard p-stable entries and replacing the source
distance by `||x-y||_p`, for all pairs with `||x-y||_p = Omega(1)`.

Packet claim: for each fixed `1<p<2`, lower threshold `lambda0>0`, and failure
exponent `a>0`, there is `C=C(p,lambda0,a)` such that a `k x D` matrix with iid
standard symmetric p-stable entries satisfies

```text
mu(||x-y||_p/(1+epsilon)) <= rho(Fx,Fy)
  <= mu((1+epsilon)||x-y||_p)
```

simultaneously for all pairs in an `N` point set with `||x-y||_p >= lambda0`,
with probability at least `1-N^{-a}`, whenever

```text
k >= C epsilon^{-2} (1-epsilon)^{-2} log N.
```

Here `rho(u,v)=k^{-1} sum_i xi(|u_i-v_i|)`,
`xi(t)=log(1+sqrt(t))+1/2 log(1+t)`, and
`mu(lambda)=E xi(lambda |W|)` for a standard symmetric p-stable random variable
`W`.

The source statement writes `mu(lambda)=E xi(lambda F_11)`, but the metric and
the surrounding proof use absolute values; without the absolute value `xi` is
not defined on negative arguments.  The packet therefore uses the only
consistent interpretation, `E xi(lambda |W|)`.

Proof mechanism: p-stability reduces each difference vector to the one-variable
law `||x-y||_p W`.  On logarithmic scale,
`phi(s)=xi(e^s)` is 1-Lipschitz, while `log |W|` has exponential tails on both
sides.  Hence `xi(lambda |W|)-E xi(lambda |W|)` is uniformly sub-exponential in
`lambda`.  A uniform Bernstein inequality gives deviations of order `epsilon`.
The deterministic gap between `mu(lambda/(1+epsilon))`, `mu(lambda)`, and
`mu((1+epsilon)lambda)` is also at least a constant times `epsilon` once
`lambda >= lambda0`.

Limitations: this does not address a stronger reading in which the hidden
constant in `Omega(1)` is allowed to decay with `N`, `epsilon`, or `p`.  The
dependence of the dimension constant on `lambda0` is explicit in the proof and
is expected for this argument.

Novelty check performed:

- local run registry, solution, attempt, and ledger indexes searched for
  `1906.03536`, `p-stable`, `metric preserving`, and `Conjecture 1.0.2`;
- source TeX inspected at `data/parsed/arxiv_sources/1906.03536`;
- web/arXiv searches performed for exact title, p-stable metric-preserving
  variants, Casey p-stable conjecture, and Cauchy projection metric-preserving
  variants.

No exact prior solution packet or external answer was found in those bounded
searches.  Human review should focus on the uniform sub-exponential reduction
via `log |W|`, the deterministic gap estimate for `mu`, and whether the intended
reading of `Omega(1)` is indeed a fixed lower threshold.

Files:

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop containing Theorem 1.0.1 and
  Conjecture 1.0.2 from the source PDF.
