# Literature-implied negative answer: unrestricted isotropic log-concave LSI

Source paper: Yin Tat Lee and Santosh S. Vempala, *The
Kannan-Lovász-Simonovits Conjecture*, arXiv:1807.03465.

Supporting paper: Pierre Bizeul, *On the Log-Sobolev Constant of
Log-Concave Vectors*, arXiv:2306.12997v3.

Status: `literature_implied_answer (negative)`.

## Source Question

On PDF page 21, immediately before Definition 36, Lee and Vempala ask whether
the classical log-Sobolev constant is `Theta(1)` for every isotropic
log-concave distribution.

## Identification

As written, the answer is no. Bizeul's abstract and page-1 introduction state
the standard implication that a classical log-Sobolev inequality forces every
one-dimensional marginal to have subgaussian tails. The isotropic two-sided
exponential law

```text
p(x) = (1/sqrt(2)) exp(-sqrt(2) |x|)
```

is log-concave, centered, and has variance one, but it has exponential rather
than subgaussian tails. Therefore it cannot have a positive classical
log-Sobolev constant.

The packet also gives a self-contained variational certificate. For normalized
test functions `f_t(x)=exp(t x)/sqrt(M(2t))`, where
`M(s)=2/(2-s^2)` and `0<t<1/sqrt(2)`, the Dirichlet energy is `t^2`, whereas
the entropy diverges as `t` approaches `1/sqrt(2)`. Hence the source-normalized
log-Sobolev constant is exactly zero.

## Literature Status and Search Bounds

This is not claimed as a new counterexample. The supporting authors do not
name the Lee--Vempala question, so the relation is an agent-identified
implication rather than an explicit literature resolution.

The bounded search covered the run's four cheap indexes; the exact source id,
title, and phrases `isotropic logconcave log-Sobolev constant`, `Laplace
measure`, and `subgaussian tails`; arXiv:1712.01791; and arXiv:2306.12997.
No paper was found that explicitly says it answers the source question.
ArXiv:2306.12997 gives the decisive standard implication and formulates the
meaningful nearby problem for **subgaussian** log-concave measures.

## Scope

The answer concerns the unrestricted question exactly as written. It does not
contradict the source's bounded-support estimate `rho_p >= c/D`, and it does
not settle dimension-free LSI bounds under additional bounded-support,
subgaussian-tail, strong-convexity, or other hypotheses.

## Files

- `main.tex`: compact review packet with the explicit certificate.
- `solution_packet.pdf`: rendered and visually verified packet.
- `source_paper.pdf`: arXiv:1807.03465.
- `supporting_paper_2306.12997.pdf`: decisive supporting source.
- `figures/open_question_crop.png`: source question and Definition 36.
- `figures/supporting_implication_crop.png`: supporting implication on page 1.

Ledger:
`runs/fa_banach_001/ledger/results/1807.03465_logsobolev_laplace_negative.json`.

## Human Review Recommendation

Accept as a literature-implied negative answer to the unrestricted wording.
Do not count it as an original counterexample, and do not extend the conclusion
to the bounded-support or subgaussian variants.

