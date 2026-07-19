# Partial packet: peak-point uniqueness for positive isometry extensions

Status: `candidate partial result` (superseded by
`runs/fa_banach_001/solutions/full/2504.03386_irreducible_surjection_unique_positive_isometry_extension/`)

Source paper: Tanmoy Paul and T. S. S. R. K. Rao, "Order-preserving unique Hahn-Banach extensions", arXiv:2504.03386.

Source problem: the final Problem on PDF page 14 asks for conditions under which an order-preserving isometric embedding
`Phi: A(K) -> C(K)` has a unique extension to an into order-preserving isometry from `C(K)` to `C(K)`.

Packet result: if every point of the compact convex set `K` is a peak point for `C(K)`, and if the embedding is the natural
composition embedding `Phi(a)=a o h` induced by a homeomorphism `h:K->K`, then the only positive linear isometry
`T:C(K)->C(K)` extending `Phi` is `T(f)=f o h`. In particular, this applies to compact metrizable `K` and gives uniqueness
for the canonical inclusion when `h=id`.

Scope note: this addresses the literal last-sentence "into order-preserving isometry `C(K)->C(K)`" reading of the source
problem. It does not settle the projection-valued or broader operator-space extension questions suggested by the surrounding
paragraph in the source paper, and it does not classify arbitrary order-preserving isometric embeddings of `A(K)` into `C(K)`.

Evidence files:

- `source_paper.pdf`: downloaded arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source problem statement.
- `code/make_open_problem_crop.py`: crop-generation helper.
- `main.tex` and `solution_packet.pdf`: human-readable proof packet.

Novelty check: before packaging, the lane searched the run's cheap indexes for `2504.03386`, the paper title, and core
terms around order-preserving Hahn-Banach/isometry extensions. No exact packet was present. A bounded web search for exact
phrases around the source problem and Rao's operator-version phrasing found no direct later answer.

Human review focus: check that the interpretation of the source problem is accepted as the intended literal `C(K)->C(K)`
extension question, and verify the point-peak argument forcing all representing measures to be point masses.

Supersession note: the later full-style packet replaces the peak-point argument with Holsztynski's into-isometry theorem,
removing the metrizability/point-peak hypothesis and covering all irreducible-surjection composition embeddings.
