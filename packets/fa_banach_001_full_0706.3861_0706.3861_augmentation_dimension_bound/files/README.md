# Augmentation-Dimension Bound for Ferenczi--Galego Question 13

Status: likely valid full negative answer.

Source: Valentin Ferenczi and Eloi Medina Galego, *Countable groups of isometries on Banach spaces*, arXiv `0706.3861`, Question 13 on PDF page 18.

Question answered: whether there are arbitrarily large `n` and finite groups `G` of order `n` such that `{-1,1} x G` is representable in a separable real Banach space `X` if and only if `dim X >= n`.

Result: no. If `|G|=n>=3`, then `{-1,1} x G` is representable in every separable real Banach space of dimension at least `n-1`.

Core idea: replace the regular representation on `ell_2(G)` by its augmentation hyperplane. The regular action restricted to the augmentation hyperplane is faithful, and for `|G|>2` no element acts as `-Id`. Therefore the central sign can act as the global scalar `-1` on the augmentation part and on the complement, giving a faithful finite group of isomorphisms containing `-Id`; Ferenczi--Galego's finite renorming theorem then makes it the full isometry group.

Packet contents:

- `main.tex` - full proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - source paper PDF.
- `figures/open_problem_crop.png` - crop of Question 13 from the source paper.
- `tmp/` - LaTeX build files and rendered source page images.

Novelty check: local run indexes and bounded web searches on July 3, 2026 found no prior packet or visible literature statement of this `n-1` improvement. Ferenczi--Rosendal `1110.2970` was checked as later context and recalls the original finite theorem, not this sharpening. Novelty confidence is moderate because the argument is elementary.

Human-review focus: verify the edge case exclusion `n=2`, the proof that the augmentation representation never contains `-Id` for `n>=3`, and the application of Ferenczi--Galego Theorem 8 to the finite group of isomorphisms.
