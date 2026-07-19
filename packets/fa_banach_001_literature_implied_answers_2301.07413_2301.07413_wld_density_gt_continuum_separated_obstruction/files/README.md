# Literature-Implied Answer: WLD Density Above the Continuum

- Source arXiv: 2301.07413
- Source paper: Piotr Koszmider and Kamil Ryduchowski, *Equilateral and separated sets in some Hilbert generated Banach spaces*
- Supporting arXiv: 1803.11501
- Supporting paper: Petr Hajek, Tomasz Kania, and Tomasz Russo, *Separated sets and Auerbach systems in Banach spaces*
- Status: `literature_implied_answer (partial subcase)`
- Packet path: `runs/fa_banach_001/solutions/literature_implied_answers/2301.07413_wld_density_gt_continuum_separated_obstruction/`
- Ledger record: `runs/fa_banach_001/ledger/results/2301.07413_wld_density_gt_continuum_separated_obstruction.json`

## Identification

Question 5 in arXiv:2301.07413 asks, among other things, whether there is a
nonseparable Hilbert generated, WCG, or WLD Banach space whose unit sphere does
not admit an uncountable `(1+)`-separated set. The source gives consistent
examples without uncountable `(1+epsilon)`-separated sets, but its own
`sw`/`sss` classes still have uncountable `(1+)`-separated sets.

Hajek--Kania--Russo, arXiv:1803.11501, Theorem A(ii), proves that if `X` is a
WLD Banach space with `dens X > c`, then the unit spheres of `X` and `X*`
contain uncountable symmetrically `(1+)`-separated subsets. Symmetric
`(1+)`-separation is stronger than ordinary `(1+)`-separation. Therefore no
WLD counterexample to Question 5(4) can have density strictly larger than the
continuum. Since Hilbert generated and WCG spaces are WLD, the same density
restriction applies to those classes.

## Scope

This is not an original partial result. It is an agent-identified implication
from known literature, and the supporting paper predates and is cited by the
source paper. The remaining open territory is the density-at-most-continuum
case, in particular the natural density `omega_1` cases highlighted by the
source paper.

## Files

- `README.md`: packet summary.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2301.07413.
- `supporting_paper_1803.11501.pdf`: arXiv:1803.11501.
