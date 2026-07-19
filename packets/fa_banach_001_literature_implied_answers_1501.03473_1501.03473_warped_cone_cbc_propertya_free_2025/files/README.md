# Literature-Implied Partial Answer Packet: Warped Cone Coarse Baum--Connes

Run: `fa_banach_001`

Result type: `literature_implied_answer` (partial subcase)

## Original Problem Source

- Cornelia Dru\c{t}u and Piotr W. Nowak, *Kazhdan projections, random walks
  and ergodic theorems*, arXiv:1501.03473.
- Local PDF: `source_paper.pdf`.
- Evidence image: `figures/open_problem_crop.png` (page 39).

The relevant visible target is Conjecture 6.7: if `G,M` satisfy the
assumptions of the warped-cone ghost-projection theorem, then the coarse
assembly map is not surjective for the warped cone `X = O_G M`.

Two adjacent scan hits were not used as targets: Willett--Yu Problem 5.4 is
answered in the same source by the warped-cone construction, and the
"does not coarsely contain expanders?" question is inside the source's
`\comment ... \endcomment` block.

## Supporting Literature

- Christos Kitsios, Thomas Schick, and Federico Vigolo, *Coarse
  Baum-Connes and warped cones: failure of surjectivity in odd degree*,
  arXiv:2504.21811.
- Local PDF: `supporting_paper_2504.21811.pdf`.
- Extracted source: `tmp/wc_vs_bc.tex`.
- Evidence images:
  - `figures/supporting_conjecture_theorem_crop.png` (page 2)
  - `figures/supporting_theorem_c_crop.png` (page 3)

The 2025 paper explicitly formulates Roe/Dru\c{t}u--Nowak Conjecture 7.7:
for a compact Riemannian manifold `M` and a measure-preserving
diffeomorphism action with spectral gap, the coarse assembly map should not
be surjective for the unified warped cone. Its Theorem C proves
non-surjectivity for actions by groups with property A that are free and
strongly ergodic; the paper also notes that the free subgroup action on
`SU(2,C)` discussed there satisfies these hypotheses.

## Match

This is not a full resolution of Conjecture 6.7 as stated in arXiv:1501.03473.
It is a direct literature partial answer for a natural and explicitly named
subcase:

- spectral gap implies strong ergodicity for measure-preserving actions;
- free groups have property A;
- the free, isometric Bourgain--Gamburd `SU(2)` example is one of the
  concrete examples highlighted around the Dru\c{t}u--Nowak warped-cone
  construction;
- Kitsios--Schick--Vigolo prove the coarse Baum--Connes map is not
  surjective for this type of unified warped cone.

The same paper also records that the expected K-theory obstruction from the
Dru\c{t}u--Nowak ghost projection itself vanishes in `K_0`, so the successful
obstruction is in odd degree rather than the original even-degree projection
route.

## Literature Check Bounds

Searches used:

- run indexes for `1501.03473`, `Kazhdan projections`, `warped cone`,
  `coarse Baum-Connes`, `ghost projection`, and `coarse assembly`;
- local source/title pools for `warped cone` plus `coarse Baum-Connes`;
- web searches for `"warped cones" "coarse Baum-Connes" conjecture spectral gap`
  and close variants.

The local corpus also showed Li--Vigolo--Zhang arXiv:2008.12572 and Sawicki's
sparse warped-cone results, but those concern sparse or integral variants and
do not by themselves settle the unified warped-cone statement. The 2025
Kitsios--Schick--Vigolo paper is the decisive source for the unified
warped-cone partial result recorded here.

## Limitations

- This is a literature-status packet, not an original proof from the run.
- The full statement "every spectral-gap action satisfying the 2015
  hypotheses gives non-surjectivity" remains broader than the 2025 theorem.
- The supporting theorem assumes property A, freeness, and strong ergodicity.
  It does not require the full power of spectral gap, but it does require
  extra hypotheses not present in the original conjecture.
- The packet should not be upgraded to `literature_already_answered` or
  `full` unless a later source proves the complete Conjecture 6.7 without
  the additional hypotheses.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original problem source.
- `supporting_paper_2504.21811.pdf`: supporting literature source.
- `figures/open_problem_crop.png`: original conjecture crop.
- `figures/supporting_conjecture_theorem_crop.png`: supporting conjecture
  identification crop.
- `figures/supporting_theorem_c_crop.png`: supporting theorem crop.
- `tmp/`: render intermediates and copied supporting TeX.

## Human Review Recommendation

Verify the classification boundary: this packet records a strong literature
partial answer for property-A free strongly ergodic actions, including the
standard free-subgroup `SU(2)` example, but not a full answer to all
Dru\c{t}u--Nowak spectral-gap warped cones.
