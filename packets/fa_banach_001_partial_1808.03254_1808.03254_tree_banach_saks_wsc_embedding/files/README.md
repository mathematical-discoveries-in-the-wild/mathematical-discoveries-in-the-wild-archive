# Braga Weak p-Banach-Saks WSC Embedding Partial Result

Result type: `partial`

Status: strengthened candidate partial result, likely valid pending human
review.

Source paper:

- Bruno de Mendonca Braga, "On asymptotically uniformly smoothness and
  nonlinear geometry of Banach spaces", arXiv:1808.03254.
- Source question: Problem 8.6 / `ProblemBS`.
- Local source PDF: `source_paper.pdf`.
- Open-problem evidence crop: `figures/open_problem_crop.png`.

## Upgrade Incorporated

The supplied report
`evidence/supplied_braga_weak_p_banach_saks_note_2026_06_22/braga_weak_p_banach_saks_note.tex`
audits the previous packet and strengthens it.  The old active packet proved
only that tree-`p`-Banach-Saks passes under weakly sequentially continuous
coarse Lipschitz embeddings.  The new packet keeps that result, corrects the
signed-tree citation to Braga Proposition 6.3, records the missing
normalization and rescaling justifications, and adds a sharper modulus-transfer
form.

## Claimed Contribution

Braga asks whether weak `p`-Banach-Saks passes from `Y` to `X` whenever `X`
admits a weakly sequentially continuous coarse Lipschitz embedding into `Y`.

This packet gives:

- a scale-sensitive modulus-transfer theorem for arbitrary weakly
  sequentially continuous coarse embeddings when `Y` has tree-`p`-Banach-Saks;
- coarse Lipschitz permanence of tree-`p`-Banach-Saks with constants controlled
  by the asymptotic slope ratio;
- power-compression and `p = infinity` variants;
- a direct positive theorem under the original weak `p`-Banach-Saks target
  assumption when the embedding has controlled finite-sum additive defect.

## Scope

This is not a full solution of Problem 8.6.  The original weak-`p` target
hypothesis remains open for arbitrary weakly sequentially continuous coarse
Lipschitz embeddings.  The obstacle is the tree-versus-sequence gap: the
nonlinear telescoping argument creates weakly null trees, while weak
`p`-Banach-Saks only controls single weakly null sequences.

## Files

- `main.tex`: consolidated strengthened proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1808.03254.
- `figures/open_problem_crop.png`: crop of Problem 8.6 from page 33.
- `evidence/supplied_braga_weak_p_banach_saks_note_2026_06_22/`: supplied TeX
  and PDF report.
- `history/previous_tree_packet_2026_06_22/`: previous active packet snapshot.
- `tmp/`: LaTeX build intermediates and rendered verification pages.

## Human Review Notes

Verifier focus:

- Check the signed stabilization step and its citation to Braga Proposition
  6.3.
- Check the modulus-transfer telescoping proof and the use of compression and
  expansion moduli.
- Check the finite-sum additive-defect criterion, especially the scaling by
  `r_k`.
- Confirm that the packet does not overclaim a full answer to Problem 8.6.

No computational verification is needed; the argument is analytic.
