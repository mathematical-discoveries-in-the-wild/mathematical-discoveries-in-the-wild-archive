# Full Solution Packet: `1112.1289_c0_weighted_shift_gaussian_eigenvalues`

Status: `candidate_full_solution_likely_valid`

Source: Frederic Bayart and Etienne Matheron, *Mixing operators and small subsets of the circle*, arXiv:1112.1289.

## Result

This packet answers Question 7 in Section 7.8 of the source paper negatively:

> Is there an ergodic weighted shift on \(c_0(\mathbb N)\) with no unimodular eigenvalues?

There is no such weighted shift. More strongly, if a weighted backward shift
\(B_{\mathbf w}\) on \(c_0(\mathbb N)\) admits any invariant Gaussian
probability measure with full support, then
\[
  |w_1\cdots w_n| \to \infty.
\]
Equivalently, \(B_{\mathbf w}\) has unimodular eigenvalues; in fact every
\(\lambda\in\mathbb T\) is then a unimodular eigenvalue.

## Proof Sketch

Let \(X=(X_n)_{n\ge 0}\) have the invariant Gaussian law. Since
\(B_{\mathbf w}X\) has the same law as \(X\), the centered coordinate variances
\(a_n=\mathbb E|X_n-\mathbb E X_n|^2\) satisfy
\[
  a_n=|w_{n+1}|^2 a_{n+1}.
\]
Full support gives \(a_0>0\), so \(a_n=a_0/|w_1\cdots w_n|^2\). But \(X\in
c_0\) almost surely and its mean is in \(c_0\), hence the centered coordinates
converge to \(0\) in probability. For scalar Gaussian variables this forces
\(a_n\to0\). Thus \(|w_1\cdots w_n|\to\infty\), which is exactly the standard
unimodular eigenvalue criterion for weighted shifts on \(c_0\).

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of Section 7.8, including Question 7.
- `code/README.md`: notes that no computation is used.

## Verification

The proof was checked against the source paper's weighted-shift convention:
\[
  B_{\mathbf w}(x_0,x_1,\ldots)=(w_1x_1,w_2x_2,\ldots).
\]
The eigenvector recursion gives
\[
  x_n=\lambda^n x_0/(w_1\cdots w_n),
\]
so a nonzero unimodular eigenvector lies in \(c_0\) exactly when
\((1/(w_1\cdots w_n))\in c_0\).

Bounded novelty check: local run indexes were searched for `1112.1289`,
`ergodic weighted shift`, `c0`, `unimodular eigenvalues`, and related terms.
Web searches on 2026-06-20 for exact phrases including `"ergodic weighted
shift" "c0" "unimodular eigenvalues"` and `"weighted shift" "c_0" "no
unimodular eigenvalues" "ergodic"` did not reveal a later explicit answer.

## Human Review Recommendation

Review as a claimed full negative answer to Question 7. The main points to
check are the covariance recursion under invariance and the use of almost sure
\(c_0\)-convergence to force Gaussian coordinate variances to vanish.
