# Scattered `C_0` tensor subcases for the CWO tensor question

Status: strengthened partial result, likely valid, low-to-moderate novelty.

Source paper: T. A. Abrahamsen, J. Becerra Guerrero, R. Haller, V. Lima, and M. Poldvere, *Banach spaces where convex combinations of relatively weakly open subsets of the unit ball are relatively weakly open*, arXiv:1806.10693.

Source question: Section 6 asks whether, if Banach spaces `X` and `Y` have property `CWO`, the injective tensor product `X \hat{\otimes}_\varepsilon Y` must also have `CWO`; it also asks the analogous question for `CWO-S` and `CWO-B`.

Packet claim:

- If `E` is finite dimensional, then `E` has `CWO` if and only if `E` has the source paper's property `(co)`.
- Consequently, if `K` is scattered locally compact Hausdorff and `E` is finite-dimensional with `CWO`, then `C_0(K) \hat{\otimes}_\varepsilon E = C_0(K,E)` has `CWO`.
- If `K` and `L` are scattered locally compact Hausdorff spaces, then `C_0(K) \hat{\otimes}_\varepsilon C_0(L)` has `CWO`; the same holds for any finite injective tensor product of scalar scattered `C_0` spaces.

Core proof: the finite-dimensional implication `CWO => (co)` follows by applying `CWO` to small relative balls around a fixed convex decomposition, then using a finite-dimensional continuous selection theorem for the resulting lower-semicontinuous convex fiber map. The `C_0(K,E)` conclusion then follows from Theorem 2.5 of the source paper. The scalar `C_0(K) \hat{\otimes}_\varepsilon C_0(L)` case uses the standard identification with `C_0(K \times L)` and the elementary fact that finite products of scattered spaces are scattered.

Limitations: this does not settle the general tensor-product stability question. The scalar `C_0` part is best viewed as an explicit recorded corollary of the source paper plus standard tensor-product/topological facts; the finite-dimensional `CWO => (co)` upgrade is the main new argument for human review.

Files:

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: crop of the source question.

Human-review recommendation: verify the finite-dimensional selection argument proving `CWO => (co)`, and then check the locally compact tensor identifications used in the two corollaries.
