# Nilpotent sharpness for the q-numerical spectral constant

Status: `partial_result_likely_valid`

Source target: Ryan O'Loughlin and Jyoti Rani, "$q$-Numerical Ranges and Spectral Sets", arXiv:2603.15536.

Conjecture 4.2 asks whether, for every matrix \(A\), \(0<|q|\le 1\), and polynomial \(p\),
\[
\|p(A)\|\le
\max\!\left(1,\frac{2|q|}{1+\sqrt{1-|q|^2}}\right)
\sup_{z\in\Omega_q}|p(z)|,
\qquad \Omega_q=W_q(A)/q .
\]

This packet proves the conjectured constant is sharp. For the \(2\times2\)
nilpotent Jordan block \(J=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), the scaled
\(q\)-numerical range is exactly the disk
\[
\Omega_q(J)=\{z: |z|\le (1+\sqrt{1-|q|^2})/(2|q|)\}.
\]
Hence \(p(z)=z\) forces equality in the nontrivial branch \(|q|\ge 4/5\), while
constant polynomials force the lower branch \(1\). The packet also verifies
that the conjectured inequality itself holds for this nilpotent model.

Contents:

- `main.tex` and `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: local copy of arXiv:2603.15536.
- `figures/open_problem_crop.png`: crop of Conjecture 4.2.
- `code/verify_nilpotent_radius.py`: scalar sanity checks for the radius and threshold.

Human-review recommendation: useful as a sharpness lemma/partial result for
Conjecture 4.2; it is not a proof of the full conjecture for arbitrary matrices.
