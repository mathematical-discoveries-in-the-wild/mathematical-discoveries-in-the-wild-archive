# Partial result: a p>2 obstruction for property P_1(m) into ell_r targets

Status: `strong_partial_likely_valid`

Source paper: Omer Friedland and Olivier Guedon, *Sparsity and non-Euclidean
embeddings*, arXiv:1107.0992.

## Claim

The source asks what happens for \(p>2\) in the search for operators satisfying
the restricted isomorphism property \(\mathcal P_1(m)\), after explaining that
the \(p\)-stable construction works only for \(0<p<2\).

This packet proves a negative obstruction for the most direct analogue of the
paper's \(\ell_r\)-target construction:

If \(p>2\), \(0<r\le 1\), and \(A:\ell_p^n\to \ell_r^N\) satisfies
\(\mathcal P_1(m)\) with constants \(\alpha,\beta\), then
\[
  m^{1/2-1/p}\le K_r\,\frac{\beta}{\alpha},
\]
where \(K_r\) depends only on \(r\).  Hence, with fixed distortion
\(\beta/\alpha\), the sparsity order \(m\) is bounded independently of \(n\).
In particular, the \(p<2\) result with \(m\simeq \eta n/\log(1+1/\eta)\)
cannot extend to \(p>2\) for targets \(\ell_r^N\), \(0<r\le1\), by any choice
of random or deterministic operator.

The packet also records the matching upper construction: normalized Gaussian
operators into \(\ell_r^N\), with
\(N \gtrsim_r m\log(en/m)\), satisfy \(\mathcal P_1(m)\) with distortion
\(\lesssim_r m^{1/2-1/p}\).  Thus the \(p>2\) tradeoff for the natural
\(\ell_r\)-target family is sharp up to constants depending only on \(r\).

The same sign argument gives a Banach-space variant: if the target has cotype
2 constant \(C_2(E)\), then any \(A:\ell_p^n\to E\) satisfying
\(\mathcal P_1(m)\) obeys
\[
  m^{1/2-1/p}\le C_2(E)\,\beta/\alpha.
\]
This rules out large \(m\) for the Hilbert and \(L_1/\ell_1^N\) target classes
explicitly mentioned in the source's \(p=2\) discussion.

## Proof Idea

Apply \(\mathcal P_1(m)\) only to one coordinate set of size \(m\).  The images
\(y_i=Ae_i\) have \(\|y_i\|_r\ge\alpha\), while every signed sum has norm at
most \(\beta m^{1/p}\).  Taking random signs and applying the lower
Khinchine inequality coordinatewise forces a lower bound of order
\(\alpha m^{1/2}\) on the signed sums.  Comparing with the upper bound
\(\beta m^{1/p}\) gives the obstruction.

## Scope

This is not a full answer to every possible meaning of "what happens for
\(p>2\)".  It rules out the natural large-sparsity extension for the paper's
\(\ell_r\) targets and for Banach targets of cotype 2.  It does not rule out
other exotic quasi-Banach targets whose finite-dimensional structure is
designed to contain \(\ell_p^m\) uniformly.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1107.0992.
- `figures/p1_definition_crop.png`: source definition of \(\mathcal P_1(m)\).
- `figures/p_gt_2_question_crop.png`: source paragraph asking about \(p>2\).

## Human Review Focus

Check the lower Khinchine step for \(0<r\le1\), the standard Gaussian net
argument in the matching upper construction, and the interpretation of the
source question as targeting the same \(\ell_r^N\) codomain family used in the
\(0<p<2\) construction.
