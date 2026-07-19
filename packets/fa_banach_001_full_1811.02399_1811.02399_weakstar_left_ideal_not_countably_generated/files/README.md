# Full result: the Wark-dual ideal is not countably generated

## Status

`full_result_strengthening_likely_valid`

Source paper: Niels Jakob Laustsen and Jared T. White,
*Subspaces that can and cannot be the kernel of a bounded operator on a Banach
space*, arXiv:1811.02399.

## Result

Laustsen and White prove that, for \(E=X^*\), where \(X\) is one of Wark's
non-separable reflexive spaces with few operators, \(\mathscr B(E)\) has a
weak-star closed left ideal that is not weak-star topologically finitely
generated.

This packet strengthens that conclusion: the same ideal is not even weak-star
topologically countably generated.

The key observation is that their finite-intersection kernel dichotomy extends
to countable intersections.  If
\[
D=\bigcap_{n=1}^\infty \ker T_n,\qquad T_n\in\mathscr B(E),
\]
then either \(D\) or \(E/D\) is separable.  The source paper chooses a closed
subspace \(D\subseteq E\) for which both \(D\) and \(E/D\) are non-separable,
so \(D\) cannot arise as a countable kernel intersection.  The ideal
\[
\mathscr I_D=\{T\in\mathscr B(E):D\subseteq\ker T\}
\]
therefore cannot be weak-star countably generated, since any countable
generating sequence would recover \(D\) as the intersection of its kernels.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:1811.02399.
- `figures/open_problem_crop.png` - crop of the source abstract and natural question.
- `code/crop_source_question.py` - crop-generation helper.

## Verification

LaTeX was compiled with `pdflatex`.  The crop was generated from page 1 of the
source PDF with PyMuPDF.

Novelty checks covered the run indexes for `1811.02399`, kernel/intersection
keywords, and weak-star countable-generation phrases, plus web searches for
the exact countable-generation strengthening.  No existing statement of this
strengthening was found.
