# Partial result: tree-p Banach-Saks permanence for WSC coarse Lipschitz embeddings

- Run: `fa_banach_001`
- arXiv source: `1808.03254`
- Source paper: Bruno de Mendonca Braga, *On asymptotically uniformly smoothness and nonlinear geometry of Banach spaces*
- Source question: Problem 8.6 / `ProblemBS`
- Packet status: `partial_result`
- Packet slug: `1808.03254_tree_banach_saks_wsc_embedding`

## Result

Braga asks whether, if `Y` has the weak `p`-Banach-Saks property and `X` coarse Lipschitzly embeds into `Y` by a weakly sequentially continuous map, then `X` must have the weak `p`-Banach-Saks property.

This packet proves the affirmative answer under the stronger target hypothesis that `Y` has the tree-`p`-Banach-Saks property. More precisely:

> If `Y` has tree-`p`-Banach-Saks and `X` admits a weakly sequentially continuous coarse Lipschitz embedding into `Y`, then `X` has tree-`p`-Banach-Saks, hence weak `p`-Banach-Saks.

The proof follows Braga's nonlinear telescoping tree construction, but replaces upper `ell_p` tree estimates by the sign-stabilized form of tree-`p`-Banach-Saks plus a convex-hull argument for bounded positive coefficients.

## Scope

This is not a full solution of Problem 8.6. The original hypothesis assumes only weak `p`-Banach-Saks for `Y`; the packet assumes the stronger tree version. The result is still a meaningful partial permanence theorem because it preserves the endpoint exponent `p` under a target condition weaker than upper `ell_p` tree estimates.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of Problem 8.6 from page 33 of the source PDF.
- `tmp/make_open_problem_crop.py`: helper used to render the source-problem crop.

## Literature and duplicate checks

Cheap run indexes were searched for `1808.03254`, Braga, weak `p`-Banach-Saks, tree-Banach-Saks, and weakly sequentially continuous coarse Lipschitz embeddings. Web searches for the exact problem label and core phrase combinations found only the source arXiv page and no later direct answer. A later local source on Hamming graph concentration properties was checked for overlap and did not answer Problem 8.6.

Human review should focus on the sign-stabilized tree-p Banach-Saks lemma and the convex-hull step converting signs into bounded coefficients.
