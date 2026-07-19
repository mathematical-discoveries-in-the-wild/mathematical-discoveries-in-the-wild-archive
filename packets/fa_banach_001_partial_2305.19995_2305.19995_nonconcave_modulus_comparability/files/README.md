# Partial Result: nonconcave moduli must be concave-comparable

Status: candidate partial result, likely valid; human review recommended.

Source paper: Michal Johanis, Vaclav Krystof, and Ludek Zajicek,
"On Whitney-type extension theorems on Banach spaces for \(C^{1,\omega}\),
\(C^{1,+}\), \(C_{\mathrm{loc}}^{1,+}\), and
\(C_{\mathrm B}^{1,+}\)-smooth functions", arXiv:2305.19995.

## Target

Remark `r:moduli_nonconc` asks whether the sufficient condition in part (b)
is necessary: for a nonconcave finite modulus \(\omega\), if the
Whitney-Glaeser extension theorem `t:ext_C1om` remains valid with \(\omega\),
must there exist a concave modulus \(\psi\) and \(K>0\) such that
\[
\psi\le \omega\le K\psi?
\]

## Result

Yes, for the sufficiency direction with derivative interpolation. If the
Whitney-Glaeser principle for \(\omega\) holds even on a one-dimensional line,
then \(\omega\) is equivalent up to constants to a concave modulus. Combined
with the source paper's sufficient direction, this gives an exact
characterization:
\[
\text{the nonconcave } C^{1,\omega}\text{ extension theorem holds}
\quad\Longleftrightarrow\quad
\omega \text{ is concave-comparable.}
\]

## Proof Idea

Place countably many dyadic pairs very far apart on a line. On the pair of
length \(2^k\), prescribe derivative jump exactly \(\omega(2^k)\), while
setting the function values equal to zero. Wide separation makes the whole
datum satisfy the Whitney-Glaeser condition with modulus \(\omega\).

Any \(C^{1,\omega}\) extension whose derivative matches the prescribed data
has derivative modulus \(m\) satisfying \(m(2^k)\ge \omega(2^k)\) for every
dyadic scale and \(m\le C\omega\). Since \(m\) is subadditive, Stechkin's
concavification lemma gives a concave \(\theta\) with
\[
\omega(t)\lesssim \theta(t)\lesssim \omega(t).
\]
Rescaling \(\theta\) gives \(\psi\le\omega\le K\psi\).

## Files

- `main.tex`: theorem, proof intuition, proof, and review notes.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2305.19995.

## Verification

Local cheap-index search found no existing packet or attempt for arXiv:2305.19995.
Local parsed-source search found only the original open remark. Web search on
2026-06-18 found the source paper and the later arXiv:2507.09384 follow-up,
but no answer to the nonconcave-modulus comparability question.
