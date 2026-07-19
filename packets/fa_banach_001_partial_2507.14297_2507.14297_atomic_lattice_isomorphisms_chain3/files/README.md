# Partial result for arXiv:2507.14297

Status: `partial_result_likely_valid`.

Source paper: Tomasz Szczepanski, *On the chain of commuting operators on Banach
spaces and Lomonosov's invariant subspace theorem*, arXiv:2507.14297.

Question addressed: Question 3.4 asks whether every lattice isomorphism
`T:X -> X` on a Banach lattice is of chain 3.

Result in this packet: yes for the standard infinite atomic coordinate
lattices `ell_p(Gamma)`, `1 <= p < infinity`, and `c_0(Gamma)`, for an
arbitrary infinite index set `Gamma`. This extends the source paper's separable
`ell_p` corollary from countable coordinate bases to arbitrary-cardinality
atomic coordinate lattices.

Main files:

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: locally compiled PDF from the ingested arXiv source.
- `figures/open_problem_crop.png`: page-9 crop containing Question 3.4.
- `code/make_open_problem_crop.py`: reproducible crop script.

Scope limitation: this does not settle the non-atomic or band-ergodic cases of
the source question. The proof uses coordinate atoms and bounded coordinate
band projections.
