# Finite-dimensional kernel pairing for Nowak Remark 4.3

Status: `candidate_partial_result_likely_valid`.

## Source problem

Piotr W. Nowak, "Poincare inequalities and rigidity for actions on Banach spaces", arXiv:1107.1896.

The target is Remark 4.3. In the paper's notation, for an isometric representation
\(\pi\) on a reflexive Banach space \(X\), the remark asks for which representations the natural map
\[
  i^*\circ \bar i:\ker d_{\bar\pi}\longrightarrow (\ker d_\pi)^*
\]
is automatically an isomorphism, or at least surjective. Such a result would remove one of the two Poincare-constant inequalities from the main proof for those representations.

## Result

For every finite-dimensional real or complex normed space \(X\), and every isometric representation \(\pi:G\to \mathrm{Isom}(X)\), the map above is an isomorphism.

The proof averages an auxiliary Euclidean/Hermitian inner product over the compact closure of \(\pi(G)\). The resulting invariant inner product gives a Riesz identification \(J:X\to X^*\) (linear in the real case and conjugate-linear in the complex case) satisfying
\[
  J\pi_g=\bar\pi_gJ .
\]
Applying \(J\) coordinatewise sends \(\ker d_\pi\) onto \(\ker d_{\bar\pi}\). The restriction pairing is positive on the graph of this identification:
\[
  \sum_{s\in S} (Jf(s))(f(s))\,\deg_\omega(s)
  =
  \sum_{s\in S}\|f(s)\|_H^2\,\deg_\omega(s)>0
\]
for every nonzero \(f\in\ker d_\pi\). Since the kernels have equal finite dimension, the natural map is an isomorphism.

## Scope

This is a partial answer to Remark 4.3. It covers all finite-dimensional isometric representations, including but not limited to the finite quotient example treated later in Section 7.2 of the source paper. It does not address infinite-dimensional isometric representations.

## Verification and novelty notes

- Cheap-index search found no existing packet for arXiv:1107.1896 or this finite-dimensional kernel-pairing strengthening.
- Web searches on 2026-07-03 for exact phrases around `i^* circ overline{i}`, `finite-dimensional`, and the paper title found no prior answer beyond the source arXiv page.
- `code/finite_dimensional_kernel_pairing_check.py` performs finite-dimensional rank sanity checks for cyclic and free-group-style generating sets with non-orthogonal conjugates of rotations. These checks are not used as proof.

## Packet contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop_page15.png` and `figures/open_problem_crop_page16.png`: source crops for Remark 4.3.
- `code/finite_dimensional_kernel_pairing_check.py`: sanity-check script.
