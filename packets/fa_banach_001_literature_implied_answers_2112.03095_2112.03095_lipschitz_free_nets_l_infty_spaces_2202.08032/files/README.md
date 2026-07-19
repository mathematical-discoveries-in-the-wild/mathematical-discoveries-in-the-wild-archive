# Literature-Implied Partial Subcase: Nets in Separable L-infinity Spaces

Status: `literature_implied_answer (partial subcase)`

Source problem paper: P. Hajek and R. Medina, *Schauder bases in Lipschitz
free spaces over nets in Banach spaces*, arXiv:2112.03095.

Supporting paper: P. Hajek and R. Medina, *Schauder bases in Lipschitz free
spaces over nets of L-infinity-spaces*, arXiv:2202.08032.

## Target

The source paper recalls Kalton's question whether Lipschitz free spaces over
separable uniformly discrete metric spaces have the bounded approximation
property. It notes that it suffices to consider nets `N` in Banach spaces `X`,
that the case where `X` has separable dual is positive, and that the case of a
general separable Banach space `X` remains open.

The source paper then proves stronger Schauder-basis conclusions in special
cases: finite-dimensional `X`, and nets in Banach spaces with a Schauder basis
containing `c_0` or with a `c_0`-like FDD.

## Result

The later paper arXiv:2202.08032 gives a literature answer to a further
nontrivial subcase: if `X` is a separable infinite-dimensional
`L_infinity`-space and `N` is a net in `X`, then `F(N)` has a Schauder basis.
Consequently `F(N)` has the bounded approximation property.

This is stronger than the BAP conclusion requested by Kalton's question for
that subcase, because a Schauder basis gives uniformly bounded finite-rank
partial-sum projections.

## Identification

In the introduction of arXiv:2112.03095, the authors state the Kalton BAP
question for uniformly discrete metric spaces and reduce it to the case of
nets in Banach spaces. They explicitly say that the general separable Banach
space case remains open.

The introduction of arXiv:2202.08032 says the paper is motivated by the same
Kalton question and obtains that `F(N)` over a net in any separable
`L_infinity`-space has a Schauder basis. Its `Main Theorem` states that a net
in any separable infinite-dimensional `L_infinity`-space has a retractional
basis, and the immediately following corollary states that `F(N)` has a
Schauder basis.

The relation is therefore an agent-identified literature implication for a
proper subcase of the 2112.03095 target. The supporting paper knows it is
working on the Kalton/net BAP problem and explicitly describes the result as
extending the authors' previous net-basis papers, but it does not settle the
general separable Banach-space case.

## Evidence

- `source_paper.pdf`: local copy of arXiv:2112.03095. The target question is
  in the introduction paragraph beginning with Kalton's BAP question and the
  sentence that the general separable Banach-space case remains open.
- `supporting_paper_2202.08032.pdf`: local copy of arXiv:2202.08032. The
  decisive statements are the introduction paragraph about the Kalton question,
  the `Main Theorem`, and the following corollary.
- `solution_packet.pdf`: compact human-readable status note built from
  `main.tex`.

## Search Bounds

Before packaging, the cheap run indexes were searched for `2112.03095`,
`Schauder bases in Lipschitz-free`, `Lipschitz-free spaces basis`, `free space
Schauder basis`, `metric space basis`, and `approximation property
Lipschitz-free`. No prior packet or attempt for this exact arXiv target or
this `L_infinity` subcase was found.

External literature search found the source paper arXiv:2112.03095, the later
supporting paper arXiv:2202.08032, Novotny's arXiv:1905.13188 on
retractional-basis obstructions, and Aliaga--Medina arXiv:2601.03131 on
Lipschitz-free spaces over nets. Only arXiv:2202.08032 is decisive for this
packet.

## Scope Limitations

This packet does not solve Kalton's question for arbitrary separable Banach
spaces. It records only the positive Schauder-basis, hence BAP, subcase for
nets in separable infinite-dimensional `L_infinity`-spaces. Finite-dimensional
and `c_0`/`c_0`-like FDD cases are already handled in the source paper itself.

## Human Review Notes

Recommended review focus:

- Confirm that the source target is the Kalton/net BAP question as stated in
  the introduction of arXiv:2112.03095.
- Confirm that arXiv:2202.08032's `Main Theorem` and corollary cover every
  net in every separable infinite-dimensional `L_infinity`-space.
- Confirm the standard implication from a Schauder basis in `F(N)` to the
  bounded approximation property.
