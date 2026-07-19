# Net Diamond Fragmentability Obstruction

Status: `partial_result_likely_valid`

Source: Estelle Basset, Gilles Lancien, Antonin Prochazka, *Diversity of Lipschitz-free spaces over countable complete discrete metric spaces*, arXiv:2505.19891.

This packet records a partial theorem adjacent to Remark 3.7 of the source paper. The source asks for examples of nets in infinite-dimensional Banach spaces, or integer grids of infinite semi-normalized Schauder bases, whose Lipschitz-free spaces have weak-fragmentability index `omega`; it points to the canonical integer grid of `ell_1` as a natural candidate.

The result here does not settle that candidate. It proves instead that a broad obstruction forces the opposite value for genuine nets: if a Banach space carries equi-bi-Lipschitz copies of the countably branching diamond graphs `D_n^omega`, then every separated coarsely dense net in that Banach space also carries those diamonds with uniformly bounded distortion. Consequently the source paper's diamond lower bound and uniformly-discrete upper bound give `Phi(F(N)) = omega^2` for every such net `N`.

The packet includes:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2505.19891.
- `figures/open_problem_crop.png`: crop of Remark 3.7 on PDF page 10.
- `code/make_open_problem_crop.py`: reproducible crop script.

Human review should focus on the nearest-net projection lemma: after scaling the ambient diamond copy, the additive projection error is absorbed uniformly because graph distances in `D_n^omega` are at least one.
