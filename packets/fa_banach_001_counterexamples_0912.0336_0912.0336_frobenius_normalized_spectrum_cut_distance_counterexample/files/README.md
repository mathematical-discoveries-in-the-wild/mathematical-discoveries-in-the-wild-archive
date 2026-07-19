# Counterexample: Frobenius-normalized spectra are not cut-distance continuous

Status: `counterexample_likely_valid`.

Source target: Vladimir Nikiforov, *Cut-norms and spectra of matrices*, arXiv:0912.0336.

The source's concluding remarks ask whether Theorem 3 can be modified by replacing the normalizations
\(\sigma_i(A)/\sqrt{mn}\) and \(\sigma_i(B)/\sqrt{pq}\) with the Frobenius-normalized quantities
\(\sigma_i(A)/\|A\|_F\) and \(\sigma_i(B)/\|B\|_F\).

This packet gives a negative answer to the natural cut-distance-continuity version of that modification. Let
\[
A_n=e_1{\bf 1}^T,\qquad B_n=I_n.
\]
Then \(A_n\) and \(B_n\) are \(n\times n\) \(0\)-\(1\) matrices with \(\|A_n\|_F=\|B_n\|_F=\sqrt n\), while
\[
\delta_{\boxminus}(A_n,B_n)\le \|A_n-B_n\|_\square\le 2/n.
\]
However,
\[
\frac{\sigma_1(A_n)}{\|A_n\|_F}=1,\qquad
\frac{\sigma_1(B_n)}{\|B_n\|_F}=1/\sqrt n.
\]
Thus the Frobenius-normalized singular spectra remain separated by a quantity tending to \(1\), even though the cut-distance tends to \(0\).

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source page containing the concluding question.
- `code/verify_counterexample.py`: small verifier for the family.

Human-review recommendation: check that the intended reading of the source question is the natural analogue of Theorem 3 with a cut-distance-only modulus. The example leaves open modified statements with additional density/Frobenius-size hypotheses.
