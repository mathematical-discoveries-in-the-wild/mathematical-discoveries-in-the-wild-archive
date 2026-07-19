# Rapid P-point characterization for Problem 5.5

- source: Arkady Leiderman and Vladimir Uspenskij, *Is the free locally convex space \(L(X)\) nuclear?*, arXiv:2106.13413.
- target: Problem 5.5 asks whether, for \(p\in\beta\mathbb N\setminus\mathbb N\) and \(X=\mathbb N\cup\{p\}\), the free locally convex space \(L(X)\) is nuclear or multi-Hilbert.
- status: `full_solution_likely_valid`
- result: \(L(\mathbb N\cup\{p\})\) is nuclear iff it is multi-Hilbert iff \(p\) is a rapid \(P\)-point.

## Contents

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: the source arXiv paper.
- `supporting_paper_1208.3690.pdf`: Flašková, *Rapid ultrafilters and summable ideals*, used for the rapid/summable-ideal characterization.
- `figures/open_problem_5_5_crop.png`: crop of the source problem.
- `figures/rapid_summable_theorem_page1_crop.png` and `figures/rapid_summable_theorem_page2_crop.png`: crops of the supporting rapid-ultrafilter theorem across its page break.
- `code/render_evidence.py`: script that regenerates the evidence crops.

## Proof Summary

For rapid \(P\)-points, every \(p\)-null norm sequence admits weights \(s_n\to_p\infty\) with \(\sum s_n\|x_n\|<\infty\). This turns any Banach-valued continuous map on \(X\) into an explicit nuclear series using the coordinate functions \(\chi_{\{n\}}/s_n\).

If \(p\) is not rapid or not a \(P\)-point, there are weights \(\alpha_n\to_p0\) such that every \(A\in p\) has \(\sum_{n\in A}\alpha_n^2=\infty\). The continuous map \(n\mapsto \alpha_n e_n\) into \(\ell_1\) cannot factor through a Hilbert space, because a Hilbert ellipsoid in \(\ell_1\) can contain coordinate vectors \(\alpha_n e_n\) only on square-summable index sets.

## Literature Check

Local indexes and web searches on 2026-06-20 found no prior packet or later-paper answer for Problem 5.5. Searches included exact arXiv id and close phrases involving `free locally convex`, `multi-Hilbert`, `beta N`, `N union {p}`, `rapid ultrafilter`, and `P-point`.

## Human Review Focus

Check the free-LCS equicontinuity criterion used for the coordinate family \(\chi_{\{n\}}/s_n\), and check the rapid \(P\)-point diagonal lemma. The rest of the argument is a direct nuclear-series construction plus a standard Hilbert-ellipsoid estimate in \(\ell_1\).
