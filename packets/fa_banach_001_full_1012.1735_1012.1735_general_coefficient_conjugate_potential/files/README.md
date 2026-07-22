# General-coefficient conjugate potential

Status: `candidate full solution`

Source: Pascal Auscher and Andreas Rosen, *Weighted maximal regularity estimates and solvability of non-smooth elliptic systems II*, arXiv:1012.1735, Section 3 after Proposition 3.5, PDF page 16.

## Result

Every weak solution covered by Proposition 3.3 has an associated vector-valued potential `v` satisfying the companion `BD` first-order system, for arbitrary bounded strictly accretive coefficients. No radial-independence, perturbative, or Carleson hypothesis is needed for existence.

The construction fixes the normal component as `r^((n-1)/2) u_r`, chooses one tangential slice with the required divergence, and evolves it by the tangential equation. The normal component of the conormal-gradient equation preserves the divergence constraint.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on PDF page 16.
- `verification_report.md`: line-by-line proof audit.

## Scope

This answers the existence question immediately after Proposition 3.5. It does not supply the stronger boundary estimates and trace properties later proved under perturbative assumptions.

## Review recommendation

Recommended for expert review as a full result. The main points to check are the distributional variation-of-constants argument in `W^{-1,2}(S^n)` and whether the source intended any unstated global bound on `v` beyond Proposition 3.5.

