# Counterexample: non-log-concave marginal information production

Source paper: Keith Ball and Van Hoang Nguyen, *Entropy jumps for isotropic
log-concave random vectors and spectral gap*, arXiv:1206.5098 / Studia
Mathematica 213 (2012), 81-96.

Status: scoped counterexample, likely valid.

## Source Question

After Theorem 1, the source says that the log-concavity assumption is crucial
for the proof of inequality (3.2), and that the authors do not know whether
the inequality holds without this assumption.

Inequality (3.2) is the marginal information-production estimate

```text
int_E Tr[(Hess log h)^2] h
  <= int_R^N Tr[(P_E Hess log omega P_E)^2] omega.
```

## Result

The log-concavity-free extension of (3.2) is false.

Let `a=5/2`. Let `Y` have a narrow symmetric two-Gaussian mixture law and,
conditionally on `Y=y`, let

```text
X | Y=y  ~  N(a y, 1).
```

The joint density `omega(x,y)` is smooth and positive. For the projection
onto the `x`-axis,

```text
partial_xx log omega(x,y) = -1,
```

so the right side of (3.2) equals `1`. The `x`-marginal is a separated
two-Gaussian mixture. In the zero-variance mixing limit its squared
log-curvature integral is strictly greater than `1`; a short analytic
central/tail estimate proves the strict gap. By continuity, the same failure
persists for sufficiently narrow smooth two-Gaussian mixing.

## Scope

This does not refute the source theorem, Lemma 4 as stated, or the
log-concave case. It shows that the sign/log-concavity mechanism behind
Lemma 4 is genuinely necessary for inequality (3.2): without it, marginal
log-curvature can be larger in square than the averaged projected conditional
log-curvature.

## Files

- `main.tex`: counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_question_crop.png`: source line saying the non-log-concave
  case was unknown.
- `figures/source_inequality_crop.png`: source Lemma 4 and inequality (3.2).
- `code/mixture_curvature_check.py`: numerical sanity check for the integral.

## Human Review Recommendation

Accept as a scoped counterexample to the log-concavity-free version of
inequality (3.2). Do not count it as a counterexample to the source's
log-concave theorem.
