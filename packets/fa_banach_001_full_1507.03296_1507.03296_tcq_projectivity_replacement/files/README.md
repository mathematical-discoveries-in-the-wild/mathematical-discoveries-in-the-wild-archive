# Full solution packet: projectivity replacement for trace-class convolution modules

Status: `full_solution_likely_valid`

Source target: Jason Crann, *Amenability and covariant injectivity of locally compact quantum groups II*, arXiv:1507.03296. The target is Remark 5.14 on page 20, asking whether relative 1-projectivity of
`T(L^2(G))` can be replaced by ordinary 1-projectivity in Theorems 5.12 and 5.13.

## Result

Yes. For every locally compact quantum group `G`, the following are equivalent:

- `\widehat G` is compact, equivalently `G` is discrete.
- `T(L^2(G))` is 1-projective in `(T(L^2(G)),\triangleright)-mod`.
- `T(L^2(G))` is relatively 1-projective in `(T(L^2(G)),\triangleright)-mod`.

The analogous right-module statement for `(T(L^2(G)),\triangleleft)` also holds.

## Proof mechanism

Ordinary 1-projectivity gives approximate norm-one module splittings of the multiplication
`m = (\Gamma^r)_*`. Since `m` is the preadjoint of the normal complete isometry
`\Gamma^r`, the adjoint splittings are normal completely bounded maps on
`B(L^2(G) \otimes L^2(G))`. A weak-star cluster point has cb-norm at most 1 and is still a module left inverse to `\Gamma^r`; taking its preadjoint gives an honest relative 1-projective splitting. Crann's Theorem 5.12 then gives compactness of the dual.

Conversely, if `\widehat G` is compact then `G` is discrete. Hu-Neufang-Ruan show that in the discrete case any normal extension to `T(L^2(G))` of the identity of `L^1(G)` is a right identity for `(T(L^2(G)),\triangleright)`. Choosing a norm-one extension, the elementary module lemma says a completely contractive Banach algebra with a contractive right identity is 1-projective as a left module over itself. The unitary antipode gives the right-module version for `\triangleleft`.

## Files

- `main.tex` and `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `supporting_paper_hu_neufang_ruan_2013.pdf`: supporting paper for the right-identity/discreteness input.
- `figures/open_problem_crop.png`: rendered page containing Remark 5.14.
- `code/verify_module_lemma.py`: small symbolic sanity check for the abstract lifting lemma.

## Literature check

Checked local run indexes for `1507.03296`, the paper title, `relative 1-projectivity`, `TCQ`, and trace-class projectivity: no duplicate packet or exact settlement was present. Web/local literature checks found the source paper, Hu-Neufang-Ruan's trace-class convolution paper, Crann's 2021 local-theory paper, and related 2024/2026 trace-class convolution papers, but no later paper explicitly answering Remark 5.14. The packet uses HNR only as a supporting ingredient, not as an already-known answer.

Human review recommendation: verify the weak-star compactness step inside the dual operator space of normal completely bounded maps and the side conventions for the `\triangleright`/`\triangleleft` module identities.
