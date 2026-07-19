# RMF Stability Under Subquotients and Complex Interpolation

Status: candidate partial result, likely valid.

Source paper: Tuomas Hytonen, Alan McIntosh, Pierre Portal, "Kato's square root problem in Banach spaces", arXiv:math/0703012.

Extracted question: the source asks whether every UMD Banach space has the RMF property. A positive answer would remove the extra RMF hypothesis from the Banach-valued Kato square-root theorem.

Partial result: the RMF property is stable under closed subspaces, Banach-space quotients, and complex interpolation of compatible couples. Consequently every Banach space obtained from the known RMF examples in the source paper by these operations also has RMF. In particular, the source Kato theorem applies to UMD spaces whose space and dual lie in this RMF-preserving hull.

What remains open: the packet does not show that every UMD space belongs to this hull, and it does not give a counterexample to RMF among UMD spaces.

Novelty/literature check:
- Cheap run indexes searched for `0703012`, `Kato`, `square root`, `RMF`, `Rademacher maximal`, `UMD`.
- Local corpus hits include arXiv:1002.2876, which records the RMF-vs-UMD question as still open in 2010 and gives Carleson-embedding characterizations.
- Web searches on June 14, 2026 for `Rademacher maximal function RMF UMD counterexample`, `"every UMD space" "RMF"`, and `"RMF property" interpolation Banach spaces` found later RMF/multilinear work but no exact settlement of the full UMD question or this stability packet.

Files:
- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:math/0703012.
- `figures/open_problem_crop.png`: crop of the source open-question paragraph on PDF page 8.

Human-review focus:
- Check the interpolation step, especially the standard identity `Rad_N([X_0,X_1]_theta) = [Rad_N(X_0),Rad_N(X_1)]_theta` with constants independent of `N`, and the operator-space embedding used for the finite linearized RMF operators.
- Check the quotient-lifting argument through the Bochner quotient `L^p(X)/L^p(Y)`.
