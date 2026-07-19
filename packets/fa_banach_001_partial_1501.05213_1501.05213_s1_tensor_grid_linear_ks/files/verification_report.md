# Verification Report

Candidate: arXiv:1501.05213, weighted tensor-grid subcase of the \(S_1\) linear-KS question.

## Claim checked

For \(z_{jk}=a_{jk}u_jv_k^*\), with both vector families orthonormal, source equation (8) holds with constant \(1\), and source equation (10) holds with constant \(e\), uniformly in \(n\), the scalar field, and the coefficients.

## Verdict

`likely valid` (scoped partial result).

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Row signed sum is rank one with norm \((\sum_k|a_{jk}|^2)^{1/2}\) | valid | Orthogonality of the \(v_k\)'s gives the unique nonzero singular value. |
| Permutation transversal has singular values \(|a_{j,\pi(j)}|\) | valid | The selected initial and terminal vectors are both orthonormal. |
| General selector has norm \(\sum_k(\sum_{j:K_j=k}|a_{jk}|^2)^{1/2}\) | valid | The selected rows partition by \(k\); the corresponding range vectors are orthogonal, as are the domain vectors \(v_k\). |
| Bernoulli first-hit identity | valid | After decreasing rearrangement in a fixed column, the first successful selector has probability \(n^{-1}(1-n^{-1})^{r-1}\). |
| Uniform bound \((1-1/n)^{n-1}\ge e^{-1}\) | valid | Standard monotonic limit bound; \(n=1\) is handled directly. |
| Comparison with the left side | valid | Row \(\ell_2\) norms are bounded by row \(\ell_1\) norms. |

## Counterexample search

Small cases checked: all selectors for randomized scalar arrays for \(1\le n\le5\); direct SVD checks of the selector formula for small matrices; unrestricted gradient searches for real matrix arrays at \(n=2,3,4,5\).

Result: no contradiction. The unrestricted searches are heuristic and are not used to validate the theorem.

## Gaps and limitations

- The proof applies only to tensor-grid arrays. It does not permit \(u\) or \(v\) to depend on both indices.
- It gives no metric KS inequality for nonlinear maps into \(S_1\).
- The constant \(e\) is not claimed optimal.
- The bounded novelty search does not establish publication novelty.

## Confidence

Score: 92/100.

Reason: the proof reduces to explicit singular values and a one-line finite Bernoulli estimate. The confidence deduction is entirely for literature novelty and the risk of a hidden equivalent known lemma, not for the algebraic argument.

## Human review recommendation

Send to human as a narrow partial result. Verify the column-block singular-value calculation first; if accepted, the remaining inequalities are routine.

