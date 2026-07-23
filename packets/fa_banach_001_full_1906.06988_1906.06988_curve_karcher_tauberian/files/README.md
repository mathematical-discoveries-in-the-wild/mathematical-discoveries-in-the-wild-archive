# A continuous Tauberian theorem for Karcher means

Status: `candidate_full_likely_valid`

Source: Hadi Khatibzadeh and Hadi Pouladi, *Tauberian Conditions for
Almost Convergence in a Geodesic Metric Space*, arXiv:1906.06988.

Source location: Remark 3.1, PDF page 14. The authors define the Karcher
mean `sigma_T` of a curve and state that the curve analogue of their
Theorem 3.5 remains open.

## Full resolution of the curve analogue

Let `c:[0,infinity)->H` be a locally absolutely continuous curve in a
Hadamard space. Let `g` be a locally integrable upper gradient:

```text
d(c(s),c(t)) <= integral_s^t g(u) du  (0 <= s <= t).
```

If its Karcher means `sigma_T` converge to `y` and

```text
(1/T) integral_0^T t g(t) dt -> 0,
```

then `c(T)->y`. More precisely,

```text
d(c(T),y)
 <= d(sigma_T,y) + (1/T) integral_0^T t g(t) dt.
```

Thus the pointwise metric-derivative condition
`t |c'|(t)->0` is a sufficient continuous counterpart of
`n d(x_n,x_(n-1))->0`.

The apparently literal unit-lag condition is not sufficient. On the real
line,

```text
c(t)=sin(2 pi t)
```

has `t |c(t)-c(t-1)|=0`, and its Karcher means converge to zero, but the
curve does not converge. This counterexample explains why an infinitesimal
or local-variation hypothesis is essential.

## Proof mechanism

The CAT(0) variance inequality and the triangle inequality imply the
continuous barycenter estimate

```text
d(sigma_T,z) <= (1/T) integral_0^T d(c(t),z) dt.
```

Take `z=c(T)`, bound each distance by the upper-gradient integral from `t`
to `T`, and reverse the order of integration. The resulting triangular
integral is exactly `(1/T) integral_0^T t g(t) dt`.

## Scope and novelty

This resolves the curve version of Theorem 3.5 in every Hadamard space under
the correct continuous analogue, and it disproves the competing unit-lag
interpretation. It does not answer the paper's separate question about
uniformly convex non-CAT(0) spaces or its separate Delta-convergence question.

The cheap run indexes were searched by arXiv id, title, almost convergence,
Karcher mean, curve, and Tauberian terms. A bounded web/arXiv search through
23 July 2026 used the exact title, the phrase "Theorem 3.5 for curves",
"Karcher mean curve Tauberian condition", and the authors' names. It found
the source and a later mean-ergodic paper by the same authors that reuses the
curve Karcher-mean framework, but no resolution of this open question. This
is a bounded novelty check, not an exhaustive certification.

## Packet contents

- `main.tex`: formal theorem, proof, exact counterexample, scope, and
  novelty record.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Remark 3.1 on page 14.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `verification.md`: adversarial proof audit.

Human review recommendation: **send to an analyst familiar with CAT(0)
barycenters and Tauberian theorems**. The main point to assess is whether the
source authors intended the metric-derivative or unit-lag interpretation; the
packet resolves both.
