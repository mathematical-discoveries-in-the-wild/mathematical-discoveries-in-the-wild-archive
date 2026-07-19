# Verification Report

Candidate: arXiv:1907.11583, Section 5

## Claim Checked

The measure \(\mu=\sum_{n\ge1}\delta_{n^2+i}\) satisfies
\(\mu(Q_I)\lesssim |I|^{1/2}\), but the Laplace--Carleson embedding
\[
  \mathcal L:L^{3/2}(\mathbb R_+)\longrightarrow
  L^{3/2}(\mathbb C_+,\mu)
\]
is unbounded.

## Verdict

**likely valid**

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Local finiteness | valid | The atoms \(n^2+i\) escape every compact set. |
| Box estimate | valid | Boxes of width below 1 contain no atom; an interval of length \(L\ge1\) contains at most \(\sqrt L+1\le2\sqrt L\) positive squares. |
| Domain test functions | valid | Every \(f_N\) is bounded and supported in \((0,1)\), hence belongs to \(L^1\cap L^{3/2}\). |
| Laplace sign | valid | At \(z=n^2+i\), \(e^{2\pi i tz}=e^{2\pi i n^2t}e^{-2\pi t}\), exactly cancelling the factor \(e^{2\pi t}\) in \(f_N\). |
| Sampling identity | valid | The remaining integrals are integer Fourier integrals on \((0,1)\), equal to 1 only when \(n=k\). |
| Output norm | valid | There are exactly \(N\) unit samples, so the \(L^{3/2}(\mu)\)-norm is \(N^{2/3}\). |
| Input norm | valid | On the unit interval, \(\|S_N\|_{3/2}\le\|S_N\|_2\), and Parseval gives \(\|S_N\|_2=\sqrt N\). |
| Divergence | valid | The norm ratio is at least \(e^{-2\pi}N^{1/6}\). |
| Stronger \(1<p\le q<2\) wedge | valid | The integer sequence \(m_n=\lceil n^{p'/q}\rceil\) has interval counts \(O(L^{q/p'})\), and the same test has ratio \(N^{1/q-1/2}\to\infty\). |

## Counterexample Search Against The Proof

Small cases were checked by `code/verify_square_counterexample.py`. It verifies finite square-count bounds and the exact finite sampling matrix. No contradiction was found. This code is a sanity check, not proof evidence.

## External Dependencies

None. The mathematical proof uses only elementary counting, orthogonality of integer exponentials on \((0,1)\), Parseval for a finite trigonometric polynomial, and monotonicity of \(L^p\)-norms on a probability space.

## Gaps

No proof gap identified. The only residual uncertainty is literature novelty beyond the bounded search recorded in the packet.

## Confidence

Score: 98/100.

Reason: every operator, measure, exponent, and normalization is checked explicitly; the unbounded norm ratio is exact up to a harmless fixed factor.

## Human Review Recommendation

Send to a functional analyst familiar with Laplace--Carleson embeddings. The proof is short enough for line-by-line verification; ask the reviewer to focus on whether the source uses any convention that excludes complex test functions or horizontally unbounded nonsectorial atomic measures. No such exclusion appears in the source definitions.
