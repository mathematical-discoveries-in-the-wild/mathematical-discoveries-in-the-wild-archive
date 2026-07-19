# Literature-Implied Status Packet: Zone Diagram Approximation

status: literature_implied_answer (partial subcase)

target_source: arXiv:1002.3583, Eva Kopecka, Daniel Reem, Simeon Reich, "Zone diagrams in compact subsets of uniformly convex normed spaces"

supporting_source: arXiv:1208.3124, Daniel Reem, "On the Computation of Zone and Double Zone Diagrams"

packet_pdf: solution_packet.pdf

ledger_record: runs/fa_banach_001/ledger/results/1002.3583_zone_diagram_approximation_by_1208.3124.json

## Identification

The source paper ends with several open directions. The branch recorded here is
the question of how to approximate zone diagrams in the paper's setting,
together with the observation that no error estimates are obtained.

Reem's later computation paper develops the inner and outer approximation
sequences, proves convergence to the least and greatest double zone diagrams in
proper geodesic spaces with the geodesic inclusion property, gives Hausdorff
convergence in compact worlds, and describes the ray-shooting/Voronoi-based
approximate computation method in normed spaces. Finite-dimensional strictly
convex normed spaces are included in that framework.

## Scope

This is a partial literature-implied answer, not a new proof by the run. It
does not settle all open problems in the 2010 concluding paragraph. In
particular, it does not give convergence-rate/error estimates, and the 2018
paper explicitly leaves the estimation of the required iteration count
`n_0(epsilon)` open. It also does not settle the local-connectedness,
general-all-normed-spaces, uniqueness, or no-emanation-property questions from
the source paper.
