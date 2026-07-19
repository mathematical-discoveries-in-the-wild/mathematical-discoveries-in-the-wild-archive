# Full packet: irreducible-surjection conditions for unique positive isometry extensions

Status: `candidate full literal answer`

Source paper: Tanmoy Paul and T. S. S. R. K. Rao, "Order-preserving unique Hahn-Banach extensions", arXiv:2504.03386.

Source problem: the final Problem on PDF page 14 asks for conditions under which an order-preserving isometric embedding
`Phi: A(K) -> C(K)` has a unique extension to an into order-preserving isometry from `C(K)` to `C(K)`.

Result: in the unital setting used throughout the source paper, every order-preserving embedding `Phi:A(K)->C(K)`
has an associated continuous state map `alpha:K->K` satisfying `Phi(a)(t)=a(alpha(t))`. If `alpha` is an irreducible
continuous surjection, meaning no proper closed subset of `K` maps onto `K`, then `Phi` has a unique positive linear
isometric extension `C(K)->C(K)`, namely `T(f)=f o alpha`.

Why this is an upgrade over the prior partial packet: the earlier packet proved uniqueness for homeomorphism-induced
embeddings under a point-peak hypothesis. This packet removes the point-peak/metrizability hypothesis and replaces
homeomorphism by the broader topological condition of irreducible surjectivity. It includes the canonical inclusion
`A(K) subset C(K)` for every compact convex `K`.

Scope note: this is a full literal answer to the source request to "find conditions" ensuring uniqueness. It is not a
complete classification of all order-preserving isometric embeddings for which uniqueness holds.

Evidence files:

- `source_paper.pdf`: downloaded arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source problem statement.
- `code/make_open_problem_crop.py`: crop-generation helper.
- `main.tex` and `solution_packet.pdf`: human-readable proof packet.

Novelty check: before packaging, the lane searched the run's cheap indexes for `2504.03386`, the source title, and core
terms around order-preserving isometric embeddings, unique positive isometry extensions, irreducible surjections, and
Holsztynski/Banach-Stone. The only exact hit was the prior partial packet. A bounded web search for exact problem phrases
and close variants did not find a direct later answer.

Human review focus: verify that the unital interpretation matches the source context, and check the invocation of
Holsztynski's into-isometry theorem for real `C(K)` spaces.
