# Counterexample packet: every separable space has a filter-pi basis for some filter

Status: `candidate_counterexample_likely_valid`

Source paper: Tomasz Kania and Jaroslaw Swaczyna, *The pi-property of a Banach space along a filter*, arXiv:2508.21242.

Target: Question 1.2 asks whether a separable Banach space with the `F-pi`-property for a certain filter `F` must have a finite-dimensional decomposition.

Answer claimed here: no. In fact, every separable Banach space has the `F-pi`-property for some filter containing the Frechet filter. Taking Enflo's separable Banach space without the approximation property gives a space with such a filter-pi basis but with no FDD. By Theorem B of the source paper, and by adjoining the Frechet filter inside the original filter if necessary, the witnessing filter may additionally be chosen analytic while still containing the Frechet filter.

Packet files:

- `main.tex`: compact proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: crop of Question 1.2 from the source PDF.

Novelty and duplicate check:

- Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Exact local terms searched included `2508.21242`, `Filter_pi_bases`, `Banach space along`, `finite-dimensional decomposition`, `FDD`, and `pi-property`; no prior packet for this target was found.
- Source scan found Question 1.2 on PDF page 3 and no same-paper explicit answer. The paper's Theorem B is used only to sharpen the constructed filter to an analytic one after the direct counterexample is built.
- External bounded web check on 2026-06-28 used exact title and close phrases such as `"every separable Banach space" "filter" "pi-property" "finite-rank projections"`; it surfaced the source arXiv page but no existing statement of this universal counterexample route.

Scope limitations:

- This does not answer the classical open problem whether the usual Frechet-filter pi-property implies an FDD.
- This does not claim anything for a fixed prescribed filter, nor for countably generated filters beyond the implications already discussed in the source paper.

Human review focus:

- Check the SOT separability lemma for norm-bounded sets of finite-rank projections and the filter finite-intersection argument.
- Check that the source paper's convention "all filters considered contain the Frechet filter" is exactly met by the generated filter.
