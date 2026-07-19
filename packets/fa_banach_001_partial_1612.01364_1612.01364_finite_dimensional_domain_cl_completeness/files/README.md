# Partial packet: finite-dimensional domains give completeness of CL(X,Y)

status: partial_result

source: Antonin Dalet and Gilles Lancien,
*Some properties of coarse Lipschitz maps between Banach spaces*,
arXiv:1612.01364.

target: Section 4 asks whether `(CL(X,Y), || ||_CL)` is always a Banach
space. The authors conjecture a negative answer, but no counterexample is
constructed in the source.

packet: `runs/fa_banach_001/solutions/partial/1612.01364_finite_dimensional_domain_cl_completeness/`

## Result

This packet proves a positive finite-dimensional-domain subcase.

If `X` is finite-dimensional and `Y` is any Banach space, then `(X,Y)` has
the net extension property (NEP) of Definition 4.1 in the source paper.
Consequently, by Propositions 4.4 and 4.5 of the source paper,
`(CL(X,Y), || ||_CL)` is a Banach space.

Equivalently, any counterexample to the source's general completeness
conjecture must have infinite-dimensional domain.

## Proof Mechanism

Choose a maximal 1-separated net `M` in the finite-dimensional space `X`.
Finite-dimensionality gives uniform packing bounds for the number of net
points in bounded balls. These bounds allow one to build a Lipschitz
partition of unity from radius-2 tent functions around points of `M`.

For a Lipschitz map `h: M -> Y`, the partition gives a Lipschitz approximate
extension `H_0`. The interpolation error at the net points is uniformly
bounded. A second family of disjoint radius-1/2 bump functions corrects this
bounded error exactly at every point of `M`, while preserving Lipschitzness.
Thus every Lipschitz map on `M` extends Lipschitzly to all of `X`.

## Verification

- Cheap run indexes were searched for `1612.01364`, `coarse Lipschitz`,
  `CL(X,Y) completeness`, `net extension property`, `LRP`, and nearby
  keywords.
- No existing packet or attempt for this arXiv id was found before this pass.
- Neighboring run entries about coarse Lipschitz maps and asymptotic
  smoothness were inspected and do not duplicate this finite-dimensional
  NEP/completeness subcase.
- A related prior run artifact,
  `solutions/literature_implied_answers/1506.05391_finite_dimensional_net_extensions/`,
  records the same finite-dimensional net-extension mechanism for Naor's
  Rosendal-net question, using later literature. This packet is therefore not
  claiming novelty of the finite-dimensional extension lemma itself; its new
  target-level contribution is applying NEP to Dalet--Lancien's
  `CL(X,Y)` completeness question via their Propositions 4.4 and 4.5.
- The source text was checked directly: Definition 4.1, Proposition 4.4,
  Proposition 4.5, and the open completeness remark are all in Section 4.

## Scope

This is not a full solution of the general completeness problem and gives no
counterexample. The infinite-dimensional-domain case remains open in this
packet. The separate converse direction LRP/ANEP versus NEP mentioned in the
preceding source remark is handled in the companion full packet
`solutions/full/1612.01364_lrp_anep_nep_equivalence/`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of the source completeness
  proposition and open completeness remark.
