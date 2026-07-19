# Counterexample: gamma-plus Is Not Locally Lipschitz on the PSD Boundary

Status: `counterexample_likely_valid`

Source: Radu Balan and Fushuai Jiang, *Factorization of positive-semidefinite
operators with absolutely summable entries*, arXiv:2409.20372. Remark 2.7 on
PDF page 7 asks whether the factorization functional `gamma_+`, already known
to be locally Lipschitz on the positive-definite cone, remains locally
Lipschitz on the entire positive-semidefinite cone.

## Claimed contribution

The answer is no, already for complex Hermitian `4 x 4` matrices. Put

```text
V = [[ 4,  1],
     [-1, -1],
     [-4,  1],
     [ 0,  4]]

A = V V^T
  = [[ 17, -5, -15,  4],
     [ -5,  2,   3, -4],
     [-15,  3,  17,  4],
     [  4, -4,   4, 16]].
```

Then `A` is positive semidefinite of rank two, `gamma_+(A)=125`, and
`gamma_+` is not locally Lipschitz at `A` relative to the PSD cone. Since all
norms on the finite-dimensional Hermitian matrix space are equivalent, this
includes the source paper's entrywise `l1` metric.

## Proof mechanism

For `N(z)=||Vz||_1`, the exact quadratic minorant

```text
N(z)^2 >= z^* H z,    H = [[81, 7], [7, 44]],
```

holds for all complex `z`. Three contact directions

```text
q0=(1,0),  q+=(1,4),  q-=(-1,4)
```

form a weighted tight frame with weights `15/16, 1/32, 1/32`. They give both
an optimal factorization of `A` and the exact value `gamma_+(A)=125`.

If `gamma_+` were locally Lipschitz at `A`, a finite-dimensional convex
extension argument would produce a Hermitian supporting form `T` satisfying

```text
x^* T x <= ||x||_1^2  for all x,    tr(A T)=gamma_+(A).
```

The tight-frame identity forces equality at `x0=Vq0`, `x+=Vq+`, and
`x-=Vq-`. Differentiating the three equality constraints in their nonzero
second coordinates gives

```text
(T x0)_2=-9,   (T x+)_2=-29,   (T x-)_2=-27.
```

But `x+ - x- = 2 x0`, so linearity would require `-2=-18`. Thus no such
supporting form exists, contradicting local Lipschitzness.

## Verification

The symbolic checker verifies the Gram matrix, rank, piecewise factorization
of the quadratic minorant, tight-frame identity, optimal cost 125, and final
linear contradiction:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2409.20372_gamma_plus_not_locally_lipschitz_boundary/code/verify_counterexample.py
```

Result: all exact checks pass.

Verifier focus:

- Check the lemma that relative local Lipschitzness of a convex homogeneous
  functional yields an ambient supporting form. The packet proves it using an
  infimal-convolution extension.
- Check the passage from the real piecewise inequality to complex vectors.
- Check that equality in the three positive-weight frame inequalities forces
  the three coordinate derivative identities.

## Novelty and scope

The bounded novelty search on 2026-07-19 covered the four lightweight run
indexes, the exact arXiv id and title, the exact local-Lipschitz phrase,
`gamma_+ locally Lipschitz positive semidefinite`, and `Optimal l1 Rank One
Matrix Decomposition Lipschitz boundary`. It checked arXiv:2409.20372, the
locally loaded 2021 predecessor arXiv:2002.00879, and Radu Balan's January 2026
author presentation, which still labels the Lipschitz problem open. No later
proof or counterexample was found.

This packet settles only the yes/no question in Remark 2.7. It does not
classify the boundary points where local Lipschitzness holds, and it does not
settle whether dimension three already admits a counterexample.

Human review recommendation: send to a convex-analysis/matrix-factorization
reviewer. The argument is short and exact; the most important audit point is
the Lipschitz-to-support lemma.

Files:

- `source_paper.pdf`: arXiv:2409.20372.
- `figures/open_problem_crop.png`: source PDF page 7, Remark 2.7.
- `main.tex`, `solution_packet.pdf`: full proof packet.
- `code/verify_counterexample.py`: exact symbolic checks.

