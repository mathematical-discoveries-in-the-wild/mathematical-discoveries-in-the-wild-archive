# Literature-implied status: equal-weight Parseval fusion-frame dimensions

Status: `literature_implied_answer (partial subcase)`.

Source/open-problem paper: arXiv:2303.01202, L. Kohldorfer, P. Balazs,
P. Casazza, S. Heineken, C. Hollomey, P. Morillas, and M. Shamsabadi,
*A Survey of Fusion Frames in Hilbert Spaces*.

Supporting paper: arXiv:1112.3060, M. Bownik, K. Luoto, and E. Richmond,
*A combinatorial characterization of tight fusion frames*.

## Identification

The source survey flags the existence of Parseval fusion frames as a trap:
in the finite-dimensional fusion-frame setting, it says there are no known
necessary and sufficient conditions for Parseval fusion frames for arbitrary
subspace dimensions. The clearest source locations are the introductory
``There Be Dragons'' list and Remark `rank1fusion`, where the paper also gives
the example of two two-dimensional subspaces in `R^3`.

The equal-weight finite-dimensional subcase is already characterized by
Bownik-Luoto-Richmond. Their Problem 1 asks for a characterization of rank
sequences `(L_1,...,L_K)` for which projections of those ranks satisfy
`P_1+...+P_K = alpha I_N`, and Theorem `th:combchar` gives the necessary and
sufficient Littlewood-Richardson condition
`c((N^{L_1}),...,(N^{L_K});(M^N)) != 0`, where `M=sum_i L_i`.

This answers the finite equal-weight Parseval version because
`sum_i P_i = alpha I_N` is equivalent to a Parseval fusion frame with common
weight `alpha^{-1/2}`. Conversely, a common-weight Parseval fusion frame gives
an unweighted tight fusion-frame sequence after dividing by the common weight.

## Scope

This is not a new proof packet and not a full answer to the arbitrary-weight
or fixed-subspace scalability problem. It clears the finite equal-weight /
unit-weight tight dimension-sequence subcase and records that the exact
identification is a literature implication rather than an original result.

Local PDFs were not present in the workspace for either arXiv id; this packet
uses the parsed TeX sources under `data/parsed/arxiv_sources/`.
